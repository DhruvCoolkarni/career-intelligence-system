SKILL_MAPPING = {
    "python": "python",
    "java": "java",
    "c++": "c++",

    "sql": "database",
    "mysql": "database",
    "postgresql": "database",
    "postgres": "database",
    "mongodb": "database",

    "data base management system software": "database",
    "data base user interface and query software": "database",
    "object oriented data base management software": "database",

    "scikit-learn": "scikit-learn",
    "sklearn": "scikit-learn",
    "machine learning": "machine learning",

    "pytorch": "pytorch",
    "tensorflow": "tensorflow",

    "git": "git",
    "github": "git",
    "docker": "docker",

    "pandas": "pandas",
    "numpy": "numpy",
    "power bi": "business intelligence",
    "tableau": "business intelligence",

    "business intelligence and data analysis software": "business intelligence",
    "development environment software": "development environment",
}


def normalize_skill(skill):
    skill = skill.lower().strip()

    return SKILL_MAPPING.get(skill, skill)


def normalize_skills(skills):
    normalized_skills = []

    for skill in skills:
        normalized_skill = normalize_skill(skill)

        if normalized_skill not in normalized_skills:
            normalized_skills.append(normalized_skill)

    return normalized_skills