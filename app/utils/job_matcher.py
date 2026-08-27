import pandas as pd


def get_required_skills(target_job):
    job_data = pd.read_csv("data/job_requirements.csv")

    matching_job = job_data[
        job_data["job"].str.lower() == target_job.lower()
    ]

    if matching_job.empty:
        return []

    skills = matching_job.iloc[0]["required_skills"]

    return [skill.strip() for skill in skills.split(",")]