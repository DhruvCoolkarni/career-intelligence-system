import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.skill_gap import calculate_skill_gap
from utils.job_matcher import get_required_skills
from utils.skill_normalizer import normalize_skill
from utils.skill_priority import calculate_skill_priorities
from utils.learning_recommender import get_learning_recommendations
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


            priorities = calculate_skill_priorities(
                missing_skills,
                software_data,
                essential_data
            )


            recommendations = get_learning_recommendations(
                missing_skills
            )


            st.subheader("Career Readiness")

            st.caption(
                "Shows how closely your current skills match "
                "the skills expected for the selected career."
            )


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


            st.caption(
                "Technical Skills = match with job-related technologies. "
                "Core Skills = match with important workplace skills. "
                "Market Relevance = match with technologies marked "
                "In Demand or Hot Technology in O*NET."
            )


            st.subheader("Skill Gap Analysis")

            st.caption(
                "Shows which required skills you already have "
                "and which skills are missing from your resume."
            )


            st.write("Matched Skills:")
            st.write(matched_skills)


            st.write("Missing Skills:")
            st.write(missing_skills)


            st.subheader("Learning Priorities")

            st.caption(
                "Missing skills ranked by their importance "
                "and market relevance."
            )


            high_priority = [
                item for item in priorities
                if item["priority"] == "High"
            ]

            medium_priority = [
                item for item in priorities
                if item["priority"] == "Medium"
            ]

            low_priority = [
                item for item in priorities
                if item["priority"] == "Low"
            ]


            if high_priority:

                st.markdown("### 🔴 High Priority")

                st.caption(
                    "Skills that should receive attention first."
                )

                for item in high_priority:

                    st.write(
                        f"**{item['skill']}**"
                    )

                    st.caption(
                        f"Type: {item['type']} | "
                        f"Priority Score: "
                        f"{item['priority_score']}"
                    )

                    if item["type"] == "Core Skill":

                        st.caption(
                            f"O*NET Importance: "
                            f"{item['importance']}"
                        )

                    elif item["type"] == "Technical Skill":

                        st.caption(
                            f"In Demand: {item['in_demand']} | "
                            f"Hot Technology: "
                            f"{item['hot_technology']}"
                        )


            if medium_priority:

                st.markdown("### 🟠 Medium Priority")

                st.caption(
                    "Useful skills to learn after "
                    "the high-priority gaps."
                )

                for item in medium_priority:

                    st.write(
                        f"**{item['skill']}**"
                    )

                    st.caption(
                        f"Type: {item['type']} | "
                        f"Priority Score: "
                        f"{item['priority_score']}"
                    )


            if low_priority:

                st.markdown("### 🟢 Low Priority")

                st.caption(
                    "Lower-priority gaps that can "
                    "be addressed later."
                )

                for item in low_priority:

                    st.write(
                        f"**{item['skill']}**"
                    )

                    st.caption(
                        f"Type: {item['type']} | "
                        f"Priority Score: "
                        f"{item['priority_score']}"
                    )


            st.subheader("Personalized Learning Recommendations")

            st.caption(
                "Actionable learning paths for your missing skills, "
                "ordered by learning priority."
            )


            priority_lookup = {
                item["skill"]: item
                for item in priorities
            }


            actionable_recommendations = [
                recommendation
                for recommendation in recommendations
                if recommendation["level"] != "Not available"
            ]


            actionable_recommendations.sort(
                key=lambda recommendation: priority_lookup.get(
                    recommendation["skill"],
                    {}
                ).get("priority_score", 0),
                reverse=True
            )


            for recommendation in actionable_recommendations:

                skill = recommendation["skill"]

                priority_data = priority_lookup.get(
                    skill,
                    {}
                )

                priority = priority_data.get(
                    "priority",
                    "N/A"
                )

                priority_score = priority_data.get(
                    "priority_score",
                    "N/A"
                )


                if priority == "High":

                    priority_label = "🔴 High Priority"

                elif priority == "Medium":

                    priority_label = "🟠 Medium Priority"

                elif priority == "Low":

                    priority_label = "🟢 Low Priority"

                else:

                    priority_label = "⚪ Priority unavailable"


                st.markdown(
                    f"### {priority_label}"
                )

                st.markdown(
                    f"**{skill}**"
                )

                st.caption(
                    f"Priority Score: {priority_score}"
                )

                st.write(
                    f"**Level:** {recommendation['level']}"
                )

                st.write(
                    f"**Learning Path:** "
                    f"{recommendation['learning_path']}"
                )

                st.write(
                    f"**Project Idea:** "
                    f"{recommendation['project_idea']}"
                )

                st.divider()


            if not actionable_recommendations:

                st.info(
                    "No personalized learning recommendations "
                    "are currently available for your missing skills."
                )
            


        else:

            st.warning(
                "Target job not found in our job database."
            )


    st.subheader("Detected Skills")

    st.caption(
        "Skills identified from the text extracted "
        "from your resume."
    )

    st.write(detected_skills)


    st.subheader("Normalized Skills")

    st.caption(
        "Skills converted into standardized names so "
        "different terms can be matched consistently."
    )

    st.write(normalized_skills)


    st.subheader("Extracted Resume Text")

    st.caption(
        "The text extracted from your uploaded PDF resume."
    )

    st.text_area(
        "Resume content",
        resume_text,
        height=400
    )