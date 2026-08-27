import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.skill_gap import calculate_skill_gap
from utils.job_matcher import get_required_skills


st.title("Career Intelligence System")
st.write("Your AI-powered career analysis platform.")

target_job = st.text_input(
    "What job are you targeting?",
    placeholder="e.g. Machine Learning Engineer"
)

uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_resume:
    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_resume)

    cleaned_resume_text = clean_text(resume_text)

    detected_skills = extract_skills(cleaned_resume_text)

    if target_job:
        required_skills = get_required_skills(target_job)

        if required_skills:
            matched_skills, missing_skills = calculate_skill_gap(
                detected_skills,
                required_skills
            )

            st.subheader("Skill Gap Analysis")

            st.write("Matched Skills:")
            st.write(matched_skills)

            st.write("Missing Skills:")
            st.write(missing_skills)

        else:
            st.warning("Target job not found in our job database.")

    st.subheader("Detected Skills")
    st.write(detected_skills)

    st.subheader("Extracted Resume Text")
    st.text_area(
        "Resume content",
        resume_text,
        height=400
    )