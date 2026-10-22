def evidence_is_sufficient(chunks: list[dict]) -> bool:
    return len(chunks) >= 2

def refine_query(user_request: str, chunks: list[dict]) -> str:
    return f"{user_request} official procedure responsibilities approval authority"
