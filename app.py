import streamlit as st
from utils import extract_audio_from_file, transcribe_audio, classify_accent
import os
import uuid

# Setup page
st.set_page_config(page_title="Accent Analyzer", layout="centered")
st.title("🎤 Accent Analyzer")
st.write("Upload a `.mp4`, `.mp3`, `.wav`, or `.mpeg` file to detect the speaker's English accent.")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# File upload
uploaded_file = st.file_uploader(
    "Upload a video or audio file",
    type=["mp4", "mp3", "wav", "mpeg"]
)

# Handle upload
if uploaded_file is not None:
    file_ext = uploaded_file.name.split(".")[-1]
    temp_path = f"temp_{uuid.uuid4()}.{file_ext}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Analyze"):
        with st.spinner("Processing..."):
            try:
                # Extract audio if it's a video
                if temp_path.endswith(".mp4"):
                    audio_path = extract_audio_from_file(temp_path)
                else:
                    audio_path = temp_path  # already audio

                # Transcribe and classify
                transcript = transcribe_audio(audio_path)
                accent, confidence = classify_accent(transcript)

                # Flags
                accent_flags = {
                    "American": "🇺🇸",
                    "British": "🇬🇧",
                    "Australian": "🇦🇺",
                    "Uncertain": "❓"   # The uploaded file will be "Uncertain" if the words used in the audio is not mentioned in def classify_accent(text)
                }
                flag = accent_flags.get(accent, "🌍")

                # Display results
                st.success("✅ Analysis Complete")
                st.markdown("### Transcript")
                st.text(transcript)

                st.markdown("### Accent Classification")
                st.markdown(f"**Accent:** {flag} {accent}")
                st.markdown(f"**Confidence Score:** {confidence}%")
                st.progress(int(confidence))
                st.markdown(f"**Summary:** The speech shows characteristics of a {accent} English accent.")

                st.markdown("### ▶️ Playback Extracted Audio")
                with open(audio_path, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/wav")

                # Save to history
                st.session_state.history.append({
                    "accent": accent,
                    "confidence": confidence,
                    "transcript": transcript[:100] + "..." if len(transcript) > 100 else transcript
                })

                # Cleanup
                if audio_path != temp_path:
                    os.remove(audio_path)
                os.remove(temp_path)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
