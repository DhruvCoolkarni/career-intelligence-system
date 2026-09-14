import pandas as pd

from app.utils.knowledge_matcher import (
    calculate_knowledge_evidence
)


target_job = "Computer and Information Systems Managers"


knowledge_data = pd.read_csv(
    "data/onet/knowledge.csv"
)


knowledge_data = knowledge_data[
    knowledge_data["Title"].str.lower()
    == target_job.lower()
]


user_skills = [
    "Python",
    "SQL",
    "MySQL",
    "Docker",
    "Linux",
    "Pandas",
    "NumPy",
    "Machine Learning"
]


results = calculate_knowledge_evidence(
    user_skills,
    knowledge_data
)


print("\n===== KNOWLEDGE EVIDENCE =====\n")


for result in results:

    if result["evidence_score"] > 0:

        print(
            f"{result['knowledge']} | "
            f"Importance: {result['importance']} | "
            f"Evidence: {result['evidence_score']} | "
            f"Matched Skills: "
            f"{result['matched_skills']}"
        )