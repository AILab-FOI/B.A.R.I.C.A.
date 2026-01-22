# main.py
import os
import uuid
import asyncio
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI, UploadFile, File, Form, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# ================================
# Folder setup
# ================================

BASE_DIR = Path(__file__).resolve().parent
QUEUE_DIR = BASE_DIR / "audio_queue"
PLAYED_DIR = BASE_DIR / "audio_played"
TMP_DIR = BASE_DIR / "tmp"

QUEUE_DIR.mkdir(exist_ok=True)
PLAYED_DIR.mkdir(exist_ok=True)
TMP_DIR.mkdir(exist_ok=True)
# ================================
# FastAPI app
# ================================

app = FastAPI()

# Allow Unity WebGL (or anything) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict later if needed
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Serve audio files statically (files inside audio_queue)
app.mount("/audio-files", StaticFiles(directory=str(QUEUE_DIR)), name="audio-files")

# ================================
# Data models
# ================================

class AudioTrack(BaseModel):
    name: str
    url: str
    created_at: str

class AudioTrackList(BaseModel):
    tracks: list[AudioTrack]

# --- Optional REST TTS endpoint models (gTTS) ---
class GenerateRequest(BaseModel):
    text: str
    lang: str = "en"

# ================================
# Helpers
# ================================

def list_queue_files():
    """Return sorted list of audio files in the queue."""
    files = [
        f for f in QUEUE_DIR.iterdir()
        if f.is_file()
        and not f.name.endswith(".tmp")  # ignore atomic-write temp files
    ]
    files.sort(key=lambda p: p.stat().st_mtime)  # Oldest first
    return files

def atomic_write_bytes(final_path: Path, data: bytes) -> None:
    """Write bytes atomically so consumers never see partial files."""
    tmp_path = final_path.with_suffix(final_path.suffix + f".{uuid.uuid4().hex}.tmp")
    with open(tmp_path, "wb") as out:
        out.write(data)
    os.replace(tmp_path, final_path)

# ================================
# API Endpoints (REST)
# ================================

@app.get("/audio/list", response_model=AudioTrackList)
async def get_audio_list():
    """
    List all audio files waiting to be played.
    Unity will poll this regularly.
    """
    tracks: list[AudioTrack] = []

    for f in list_queue_files():
        created = datetime.fromtimestamp(f.stat().st_mtime).isoformat()
        tracks.append(
            AudioTrack(
                name=f.name,
                url=f"/audio-files/{f.name}",  # Unity will prepend domain
                created_at=created,
            )
        )

    return AudioTrackList(tracks=tracks)

@app.post("/audio/mark-played")
async def mark_audio_played(name: str = Form(...)):
    """
    Unity calls this after it finishes playing a file.
    The file is moved to the 'audio_played' folder.
    """
    src = QUEUE_DIR / name
    if not src.exists():
        return JSONResponse({"status": "error", "detail": "file not found"}, status_code=404)

    dest = PLAYED_DIR / name
    src.rename(dest)

    return {"status": "ok", "file": name}

@app.post("/audio/upload")
async def upload_audio(file: UploadFile = File(...)):
    """
    Upload an audio file manually or from another app.
    Saved directly into the queue.
    """
    ext = os.path.splitext(file.filename)[1].lower()
    new_name = f"{uuid.uuid4().hex}{ext}"
    dest = QUEUE_DIR / new_name

    data = await file.read()
    atomic_write_bytes(dest, data)

    return {"status": "ok", "file": new_name}

# ===========================================
# Optional TTS Endpoint (using gTTS)
# ===========================================

try:
    from gtts import gTTS
except ImportError:
    gTTS = None

@app.post("/audio/generate")
async def generate_audio(req: GenerateRequest):
    """
    Generate audio from text using Google TTS (gTTS).
    Save the generated .mp3 file into the queue.
    """
    if gTTS is None:
        return JSONResponse(
            {"status": "error", "detail": "gTTS is not installed"},
            status_code=500
        )

    filename = f"{uuid.uuid4().hex}.mp3"
    dest = QUEUE_DIR / filename

    # gTTS saves directly; to keep atomic semantics, write to a tmp file then replace
    tmp_path = TMP_DIR / filename
    tts = gTTS(text=req.text, lang=req.lang)
    tts.save(str(tmp_path))
    os.replace(tmp_path, dest)

    return {"status": "ok", "file": filename}

# ===========================================
# WebSocket + LLM + SpeechT5 Integration
# ===========================================

# If these imports fail, install:
# pip install transformers datasets torch soundfile python-dotenv
from dotenv import load_dotenv
import soundfile as sf
import torch
from datasets import load_dataset
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

# Your helpers
from llmHelper import ask_foi_llm, dummy_foi_response

load_dotenv()

# Load models ONCE at import/startup (not per message)
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("nikolab/speecht5_tts_hr")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

embeddings_dataset = load_dataset("regisss/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

def generate_speech_to_queue(text: str) -> str:
    """
    Generate speech audio into QUEUE_DIR and return filename.
    Uses atomic write to avoid partial files being listed/played.
    """
    inputs = processor(text=text, return_tensors="pt")
    speech = model.generate_speech(
        inputs["input_ids"],
        speaker_embedding,
        vocoder=vocoder
    )

    filename = f"{uuid.uuid4().hex}.wav"
    final_path = QUEUE_DIR / filename

    # temp file must still look like WAV so soundfile knows the format
    tmp_path = TMP_DIR / filename

    sf.write(str(tmp_path), speech.cpu().numpy(), samplerate=16000)
    os.replace(str(tmp_path), str(final_path))  # atomic

    return filename

# Heavy work (LLM + TTS) should not block the async event loop.
executor = ThreadPoolExecutor(max_workers=1)

def llm_then_tts(user_message: str) -> dict:
    """
    Runs in a background thread (via executor).
    """
    answer = ask_foi_llm(user_message)
    print(f"LLM response: {answer}")
    lines = answer.splitlines()
    lines_array = [];
    for line in lines:
        audio_file = generate_speech_to_queue(line)
        lines_array.append(audio_file)
    return {"answer": answer, "file": lines_array}

@app.websocket("/")
async def ws_endpoint(ws: WebSocket):
    """
    WebSocket endpoint:
    - Receive text messages
    - Generate LLM answer + speech file into audio_queue
    - Respond with JSON containing answer + filename
    """
    await ws.accept()
    try:
        while True:
            message = await ws.receive_text()
            print(f"Incoming WS message: {message}")

            loop = asyncio.get_running_loop()
            try:
                result = await loop.run_in_executor(executor, llm_then_tts, message)
                await ws.send_json({"status": "ok", **result})
            except Exception as e:
                print(f"Error in LLM/TTS: {e}")
                fallback = dummy_foi_response()

                # Optional: also generate speech for fallback
                # fallback_file = generate_speech_to_queue(fallback)

                await ws.send_json({
                    "status": "error",
                    "detail": str(e),
                    "fallback": fallback,
                    # "file": fallback_file,
                })

    except WebSocketDisconnect:
        print("WebSocket disconnected")
