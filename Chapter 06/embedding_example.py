from openai import OpenAI

client = OpenAI()

def embed_text(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return response.data[0].embedding
Each chunk can then be packaged for storage in the retrieval layer:
indexed_chunk = {
    "id": chunk_record["chunk_id"],
    "vector": embed_text(chunk_record["text"]),
    "text": chunk_record["text"],
    "metadata": {
        "doc_id": chunk_record["doc_id"],
        "section_title": chunk_record["section_title"],
        "chunk_index": chunk_record["chunk_index"],
        "last_modified": chunk_record["last_modified"],
        "classification": chunk_record["classification"]
    }
}
