from app.utils.skill_priority import calculate_skill_priorities
from app.utils.onet_loader import (
    get_software_skills_for_job,
    get_essential_skills_for_job
)


target_job = "Computer and Information Systems Managers"

missing_skills = [
    "Database Management",
    "Business Intelligence",
    "Critical Thinking",
    "Python",
    "Docker"
]


software_data = get_software_skills_for_job(target_job)

essential_data = get_essential_skills_for_job(target_job)


priorities = calculate_skill_priorities(
    missing_skills,
    software_data,
    essential_data
)


print("\n===== SKILL PRIORITY ANALYSIS =====\n")


for item in priorities:

    print(f"Skill: {item['skill']}")
    print(f"Type: {item['type']}")
    print(f"Importance: {item['importance']}")
    print(f"In Demand: {item['in_demand']}")
    print(f"Hot Technology: {item['hot_technology']}")
    print(f"Priority Score: {item['priority_score']}")
    print(f"Priority: {item['priority']}")
    print("-----------------------------------")