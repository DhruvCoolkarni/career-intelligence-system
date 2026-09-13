from app.utils.readiness_score import calculate_readiness_score


matched_skills = [
    "Python",
    "SQL",
    "Docker",
    "Git"
]

required_skills = [
    "Python",
    "Scikit-learn",
    "SQL",
    "Machine Learning",
    "Docker",
    "Git"
]

score = calculate_readiness_score(
    matched_skills,
    required_skills
)

print("Career Readiness Score:", score)