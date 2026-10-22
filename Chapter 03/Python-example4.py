from fastapi import FastAPI, HTTPException
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/compliance-assessment")
async def compliance_assessment(request: dict):
    if "analysis_input" not in request:
        raise HTTPException(status_code=400, detail="Missing analysis input")

    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "system",
                "content": "You are a regulatory analyst operating within BlueVivo's governance framework."
            },
            {
                "role": "user",
                "content": request["analysis_input"]
            }
        ]
    )

    try:
        output_text = response.output[0].content[0].text
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected response structure")

    return {"assessment": output_text}
