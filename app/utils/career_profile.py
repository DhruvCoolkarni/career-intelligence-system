from .career_catalog import resolve_career
from .career_catalog import CAREER_CATALOG


def get_career_profile(target_job):

    canonical_career = resolve_career(
        target_job
    )

    if canonical_career is None:
        return None

    profile = CAREER_CATALOG[
        canonical_career
    ]

    return {
        "onet_title": profile["onet_title"],
        "onet_soc": profile["onet_soc"]
    }