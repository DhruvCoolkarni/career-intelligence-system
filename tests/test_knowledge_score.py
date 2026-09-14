from app.utils.career_scores import calculate_knowledge_score


sample_knowledge_scores = [
    {
        "knowledge": "Computers and Electronics",
        "importance": 4.77,
        "evidence_score": 1
    },
    {
        "knowledge": "Engineering and Technology",
        "importance": 3.50,
        "evidence_score": 1
    },
    {
        "knowledge": "Mathematics",
        "importance": 3.16,
        "evidence_score": 0.67
    }
]


score = calculate_knowledge_score(
    sample_knowledge_scores
)

print("Knowledge Score:", score)