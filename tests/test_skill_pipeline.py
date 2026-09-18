from app.utils.skill_extractor import extract_skills
from app.utils.skill_normalizer import normalize_skills
from app.utils.skill_gap import calculate_skill_gap


def test_skill_extraction():

    resume_text = """
    Python SQL Pandas NumPy Machine Learning Git Docker
    """

    skills = extract_skills(resume_text)

    assert "Python" in skills
    assert "SQL" in skills
    assert "Machine Learning" in skills
    assert "Docker" in skills


def test_skill_normalization():

    skills = [
        "Python",
        "SQL",
        "MySQL",
        "GitHub"
    ]

    normalized = normalize_skills(skills)

    assert "python" in normalized
    assert "database" in normalized
    assert "git" in normalized


def test_skill_gap():

    user_skills = [
        "Python",
        "SQL",
        "Git"
    ]

    required_skills = [
        "python",
        "database",
        "git",
        "docker"
    ]

    matched, missing = calculate_skill_gap(
        user_skills,
        required_skills
    )

    assert "python" in matched
    assert "database" in matched
    assert "git" in matched
    assert "docker" in missing