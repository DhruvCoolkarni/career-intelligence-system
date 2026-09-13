from .skill_normalizer import normalize_skill


def calculate_skill_gap(user_skills, required_skills):
    normalized_user_skills = [
        normalize_skill(skill)
        for skill in user_skills
    ]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        normalized_required_skill = normalize_skill(skill)

        if normalized_required_skill in normalized_user_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills