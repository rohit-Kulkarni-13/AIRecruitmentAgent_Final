
import streamlit as st
from speech.stt import recognize_speech_from_mic
from speech.tts import speak
from agents.extractor_agent import extract_requirements
from agents.recommender_agent import recommend_services
from agents.writer_agent import generate_proposal

st.set_page_config(page_title="AI Recruitment Voice Agent", layout="wide")

st.title("🎙️ AI Recruitment Voice Assistant")

if st.button("🎤 Start Voice Input"):
    user_input = recognize_speech_from_mic()
    st.write("You said:", user_input)

    if user_input:
        # Step 1: Extract requirements
        extracted = extract_requirements(user_input)
        st.json(extracted)

        # Step 2: Recommend service
        recommendation = recommend_services(extracted)
        st.write("📦 Recommendation:", recommendation)

        # Step 3: Generate proposal
        proposal = generate_proposal(extracted)
        st.write("📄 Proposal:")
        st.text(proposal)

        # Speak out
        speak(recommendation)
        speak("Would you like to proceed with this proposal?")
