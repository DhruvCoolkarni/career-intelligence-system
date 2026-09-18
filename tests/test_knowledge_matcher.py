import pandas as pd

from app.utils.knowledge_matcher import (
    calculate_knowledge_evidence
)


target_job = "Computer and Information Research Scientists"


knowledge_data = pd.read_csv(
    "data/onet/knowledge.csv"
)


knowledge_data = knowledge_data[
    knowledge_data["Title"].str.lower()
    == target_job.lower()
]


resume_text = """
Built machine learning projects using Python,
Pandas, NumPy, SQL, Docker and PyTorch.

Completed machine learning courses and certifications.

Created technical documentation and reports.
"""


results = calculate_knowledge_evidence(
    resume_text,
    knowledge_data
)


print("\n===== KNOWLEDGE EVIDENCE =====\n")


for result in results:

    if result["evidence_score"] > 0:

        print(
            f"{result['knowledge']} | "
            f"Importance: {result['importance']} | "
            f"Evidence: {result['evidence_score']} | "
            f"Matched Keywords: "
            f"{result['matched_keywords']}"
        )