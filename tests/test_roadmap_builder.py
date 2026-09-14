from app.utils.roadmap_builder import build_learning_roadmap


recommendations = [
    {
        "skill": "Python",
        "level": "Beginner",
        "learning_path": "Python fundamentals → functions → data structures",
        "project_idea": "Build a Python project"
    },
    {
        "skill": "Pandas",
        "level": "Beginner",
        "learning_path": "DataFrames → cleaning → filtering",
        "project_idea": "Build a data analysis project"
    },
    {
        "skill": "Machine Learning",
        "level": "Intermediate",
        "learning_path": "Supervised learning → preprocessing → evaluation",
        "project_idea": "Build an ML project"
    },
    {
        "skill": "Docker",
        "level": "Intermediate",
        "learning_path": "Docker basics → images → containers",
        "project_idea": "Containerize a Python application"
    }
]


priorities = [
    {
        "skill": "Python",
        "priority": "High",
        "priority_score": 4
    },
    {
        "skill": "Pandas",
        "priority": "Medium",
        "priority_score": 3
    },
    {
        "skill": "Machine Learning",
        "priority": "High",
        "priority_score": 4
    },
    {
        "skill": "Docker",
        "priority": "Medium",
        "priority_score": 2
    }
]


roadmap = build_learning_roadmap(
    recommendations,
    priorities
)


print("\n===== CAREER LEARNING ROADMAP =====\n")


for phase, skills in roadmap.items():

    print(phase)

    for skill in skills:

        print(
            f"  {skill['skill']} | "
            f"{skill['priority']} | "
            f"Score: {skill['priority_score']}"
        )

    print()