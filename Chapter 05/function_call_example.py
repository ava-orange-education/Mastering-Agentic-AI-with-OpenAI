import json
from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_project_status",
        "description": "Retrieve the current status for a BlueVivo project.",
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
    instructions="You are BlueVivo's PMO support agent.",
    input="What is the current status of project BV-2042, and what should I tell leadership?",
    tools=tools
)

# Inspect response.output for function calls
for item in response.output:
    if item.type == "function_call" and item.name == "get_project_status":
        args = json.loads(item.arguments)

        # Simulated internal service call
        project_status = {
            "project_code": args["project_code"],
            "status": "Yellow",
            "summary": "Access-control validation is behind schedule by four days.",
            "next_milestone": "Security review on Friday"
        }

        follow_up = client.responses.create(
            model="gpt-5.4",
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(project_status)
                }
            ]
        )

        print(follow_up.output_text)	
