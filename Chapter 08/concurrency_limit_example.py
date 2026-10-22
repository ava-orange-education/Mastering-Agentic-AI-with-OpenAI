import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()

openai_semaphore = asyncio.Semaphore(5)

async def run_model_step(prompt_text):
    async with openai_semaphore:
        response = await client.responses.create(
            model="gpt-4.1-mini",
            input=prompt_text
        )
        return response.output_text
