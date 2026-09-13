import pandas as pd


def extract_skills(resume_text):
    skills_data = pd.read_csv("data/skills.csv")

    essential_skills = pd.read_csv(
        "data/onet/essential_skills.csv"
    )

    skills = skills_data["skill"].dropna().tolist()

    core_skills = essential_skills[
        essential_skills["Scale Name"] == "Importance"
    ]["Element Name"].dropna().unique().tolist()

    all_skills = skills + core_skills

    detected_skills = []

    resume_text_lower = resume_text.lower()

    for skill in all_skills:
        if skill.lower() in resume_text_lower:
            if skill not in detected_skills:
                detected_skills.append(skill)

    return detected_skills