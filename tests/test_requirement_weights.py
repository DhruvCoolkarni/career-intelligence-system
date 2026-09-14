from app.utils.job_matcher import get_required_skill_data


target_job = "Computer and Information Systems Managers"


skill_data = get_required_skill_data(
    target_job
)


print("\n===== O*NET REQUIREMENT WEIGHTS =====\n")


print(
    "Total Requirements:",
    len(skill_data)
)


for item in skill_data[:15]:

    print(
        f"{item['skill']} | "
        f"Weight: {item['relevance_weight']} | "
        f"In Demand: {item['in_demand']} | "
        f"Hot Technology: "
        f"{item['hot_technology']}"
    )