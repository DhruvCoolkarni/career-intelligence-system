CAREER_PROFILES = {

    "machine learning engineer": {
        "onet_title": "Computer and Information Research Scientists"
    },

    "data scientist": {
        "onet_title": "Data Scientists"
    },

    "data analyst": {
        "onet_title": "Data Scientists"
    },

    "computer vision engineer": {
        "onet_title": "Computer and Information Research Scientists"
    },

    "nlp engineer": {
        "onet_title": "Computer and Information Research Scientists"
    }
}


def get_career_profile(target_job):

    job_key = (
        str(target_job)
        .strip()
        .lower()
    )

    return CAREER_PROFILES.get(
        job_key
    )