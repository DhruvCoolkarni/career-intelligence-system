from app.utils.skill_extractor import extract_skills
from app.utils.text_cleaner import clean_text
from app.utils.job_matcher import get_required_skills
from app.utils.skill_gap import calculate_skill_gap


sample_resume = """
I have experience with Python, SQL, MySQL, PostgreSQL,
GitHub, Docker, Pandas, NumPy and Business Intelligence.
"""


target_job = "Computer and Information Systems Managers"


cleaned_text = clean_text(sample_resume)

detected_skills = extract_skills(cleaned_text)

required_skills = get_required_skills(target_job)

matched_skills, missing_skills = calculate_skill_gap(
    detected_skills,
    required_skills
)


print("\n===== REAL SKILL MATCHING TEST =====\n")

print("Detected Skills:")
print(detected_skills)

print("\nTotal O*NET Required Skills:")
print(len(required_skills))

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nTotal Matched:", len(matched_skills))
print("Total Missing:", len(missing_skills))