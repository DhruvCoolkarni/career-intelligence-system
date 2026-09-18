from app.utils.technical_requirements import (
    get_technical_requirements
)


target_job = "Machine Learning Engineer"

requirements = get_technical_requirements(
    target_job
)

print("Target Job:", target_job)
print("Technical Requirements:")

for item in requirements:
    print(item)