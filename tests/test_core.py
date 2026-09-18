from app.utils.text_cleaner import clean_text
from app.utils.skill_normalizer import normalize_skill
from app.utils.skill_matcher import skills_match


def test_text_cleaning():

    text = "  Python   SQL\nMachine Learning  "

    result = clean_text(text)

    assert result == "python sql machine learning"


def test_skill_normalization():

    assert normalize_skill("MySQL") == "database"
    assert normalize_skill("GitHub") == "git"
    assert normalize_skill("sklearn") == "scikit-learn"


def test_skill_matching():

    assert skills_match(
        "GitHub",
        "Git"
    )

    assert skills_match(
        "MySQL",
        "Database"
    )

    assert skills_match(
        "Python",
        "Python"
    )

    assert not skills_match(
        "Docker",
        "Database"
    )
    