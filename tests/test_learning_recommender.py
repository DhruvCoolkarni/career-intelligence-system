from app.utils.learning_recommender import (
    get_learning_recommendations
)


missing_skills = [
    "Python",
    "MySQL",
    "Docker",
    "Pandas",
    "Unknown Skill"
]


recommendations = get_learning_recommendations(
    missing_skills
)


print("\n===== LEARNING RECOMMENDATIONS =====\n")


for recommendation in recommendations:

    print("Skill:", recommendation["skill"])
    print("Level:", recommendation["level"])
    print("Learning Path:", recommendation["learning_path"])
    print("Project Idea:", recommendation["project_idea"])
    print("-----------------------------------")