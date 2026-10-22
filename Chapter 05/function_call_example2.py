import json
from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_delivery_status",
        "description": "Return the current delivery status for a BlueVivo project.",
        "parameters": {
            "type": "object",
            "properties": {
                "project_code": {"type": "string"}
            },
            "required": ["project_code"],
            "additionalProperties": False
        },
        "strict": True
    }
]

response = client.responses.create(
    model="gpt-5.4",
    instructions=(
        "You are BlueVivo's delivery operations agent. "
        "Use tools for authoritative project data. "
        "Do not guess status values."
    ),
    input="What is the status of project BV-2042, and what should I tell the account lead?",
    tools=tools
)

for item in response.output:
    if item.type == "function_call" and item.name == "get_delivery_status":
        args = json.loads(item.arguments)

        # Simulated external service call
        service_result = {
            "project_code": args["project_code"],
            "status": "Yellow",
            "risk_summary": "Access-control validation is four days behind schedule.",
            "next_milestone": "Security review on Friday"
        }

        follow_up = client.responses.create(
            model="gpt-5.4",
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(service_result)
                }
            ]
        )
        print(follow_up.output_text)
