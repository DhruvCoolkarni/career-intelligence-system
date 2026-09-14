import pandas as pd


target_job = "Computer and Information Systems Managers"


abilities_data = pd.read_csv(
    "data/onet/abilities.csv"
)


job_data = abilities_data[
    abilities_data["Title"].str.lower()
    == target_job.lower()
].copy()


print("\n===== CAREER ABILITIES =====\n")

print("Target Job:")
print(target_job)

print("\nTotal Ability Records:")
print(len(job_data))


print("\n===== ABILITY IMPORTANCE =====\n")

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
    list(abilities_data.columns)
)