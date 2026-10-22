from openai import OpenAI

client = OpenAI()

def generate_client_brief(question, context_text, reasoning_effort="medium"):
    response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": reasoning_effort},
        input=[
            {
                "role": "system",
                "content": (
                    "You are an internal BlueVivo research agent. "
                    "Produce concise, evidence-grounded responses for consultants."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Question: {question}\n\n"
                    f"Context:\n{context_text}"
                )
            }
        ]
    )
    return response.output_text
