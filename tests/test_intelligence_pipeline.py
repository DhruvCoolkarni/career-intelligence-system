import pandas as pd

from app.utils.career_scores import (
    calculate_market_relevance_score
)

from app.utils.learning_recommender import (
    get_learning_recommendations
)

from app.utils.roadmap_builder import (
    build_learning_roadmap
)


def test_market_relevance():

    job_data = pd.read_csv(
        "data/onet/software_skills.csv"
    )

    job_data = job_data[
        job_data["Title"]
        .str.strip()
        .str.lower()
        == "computer and information research scientists"
    ]

    result = calculate_market_relevance_score(
        job_data,
        [
            "Python",
            "SQL",
            "Machine Learning",
            "Docker",
            "Git"
        ]
    )

    assert result["score"] == 7.14
    assert "database" in result["matched_groups"]
    assert len(result["missing_groups"]) == 13


def test_learning_recommendations():

    recommendations = get_learning_recommendations(
        ["database"]
    )

    assert len(recommendations) > 0
    assert recommendations[0]["skill"] == "database"
    assert "learning_path" in recommendations[0]
    assert "project_idea" in recommendations[0]


def test_roadmap():

    recommendations = get_learning_recommendations(
        ["database"]
    )

    priorities = [
        {
            "skill": "database",
            "priority": "High",
            "priority_score": 10
        }
    ]

    roadmap = build_learning_roadmap(
        recommendations,
        priorities
    )

    assert roadmap
    assert any(
        len(items) > 0
        for items in roadmap.values()
    )