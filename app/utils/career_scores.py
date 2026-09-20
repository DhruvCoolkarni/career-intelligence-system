from .skill_normalizer import normalize_skill
from .market_career_mapping import CAREER_MARKET_MAPPING


# ------------------------------------------------
# TECHNICAL SCORE
# ------------------------------------------------

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


# ------------------------------------------------
# CORE SKILL SCORE
# ------------------------------------------------

def calculate_core_skill_score(
    core_skill_evidence
):

    if not core_skill_evidence:
        return 0

    total_importance = 0
    weighted_evidence = 0

    for item in core_skill_evidence:

        importance = float(
            item["importance"]
        )

        evidence = float(
            item["evidence_score"]
        )

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


# ------------------------------------------------
# ORIGINAL MARKET RELEVANCE SCORE
# ------------------------------------------------

def calculate_market_relevance_score(
    job_data,
    user_skills
):

    from .market_skill_groups import MARKET_SKILL_GROUPS
    from .skill_matcher import skills_match

    if job_data.empty:
        return {
            "score": 0,
            "matched_groups": [],
            "missing_groups": []
        }

    relevant_data = job_data[
        (job_data["In Demand"] == "Y") |
        (job_data["Hot Technology"] == "Y")
    ]

    if relevant_data.empty:
        return {
            "score": 0,
            "matched_groups": [],
            "missing_groups": []
        }

    relevant_groups = set()
    matched_groups = set()

    for skill in relevant_data["Element Name"].dropna():

        skill_clean = skill.lower().strip()

        for group_name, group_skills in MARKET_SKILL_GROUPS.items():

            if skill_clean in group_skills:

                relevant_groups.add(group_name)

                for user_skill in user_skills:

                    if skills_match(
                        user_skill,
                        skill
                    ):
                        matched_groups.add(
                            group_name
                        )
                        break

                break

    if not relevant_groups:
        return {
            "score": 0,
            "matched_groups": [],
            "missing_groups": []
        }

    missing_groups = (
        relevant_groups -
        matched_groups
    )

    score = (
        len(matched_groups)
        / len(relevant_groups)
    ) * 100

    return {
        "score": round(score, 2),
        "matched_groups": sorted(
            matched_groups
        ),
        "missing_groups": sorted(
            missing_groups
        )
    }


# ------------------------------------------------
# CAREER-SPECIFIC MARKET RELEVANCE SCORE
# ------------------------------------------------

def calculate_career_market_relevance_score(
    job_data,
    user_skills,
    target_job
):

    if job_data.empty:
        return {
            "score": 0,
            "matched_groups": [],
            "missing_groups": []
        }

    relevant_data = job_data[
        (job_data["In Demand"] == "Y") |
        (job_data["Hot Technology"] == "Y")
    ]

    if relevant_data.empty:
        return {
            "score": 0,
            "matched_groups": [],
            "missing_groups": []
        }

    career_mapping = CAREER_MARKET_MAPPING.get(
        target_job,
        {}
    )

    # If we do not have a career-specific mapping,
    # safely fall back to the original scorer.
    if not career_mapping:
        return calculate_market_relevance_score(
            job_data,
            user_skills
        )

    required_groups = set()

    for skill in relevant_data["Element Name"].dropna():

        skill_name = skill.lower().strip()

        if skill_name in career_mapping:

            mapped_skill = career_mapping[
                skill_name
            ]

            required_groups.add(
                mapped_skill
            )

    if not required_groups:
        return {
            "score": 0,
            "matched_groups": [],
            "missing_groups": []
        }

    normalized_user_skills = {
        normalize_skill(skill)
        for skill in user_skills
    }

    matched_groups = set()

    for group in required_groups:

        normalized_group = normalize_skill(
            group
        )

        if normalized_group in normalized_user_skills:

            matched_groups.add(group)

    missing_groups = (
        required_groups -
        matched_groups
    )

    score = (
        len(matched_groups)
        / len(required_groups)
    ) * 100

    return {
        "score": round(score, 2),
        "matched_groups": sorted(
            matched_groups
        ),
        "missing_groups": sorted(
            missing_groups
        )
    }


# ------------------------------------------------
# FINAL CAREER READINESS
# ------------------------------------------------

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

    return round(
        score,
        2
    )


# ------------------------------------------------
# KNOWLEDGE SCORE
# ------------------------------------------------

def calculate_knowledge_score(
    knowledge_scores
):

    if not knowledge_scores:
        return 0

    total_importance = 0
    weighted_evidence = 0

    for item in knowledge_scores:

        importance = float(
            item["importance"]
        )

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

    return round(
        score,
        2
    )