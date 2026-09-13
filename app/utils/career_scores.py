from .skill_normalizer import normalize_skill


def calculate_technical_score(user_skills, required_skills):
    if not required_skills:
        return 0

    user_skills = [
        normalize_skill(skill)
        for skill in user_skills
    ]

    matched = 0

    for skill in required_skills:
        if normalize_skill(skill) in user_skills:
            matched += 1

    return round((matched / len(required_skills)) * 100, 2)


def calculate_core_skill_score(user_skills, essential_data):
    importance_data = essential_data[
        essential_data["Scale Name"] == "Importance"
    ]

    if importance_data.empty:
        return 0

    user_skills = [
        skill.lower()
        for skill in user_skills
    ]

    matched = 0

    for skill in importance_data["Element Name"].dropna():
        if skill.lower() in user_skills:
            matched += 1

    total = len(importance_data)

    return round((matched / total) * 100, 2)


def calculate_market_relevance_score(job_data, user_skills):
    relevant_data = job_data[
        (job_data["In Demand"] == "Y")
        | (job_data["Hot Technology"] == "Y")
    ]

    relevant_skills = relevant_data[
        "Element Name"
    ].dropna().unique()

    if len(relevant_skills) == 0:
        return 0

    user_skills = [
        normalize_skill(skill)
        for skill in user_skills
    ]

    matched = 0

    for skill in relevant_skills:
        if normalize_skill(skill) in user_skills:
            matched += 1

    return round(
        (matched / len(relevant_skills)) * 100,
        2
    )


def calculate_career_readiness(
    technical_score,
    core_skill_score,
    market_relevance_score
):
    score = (
        technical_score * 0.5
        + core_skill_score * 0.3
        + market_relevance_score * 0.2
    )

    return round(score, 2)