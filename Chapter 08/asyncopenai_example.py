import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()

model_call_limit = asyncio.Semaphore(10)

async def generate_workflow_response(workflow_id, prompt_text):
    async with model_call_limit:
        response = await client.responses.create(
            model="gpt-4.1-mini",
            input=prompt_text
        )

    return {
        "workflow_id": workflow_id,
        "output": response.output_text
    }
