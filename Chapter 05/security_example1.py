# Avoid broad tools like this
tools = [
    {
        "type": "function",
        "name": "run_sql",
        "description": "Run a SQL query against the BlueVivo production database.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    }
]

