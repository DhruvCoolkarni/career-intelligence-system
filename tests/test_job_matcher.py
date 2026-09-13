from app.utils.job_matcher import get_required_skills


target_job = "Computer and Information Systems Managers"

required_skills = get_required_skills(target_job)

print("Required O*NET skills:")
print(required_skills)

print("\nTotal required skills:", len(required_skills))