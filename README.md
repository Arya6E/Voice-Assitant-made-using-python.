# 🗣️ Jack - Your Personal Voice Assistant

Jack is a simple voice assistant built with Python that can recognize your voice, search Wikipedia, open websites, and tell the time. It uses text-to-speech and speech recognition libraries for interaction.

---

## 💡 Features

- 👂 Voice recognition using your system's microphone
- 🧠 Searches Wikipedia and reads out summaries
- 🌐 Opens websites like:
  - YouTube
  - Google
  - Stack Overflow
  - Gmail
  - Google Maps
  - Spotify
- 🕒 Tells the current time
- 🗣️ Speaks responses using the `pyttsx3` TTS engine

---

## 🔧 Technologies Used

- `pyttsx3` – Text-to-Speech (offline)
- `speech_recognition` – For listening to voice
- `wikipedia` – To fetch summaries
- `webbrowser` – To open websites
- `datetime` – To get current time

---

## 🚀 How to Run

### 1. Install Dependencies

Use pip to install the required libraries:

```bash
pip install pyttsx3 speechrecognition wikipedia
