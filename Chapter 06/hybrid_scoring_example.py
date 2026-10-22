def combined_score(vector_score: float, keyword_score: float, alpha: float = 0.7) -> float:
    return (alpha * vector_score) + ((1 - alpha) * keyword_score)
