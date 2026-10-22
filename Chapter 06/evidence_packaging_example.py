def prepare_context(chunks: list[dict]) -> list[dict]:
    return [
        {
            "title": chunk["metadata"].get("title", "Untitled"),
            "section": chunk["metadata"].get("section_title", "Unknown Section"),
            "text": chunk["text"]
        }
        for chunk in chunks
    ]
