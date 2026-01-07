import csv
import json
import os
from pathlib import Path


BASE_DIR = Path(__file__).parent

BUILDINGS_CSV = BASE_DIR / "foi_buildings.csv"
EMPLOYEES_CSV = BASE_DIR / "foi_employees.csv"
ROOMS_CSV = BASE_DIR / "foi_rooms.csv"
TEACHING_FORMS_CSV = BASE_DIR / "foi_teaching_forms.csv"

OUTPUT_JSON = BASE_DIR / "rag_data.json"

def read_csv(file_path):
    with open(file_path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def prepare_rag():
    rag = {}

    buildings = read_csv(BUILDINGS_CSV)
    rag["buildings"] = {b["id"]: {"name": b["name"], "hrId": b.get("hrId", "")} for b in buildings}

    rooms = read_csv(ROOMS_CSV)
    rag["rooms"] = {}
    for r in rooms:
        rag["rooms"][r["id"]] = {
            "name": r["name"],
            "floor": r["floor"],
            "wing": r["wing"],
            "number": r["number"],
            "capacity": r.get("capacity", ""),
            "building": rag["buildings"].get(r["building_id"], {}).get("name", "")
        }

    employees = read_csv(EMPLOYEES_CSV)
    rag["employees"] = {}
    for e in employees:
        try:
            consultations = eval(e.get("consultations", "[]"))
        except:
            consultations = []
        try:
            subjects = eval(e.get("subjects", "[]"))
        except:
            subjects = []

        rag["employees"][e["name"]] = {
            "url": e["url"],
            "location": e["Lokacija"],
            "department": e["Pripadnost odjelima"],
            "email": e["Email adresa"],
            "phone": e["Telefon"],
            "consultations": consultations,
            "subjects": subjects
        }

    teaching_forms = read_csv(TEACHING_FORMS_CSV)
    rag["teaching_forms"] = {tf["id"]: tf["name"] for tf in teaching_forms}

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(rag, f, indent=2, ensure_ascii=False)

    print(f"RAG JSON saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    prepare_rag()
