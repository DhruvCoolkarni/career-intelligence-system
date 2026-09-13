from app.utils.onet_loader import (
    load_software_skills,
    load_essential_skills,
    get_software_skills_for_job,
    get_essential_skills_for_job
)


software_skills = load_software_skills()
essential_skills = load_essential_skills()

print("Software Skills:", software_skills.shape)
print("Essential Skills:", essential_skills.shape)


target_job = "Computer and Information Systems Managers"

software_data = get_software_skills_for_job(target_job)

print("\nSoftware skills for:", target_job)
print(
    software_data[
        ["Element Name", "Hot Technology", "In Demand"]
    ].to_string(index=False)
)


essential_data = get_essential_skills_for_job(target_job)

print("\nEssential skills for:", target_job)
print(
    essential_data[
        ["Element Name", "Scale Name", "Data Value"]
    ].to_string(index=False)
)