import pandas as pd

from .career_catalog import CAREER_CATALOG


def search_careers(query):

    if not query:
        return []

    query = str(query).strip().lower()

    if not query:
        return []

    requirements = pd.read_csv(
        "data/job_requirements.csv"
    )

    recommendations = []

    for career, profile in CAREER_CATALOG.items():

        career_name = career.lower()
        score = 0

        # Exact career name
        if query == career_name:
            score = 100

        # Career name contains query
        elif query in career_name:
            score = 90

        else:

            # Check aliases
            for alias in profile["aliases"]:

                alias = alias.lower()

                if query == alias:
                    score = max(score, 80)

                elif query in alias:
                    score = max(score, 70)

                elif alias in query:
                    score = max(score, 60)

            # Check required skills
            matching_job = requirements[
                requirements["job"]
                .astype(str)
                .str.strip()
                .str.lower()
                == career_name
            ]

            if not matching_job.empty:

                required_skills = (
                    matching_job.iloc[0]["required_skills"]
                    .split(",")
                )

                for skill in required_skills:

                    skill = skill.strip().lower()

                    if query == skill:
                        score = max(score, 50)

                    elif query in skill:
                        score = max(score, 30)

        if score > 0:

            recommendations.append(
                (career, score)
            )

    recommendations.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return [
    career
    for career, score in recommendations[:5]
]