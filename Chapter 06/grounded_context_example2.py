def generate_grounded_prompt(user_request: str, context: str) -> str:
    return f"""
Answer the user's request using only the retrieved evidence below.
If the evidence does not support a complete answer, say so clearly.
Do not add unsupported details.

User request:
{user_request}

Retrieved evidence:
{context}
""".strip()
