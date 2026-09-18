KNOWLEDGE_EVIDENCE = {

    "computers and electronics": {
        "python",
        "java",
        "c++",
        "programming",
        "software",
        "machine learning",
        "deep learning",
        "computer vision",
        "artificial intelligence",
        "database",
        "sql",
        "docker",
        "pytorch",
        "tensorflow"
    },

    "mathematics": {
        "mathematics",
        "math",
        "statistics",
        "statistical",
        "probability",
        "linear algebra",
        "calculus",
        "numerical"
    },

    "engineering and technology": {
        "engineering",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "software development",
        "programming",
        "algorithm",
        "algorithms",
        "computer vision",
        "nlp"
    },

    "english language": {
        "technical documentation",
        "documentation",
        "technical writing",
        "report",
        "reports",
        "written",
        "writing"
    },

    "design": {
        "design",
        "ui",
        "ux",
        "user interface",
        "user experience",
        "prototype",
        "prototyping"
    },

    "telecommunications": {
        "network",
        "networking",
        "tcp",
        "ip",
        "wireless",
        "telecommunication"
    },

    "education and training": {
        "teaching",
        "training",
        "course",
        "courses",
        "certification",
        "certifications",
        "workshop",
        "learning"
    },

    "administration and management": {
        "management",
        "managed",
        "leadership",
        "project management",
        "team lead",
        "planning"
    },

    "sales and marketing": {
        "marketing",
        "sales",
        "customer",
        "market research",
        "campaign"
    },

    "customer and personal service": {
        "customer",
        "client",
        "support",
        "service",
        "user support"
    },

    "public safety and security": {
        "cybersecurity",
        "security",
        "information security",
        "network security",
        "authentication",
        "encryption"
    }
}


def calculate_knowledge_evidence(
    resume_text,
    knowledge_data
):

    resume_text = resume_text.lower()

    knowledge_scores = []

    importance_data = knowledge_data[
        knowledge_data["Scale Name"] == "Importance"
    ]

    for _, row in importance_data.iterrows():

        knowledge_name = (
            row["Element Name"]
            .lower()
            .strip()
        )

        evidence_keywords = KNOWLEDGE_EVIDENCE.get(
            knowledge_name,
            set()
        )

        matched_keywords = []

        for keyword in evidence_keywords:

            if keyword in resume_text:
                matched_keywords.append(keyword)

        if matched_keywords:

            evidence_score = min(
                len(matched_keywords) / 3,
                1
            )

        else:

            evidence_score = 0

        knowledge_scores.append({
            "knowledge": row["Element Name"],
            "importance": row["Data Value"],
            "evidence_score": round(
                evidence_score,
                2
            ),
            "matched_keywords": sorted(
                matched_keywords
            )
        })

    return knowledge_scores