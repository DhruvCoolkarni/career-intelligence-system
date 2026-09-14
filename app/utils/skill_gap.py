from .skill_matcher import skills_match


def calculate_skill_gap(user_skills, required_skills):

    matched_skills = []
    missing_skills = []

    for required_skill in required_skills:

        is_match = False

        for user_skill in user_skills:

            if skills_match(
                user_skill,
                required_skill
            ):
                is_match = True
                break

        if is_match:

            matched_skills.append(required_skill)

        else:

            missing_skills.append(required_skill)

    return matched_skills, missing_skills