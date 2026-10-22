import time
import logging
from openai import OpenAI

client = OpenAI()
logger = logging.getLogger("bluevivo.agentops")

def run_workflow(workflow_name, user_input, reasoning_effort):
    start = time.time()

    response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": reasoning_effort},
        input=user_input
    )

    elapsed = round(time.time() - start, 3)

    logger.info(
        "workflow_execution",
        extra={
            "workflow_name": workflow_name,
            "reasoning_effort": reasoning_effort,
            "duration_seconds": elapsed,
            "output_length": len(response.output_text or "")
        }
    )

    return response
