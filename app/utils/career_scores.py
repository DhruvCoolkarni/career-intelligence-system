from .skill_normalizer import normalize_skill


def calculate_technical_score(
    user_skills,
    required_skill_data
):
    if not required_skill_data:
        return 0

    normalized_user_skills = [
        normalize_skill(skill)
        for skill in user_skills
    ]

    total_weight = 0
    matched_weight = 0

    for item in required_skill_data:

        required_skill = normalize_skill(
            item["skill"]
        )

        weight = item["relevance_weight"]

        total_weight += weight

        if required_skill in normalized_user_skills:

            matched_weight += weight

    if total_weight == 0:
        return 0

    score = (
        matched_weight
        / total_weight
    ) * 100

    return round(score, 2)


def calculate_core_skill_score(
    user_skills,
    essential_data
):
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

    return round(
        (matched / total) * 100,
        2
    )


def calculate_market_relevance_score(
    job_data,
    user_skills
):
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

def calculate_knowledge_score(knowledge_scores):

    if not knowledge_scores:
        return 0

    total_importance = 0
    weighted_evidence = 0

    for item in knowledge_scores:

        importance = float(item["importance"])
        evidence = item["evidence_score"]

        total_importance += importance

        weighted_evidence += (
            importance * evidence
        )

    if total_importance == 0:
        return 0

    score = (
        weighted_evidence
        / total_importance
    ) * 100

    return round(score, 2)

def calculate_career_readiness(
    technical_score,
    core_skill_score,
    knowledge_score,
    market_relevance_score
):
    score = (
        technical_score * 0.40
        + core_skill_score * 0.20
        + knowledge_score * 0.25
        + market_relevance_score * 0.15
    )

    return round(score, 2)