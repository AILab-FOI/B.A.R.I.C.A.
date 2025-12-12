import os
import uuid
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, UploadFile, File, Form
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

QUEUE_DIR.mkdir(exist_ok=True)
PLAYED_DIR.mkdir(exist_ok=True)

# ================================
# FastAPI app
# ================================

app = FastAPI()

# Allow Unity WebGL to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development; restrict later if needed
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Serve audio files statically
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

# ================================
# Helpers
# ================================

def list_queue_files():
    """Return sorted list of audio files in the queue."""
    files = [f for f in QUEUE_DIR.iterdir() if f.is_file()]
    files.sort(key=lambda p: p.stat().st_mtime)  # Oldest first
    return files

# ================================
# API Endpoints
# ================================

@app.get("/audio/list", response_model=AudioTrackList)
async def get_audio_list():
    """
    List all audio files waiting to be played.
    Unity will poll this regularly.
    """
    tracks = []

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

    with open(dest, "wb") as out:
        out.write(await file.read())

    return {"status": "ok", "file": new_name}


# ===========================================
# Optional TTS Endpoint (using gTTS)
# ===========================================

try:
    from gtts import gTTS
except ImportError:
    gTTS = None

class GenerateRequest(BaseModel):
    text: str
    lang: str = "en"

@app.post("/audio/generate")
async def generate_audio(req: GenerateRequest):
    """
    Generate audio from text using Google TTS.
    Save the generated .mp3 file into the queue.
    """
    if gTTS is None:
        return JSONResponse(
            {"status": "error", "detail": "gTTS is not installed"},
            status_code=500
        )

    filename = f"{uuid.uuid4().hex}.mp3"
    dest = QUEUE_DIR / filename

    tts = gTTS(text=req.text, lang=req.lang)
    tts.save(str(dest))

    return {"status": "ok", "file": filename}
