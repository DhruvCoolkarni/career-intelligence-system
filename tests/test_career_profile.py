from app.utils.onet_loader import (
    get_essential_skills_for_job
)

import pandas as pd


target_job = "Computer and Information Systems Managers"


print("\n===== CAREER PROFILE INSPECTION =====\n")

print("Target Job:")
print(target_job)


essential_data = get_essential_skills_for_job(
    target_job
)


print("\n===== ESSENTIAL SKILLS =====\n")

importance_data = essential_data[
    essential_data["Scale Name"] == "Importance"
].copy()


importance_data = importance_data.sort_values(
    by="Data Value",
    ascending=False
)


print(
    importance_data[
        ["Element Name", "Data Value"]
    ].to_string(index=False)
)


print("\n===== AVAILABLE O*NET COLUMNS =====\n")

print(
    list(essential_data.columns)
)