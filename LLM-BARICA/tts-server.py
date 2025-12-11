import socket
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from os import walk, path, makedirs, listdir

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 8089))
serversocket.listen(5)

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("nikolab/speecht5_tts_hr")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
embeddings_dataset = load_dataset("regisss/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

output_directory = "wav-output"

def get_latest_file_index():
    return max([int(f[1:f.index('.')]) for f in listdir(output_directory)])


if not path.exists(output_directory):
    makedirs(output_directory)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(4096)
    if len(buf) > 0:
        inputs = processor(text=buf.decode(), return_tensors="pt")

        speech = model.generate_speech(
            inputs["input_ids"],
            speaker_embedding,
            vocoder=vocoder
        )

        filenames = next(walk(output_directory), (None, None, []))[2]
        
        output_filename = output_directory + "/o"
        if len(filenames) > 0:
            output_filename += str(get_latest_file_index() + 1)
        else:
            output_filename += "1"
        
        output_filename += ".wav"

        sf.write(output_filename, speech.cpu().numpy(), samplerate=16000)
