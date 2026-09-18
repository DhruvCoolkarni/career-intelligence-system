from app.utils.job_matcher import get_required_skill_data
from app.utils.skill_matcher import skills_match


target_job = "Computer and Information Systems Managers"

user_skills = [
    "Python",
    "SQL",
    "MySQL",
    "Docker",
    "Linux",
    "Pandas",
    "NumPy",
    "Machine Learning"
]


required_skill_data = get_required_skill_data(
    target_job
)


matched = []
missing = []


for item in required_skill_data:

    required_skill = item["skill"]

    is_match = False

    for user_skill in user_skills:

        if skills_match(
            user_skill,
            required_skill
        ):
            is_match = True
            break


    if is_match:

        matched.append(item)

    else:

        missing.append(item)


print("\n===== TECHNICAL SCORE DIAGNOSTIC =====\n")

print(
    "Total requirements:",
    len(required_skill_data)
)

print(
    "Matched requirements:",
    len(matched)
)

print(
    "Missing requirements:",
    len(missing)
)


print("\n===== MATCHED =====\n")

for item in matched:

    print(
        f"{item['skill']} | "
        f"Weight: {item['relevance_weight']}"
    )


print("\n===== TOP MISSING REQUIREMENTS =====\n")

for item in missing[:20]:

    print(
        f"{item['skill']} | "
        f"Weight: {item['relevance_weight']}"
    )