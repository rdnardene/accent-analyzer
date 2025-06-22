# 🎤 Accent Analyzer

A practical Streamlit-based tool to analyze spoken English from uploaded video or audio files. It detects the speaker's accent and returns a confidence score, making it useful for hiring assessments, interviews, and language analysis.

---

## 🔍 Features

- 📁 Upload support for `.mp4`, `.mp3`, `.wav`, `.mpeg`
- 🧠 Transcribes speech using OpenAI Whisper
- 🌍 Detects English accents:  
  - 🇺🇸 American  
  - 🇬🇧 British  
  - 🇦🇺 Australian
- 📊 Shows confidence score with a progress bar
- 🎧 Playback of extracted audio
- 🕓 Session-based analysis history for comparisons

---

## 💡 Project Purpose

This tool was developed as part of a hiring process to demonstrate the ability to build a working AI-based solution for analyzing spoken English accents from uploaded media files.

---

## 🚀 Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [MoviePy](https://zulko.github.io/moviepy/)
- FFmpeg (system-level dependency)

---

## 🛠 Installation

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/accent-analyzer.git
cd accent-analyzer


# 2. Create virtual environment & activate
python -m venv venv
-source venv/bin/activate


# 3. Install dependencies
pip install -r requirements.txt


# 4. Run the app
streamlit run app.py

### ⚠️ Notes Section  
This helps prevent errors (like FFmpeg or missing Python versions).
- Make sure [FFmpeg](https://ffmpeg.org/) is installed and added to your system PATH.
- Recommended Python version: **3.10+**
- If `streamlit run` doesn't stop, press `Ctrl + C` or close the terminal.
- The tool works offline — no API keys required.

# Requires FFmpeg to be installed and added to your system PATH.
# For .mp4 files, moviepy is used to extract the audio before transcription.
# Keyword-based accent detection allows fast, lightweight classification.




🧑‍💻 Author
# Developed by [Ardene Palima] as part of an AI Agent Solutions Engineer assessment for REM Waste.