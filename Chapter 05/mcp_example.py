from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4",
    instructions=(
        "You are BlueVivo's enterprise workflow agent. "
        "Use approved MCP tools when project or governance actions are required."
    ),
    input="Check whether project BV-2042 requires a governance review before rollout.",
    tools=[
        {
            "type": "mcp",
            "server_label": "bluevivo-governance",
            "server_url": "https://mcp.bluevivo.internal/governance"
        }
    ]
)
print(response.output_text)
