from .skill_normalizer import normalize_skill


SKILL_RELATIONSHIPS = {

    "linux": {
        "operating system software"
    },

    "mysql": {
        "database"
    },

    "postgresql": {
        "database"
    },

    "sql": {
        "database"
    },

    "github": {
        "git"
    }
}


def skills_match(user_skill, required_skill):

    normalized_user_skill = normalize_skill(
        user_skill
    )

    normalized_required_skill = normalize_skill(
        required_skill
    )


    # Exact match
    if normalized_user_skill == normalized_required_skill:
        return True


    # Strong relationship match
    related_skills = SKILL_RELATIONSHIPS.get(
        normalized_user_skill,
        set()
    )


    if normalized_required_skill in related_skills:
        return True


    return False