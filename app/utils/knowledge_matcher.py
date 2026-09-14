from .skill_normalizer import normalize_skill


KNOWLEDGE_EVIDENCE = {

    "computers and electronics": {
        "python",
        "java",
        "c++",
        "database",
        "pandas",
        "numpy",
        "scikit-learn",
        "machine learning",
        "pytorch",
        "tensorflow",
        "git",
        "docker",
        "operating system software",
        "development environment"
    },

    "mathematics": {
        "numpy",
        "machine learning",
        "scikit-learn"
    },

    "engineering and technology": {
        "python",
        "java",
        "c++",
        "docker",
        "machine learning",
        "pytorch",
        "tensorflow"
    },

    "telecommunications": {
        "network monitoring software",
        "network security and virtual private network vpn equipmentsoftware",
        "lan software",
        "wireless software"
    }
}


def calculate_knowledge_evidence(
    user_skills,
    knowledge_data
):
    normalized_user_skills = {
        normalize_skill(skill)
        for skill in user_skills
    }

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

        evidence_skills = KNOWLEDGE_EVIDENCE.get(
            knowledge_name,
            set()
        )

        matched_evidence = (
            normalized_user_skills
            & evidence_skills
        )

        if matched_evidence:

            evidence_score = min(
                len(matched_evidence) / 3,
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
            "matched_skills": sorted(
                matched_evidence
            )
        })


    return knowledge_scores