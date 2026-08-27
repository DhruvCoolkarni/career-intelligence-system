from app.utils.job_matcher import get_required_skills


target_job = "Machine Learning Engineer"

required_skills = get_required_skills(target_job)

print("Required skills:")
print(required_skills)