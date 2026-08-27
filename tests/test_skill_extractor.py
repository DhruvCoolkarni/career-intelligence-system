from app.utils.skill_extractor import extract_skills


sample_resume = """
I know Python, Pandas, NumPy, SQL and Machine Learning.
I have also used Git and Docker.
"""

skills = extract_skills(sample_resume)

print("Detected skills:")
print(skills)