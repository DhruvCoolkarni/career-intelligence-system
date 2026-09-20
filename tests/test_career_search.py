from app.utils.career_search import search_careers


def test_software_developer_alias():

    results = search_careers(
        "software developer"
    )

    assert "Software Engineer" in results


def test_ai_alias():

    results = search_careers(
        "ai"
    )

    assert "AI Engineer" in results


def test_pentesting_alias():

    results = search_careers(
        "pentesting"
    )

    assert "Ethical Hacker / Penetration Tester" in results


def test_python_returns_multiple_careers():

    results = search_careers(
        "python"
    )

    assert "Machine Learning Engineer" in results
    assert "Data Scientist" in results
    assert "Data Analyst" in results


def test_empty_search():

    results = search_careers("")

    assert results == []