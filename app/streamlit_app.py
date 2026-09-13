import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.skill_gap import calculate_skill_gap
from utils.job_matcher import get_required_skills
from utils.skill_normalizer import normalize_skill
from utils.career_scores import (
    calculate_technical_score,
    calculate_core_skill_score,
    calculate_market_relevance_score,
    calculate_career_readiness
)
from utils.onet_loader import (
    get_software_skills_for_job,
    get_essential_skills_for_job
)


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

    normalized_skills = [
        normalize_skill(skill)
        for skill in detected_skills
    ]


    if target_job:
        required_skills = get_required_skills(target_job)

        if required_skills:

            matched_skills, missing_skills = calculate_skill_gap(
                detected_skills,
                required_skills
            )

            software_data = get_software_skills_for_job(
                target_job
            )

            essential_data = get_essential_skills_for_job(
                target_job
            )


            technical_score = calculate_technical_score(
                detected_skills,
                required_skills
            )

            core_skill_score = calculate_core_skill_score(
                detected_skills,
                essential_data
            )

            market_score = calculate_market_relevance_score(
                software_data,
                detected_skills
            )

            career_score = calculate_career_readiness(
                technical_score,
                core_skill_score,
                market_score
            )


            st.subheader("Career Readiness")


            col1, col2, col3, col4 = st.columns(4)


            col1.metric(
                "Overall Readiness",
                f"{career_score}%"
            )

            col2.metric(
                "Technical Skills",
                f"{technical_score}%"
            )

            col3.metric(
                "Core Skills",
                f"{core_skill_score}%"
            )

            col4.metric(
                "Market Relevance",
                f"{market_score}%"
            )


            st.subheader("Skill Gap Analysis")


            st.write("Matched Skills:")
            st.write(matched_skills)


            st.write("Missing Skills:")
            st.write(missing_skills)


        else:
            st.warning(
                "Target job not found in our job database."
            )


    st.subheader("Detected Skills")
    st.write(detected_skills)


    st.subheader("Normalized Skills")
    st.write(normalized_skills)


    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume content",
        resume_text,
        height=400
    )