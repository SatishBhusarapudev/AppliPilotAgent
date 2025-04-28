import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from agent.apply_agent import generate_cover_letter
import streamlit as st
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

# --- Helper: save letter to timestamped file ---
def save_application_to_file(letter: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"application_{timestamp}.txt"
    path = os.path.join(os.getcwd(), filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(letter)
    return path

st.set_page_config(page_title="ApplyPilot", page_icon="✉️")

st.title("ApplyPilot — Job Application Letter Generator")

with st.form("application_form"):
    resume_text = st.text_area("Paste your Resume", height=150)
    job_description = st.text_area("Paste Job Description", height=150)
    model = st.selectbox("Model", ["gpt-4o", "gpt-3.5-turbo"])
    submit = st.form_submit_button("Generate Letter")

if submit:
    if not resume_text or not job_description:
        st.error("Please provide both resume and job description.")
    else:
        with st.spinner("Generating…"):
            letter = generate_cover_letter(resume_text, job_description, model)
        st.success("✅ Application Letter Generated")
        st.code(letter, language="markdown")

        # Save to file
        file_path = save_application_to_file(letter)
        st.markdown(f"Saved to `{file_path}`")

        # Download button
        with open(file_path, "rb") as file:
            btn = st.download_button(
                label="Download Letter",
                data=file,
                file_name=os.path.basename(file_path),
                mime="text/plain"
            )
