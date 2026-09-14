from .onet_loader import get_software_skills_for_job
from .skill_normalizer import normalize_skill


def calculate_relevance(row):

    in_demand = row["In Demand"] == "Y"
    hot_technology = row["Hot Technology"] == "Y"

    if in_demand and hot_technology:
        return 4

    if in_demand:
        return 3

    if hot_technology:
        return 2

    return 1


def get_required_skills(target_job):

    job_data = get_software_skills_for_job(
        target_job
    )

    if job_data.empty:
        return []

    job_data = job_data.drop_duplicates(
        subset=["Element Name"]
    ).copy()

    job_data["relevance_weight"] = job_data.apply(
        calculate_relevance,
        axis=1
    )

    job_data = job_data.sort_values(
        by="relevance_weight",
        ascending=False
    )

    skills = []

    for skill in job_data["Element Name"].dropna():

        normalized_skill = normalize_skill(skill)

        if normalized_skill not in skills:
            skills.append(normalized_skill)

    return skills


def get_required_skill_data(target_job):

    job_data = get_software_skills_for_job(
        target_job
    )

    if job_data.empty:
        return []

    job_data = job_data.drop_duplicates(
        subset=["Element Name"]
    ).copy()

    job_data["relevance_weight"] = job_data.apply(
        calculate_relevance,
        axis=1
    )

    skill_data = {}

    for _, row in job_data.iterrows():

        normalized_skill = normalize_skill(
            row["Element Name"]
        )

        relevance_weight = row[
            "relevance_weight"
        ]

        if (
            normalized_skill not in skill_data
            or relevance_weight
            > skill_data[normalized_skill][
                "relevance_weight"
            ]
        ):

            skill_data[normalized_skill] = {
                "skill": normalized_skill,
                "relevance_weight": relevance_weight,
                "in_demand": row["In Demand"],
                "hot_technology": row[
                    "Hot Technology"
                ]
            }

    return sorted(
        skill_data.values(),
        key=lambda item: item["relevance_weight"],
        reverse=True
    )