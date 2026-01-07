from dotenv import load_dotenv
import os
import asyncio
import websockets
from llmHelper import ask_foi_llm, dummy_foi_response
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("nikolab/speecht5_tts_hr")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
embeddings_dataset = load_dataset("regisss/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

output_directory = "wav-output"

load_dotenv()

WS_HOST = os.getenv("WS_HOST", "localhost")
WS_PORT = int(os.getenv("WS_PORT", 8766))

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def get_latest_file_index():
    return max([int(f[1:f.index('.')]) for f in os.listdir(output_directory)])

def generate_speech(text):
    inputs = processor(text=text, return_tensors="pt")
    speech = model.generate_speech(
        inputs["input_ids"],
        speaker_embedding,
        vocoder=vocoder
    )

    filenames = next(os.walk(output_directory), (None, None, []))[2]
    
    output_filename = output_directory + "/o"
    if len(filenames) > 0:
        output_filename += str(get_latest_file_index() + 1)
    else:
        output_filename += "1"
    
    output_filename += ".wav"

    sf.write(output_filename, speech.cpu().numpy(), samplerate=16000)

async def handle_client(websocket):
    async for message in websocket:
        print(f": Incoming message from UI: {message}")

        try:
            answer = ask_foi_llm(message)
            print(f"LLM response: {answer}") 
            generate_speech(answer)
        except Exception as e:
            print(dummy_foi_response())
            print(f"Error in LLM: {e}")

async def main():
    async with websockets.serve(handle_client, WS_HOST, WS_PORT):
        print(f"LLM server running on ws://{WS_HOST}:{WS_PORT}")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())