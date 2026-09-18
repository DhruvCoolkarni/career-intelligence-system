from app.utils.skill_priority import calculate_skill_priorities
from app.utils.onet_loader import (
    get_software_skills_for_job,
    get_essential_skills_for_job
)
from app.utils.technical_requirements import (
    get_technical_requirements
)


# ------------------------------------------------
# TEST CONFIGURATION
# ------------------------------------------------

target_job = "Machine Learning Engineer"

onet_job = "Computer and Information Research Scientists"


# ------------------------------------------------
# MISSING SKILLS
# ------------------------------------------------

missing_skills = [
    "Database Management",
    "Business Intelligence",
    "Critical Thinking",
    "Python",
    "Docker"
]


# ------------------------------------------------
# LOAD O*NET DATA
# ------------------------------------------------

software_data = get_software_skills_for_job(
    onet_job
)

essential_data = get_essential_skills_for_job(
    onet_job
)


# ------------------------------------------------
# LOAD TECHNICAL REQUIREMENTS
# ------------------------------------------------

technical_requirements = get_technical_requirements(
    target_job
)


# ------------------------------------------------
# CALCULATE PRIORITIES
# ------------------------------------------------

priorities = calculate_skill_priorities(
    missing_skills,
    technical_requirements,
    software_data,
    essential_data
)


# ------------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------------

print(
    "\n===== SKILL PRIORITY ANALYSIS =====\n"
)


for item in priorities:

    print(
        f"Skill: {item['skill']}"
    )

    print(
        f"Type: {item['type']}"
    )

    print(
        f"Importance: {item['importance']}"
    )

    print(
        f"In Demand: {item['in_demand']}"
    )

    print(
        f"Hot Technology: {item['hot_technology']}"
    )

    print(
        f"Priority Score: {item['priority_score']}"
    )

    print(
        f"Priority: {item['priority']}"
    )

    print(
        "-----------------------------------"
    )