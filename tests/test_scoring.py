from app.utils.career_requirements import (
    get_curated_requirements
)

from app.utils.technical_requirements import (
    get_technical_requirements
)

from app.utils.career_scores import (
    calculate_technical_score,
    calculate_core_skill_score,
    calculate_knowledge_score,
    calculate_career_readiness
)


def test_career_requirements():

    requirements = get_curated_requirements(
        "Machine Learning Engineer"
    )

    assert "python" in requirements
    assert "database" in requirements
    assert "machine learning" in requirements
    assert "docker" in requirements
    assert "git" in requirements


def test_technical_score():

    requirements = get_technical_requirements(
        "Machine Learning Engineer"
    )

    user_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Docker",
        "Git",
        "Scikit-learn"
    ]

    score = calculate_technical_score(
        user_skills,
        requirements
    )

    assert score == 100.0


def test_core_skill_score():

    evidence = [
        {
            "skill": "Critical Thinking",
            "importance": 4.0,
            "evidence_score": 1.0
        },
        {
            "skill": "Writing",
            "importance": 3.0,
            "evidence_score": 0.5
        }
    ]

    score = calculate_core_skill_score(
        evidence
    )

    assert score == 78.57


def test_knowledge_score():

    evidence = [
        {
            "knowledge": "Computers and Electronics",
            "importance": 4.0,
            "evidence_score": 1.0
        },
        {
            "knowledge": "Mathematics",
            "importance": 2.0,
            "evidence_score": 0.5
        }
    ]

    score = calculate_knowledge_score(
        evidence
    )

    assert score == 83.33


def test_overall_career_readiness():

    score = calculate_career_readiness(
        100.0,
        50.0,
        80.0,
        20.0
    )

    assert score == 73.0