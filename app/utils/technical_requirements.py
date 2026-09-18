from .career_requirements import (
    get_curated_requirements
)


def get_technical_requirements(target_job):

    required_skills = get_curated_requirements(
        target_job
    )

    technical_requirements = []

    for skill in required_skills:

        technical_requirements.append({
            "skill": skill,
            "relevance_weight": 1
        })

    return technical_requirements