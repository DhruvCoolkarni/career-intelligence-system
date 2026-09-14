from app.utils.skill_matcher import skills_match


test_cases = [
    ("MySQL", "Data base management system software"),
    ("GitHub", "Git"),
    ("Python", "Python"),
    ("PyTorch", "PyTorch"),
    ("Linux", "Operating system software"),
    ("Docker", "Database"),
    ("Python", "Operating system software")
]


print("\n===== SKILL MATCHING TEST =====\n")


for user_skill, required_skill in test_cases:

    result = skills_match(
        user_skill,
        required_skill
    )

    print(
        f"{user_skill} ↔ {required_skill} "
        f"→ {result}"
    )