import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured.")

if not model_name:
    raise RuntimeError("OPENAI_MODEL is not configured.")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model=model_name,
    input="Summarize the approved BlueVivo project risk notes."
)

print(response.output_text)
