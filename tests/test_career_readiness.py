from app.utils.career_scores import calculate_career_readiness


technical_score = 70
core_skill_score = 80
knowledge_score = 75
market_relevance_score = 60


readiness = calculate_career_readiness(
    technical_score,
    core_skill_score,
    knowledge_score,
    market_relevance_score
)


print("Career Readiness:", readiness)