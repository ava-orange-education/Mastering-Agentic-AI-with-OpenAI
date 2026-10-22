query_vector = embed_query("What is the retention period for student disciplinary records?")

results = vector_store.search(
    vector=query_vector,
    top_k=5,
    filters={"classification": "internal", "department": "Academic Affairs"}
)
