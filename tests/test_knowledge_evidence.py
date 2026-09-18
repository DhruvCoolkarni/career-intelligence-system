from app.utils.knowledge_matcher import (
    calculate_knowledge_evidence
)

import pandas as pd


target_job = "Computer and Information Research Scientists"

resume_text = """
Developed machine learning models using Python.
Used statistics and probability for data analysis.
Built deep learning projects with PyTorch.
Created technical documentation and reports.
Completed machine learning courses and certifications.
"""


knowledge_data = pd.read_csv(
    "data/onet/knowledge.csv"
)

knowledge_data = knowledge_data[
    knowledge_data["Title"].str.lower().str.strip()
    == target_job.lower()
]


results = calculate_knowledge_evidence(
    resume_text,
    knowledge_data
)


print("===== KNOWLEDGE EVIDENCE =====")

for item in results:

    if item["evidence_score"] > 0:

        print(
            item["knowledge"],
            "| Importance:",
            item["importance"],
            "| Evidence:",
            item["evidence_score"],
            "| Keywords:",
            item["matched_keywords"]
        )