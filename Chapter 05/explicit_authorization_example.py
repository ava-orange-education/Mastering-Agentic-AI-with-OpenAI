def authorize_tool_call(tool_name: str, user_role: str) -> str:
    read_tools = {"get_engagement_status", "get_client_constraints"}
    mutation_tools = {"create_governance_exception", "update_project_note"}

    if tool_name in read_tools and user_role in {"consultant", "manager", "admin"}:
        return "allow"

    if tool_name in mutation_tools and user_role in {"manager", "admin"}:
        return "require_approval"

    return "deny"
