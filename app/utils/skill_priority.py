from .skill_normalizer import normalize_skill


def calculate_skill_priorities(
    missing_skills,
    technical_requirements,
    software_data,
    essential_data
):
    priorities = []

    importance_data = essential_data[
        essential_data["Scale Name"] == "Importance"
    ]

    importance_lookup = {}

    for _, row in importance_data.iterrows():
        skill = normalize_skill(row["Element Name"])
        importance_lookup[skill] = row["Data Value"]

    software_lookup = {}

    for _, row in software_data.iterrows():
        skill = normalize_skill(row["Element Name"])

        software_lookup[skill] = {
            "in_demand": row["In Demand"],
            "hot_technology": row["Hot Technology"]
        }

    technical_lookup = {}

    for item in technical_requirements:

        skill = normalize_skill(
            item["skill"]
        )

        technical_lookup[skill] = item[
            "relevance_weight"
        ]

    for skill in missing_skills:

        normalized_skill = normalize_skill(skill)

        is_core_skill = (
            normalized_skill in importance_lookup
        )

        is_technical_skill = (
            normalized_skill in technical_lookup
        )

        if is_core_skill:

            importance = importance_lookup[
                normalized_skill
            ]

            priority_score = float(importance)

            if priority_score >= 4:
                priority = "High"

            elif priority_score >= 3:
                priority = "Medium"

            else:
                priority = "Low"

            priorities.append({
                "skill": skill,
                "type": "Core Skill",
                "importance": importance,
                "in_demand": "N/A",
                "hot_technology": "N/A",
                "priority_score": round(
                    priority_score,
                    2
                ),
                "priority": priority
            })

        elif is_technical_skill:

            priority_score = float(
                technical_lookup[
                    normalized_skill
                ]
            )

            in_demand = "N"
            hot_technology = "N"

            if normalized_skill in software_lookup:

                in_demand = software_lookup[
                    normalized_skill
                ]["in_demand"]

                hot_technology = software_lookup[
                    normalized_skill
                ]["hot_technology"]

                if in_demand == "Y":
                    priority_score += 2

                if hot_technology == "Y":
                    priority_score += 1

            if priority_score >= 4:
                priority = "High"

            elif priority_score >= 2:
                priority = "Medium"

            else:
                priority = "Low"

            priorities.append({
                "skill": skill,
                "type": "Technical Skill",
                "importance": "N/A",
                "in_demand": in_demand,
                "hot_technology": hot_technology,
                "priority_score": round(
                    priority_score,
                    2
                ),
                "priority": priority
            })

        else:

            priorities.append({
                "skill": skill,
                "type": "Unknown",
                "importance": "N/A",
                "in_demand": "N",
                "hot_technology": "N",
                "priority_score": 0,
                "priority": "Low"
            })

    priorities.sort(
        key=lambda item: item["priority_score"],
        reverse=True
    )

    return priorities