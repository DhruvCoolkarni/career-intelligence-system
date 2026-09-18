from app.utils.core_skill_matcher import (
    calculate_core_skill_evidence
)

from app.utils.career_scores import (
    calculate_core_skill_score
)

from app.utils.onet_loader import (
    get_essential_skills_for_job
)


target_job = "Computer and Information Research Scientists"

resume_text = """
Developed machine learning projects.
Analyzed datasets and solved complex problems.
Presented project results to the team.
Completed online machine learning courses.
Created technical documentation.
Tracked model performance and metrics.
"""


essential_data = get_essential_skills_for_job(
    target_job
)

core_skill_evidence = calculate_core_skill_evidence(
    resume_text,
    essential_data
)

core_score = calculate_core_skill_score(
    core_skill_evidence
)

print("Core Skill Score:", core_score)