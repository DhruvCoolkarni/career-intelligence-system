from .onet_loader import get_software_skills_for_job
from .skill_normalizer import normalize_skill


def get_required_skills(target_job):
    job_data = get_software_skills_for_job(target_job)

    if job_data.empty:
        return []

    job_data = job_data.drop_duplicates(
        subset=["Element Name"]
    )

    job_data["priority"] = (
        (job_data["In Demand"] == "Y").astype(int) * 2
        + (job_data["Hot Technology"] == "Y").astype(int)
    )

    job_data = job_data.sort_values(
        by="priority",
        ascending=False
    )

    skills = [
        normalize_skill(skill)
        for skill in job_data["Element Name"].dropna()
    ]

    return list(dict.fromkeys(skills))