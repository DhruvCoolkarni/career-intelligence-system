from app.utils.career_scores import calculate_technical_score
from app.utils.job_matcher import get_required_skill_data


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


required_skill_data = get_required_skill_data(
    target_job
)


technical_score = calculate_technical_score(
    user_skills,
    required_skill_data
)


print("\n===== WEIGHTED TECHNICAL SCORE =====\n")

print("Target Job:")
print(target_job)

print("\nTotal Requirements:")
print(len(required_skill_data))

print("\nWeighted Technical Score:")
print(f"{technical_score}%")