from app.utils.skill_gap import calculate_skill_gap


user_skills = [
    "Python",
    "MySQL",
    "GitHub",
    "Docker"
]

required_skills = [
    "Python",
    "Data base management system software",
    "Git",
    "Docker"
]

matched_skills, missing_skills = calculate_skill_gap(
    user_skills,
    required_skills
)

print("Matched skills:")
print(matched_skills)

print("Missing skills:")
print(missing_skills)