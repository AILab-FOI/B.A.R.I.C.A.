Initial implementation of LLMs into B.A.R.I.C.A.
================================================

This implementation is partially based on [PrivateGPT](https://github.com/zylon-ai/private-gpt).

The initial implementation of document harvesting was done by student [Domagoj Sabljic](https://github.com/dsabljic/PAP-FOI-docs).


# LLM-BARICA – How to Run

## 1. Create and activate virtual environment

### Windows (PowerShell):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If activation is blocked:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
### Linux / macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install requirements

Make sure the virtual environment is active, then run:
```
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Environment variables

Create a file named .env in the project root and add:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 4. Run the backend server

Start FastAPI with:
```
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Backend will be available at:
http://localhost:8000

WebSocket endpoint:
ws://localhost:8000/

## 5. Download and run WebGL frontend

Download the WebGL build from:
https://drive.google.com/file/d/1S3O0xDOcHYuN3AnOo0gYuZMJEiAWKCUE/view?usp=sharing

## 6. Extract the archive.

## 7. From the extracted directory, run:

```
python -m http.server 8080
```
Open in browser (must be chromium based):
http://localhost:8080

Notes:

- Do not run server.py separately

- All backend functionality is unified in main.py

- Unity/WebGL polls audio from the backend automatically
