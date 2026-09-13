import pandas as pd

from .skill_normalizer import normalize_skill


def load_learning_resources():
    file_path = "data/learning_resources.csv"

    resources = pd.read_csv(file_path)

    return resources


def get_learning_recommendations(missing_skills):
    resources = load_learning_resources()

    recommendations = []

    for skill in missing_skills:

        normalized_skill = normalize_skill(skill)

        matching_resource = resources[
            resources["skill"].str.lower() == normalized_skill
        ]

        if not matching_resource.empty:

            resource = matching_resource.iloc[0]

            recommendations.append({
                "skill": skill,
                "level": resource["level"],
                "learning_path": resource["learning_path"],
                "project_idea": resource["project_idea"]
            })

        else:

            recommendations.append({
                "skill": skill,
                "level": "Not available",
                "learning_path": "No learning path available yet.",
                "project_idea": "No project recommendation available yet."
            })

    return recommendations