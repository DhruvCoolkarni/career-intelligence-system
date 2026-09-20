CAREER_CATALOG = {

    "Machine Learning Engineer": {
        "aliases": [
            "machine learning",
            "ml engineer",
            "machine learning engineer"
        ],
        "onet_title": (
            "Computer and Information Research Scientists"
        ),
        "onet_soc": "15-1221.00"
    },

    "AI Engineer": {
        "aliases": [
            "ai",
            "ai engineer",
            "artificial intelligence",
            "artificial intelligence engineer"
        ],
        "onet_title": (
            "Computer and Information Research Scientists"
        ),
        "onet_soc": "15-1221.00"
    },

    "Data Scientist": {
        "aliases": [
            "data science",
            "data scientist"
        ],
        "onet_title": "Data Scientists",
        "onet_soc": "15-2051.00"
    },

    "Data Analyst": {
        "aliases": [
            "data analyst",
            "data analysis"
        ],
        "onet_title": "Data Scientists",
        "onet_soc": "15-2051.00"
    },

    "Computer Vision Engineer": {
        "aliases": [
            "computer vision",
            "computer vision engineer",
            "cv engineer"
        ],
        "onet_title": (
            "Computer and Information Research Scientists"
        ),
        "onet_soc": "15-1221.00"
    },

    "NLP Engineer": {
        "aliases": [
            "nlp",
            "nlp engineer",
            "natural language processing"
        ],
        "onet_title": (
            "Computer and Information Research Scientists"
        ),
        "onet_soc": "15-1221.00"
    },

    "Software Engineer": {
        "aliases": [
            "software engineer",
            "software developer",
            "software development",
            "computer software engineer",
            "systems software engineer",
            "full stack software engineer"
        ],
        "onet_title": "Software Developers",
        "onet_soc": "15-1252.00"
    },

    "Cybersecurity Analyst": {
        "aliases": [
            "cybersecurity",
            "cyber security",
            "cybersecurity analyst",
            "cyber security analyst"
        ],
        "onet_title": "Information Security Analysts",
        "onet_soc": "15-1212.00"
    },

    "Ethical Hacker / Penetration Tester": {
        "aliases": [
            "ethical hacker",
            "ethical hacking",
            "penetration tester",
            "penetration testing",
            "pentester",
            "pentesting",
            "cyber security tester"
        ],
        "onet_title": "Penetration Testers",
        "onet_soc": "15-1299.04"
    },

    "Software Tester / QA Engineer": {
        "aliases": [
            "software tester",
            "software testing",
            "qa",
            "qa engineer",
            "qa tester",
            "software qa",
            "automation tester",
            "quality assurance"
        ],
        "onet_title": (
            "Software Quality Assurance Analysts and Testers"
        ),
        "onet_soc": "15-1253.00"
    },

    "DevOps Engineer": {
        "aliases": [
            "devops",
            "devops engineer",
            "dev ops",
            "devops developer",
            "devops architect"
        ],
        "onet_title": "Software Developers",
        "onet_soc": "15-1252.00"
    },

    "Business Intelligence Analyst": {
        "aliases": [
            "business intelligence",
            "bi",
            "bi analyst",
            "business intelligence analyst",
            "business intelligence engineer",
            "business intelligence specialist"
        ],
        "onet_title": "Business Intelligence Analysts",
        "onet_soc": "15-2051.01"
    }
}
def resolve_career(query):

    if not query:
        return None

    query = str(query).strip().lower()

    for career, profile in CAREER_CATALOG.items():

        if query == career.lower():
            return career

        for alias in profile["aliases"]:

            if query == alias.lower():
                return career

    return None