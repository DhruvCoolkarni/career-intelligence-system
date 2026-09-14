import pandas as pd


target_job = "Computer and Information Systems Managers"

knowledge_data = pd.read_csv(
    "data/onet/knowledge.csv"
)


job_data = knowledge_data[
    knowledge_data["Title"].str.lower()
    == target_job.lower()
].copy()


print("\n===== CAREER KNOWLEDGE =====\n")

print("Target Job:")
print(target_job)

print("\nTotal Knowledge Records:")
print(len(job_data))


print("\n===== KNOWLEDGE IMPORTANCE =====\n")

importance_data = job_data[
    job_data["Scale Name"] == "Importance"
].copy()


importance_data = importance_data.sort_values(
    by="Data Value",
    ascending=False
)


print(
    importance_data[
        ["Element Name", "Data Value"]
    ].to_string(index=False)
)


print("\n===== AVAILABLE COLUMNS =====\n")

print(
    list(knowledge_data.columns)
)