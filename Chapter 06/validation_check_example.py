def validate_chunk(chunk: dict) -> None:
    required_fields = ["chunk_id", "doc_id", "text", "chunk_index"]
    for field in required_fields:
        if field not in chunk or not chunk[field]:
            raise ValueError(f"Missing required field: {field}")

    if len(chunk["text"]) < 100:
        raise ValueError("Chunk is too small to be useful for retrieval")

