from app.utils.career_requirements import (
    get_curated_requirements
)


target_job = "Machine Learning Engineer"


requirements = get_curated_requirements(
    target_job
)


print("Target Job:", target_job)

print("Required Skills:")

print(requirements)