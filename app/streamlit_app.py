import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(
    page_title="Career Intelligence System",
    page_icon="🎯",
    layout="wide"
)

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.skill_gap import calculate_skill_gap
from utils.skill_normalizer import (
    normalize_skill,
    normalize_skills
)
from utils.skill_priority import calculate_skill_priorities
from utils.learning_recommender import get_learning_recommendations
from utils.roadmap_builder import build_learning_roadmap
from utils.knowledge_matcher import calculate_knowledge_evidence
from utils.core_skill_matcher import (
    calculate_core_skill_evidence
)
from utils.career_scores import (
    calculate_technical_score,
    calculate_core_skill_score,
    calculate_career_market_relevance_score,
    calculate_knowledge_score,
    calculate_career_readiness
)

from utils.onet_loader import (
    get_software_skills_for_job,
    get_essential_skills_for_job
)

from utils.technical_requirements import (
    get_technical_requirements
)

from utils.career_profile import (
    get_career_profile
)

from utils.career_search import search_careers
from utils.career_catalog import CAREER_CATALOG

# ------------------------------------------------
# MODERN UI STYLING
# ------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(70, 110, 255, 0.16),
            transparent 28%
        ),
        radial-gradient(
            circle at 85% 25%,
            rgba(130, 80, 255, 0.13),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 85%,
            rgba(40, 160, 255, 0.08),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #070b18 0%,
            #0b1020 45%,
            #0a0d1a 100%
        );
}

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;

        background-image:
            linear-gradient(
                rgba(255,255,255,0.025) 1px,
                transparent 1px
            ),
            linear-gradient(
                90deg,
                rgba(255,255,255,0.025) 1px,
                transparent 1px
            );

        background-size: 70px 70px;
        mask-image: linear-gradient(
            to bottom,
            black,
            transparent 80%
        );

        z-index: 0;
    }

    /* Main content */
    .block-container {
        position: relative;
        z-index: 1;
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Headings */
    h1 {
        font-size: 3rem !important;
        font-weight: 750 !important;
        letter-spacing: -1px;
    }

    h2, h3 {
        font-weight: 650 !important;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(10px);
    }

    div[data-testid="stMetricLabel"] {
        font-size: 0.9rem;
    }

    div[data-testid="stMetricValue"] {
        font-weight: 700;
    }

    /* Input fields */
    div[data-baseweb="input"],
    div[data-baseweb="select"] {
        border-radius: 12px;
    }

    /* File uploader */
    div[data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.04);
        border: 1px dashed rgba(255, 255, 255, 0.20);
        border-radius: 16px;
        padding: 10px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        font-weight: 650;
        padding: 0.65rem 1.5rem;
        border: none;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* Dividers */
    hr {
        border-color: rgba(255, 255, 255, 0.08);
    }

    /* Footer */
    .creator-footer {
        text-align: center;
        margin-top: 60px;
        padding: 30px 0 10px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.65);
    }

    .creator-name {
        font-size: 1.05rem;
        font-weight: 650;
        color: rgba(255, 255, 255, 0.90);
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("Career Intelligence System")

st.write(
    "Understand your career readiness. "
    "Discover skill gaps. Build your learning path."
)


# ------------------------------------------------
# CAREER TARGET & RESUME
# ------------------------------------------------

input_col1, input_col2 = st.columns(
    [1, 1],
    gap="large"
)


with input_col1:

    st.markdown("**Target Career**")

    selection_mode = st.radio(
        "Choose how you want to find your career",
        ["🔍 Search", "📋 Browse"],
        horizontal=True,
        label_visibility="collapsed"
    )

    target_job = None

    if selection_mode == "🔍 Search":

        target_job_input = st.text_input(
            "Search career, skill, or technology",
            placeholder="e.g. Python, AI, software developer",
            label_visibility="collapsed"
        )

        career_suggestions = search_careers(
            target_job_input
        )

        if career_suggestions:

            st.caption("Suggested Careers")

            target_job = st.radio(
                "Choose a career",
                career_suggestions,
                label_visibility="collapsed"
            )

    else:

        available_careers = list(
            CAREER_CATALOG.keys()
        )

        target_job = st.selectbox(
            "Select a career",
            ["Select a career"] + available_careers,
            label_visibility="collapsed"
        )

        if target_job == "Select a career":
            target_job = None
    

with input_col2:

    uploaded_resume = st.file_uploader(
        "Upload Your Resume",
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

    # ------------------------------------------------
    # SKILL EXTRACTION
    # ------------------------------------------------

    detected_skills = extract_skills(
        cleaned_resume_text
    )


    # ------------------------------------------------
    # REVIEW DETECTED SKILLS
    # ------------------------------------------------

    st.subheader("Review Detected Skills")

    st.write(
        "Review the skills detected from your resume. "
        "Remove any skill that does not accurately "
        "represent your current skills."
    )

    st.caption(
    "These skills are extracted from your resume. "
    "Your scores are calculated only from the skills you confirm."
    )

    confirmed_skills = []


    for skill in detected_skills:

        keep_skill = st.checkbox(
            skill,
            value=True,
            key=f"skill_{skill}"
        )

        if keep_skill:
            confirmed_skills.append(skill)


    user_skills = normalize_skills(
        confirmed_skills
    )

    normalized_skills = [
        normalize_skill(skill)
        for skill in confirmed_skills
    ]

    # ------------------------------------------------
    # CAREER ANALYSIS
    # ------------------------------------------------

    if target_job:

        target_job_clean = target_job.strip()

        career_profile = get_career_profile(
            target_job_clean
        )
        technical_requirements = (
            get_technical_requirements(
                target_job_clean
            )
        )

        required_skills = [
            item["skill"]
            for item in technical_requirements
        ]


        # ------------------------------------------------
        # O*NET DATA
        # ------------------------------------------------

        onet_job = (
            career_profile["onet_title"]
            if career_profile
            else target_job_clean
        )

        software_data = get_software_skills_for_job(
            target_job_clean
        )

        essential_data = get_essential_skills_for_job(
            target_job_clean
        )

        # ------------------------------------------------
        # SKILL ANALYSIS
        # ------------------------------------------------
        if required_skills:

            # ------------------------------------------------
            # SKILL GAP
            # ------------------------------------------------

            matched_skills, missing_skills = (
                calculate_skill_gap(
                    confirmed_skills,
                    required_skills
                )
            )


            # ------------------------------------------------
            # TECHNICAL SCORE
            # ------------------------------------------------

            technical_score = (
                calculate_technical_score(
                    user_skills,
                    technical_requirements
                )
            )


            # ------------------------------------------------
            # CORE SKILL SCORE
            # ------------------------------------------------

            core_skill_evidence = calculate_core_skill_evidence(
                cleaned_resume_text,
                essential_data
            )

            core_skill_score = calculate_core_skill_score(
                core_skill_evidence
            )



            # ------------------------------------------------
            # MARKET RELEVANCE SCORE
            # ------------------------------------------------

            market_relevance_result = calculate_career_market_relevance_score(
                software_data,
                confirmed_skills,
                target_job_clean
            )

            market_relevance_score = (
                market_relevance_result["score"]
            )

            matched_market_groups = (
                market_relevance_result["matched_groups"]
            )

            missing_market_groups = (
                market_relevance_result["missing_groups"]
            )

            # ------------------------------------------------
            # KNOWLEDGE SCORE
            # ------------------------------------------------

            knowledge_data = pd.read_csv(
                "data/onet/knowledge.csv"
            )

            knowledge_data = knowledge_data[
                knowledge_data["Title"].str.lower().str.strip()
                == onet_job.lower().strip()
            ]


            knowledge_scores = (

                calculate_knowledge_evidence(

                    cleaned_resume_text,

                    knowledge_data

                )

            )


            knowledge_score = (
                calculate_knowledge_score(
                    knowledge_scores
                )
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
                technical_requirements,
                software_data,
                essential_data
            )

            # ------------------------------------------------
            # LEARNING RECOMMENDATIONS
            # ------------------------------------------------

            recommendations = (
                get_learning_recommendations(
                    missing_skills
                )
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
                "Your current readiness for the selected career "
                "based on technical skills, core skills, knowledge, "
                "and market relevance."
            )


            # ------------------------------------------------
            # MAIN READINESS CARD
            # ------------------------------------------------

            st.markdown(
                f"""
            <div style="
            background: linear-gradient(135deg, rgba(80, 100, 255, 0.18), rgba(120, 80, 255, 0.08));
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 20px;
            padding: 30px;
            margin: 15px 0 25px 0;
            text-align: center;
            ">

            <div style="
            font-size: 0.9rem;
            color: rgba(255,255,255,0.65);
            text-transform: uppercase;
            letter-spacing: 2px;
            ">
            Overall Career Readiness
            </div>

            <div style="
            font-size: 4rem;
            font-weight: 750;
            margin: 8px 0;
            ">
            {career_score}%
            </div>

            <div style="
            font-size: 1rem;
            color: rgba(255,255,255,0.70);
            ">
            Target Career: {target_job_clean}
            </div>

            </div>
            """,
                unsafe_allow_html=True
            )


            # ------------------------------------------------
            # SCORE COMPONENTS
            # ------------------------------------------------

            col1, col2, col3, col4 = st.columns(4)


            col1.metric(
                "Technical Skills",
                f"{technical_score}%"
            )

            col2.metric(
                "Core Skills",
                f"{core_skill_score}%"
            )

            col3.metric(
                "Knowledge",
                f"{knowledge_score}%"
            )

            col4.metric(
                "Market Relevance",
                f"{market_relevance_score}%"
            )


            st.caption(
                "Technical Skills = match with job-related technologies. "
                "Core Skills = important workplace skills. "
                "Knowledge = evidence of relevant knowledge areas. "
                "Market Relevance = technologies marked In Demand "
                "or Hot Technology in O*NET."
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
                "Technical Skills": technical_score,
                "Core Skills": core_skill_score,
                "Knowledge": knowledge_score,
                "Market Relevance": market_relevance_score
            }


            fig = go.Figure(
                data=[
                    go.Bar(
                        x=list(readiness_data.keys()),
                        y=list(readiness_data.values()),
                        text=[
                            f"{score}%"
                            for score in readiness_data.values()
                        ],
                        textposition="outside",
                        hovertemplate=(
                            "<b>%{x}</b><br>"
                            "Score: %{y}%"
                            "<extra></extra>"
                        )
                    )
                ]
            )


            fig.update_layout(
                height=350,
                yaxis=dict(
                    title="Score (%)",
                    range=[0, 100],
                    gridcolor="rgba(255,255,255,0.08)"
                ),
                xaxis=dict(
                    title=""
                ),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(
                    color="rgba(255,255,255,0.85)"
                ),
                margin=dict(
                    l=20,
                    r=20,
                    t=30,
                    b=20
                ),
                showlegend=False
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


            st.markdown(
                "### ✅ Matched Skills"
            )

            if matched_skills:

                matched_html = ""

                for skill in matched_skills:

                    matched_html += f"""
            <span style="
            display:inline-block;
            background:rgba(46, 204, 113, 0.12);
            border:1px solid rgba(46, 204, 113, 0.30);
            color:#7bed9f;
            border-radius:20px;
            padding:8px 14px;
            margin:4px;
            font-size:0.9rem;
            ">
            ✓ {skill}
            </span>
            """

                st.markdown(
                    matched_html,
                    unsafe_allow_html=True
                )

            else:

                st.info(
                    "No required skills were matched."
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
                height=330
            )


            st.plotly_chart(
                skill_gap_fig,
                use_container_width=True,
                key="skill_gap_overview_chart"
            )


            st.markdown(
                "### ⚠️ Missing Skills"
            )

            if missing_skills:

                missing_html = ""

                for skill in missing_skills:

                    missing_html += f"""
            <span style="
            display:inline-block;
            background:rgba(255, 165, 0, 0.10);
            border:1px solid rgba(255, 165, 0, 0.30);
            color:#ffb86c;
            border-radius:20px;
            padding:8px 14px;
            margin:4px;
            font-size:0.9rem;
            ">
            ! {skill}
            </span>
            """

                st.markdown(
                    missing_html,
                    unsafe_allow_html=True
                )

            else:

                st.success(
                    "🎉 No missing technical skills detected."
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
            # PRIORITY CARDS
            # ------------------------------------------------

            priority_sections = [
                (
                    high_priority,
                    "🔴",
                    "High Priority",
                    "Skills that should receive attention first."
                ),
                (
                    medium_priority,
                    "🟠",
                    "Medium Priority",
                    "Useful skills to learn after the high-priority gaps."
                ),
                (
                    low_priority,
                    "🟢",
                    "Low Priority",
                    "Lower-priority gaps that can be addressed later."
                )
            ]


            for priority_items, icon, title, description in priority_sections:

                if not priority_items:
                    continue

                st.markdown(
                    f"### {icon} {title}"
                )

                st.caption(
                    description
                )

                for item in priority_items:

                    st.markdown(
                        f"""
            <div style="
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.09);
            border-radius: 16px;
            padding: 18px 22px;
            margin: 10px 0;
            ">

            <div style="
            font-size: 1.1rem;
            font-weight: 650;
            margin-bottom: 8px;
            ">
            {item['skill']}
            </div>

            <div style="
            color: rgba(255,255,255,0.65);
            font-size: 0.88rem;
            ">
            Type: {item['type']}
            &nbsp;&nbsp;•&nbsp;&nbsp;
            Priority Score: {item['priority_score']}
            </div>

            </div>
            """,
                        unsafe_allow_html=True
                    )


            # =================================================
            # PRIORITY DISTRIBUTION
            # =================================================

            st.subheader(
                "Priority Distribution"
            )

            st.caption(
                "Number of missing skills in each priority level."
            )

            if missing_skills:

                priority_data = {
                    "High Priority": len(high_priority),
                    "Medium Priority": len(medium_priority),
                    "Low Priority": len(low_priority)
                }

                priority_data = {
                    "High Priority": len(high_priority),
                    "Medium Priority": len(medium_priority),
                    "Low Priority": len(low_priority)
                }


                priority_fig = go.Figure(
                    data=[
                        go.Bar(
                            x=list(priority_data.keys()),
                            y=list(priority_data.values()),
                            text=list(priority_data.values()),
                            textposition="outside",
                            hovertemplate=(
                                "<b>%{x}</b><br>"
                                "Missing Skills: %{y}"
                                "<extra></extra>"
                            )
                        )
                    ]
                )


                priority_fig.update_layout(
                    height=330,
                    yaxis=dict(
                        title="Missing Skills",
                        gridcolor="rgba(255,255,255,0.08)",
                        range=[
                            0,
                            max(
                                1,
                                max(priority_data.values()) + 1
                            )
                        ]
                    ),
                    xaxis=dict(
                        title=""
                    ),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    font=dict(
                        color="rgba(255,255,255,0.85)"
                    ),
                    margin=dict(
                        l=20,
                        r=20,
                        t=30,
                        b=20
                    ),
                    showlegend=False
                )


                st.plotly_chart(
                    priority_fig,
                    use_container_width=True,
                    key="priority_distribution_chart"
                )

            else:

                st.success(
                    "No skill gaps detected. "
                    "You currently meet all defined technical requirements."
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


            if not missing_skills:

                st.success(
                    "🎉 You currently meet all defined technical "
                    "requirements for this career. "
                    "No immediate learning gaps were detected."
                )

            else:

                for phase, skills in roadmap.items():

                    if not skills:
                        continue

                    icon = phase_icons.get(
                        phase,
                        "📚"
                    )

                    st.markdown(
                        f"### {icon} {phase}"
                    )

                    for item in skills:

                        priority = item["priority"]

                        if priority == "High":
                            priority_label = "🔴 High"

                        elif priority == "Medium":
                            priority_label = "🟠 Medium"

                        else:
                            priority_label = "🟢 Low"

                        st.markdown(
                            f"""
            <div style="
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.09);
            border-radius: 18px;
            padding: 22px;
            margin: 12px 0 20px 0;
            ">

            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:12px;
            ">

            <div style="
            font-size:1.2rem;
            font-weight:700;
            ">
            {item['skill']}
            </div>

            <div style="
            font-size:0.85rem;
            padding:5px 10px;
            border-radius:12px;
            background:rgba(255,255,255,0.07);
            ">
            {priority_label}
            </div>

            </div>

            <div style="
            color:rgba(255,255,255,0.55);
            font-size:0.8rem;
            margin-bottom:8px;
            ">
            Priority Score: {item['priority_score']}
            </div>

            <div style="
            font-weight:650;
            margin-top:14px;
            ">
            📚 Learning Path
            </div>

            <div style="
            color:rgba(255,255,255,0.75);
            margin-top:5px;
            ">
            {item['learning_path']}
            </div>

            <div style="
            font-weight:650;
            margin-top:16px;
            ">
            🛠️ Build This
            </div>

            <div style="
            color:rgba(255,255,255,0.75);
            margin-top:5px;
            ">
            {item['project_idea']}
            </div>

            </div>
            """,
                            unsafe_allow_html=True
                        )


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
                    f"""
            <div style="
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.09);
            border-radius: 18px;
            padding: 24px;
            margin: 14px 0 20px 0;
            ">

            <div style="
            font-size:0.85rem;
            font-weight:650;
            margin-bottom:8px;
            ">
            {priority_label}
            </div>

            <div style="
            font-size:1.35rem;
            font-weight:700;
            margin-bottom:6px;
            ">
            {skill}
            </div>

            <div style="
            color:rgba(255,255,255,0.60);
            font-size:0.85rem;
            margin-bottom:18px;
            ">
            Priority Score: {priority_score}
            &nbsp;&nbsp;•&nbsp;&nbsp;
            Level: {recommendation['level']}
            </div>

            <div style="
            font-weight:650;
            margin-bottom:5px;
            ">
            📚 Learning Path
            </div>

            <div style="
            color:rgba(255,255,255,0.75);
            line-height:1.6;
            margin-bottom:18px;
            ">
            {recommendation['learning_path']}
            </div>

            <div style="
            font-weight:650;
            margin-bottom:5px;
            ">
            🛠️ Project Idea
            </div>

            <div style="
            color:rgba(255,255,255,0.75);
            line-height:1.6;
            ">
            {recommendation['project_idea']}
            </div>

            </div>
            """,
                    unsafe_allow_html=True
                )


            if not actionable_recommendations:

                st.info(
                    "No personalized learning recommendations "
                    "are currently available for your missing skills."
                )


        else:

            st.warning(
                f"Target job '{target_job_clean}' "
                "was not found in our curated career database."
            )

    # =================================================
    # ADVANCED ANALYSIS DETAILS
    # =================================================

    with st.expander(
        "🔍 Advanced Analysis Details"
    ):

        st.caption(
            "Technical details showing how the system "
            "processed your resume."
        )


        # ------------------------------------------------
        # DETECTED SKILLS
        # ------------------------------------------------

        st.markdown(
            "### Detected Skills"
        )

        st.caption(
            "Skills identified from the text extracted "
            "from your resume."
        )

        st.write(
            detected_skills
        )


        # ------------------------------------------------
        # NORMALIZED SKILLS
        # ------------------------------------------------

        st.markdown(
            "### Normalized Skills"
        )

        st.caption(
            "Standardized skill names used internally "
            "for consistent matching."
        )

        st.write(
            normalized_skills
        )


        # ------------------------------------------------
        # EXTRACTED TEXT
        # ------------------------------------------------

        st.markdown(
            "### Extracted Resume Text"
        )

        st.caption(
            "The text extracted from your uploaded PDF resume."
        )

        st.text_area(
            "Resume content",
            resume_text,
            height=400
        )

# =================================================
# CREATOR FOOTER
# =================================================

st.markdown(
    """
    <div class="creator-footer">
        <div>Career Intelligence System</div>
        <div class="creator-name">
            Designed & Developed by Dhruv Kulkarni
        </div>
        <div>AI & Data Science • 2026</div>
    </div>
    """,
    unsafe_allow_html=True
)
