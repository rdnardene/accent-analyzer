import os
import whisper
from moviepy.editor import VideoFileClip

def extract_audio_from_file(video_path):
    audio_path = video_path.replace(".mp4", ".wav")
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path, codec='pcm_s16le')
    clip.close()
    return audio_path

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def classify_accent(text):
    british_keywords = ["lorry", "mate", "queue", "petrol", "boot", "holiday", "bloke", "rubbish", "cheers", "loo", "knackered", "dodgy", "chuffed", "quid", "skint", "snog", "naff"]
    american_keywords = ["truck", "apartment", "dude", "line", "gas", "cookie", "trunk", "vacation", "flat", "biscuit", "cool", "awesome", "diaper", "hair"]
    australian_keywords = ["arvo", "barbie", "mate", "servo", "thongs", "brekkie", "bogan", "mozzie", "How ya goin'?", "G'day", "Dunny", "Chook", "Esky", "Footy"]

    text_lower = text.lower()

    brit_score = sum(1 for word in british_keywords if word in text_lower)
    us_score = sum(1 for word in american_keywords if word in text_lower)
    aus_score = sum(1 for word in australian_keywords if word in text_lower)

    scores = {
        "British": brit_score,
        "American": us_score,
        "Australian": aus_score
    }

    top_accent = max(scores, key=scores.get)
    top_score = scores[top_accent]
    total_score = sum(scores.values()) + 0.001  # prevent division by zero

    if top_score == 0:
        return "Uncertain", 50.0  # The uploaded file will be "Uncertain" if the words used in the audio is not mentioned in def classify_accent(text)

    confidence = round(70 + 30 * (top_score / total_score), 2)
    return top_accent, confidence
