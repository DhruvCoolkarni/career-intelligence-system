from app.utils.career_scores import calculate_career_readiness


profiles = {
    "Strong Candidate": {
        "technical": 90,
        "core": 90,
        "knowledge": 90,
        "market": 90
    },

    "Average Candidate": {
        "technical": 60,
        "core": 60,
        "knowledge": 60,
        "market": 60
    },

    "Weak Candidate": {
        "technical": 20,
        "core": 30,
        "knowledge": 25,
        "market": 20
    },

    "Technical Heavy Candidate": {
        "technical": 90,
        "core": 40,
        "knowledge": 60,
        "market": 80
    }
}


for name, profile in profiles.items():

    score = calculate_career_readiness(
        profile["technical"],
        profile["core"],
        profile["knowledge"],
        profile["market"]
    )

    print(
        f"{name}: {score}%"
    )