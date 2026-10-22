tools = [
    {
        "type": "function",
        "name": "get_engagement_status",
        "description": "Return the current status summary for a BlueVivo engagement.",
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