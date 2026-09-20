from app.utils.onet_loader import (
    get_software_skills_for_job
)

from app.utils.skill_matcher import (
    skills_match
)


target_job = "Machine Learning Engineer"

user_skills = [
    "Python",
    "SQL",
    "MySQL",
    "GitHub",
    "Docker",
    "Pandas",
    "NumPy",
    "Machine Learning"
]

job_data = get_software_skills_for_job(
    target_job
)

market_data = job_data[
    (job_data["In Demand"] == "Y")
    | (job_data["Hot Technology"] == "Y")
]

market_skills = (
    market_data["Element Name"]
    .dropna()
    .drop_duplicates()
    .tolist()
)


matched = []
missing = []

for required_skill in market_skills:

    found = False

    for user_skill in user_skills:

        if skills_match(
            user_skill,
            required_skill
        ):

            matched.append(
                (
                    required_skill,
                    user_skill
                )
            )

            found = True
            break

    if not found:
        missing.append(required_skill)


print("===== MARKET MATCHES =====")

for required, user in matched:
    print(
        "O*NET:",
        required,
        "<-- Resume:",
        user
    )


print("\n===== MARKET SUMMARY =====")

print(
    "Matched:",
    len(matched)
)

print(
    "Total:",
    len(market_skills)
)

print(
    "Score:",
    round(
        len(matched) / len(market_skills) * 100,
        2
    )
)


print("\n===== MISSING MARKET TECHNOLOGIES =====")

for skill in missing:
    print(skill)
