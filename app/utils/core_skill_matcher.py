CORE_SKILL_EVIDENCE = {

    "reading comprehension": {
        "documentation",
        "technical documentation",
        "read technical documentation",
        "research",
        "researched",
        "understood requirements"
    },

    "active listening": {
        "collaborated",
        "collaboration",
        "teamwork",
        "worked with a team",
        "worked with teams",
        "cross-functional team",
        "cross-functional teams",
        "requirements",
        "discussion",
        "discussions",
        "stakeholder"
    },

    "writing": {
        "documentation",
        "technical documentation",
        "technical writing",
        "written",
        "report",
        "reports",
        "documented",
        "documented projects"
    },

    "speaking": {
        "presentation",
        "presented",
        "presentations",
        "communication",
        "communicated",
        "explained",
        "demonstrated",
        "public speaking"
    },

    "mathematics": {
        "mathematics",
        "math",
        "statistics",
        "probability",
        "calculation",
        "calculated",
        "mathematical"
    },

    "science": {
        "science",
        "scientific",
        "experiment",
        "experiments",
        "research",
        "research project"
    },

    "critical thinking": {
        "analysis",
        "analyzed",
        "analyze",
        "problem solving",
        "problem-solving",
        "solved problems",
        "solving problems",
        "evaluation",
        "evaluated",
        "decision making",
        "decision-making",
        "debugged",
        "debugging",
        "troubleshooting",
        "identified issues",
        "identified problems"
    },

    "active learning": {
        "learned",
        "learning",
        "learn new",
        "course",
        "courses",
        "certification",
        "certifications",
        "training",
        "trained",
        "self-learning",
        "self learning"
    },

    "learning strategies": {
        "training",
        "course",
        "courses",
        "certification",
        "certifications",
        "self-learning",
        "self learning",
        "learning plan",
        "learning path",
        "skill development"
    },

    "monitoring": {
        "monitor",
        "monitoring",
        "tracked",
        "tracking",
        "performance",
        "metrics",
        "measured",
        "measurement",
        "performance monitoring"
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