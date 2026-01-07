from dotenv import load_dotenv
import os
from openai import OpenAI
import numpy as np
import json
from pathlib import Path
from TextHelper import TextHelper
import pandas as pd


BASE_DIR = Path(__file__).parent
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not available in .env")

client = OpenAI(api_key=OPENAI_API_KEY)

with open(BASE_DIR / "rag_data.json", encoding="utf-8") as f:
    rag_data = json.load(f)

chunks = []
metadata = []

for b in rag_data["buildings"].values():
    text = f"Building: {b['name']}"
    chunks.append(text)
    metadata.append({"type": "building", "content": text})

for r in rag_data["rooms"].values():
    text = f"Room: {r['name']}, Floor: {r['floor']}, Wing: {r['wing']}, Building: {r['building']}"
    chunks.append(text)
    metadata.append({"type": "room", "content": text})

for name, e in rag_data["employees"].items():
    text = (
        f"Professor: {name}, Department: {e['department']}, Location: {e['location']}, "
        f"Email: {e['email']}, Phone: {e['phone']}, "
        f"Consultations: {', '.join(e['consultations'])}, "
        f"Subjects: {', '.join(e['subjects'][:10])}..."
    )
    chunks.append(text)
    metadata.append({"type": "professor", "content": text})

for tf in rag_data["teaching_forms"].values():
    text = f"Teaching Form: {tf}"
    chunks.append(text)
    metadata.append({"type": "teaching_form", "content": text})

metadata = pd.DataFrame(metadata)

embeddings = []
for chunk in chunks:
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    ).data[0].embedding
    embeddings.append(np.array(emb))

embeddings = np.array(embeddings)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query: str, top_k=5):
    query_emb = np.array(client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding)
    
    sims = [(i, cosine_similarity(query_emb, emb)) for i, emb in enumerate(embeddings)]
    sims.sort(key=lambda x: x[1], reverse=True)
    
    results = [metadata.iloc[i]["content"] for i, _ in sims[:top_k]]
    return results


def ask_foi_llm(question: str) -> str:
    context_chunks = retrieve(question, top_k=10)

    prof_name = None
    words = question.split()
    if "prof" in question.lower() or "profesor" in question.lower():
        prof_name = " ".join(words[-2:])  

    if prof_name:
        prof_chunks = [c for c in context_chunks if prof_name.lower() in c.lower()]
        if prof_chunks:
            context_chunks = prof_chunks + [c for c in context_chunks if c not in prof_chunks]

    system_prompt = (
        "Ti si Barica, stručna AI asistentica koja odgovara na pitanja o FOI.\n"
        "Odgovaraj isključivo na temelju dostupnih podataka koje ti dam.\n"
        "Odgovaraj isključivo na hrvatskom jeziku.\n"
        "Svaka rečenica odgovora mora biti u novom redu.\n"
        "Odgovor mora biti sažet i informativan.\n"
        "Zamijeni sve brojke riječima ukoliko se pojavljuju u odgovoru."
    )

    user_prompt = f"Pitanje: {question}\n\nRelevantne informacije:\n"
    for i, chunk in enumerate(context_chunks, start=1):
        user_prompt += f"[Izvor {i}]\n{chunk}\n\n"
    user_prompt += "Na temelju ovih informacija, odgovori na pitanje."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return TextHelper.remove_croatian_chars(response.choices[0].message.content)


def dummy_foi_response() -> str: 
    dummy_text = (
        "FOI je smješten u tri prostrane zgrade u centru grada Varaždina.\n"
        "Prostorni uvjeti omogućuju primjenu europskih standarda za izvođenje nastave.\n"
        "Na FOI-ju se provodi mnogo praktične nastave iz informatike.\n"
        "U praktičnoj nastavi svaki student raspolaže računalom i pristupom internetu."
    )
    return TextHelper.remove_croatian_chars(dummy_text)