import pandas as pd


file_path = "data/onet/essential_skills.csv"

essential_skills = pd.read_csv(file_path)

print("Dataset shape:")
print(essential_skills.shape)

print("\nColumn names:")
print(essential_skills.columns.tolist())

print("\nFirst 5 rows:")
print(essential_skills.head())


target_occupation = "Computer and Information Systems Managers"

occupation_data = essential_skills[
    essential_skills["Title"] == target_occupation
]

print("\nEssential skills for", target_occupation)

print(
    occupation_data[
        ["Element Name", "Scale Name", "Data Value"]
    ].to_string(index=False)
)

print("\nImportance values:")

importance_data = occupation_data[
    occupation_data["Scale Name"] == "Importance"
]

print(
    importance_data[
        ["Element Name", "Data Value"]
    ].sort_values(
        by="Data Value",
        ascending=False
    )
)