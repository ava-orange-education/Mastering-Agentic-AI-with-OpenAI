from openai import OpenAI

client = OpenAI()

# Turn 1: initial summary request
response_1 = client.responses.create(
    model="gpt-5.4",
    instructions=(
        "You are BlueVivo's internal delivery support agent. "
        "Provide concise, professional output suitable for consulting teams."
    ),
    input=(
        "Summarize the following client discovery notes into five bullet points: "
        "The client wants an AI-assisted knowledge portal, requires role-based access, "
        "must support audit logging, and is concerned about latency and data residency."
    )
)
print(response_1.output_text)

# Turn 2: refine the prior result without manually replaying it
response_2 = client.responses.create(
    model="gpt-5.4",
    previous_response_id=response_1.id,
    input=(
        "Rewrite that summary for an executive sponsor. Use a short paragraph instead of bullets."
    )
)
print(response_2.output_text)
