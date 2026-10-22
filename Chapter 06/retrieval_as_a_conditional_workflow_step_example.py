def should_retrieve(user_request: str) -> bool:
    retrieval_signals = [
        "current policy",
        "latest",
        "based on our documentation",
        "what does the handbook say",
        "according to",
        "find"
    ]
    lowered = user_request.lower()
    return any(signal in lowered for signal in retrieval_signals)
