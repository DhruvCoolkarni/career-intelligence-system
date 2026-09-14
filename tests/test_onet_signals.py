from app.utils.onet_loader import get_software_skills_for_job


target_job = "Computer and Information Systems Managers"


software_data = get_software_skills_for_job(
    target_job
)


unique_skills = software_data.drop_duplicates(
    subset=["Element Name"]
)


in_demand = unique_skills[
    unique_skills["In Demand"] == "Y"
]


hot_technology = unique_skills[
    unique_skills["Hot Technology"] == "Y"
]


both = unique_skills[
    (unique_skills["In Demand"] == "Y")
    & (unique_skills["Hot Technology"] == "Y")
]


print("\n===== O*NET TECHNOLOGY SIGNALS =====\n")

print("Target Job:")
print(target_job)

print("\nUnique Software Skills:")
print(len(unique_skills))

print("\nIn Demand Skills:")
print(len(in_demand))

print("\nHot Technology Skills:")
print(len(hot_technology))

print("\nBoth In Demand + Hot Technology:")
print(len(both))


print("\n===== IN DEMAND =====\n")

print(
    in_demand[
        ["Element Name", "In Demand", "Hot Technology"]
    ].to_string(index=False)
)


print("\n===== HOT TECHNOLOGY =====\n")

print(
    hot_technology[
        ["Element Name", "In Demand", "Hot Technology"]
    ].to_string(index=False)
)