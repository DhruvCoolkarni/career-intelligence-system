from app.utils.job_matcher import get_required_skills
from app.utils.skill_matcher import skills_match


target_job = "Computer and Information Systems Managers"


user_skills = [
    "Python",
    "Java",
    "C++",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Machine Learning",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Git",
    "GitHub",
    "Docker",
    "Linux",
    "Business Intelligence",
    "Data Visualization",
    "REST APIs"
]


required_skills = get_required_skills(target_job)


matched_skills = []
missing_skills = []


for required_skill in required_skills:

    matched = False

    for user_skill in user_skills:

        if skills_match(
            user_skill,
            required_skill
        ):
            matched = True
            break

    if matched:

        matched_skills.append(required_skill)

    else:

        missing_skills.append(required_skill)


print("\n===== REAL O*NET SKILL MATCHING =====\n")

print("Target Job:")
print(target_job)

print("\nTotal Required Skills:")
print(len(required_skills))

print("\nMatched Skills:")
print(matched_skills)

print("\nTotal Matched:")
print(len(matched_skills))

print("\nMissing Skills:")
print(missing_skills)

print("\nTotal Missing:")
print(len(missing_skills))

print("\nCurrent Matching Percentage:")

if required_skills:

    percentage = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    print(round(percentage, 2), "%")

else:

    print("0%")