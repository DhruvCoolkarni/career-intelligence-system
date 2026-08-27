def calculate_skill_gap(user_skills, required_skills):
    user_skills_lower = [skill.lower() for skill in user_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in user_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills