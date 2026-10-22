from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4",
    instructions=(
        "You are BlueVivo's reporting support agent. "
        "Use code interpreter when calculation or data transformation is required."
    ),
    input="Analyze the attached CSV of weekly project metrics and identify the two projects with the highest risk trend.",
    tools=[{"type": "code_interpreter"}]
)
print(response.output_text)
