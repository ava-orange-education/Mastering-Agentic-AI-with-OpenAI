import os
from openai import OpenAI

MODEL_NAME = os.getenv("OPENAI_MODEL")

if not MODEL_NAME:
    raise RuntimeError("OPENAI_MODEL is not configured.")

client = OpenAI()

TOOL_REGISTRY = {
    "search_client_documents": {
        "name": "search_client_documents",
        "description": "Search approved client documents for the active workflow.",
        "parameters": {
            "type": "object",
            "properties": {
                "client_id": {"type": "string"},
                "query": {"type": "string"}
            },
            "required": ["client_id", "query"]
        }
    },
    "draft_status_update": {
        "name": "draft_status_update",
        "description": "Draft a project status update for review.",
        "parameters": {
            "type": "object",
            "properties": {
                "client_id": {"type": "string"},
                "summary": {"type": "string"}
            },
            "required": ["client_id", "summary"]
        }
    }
}

def allowed_tools_for(user, workflow_name):
    tools = []

    if workflow_name == "client_summary":
        tools.append(TOOL_REGISTRY["search_client_documents"])

    if workflow_name == "project_status" and "ProjectManager" in user["roles"]:
        tools.append(TOOL_REGISTRY["search_client_documents"])
        tools.append(TOOL_REGISTRY["draft_status_update"])

    return tools

def run_agent_workflow(user, workflow_name, user_request):
    tools = allowed_tools_for(user, workflow_name)

    return client.responses.create(
        model=MODEL_NAME,
        input=user_request,
        tools=tools,
        metadata={
            "user_id": user["id"],
            "workflow": workflow_name
        }
    )
