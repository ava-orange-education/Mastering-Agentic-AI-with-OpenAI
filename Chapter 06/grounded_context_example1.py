def build_grounded_context(chunks: list[dict]) -> str:
    sections = []
    for chunk in chunks:
        title = chunk["metadata"].get("title", "Untitled Source")
        text = chunk["text"]
        sections.append(f"Source: {title}\n{text}")
    return "\n\n".join(sections)
