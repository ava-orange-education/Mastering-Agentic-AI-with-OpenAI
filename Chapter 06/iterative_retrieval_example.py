def multi_step_hr_workflow(user_request: str, retriever, generator) -> str:
    policy_chunks = retriever.search("employee leave policy", top_k=3)
    category_chunks = retriever.search("employee classification definitions", top_k=3)

    combined_context = prepare_context(policy_chunks) + prepare_context(category_chunks)

    return generator(user_request, context=combined_context)
