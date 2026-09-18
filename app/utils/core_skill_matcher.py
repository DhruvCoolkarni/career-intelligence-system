CORE_SKILL_EVIDENCE = {

    "reading comprehension": {
        "read",
        "documentation",
        "research",
        "technical documentation"
    },

    "active listening": {
        "collaborated",
        "teamwork",
        "requirements",
        "discussion"
    },

    "writing": {
        "documentation",
        "report",
        "reports",
        "technical writing",
        "written"
    },

    "speaking": {
        "presentation",
        "presented",
        "presentations",
        "communication",
        "explained"
    },

    "mathematics": {
        "mathematics",
        "math",
        "statistics",
        "probability",
        "calculation"
    },

    "science": {
        "science",
        "scientific",
        "experiment",
        "experiments"
    },

    "critical thinking": {
        "analysis",
        "analyzed",
        "problem solving",
        "problem-solving",
        "evaluation",
        "evaluated",
        "decision making"
    },

    "active learning": {
        "learned",
        "learning",
        "course",
        "courses",
        "certification",
        "certifications",
        "training"
    },

    "learning strategies": {
        "training",
        "course",
        "courses",
        "certification",
        "self-learning",
        "self learning"
    },

    "monitoring": {
        "monitor",
        "monitoring",
        "tracked",
        "tracking",
        "performance",
        "metrics"
    }
}


def calculate_core_skill_evidence(
    resume_text,
    essential_data
):

    resume_text = resume_text.lower()

    evidence_scores = []

    importance_data = essential_data[
        essential_data["Scale Name"] == "Importance"
    ]

    for _, row in importance_data.iterrows():

        skill_name = (
            row["Element Name"]
            .lower()
            .strip()
        )

        evidence_keywords = CORE_SKILL_EVIDENCE.get(
            skill_name,
            set()
        )

        matched_keywords = []

        for keyword in evidence_keywords:

            if keyword in resume_text:
                matched_keywords.append(keyword)

        if matched_keywords:

            evidence_score = min(
                len(matched_keywords) / 2,
                1
            )

        else:

            evidence_score = 0

        evidence_scores.append({
            "skill": row["Element Name"],
            "importance": row["Data Value"],
            "evidence_score": round(
                evidence_score,
                2
            ),
            "matched_keywords": sorted(
                matched_keywords
            )
        })

    return evidence_scores