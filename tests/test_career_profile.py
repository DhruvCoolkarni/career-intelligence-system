from app.utils.career_profile import get_career_profile
from app.utils.onet_loader import (
    get_essential_skills_for_job
)


target_job = "Machine Learning Engineer"

profile = get_career_profile(target_job)

print("Selected Career:")
print(target_job)

print("\nCareer Profile:")
print(profile)

if profile:

    onet_job = profile["onet_title"]

    print("\nO*NET Reference Career:")
    print(onet_job)

    essential_data = get_essential_skills_for_job(
        onet_job
    )

    print("\nO*NET Core Skill Records:")
    print(len(essential_data))

    if not essential_data.empty:
        print("✅ O*NET mapping works")
    else:
        print("❌ O*NET occupation not found")