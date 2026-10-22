from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "system", "content": "You are a compliance analysis assistant for BlueVivo."},
        {"role": "user", "content": "Assess regulatory considerations for AI in healthcare in the EU."}
    ]
)

output_text = response.output[0].content[0].text
