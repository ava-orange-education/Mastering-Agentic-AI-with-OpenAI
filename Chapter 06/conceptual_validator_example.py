def validate_answer(answer: str, chunks: list[dict]) -> bool:
    source_text = " ".join(chunk["text"] for chunk in chunks)
    key_phrases = answer.split(".")
    supported = sum(1 for phrase in key_phrases if phrase.strip() and phrase.strip() in source_text)
    return supported > 0
