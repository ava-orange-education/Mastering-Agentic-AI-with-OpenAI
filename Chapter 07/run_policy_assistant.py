def run_policy_assistant(user_question, retrieved_documents):
    classification = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "medium"},
        input=f"Classify the user's request: {user_question}"
    )

    evaluation = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "high"},
        input=(
            f"Evaluate these documents against the request.\n\n"
            f"Request: {user_question}\n\nDocuments:\n{retrieved_documents}"
        )
    )

    final_response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        input=(
            "Convert the evaluation into a concise internal response for a consultant.\n\n"
            f"{evaluation.output_text}"
        )
    )

    return final_response.output_text
