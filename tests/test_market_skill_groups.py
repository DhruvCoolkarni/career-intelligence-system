from app.utils.market_skill_groups import MARKET_SKILL_GROUPS


def find_skill_group(skill):

    skill = skill.lower().strip()

    for group_name, skills in MARKET_SKILL_GROUPS.items():

        if skill in skills:
            return group_name

    return None


test_skills = [
    "Data base management system software",
    "Data base user interface and query software",
    "Object oriented data base management software",
    "Cloud-based management software",
    "Development environment software",
    "Data mining software",
    "Operating system software",
    "Project management software"
]


for skill in test_skills:

    group = find_skill_group(skill)

    print(
        f"{skill} -> {group}"
    )