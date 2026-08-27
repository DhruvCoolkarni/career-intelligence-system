import pandas as pd


def extract_skills(resume_text):
    skills_data = pd.read_csv("data/skills.csv")

    detected_skills = []

    for skill in skills_data["skill"]:
        if skill.lower() in resume_text.lower():
            detected_skills.append(skill)

    return detected_skills