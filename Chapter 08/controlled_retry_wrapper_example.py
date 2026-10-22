import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def call_model_with_retries(prompt_text, max_attempts=3):
    delay_seconds = 1

    for attempt in range(1, max_attempts + 1):
        try:
            response = await client.responses.create(
                model="gpt-4.1-mini",
                input=prompt_text
            )
            return response.output_text

        except TimeoutError:
            if attempt == max_attempts:
                raise

            await asyncio.sleep(delay_seconds)
            delay_seconds *= 2
