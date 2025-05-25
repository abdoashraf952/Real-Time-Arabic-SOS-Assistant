# Real-Time-Arabic-SOS-Assistant
A real-time Arabic voice assistant built using FastAPI, AraT5 (transformer model), speech recognition, and text-to-speech (gTTS). It listens to Arabic speech, understands it using a fine-tuned NLP model, responds intelligently, and speaks the reply.
# 🧠 Arabic Voice Assistant using FastAPI + AraT5

This is a real-time Arabic voice assistant application that listens to the user via microphone, transcribes the speech using Google Speech Recognition, processes the input using a fine-tuned [AraT5](https://huggingface.co/UBC-NLP/AraT5-base) transformer model, and responds using text-to-speech (gTTS). It runs with a simple FastAPI backend.

---

## 🌟 Features

- 🎙️ Arabic speech recognition via `speech_recognition`
- 🤖 Arabic text generation using a fine-tuned `AraT5` model
- 🔊 Arabic voice reply with `gTTS`
- 🚀 FastAPI API to start and stop listening loop
- 🧠 All-NLP pipeline handled offline (except gTTS uses Google's service)

---

## 📦 Requirements

1. Python 3.8 or later
2. Microphone input supported
3. Install dependencies:

```bash
pip install -r requirements.txt
```
📂 Project Structure

```bash
project/
├── SOS_Api.py                 # FastAPI main app
├── models/
│   └── AraT5_finetuned_model/ # Your local fine-tuned model
├── requirements.txt
└── README.md
```
🔧 Example requirements.txt
```bash
fastapi
uvicorn
transformers
torch
gtts
playsound
SpeechRecognition
pyaudio
```
⚠️ PyAudio install tip:
If you're on Windows, and pyaudio fails to install via pip:

Download the .whl file from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Install it like this:

```bash
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
```

🚀 Running the API
```bash
uvicorn SOS_Api:app --host 0.0.0.0 --port 8000 --reload
```
🎯 API Endpoints

| Endpoint      | Method | Description                        |
| ------------- | ------ | ---------------------------------- |
| `/start-call` | POST   | Starts the voice assistant loop    |
| `/stop-call`  | POST   | Stops the assistant and microphone |

🧠 How It Works
The API starts a background thread to listen through your microphone.

Captures your Arabic speech and transcribes it via Google Speech API.

Sends the text to a fine-tuned AraT5 model for understanding.

Converts the response back to speech using gTTS.

Plays the audio response out loud.

📹 Demo
