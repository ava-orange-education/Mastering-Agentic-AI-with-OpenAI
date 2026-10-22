from datetime import datetime
import json

def log_tool_event(user_id, workflow_id, tool_name, args, outcome, approval_state):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "workflow_id": workflow_id,
        "tool_name": tool_name,
        "arguments": args,  # sanitize before storing if needed
        "outcome": outcome,
        "approval_state": approval_state
    }
    print(json.dumps(event))
