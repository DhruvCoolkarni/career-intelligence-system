import pandas as pd

from app.utils.career_scores import (
    calculate_market_relevance_score
)


job_data = pd.read_csv(
    "data/onet/software_skills.csv"
)

job_data = job_data[
    job_data["Title"]
    .str.strip()
    .str.lower()
    == "computer and information research scientists"
]

user_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Docker",
    "Git"
]


result = calculate_market_relevance_score(
    job_data,
    user_skills
)


print("===== MARKET RELEVANCE =====")

print(
    "Score:",
    result["score"],
    "%"
)

print()

print("Matched Groups:")

for group in result["matched_groups"]:

    print(
        f"✓ {group}"
    )

print()

print("Missing Groups:")

for group in result["missing_groups"]:

    print(
        f"✗ {group}"
    )

print()

print(
    "Total Groups:",
    len(result["matched_groups"])
    + len(result["missing_groups"])
)