def agentic_rag_flow(user_request: str, retriever, generator) -> str:
    if not should_retrieve(user_request):
        return generator(user_request, context=[])

    retrieved_chunks = retriever.search(user_request, top_k=5)

    if not retrieved_chunks:
        return "I could not find supporting information in the available knowledge sources."

    if not evidence_is_sufficient(retrieved_chunks):
        refined_query = refine_query(user_request, retrieved_chunks)
        retrieved_chunks = retriever.search(refined_query, top_k=5)

    return generator(user_request, context=retrieved_chunks)
