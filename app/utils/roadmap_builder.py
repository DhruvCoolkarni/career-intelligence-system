def build_learning_roadmap(
    recommendations,
    priorities
):
    priority_lookup = {
        item["skill"]: item
        for item in priorities
    }

    roadmap = {
        "Phase 1 — Foundations": [],
        "Phase 2 — Intermediate Skills": [],
        "Phase 3 — Advanced Skills": []
    }

    for recommendation in recommendations:

        if recommendation["level"] == "Not available":
            continue

        skill = recommendation["skill"]

        priority_data = priority_lookup.get(
            skill,
            {}
        )

        priority_score = priority_data.get(
            "priority_score",
            0
        )

        level = recommendation["level"]

        roadmap_item = {
            "skill": skill,
            "priority": priority_data.get(
                "priority",
                "Low"
            ),
            "priority_score": priority_score,
            "learning_path": recommendation[
                "learning_path"
            ],
            "project_idea": recommendation[
                "project_idea"
            ]
        }

        if level == "Beginner":

            roadmap["Phase 1 — Foundations"].append(
                roadmap_item
            )

        elif level == "Intermediate":

            roadmap["Phase 2 — Intermediate Skills"].append(
                roadmap_item
            )

        else:

            roadmap["Phase 3 — Advanced Skills"].append(
                roadmap_item
            )

    for phase in roadmap:

        roadmap[phase].sort(
            key=lambda item: item["priority_score"],
            reverse=True
        )

    return roadmap