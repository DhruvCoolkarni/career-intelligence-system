import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.skill_gap import calculate_skill_gap
from utils.skill_normalizer import normalize_skill
from utils.skill_priority import calculate_skill_priorities
from utils.learning_recommender import get_learning_recommendations
from utils.roadmap_builder import build_learning_roadmap
from utils.knowledge_matcher import calculate_knowledge_evidence

from utils.career_scores import (
    calculate_technical_score,
    calculate_core_skill_score,
    calculate_market_relevance_score,
    calculate_knowledge_score,
    calculate_career_readiness
)

from utils.onet_loader import (
    get_software_skills_for_job,
    get_essential_skills_for_job
)

from utils.job_matcher import (
    get_required_skill_data
)


st.title("Career Intelligence System")

st.write(
    "Your AI-powered career analysis platform."
)


# ------------------------------------------------
# USER INPUT
# ------------------------------------------------

target_job = st.text_input(
    "What job are you targeting?",
    placeholder="e.g. Machine Learning Engineer"
)


uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


# ------------------------------------------------
# RESUME PROCESSING
# ------------------------------------------------

if uploaded_resume:

    st.success(
        "Resume uploaded successfully!"
    )

    resume_text = extract_text_from_pdf(
        uploaded_resume
    )

    cleaned_resume_text = clean_text(
        resume_text
    )

    detected_skills = extract_skills(
        cleaned_resume_text
    )

    normalized_skills = [
        normalize_skill(skill)
        for skill in detected_skills
    ]


    # ------------------------------------------------
    # CAREER ANALYSIS
    # ------------------------------------------------

    if target_job:

        required_skill_data = get_required_skill_data(
            target_job
        )

        required_skills = [
            item["skill"]
            for item in required_skill_data
        ]


        if required_skills:

            # ------------------------------------------------
            # SKILL GAP
            # ------------------------------------------------

            matched_skills, missing_skills = calculate_skill_gap(
                detected_skills,
                required_skills
            )


            # ------------------------------------------------
            # O*NET DATA
            # ------------------------------------------------

            software_data = get_software_skills_for_job(
                target_job
            )

            essential_data = get_essential_skills_for_job(
                target_job
            )


            # ------------------------------------------------
            # TECHNICAL SCORE
            # ------------------------------------------------

            technical_score = calculate_technical_score(
                detected_skills,
                required_skill_data
            )


            # ------------------------------------------------
            # CORE SKILL SCORE
            # ------------------------------------------------

            core_skill_score = calculate_core_skill_score(
                detected_skills,
                essential_data
            )


            # ------------------------------------------------
            # MARKET RELEVANCE SCORE
            # ------------------------------------------------

            market_relevance_score = calculate_market_relevance_score(
                software_data,
                detected_skills
            )


            # ------------------------------------------------
            # KNOWLEDGE SCORE
            # ------------------------------------------------

            knowledge_data = pd.read_csv(
                "data/onet/knowledge.csv"
            )

            knowledge_data = knowledge_data[
                knowledge_data["Title"].str.lower()
                == target_job.lower()
            ]


            knowledge_scores = calculate_knowledge_evidence(
                detected_skills,
                knowledge_data
            )


            knowledge_score = calculate_knowledge_score(
                knowledge_scores
            )


            # ------------------------------------------------
            # FINAL CAREER READINESS
            # ------------------------------------------------

            career_score = calculate_career_readiness(
                technical_score,
                core_skill_score,
                knowledge_score,
                market_relevance_score
            )


            # ------------------------------------------------
            # LEARNING PRIORITIES
            # ------------------------------------------------

            priorities = calculate_skill_priorities(
                missing_skills,
                software_data,
                essential_data
            )


            # ------------------------------------------------
            # LEARNING RECOMMENDATIONS
            # ------------------------------------------------

            recommendations = get_learning_recommendations(
                missing_skills
            )


            # ------------------------------------------------
            # LEARNING ROADMAP
            # ------------------------------------------------

            roadmap = build_learning_roadmap(
                recommendations,
                priorities
            )


            # =================================================
            # CAREER READINESS
            # =================================================

            st.subheader(
                "Career Readiness"
            )

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
                f"{market_relevance_score}%"
            )


            st.caption(
                "Technical Skills = match with job-related technologies. "
                "Core Skills = match with important workplace skills. "
                "Knowledge = evidence of relevant knowledge areas. "
                "Market Relevance = match with technologies marked "
                "In Demand or Hot Technology in O*NET."
            )


            # =================================================
            # READINESS BREAKDOWN
            # =================================================

            st.subheader(
                "Readiness Breakdown"
            )

            st.caption(
                "Visual comparison of your overall readiness "
                "and the factors used to calculate it."
            )


            readiness_data = {
                "Overall Readiness": career_score,
                "Technical Skills": technical_score,
                "Core Skills": core_skill_score,
                "Knowledge": knowledge_score,
                "Market Relevance": market_relevance_score
            }


            fig = go.Figure(
                data=[
                    go.Bar(
                        x=list(
                            readiness_data.keys()
                        ),
                        y=list(
                            readiness_data.values()
                        ),
                        text=[
                            f"{score}%"
                            for score in readiness_data.values()
                        ],
                        textposition="auto"
                    )
                ]
            )


            fig.update_layout(
                yaxis_title="Score (%)",
                yaxis=dict(
                    range=[0, 100]
                ),
                xaxis_title="Career Analysis",
                height=450
            )


            st.plotly_chart(
                fig,
                use_container_width=True,
                key="readiness_breakdown_chart"
            )


            # =================================================
            # SKILL GAP ANALYSIS
            # =================================================

            st.subheader(
                "Skill Gap Analysis"
            )

            st.caption(
                "Shows which required skills you already have "
                "and which skills are missing from your resume."
            )


            st.write(
                "Matched Skills:"
            )

            st.write(
                matched_skills
            )


            st.subheader(
                "Skill Gap Overview"
            )

            st.caption(
                "Comparison between the skills you already have "
                "and the skills missing for your target career."
            )


            skill_gap_data = {
                "Matched Skills": len(
                    matched_skills
                ),
                "Missing Skills": len(
                    missing_skills
                )
            }


            skill_gap_fig = go.Figure(
                data=[
                    go.Pie(
                        labels=list(
                            skill_gap_data.keys()
                        ),
                        values=list(
                            skill_gap_data.values()
                        ),
                        hole=0.45,
                        textinfo="label+percent"
                    )
                ]
            )


            skill_gap_fig.update_layout(
                height=400
            )


            st.plotly_chart(
                skill_gap_fig,
                use_container_width=True,
                key="skill_gap_overview_chart"
            )


            st.write(
                "Missing Skills:"
            )

            st.write(
                missing_skills
            )


            # =================================================
            # LEARNING PRIORITIES
            # =================================================

            st.subheader(
                "Learning Priorities"
            )

            st.caption(
                "Missing skills ranked by their importance "
                "and market relevance."
            )


            high_priority = [
                item
                for item in priorities
                if item["priority"] == "High"
            ]


            medium_priority = [
                item
                for item in priorities
                if item["priority"] == "Medium"
            ]


            low_priority = [
                item
                for item in priorities
                if item["priority"] == "Low"
            ]


            # ------------------------------------------------
            # HIGH PRIORITY
            # ------------------------------------------------

            if high_priority:

                st.markdown(
                    "### 🔴 High Priority"
                )

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
                            f"In Demand: "
                            f"{item['in_demand']} | "
                            f"Hot Technology: "
                            f"{item['hot_technology']}"
                        )


            # ------------------------------------------------
            # MEDIUM PRIORITY
            # ------------------------------------------------

            if medium_priority:

                st.markdown(
                    "### 🟠 Medium Priority"
                )

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


            # ------------------------------------------------
            # LOW PRIORITY
            # ------------------------------------------------

            if low_priority:

                st.markdown(
                    "### 🟢 Low Priority"
                )

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


            # =================================================
            # PRIORITY DISTRIBUTION
            # =================================================
            # IMPORTANT:
            # This is OUTSIDE the priority loops.
            # Therefore the chart is created only once.

            st.subheader(
                "Priority Distribution"
            )

            st.caption(
                "Number of missing skills in each priority level."
            )


            priority_data = {
                "High Priority": len(
                    high_priority
                ),
                "Medium Priority": len(
                    medium_priority
                ),
                "Low Priority": len(
                    low_priority
                )
            }


            priority_fig = go.Figure(
                data=[
                    go.Bar(
                        x=list(
                            priority_data.keys()
                        ),
                        y=list(
                            priority_data.values()
                        ),
                        text=list(
                            priority_data.values()
                        ),
                        textposition="auto"
                    )
                ]
            )


            priority_fig.update_layout(
                yaxis_title="Number of Missing Skills",
                xaxis_title="Priority Level",
                height=400
            )


            st.plotly_chart(
                priority_fig,
                use_container_width=True,
                key="priority_distribution_chart"
            )


            # =================================================
            # CAREER LEARNING ROADMAP
            # =================================================

            st.subheader(
                "Career Learning Roadmap"
            )

            st.caption(
                "A step-by-step learning sequence created from "
                "your missing skills, learning levels, and priorities."
            )


            phase_icons = {
                "Phase 1 — Foundations": "🟢",
                "Phase 2 — Intermediate Skills": "🟠",
                "Phase 3 — Advanced Skills": "🔴"
            }


            for phase, skills in roadmap.items():

                icon = phase_icons.get(
                    phase,
                    "📚"
                )


                st.markdown(
                    f"### {icon} {phase}"
                )


                if not skills:

                    st.info(
                        "No learning items available for this phase."
                    )

                    continue


                for item in skills:

                    priority = item["priority"]


                    if priority == "High":

                        priority_label = "🔴 High"

                    elif priority == "Medium":

                        priority_label = "🟠 Medium"

                    else:

                        priority_label = "🟢 Low"


                    st.markdown(
                        f"**{item['skill']}** — "
                        f"{priority_label}"
                    )


                    st.caption(
                        f"Priority Score: "
                        f"{item['priority_score']}"
                    )


                    st.write(
                        f"**Learning Path:** "
                        f"{item['learning_path']}"
                    )


                    st.write(
                        f"**Project:** "
                        f"{item['project_idea']}"
                    )


                    st.divider()


            # =================================================
            # PERSONALIZED LEARNING RECOMMENDATIONS
            # =================================================

            st.subheader(
                "Personalized Learning Recommendations"
            )

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
                ).get(
                    "priority_score",
                    0
                ),
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
                    f"**Level:** "
                    f"{recommendation['level']}"
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


    # =================================================
    # DETECTED SKILLS
    # =================================================

    st.subheader(
        "Detected Skills"
    )

    st.caption(
        "Skills identified from the text extracted "
        "from your resume."
    )

    st.write(
        detected_skills
    )


    # =================================================
    # NORMALIZED SKILLS
    # =================================================

    st.subheader(
        "Normalized Skills"
    )

    st.caption(
        "Skills converted into standardized names so "
        "different terms can be matched consistently."
    )

    st.write(
        normalized_skills
    )


    # =================================================
    # EXTRACTED TEXT
    # =================================================

    st.subheader(
        "Extracted Resume Text"
    )

    st.caption(
        "The text extracted from your uploaded PDF resume."
    )

    st.text_area(
        "Resume content",
        resume_text,
        height=400
    )