from app.utils.skill_normalizer import normalize_skills


sample_skills = [
    "Python",
    "MySQL",
    "SQL",
    "GitHub",
    "PyTorch"
]

normalized_skills = normalize_skills(sample_skills)

print("Original skills:")
print(sample_skills)

print("\nNormalized skills:")
print(normalized_skills)