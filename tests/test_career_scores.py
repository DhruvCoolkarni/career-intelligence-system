from app.utils.career_scores import (
    calculate_technical_score,
    calculate_core_skill_score,
    calculate_market_relevance_score,
    calculate_career_readiness
)

from app.utils.onet_loader import (
    get_software_skills_for_job,
    get_essential_skills_for_job
)


target_job = "Computer and Information Systems Managers"

user_skills = [
    "Python",
    "Java",
    "SQL",
    "MySQL",
    "Git",
    "GitHub",
    "Docker",
    "Machine Learning",
    "Critical Thinking",
    "Reading Comprehension",
    "Active Learning"
]


software_data = get_software_skills_for_job(target_job)
essential_data = get_essential_skills_for_job(target_job)

required_skills = software_data["Element Name"].dropna().unique().tolist()


technical_score = calculate_technical_score(
    user_skills,
    required_skills
)

core_skill_score = calculate_core_skill_score(
    user_skills,
    essential_data
)

market_score = calculate_market_relevance_score(
    software_data,
    user_skills
)

career_score = calculate_career_readiness(
    technical_score,
    core_skill_score,
    market_score
)


print("Technical Skill Score:", technical_score)
print("Core Skill Score:", core_skill_score)
print("Market Relevance Score:", market_score)
print("Overall Career Readiness:", career_score)