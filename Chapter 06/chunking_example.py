def chunk_text(text: str, max_chars: int = 1200, overlap: int = 150) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + max_chars, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap

    return chunks
