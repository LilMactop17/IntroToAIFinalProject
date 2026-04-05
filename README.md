# Intro to AI Final Project — WSL Setup & Run Guide

This guide walks you through running the project locally on **localhost:5000 using ONLY the WSL terminal**.

---

## STEP 1 — Open WSL
Open your WSL terminal (Ubuntu).

---

## STEP 2 — Go to Project Folder
```bash
cd ~/path/to/IntroToAIFinalProject-main
```
Replace the path above with your actual project location.

---

## STEP 3 — Check Python & pip
```bash
python3 --version
pip3 --version
```
If missing, install:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

## STEP 4 — Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```
You should now see `(venv)` in your terminal.

---

## STEP 5 — Install Dependencies
If `requirements.txt` exists:
```bash
pip install -r requirements.txt
```
If NOT:
```bash
pip install flask
```

---

## STEP 6 — Set Flask Environment
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
If your main file is not `app.py`, replace it accordingly.

---

## STEP 7 — Run the Server (Port 5000)
```bash
flask run --host=0.0.0.0 --port=5000
```
If that fails:
```bash
python3 -m flask run --host=0.0.0.0 --port=5000
```

---

## STEP 8 — Open in Browser
Go to:
```
http://localhost:5000
```

---

## ROUBLESHOOTING

### Port 5000 Already in Use
```bash
sudo lsof -i :5000
kill -9 <PID>
```

### Flask Not Found
```bash
pip install flask
```

### Missing Modules
```bash
pip install -r requirements.txt
```

### Virtual Environment Not Activating
```bash
source venv/bin/activate
```

---

## Expected Project Structure
```
.
├── app.py
├── requirements.txt
├── templates/
├── static/
└── README.md
```

---

## ✅ FINAL NOTES
- Everything runs inside **WSL only**
- No need for Windows Command Prompt or PowerShell
- Accessible in Windows browser via `localhost:5000`

---

## QUICK RUN (After First Setup)
```bash
cd ~/path/to/IntroToAIFinalProject-main
source venv/bin/activate
flask run --host=0.0.0.0 --port=5000
```
