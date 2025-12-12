from dotenv import load_dotenv
import os
from openai import OpenAI
from TextHelper import TextHelper

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not available in .env")

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_foi_llm(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Ti si Barica, stručna AI asistentica koja odgovara na pitanja o Fakultetu organizacije i informatike Varaždin," +
                    "FOI, Sveučilište u Zagrebu." +
                    "Odgovaraj isključivo na temelju dostupnih podataka. Odgovaraj isključivo na hrvatskom jeziku." +
                    "Odgovor isključivo mora biti bez rednih brojeva, lista, skraćenica i brojevi moraju biti napisani slovima." +
                    "Svaka rečenica odgovora mora biti u novom redu." +
                    "Tvoj odgovor će se dalje procesuirati računalno i pretvarati u audio." +
                    "Zamijeni sve brojke riječima ukoliko su takve u kontekstu."
                    "Odgovaraj sažeto."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    response_without_croatian_characters = TextHelper.remove_croatian_chars(response.choices[0].message.content)
    return response_without_croatian_characters

def dummy_foi_response() -> str: 
    dummy_text = (
        "FOI je smješten u tri prostrane zgrade u centru grada Varaždina.\n"
        "Prostorni uvjeti omogućuju primjenu europskih standarda za izvođenje nastave.\n"
        "Na FOI-ju se provodi mnogo praktične nastave iz informatike.\n"
        "U praktičnoj nastavi svaki student raspolaže računalom i pristupom internetu."
    )

    return TextHelper.remove_croatian_chars(dummy_text)
