def calculate_readiness_score(matched_skills, required_skills):
    if not required_skills:
        return 0

    score = (len(matched_skills) / len(required_skills)) * 100

    return round(score, 2)