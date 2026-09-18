import pandas as pd

from .skill_normalizer import normalize_skill


def load_curated_requirements():

    file_path = "data/job_requirements.csv"

    requirements = pd.read_csv(
        file_path
    )

    requirements["job"] = (
        requirements["job"]
        .astype(str)
        .str.strip()
    )

    return requirements


def get_curated_requirements(target_job):

    requirements = load_curated_requirements()

    target_job_clean = (
        str(target_job)
        .strip()
        .lower()
    )

    matching_job = requirements[
        requirements["job"]
        .str.strip()
        .str.lower()
        == target_job_clean
    ]

    if matching_job.empty:
        return []

    required_skills = (
        matching_job.iloc[0]["required_skills"]
        .split(",")
    )

    normalized_skills = []

    for skill in required_skills:

        normalized_skill = normalize_skill(
            skill.strip()
        )

        if normalized_skill not in normalized_skills:

            normalized_skills.append(
                normalized_skill
            )

    return normalized_skills