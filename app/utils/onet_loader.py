import pandas as pd


def load_software_skills():
    file_path = "data/onet/software_skills.csv"

    software_skills = pd.read_csv(file_path)

    return software_skills


def load_essential_skills():
    file_path = "data/onet/essential_skills.csv"

    essential_skills = pd.read_csv(file_path)

    return essential_skills


def get_software_skills_for_job(target_job):
    software_skills = load_software_skills()

    matching_data = software_skills[
        software_skills["Title"].str.lower() == target_job.lower()
    ]

    return matching_data


def get_essential_skills_for_job(target_job):
    essential_skills = load_essential_skills()

    matching_data = essential_skills[
        essential_skills["Title"].str.lower() == target_job.lower()
    ]

    return matching_data