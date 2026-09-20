import pandas as pd

from .career_catalog import resolve_career
from .career_catalog import CAREER_CATALOG


def load_software_skills():
    file_path = "data/onet/software_skills.csv"

    software_skills = pd.read_csv(file_path)

    return software_skills


def load_essential_skills():
    file_path = "data/onet/essential_skills.csv"

    essential_skills = pd.read_csv(file_path)

    return essential_skills


def get_onet_title(target_job):

    canonical_career = resolve_career(
        target_job
    )

    if canonical_career is None:
        return None

    return CAREER_CATALOG[
        canonical_career
    ]["onet_title"]


def get_software_skills_for_job(target_job):

    software_skills = load_software_skills()

    onet_title = get_onet_title(
        target_job
    )

    if onet_title is None:
        return software_skills.iloc[0:0]

    matching_data = software_skills[
        software_skills["Title"].str.lower()
        == onet_title.lower()
    ]

    return matching_data


def get_essential_skills_for_job(target_job):

    essential_skills = load_essential_skills()

    onet_title = get_onet_title(
        target_job
    )

    if onet_title is None:
        return essential_skills.iloc[0:0]

    matching_data = essential_skills[
        essential_skills["Title"].str.lower()
        == onet_title.lower()
    ]

    return matching_data