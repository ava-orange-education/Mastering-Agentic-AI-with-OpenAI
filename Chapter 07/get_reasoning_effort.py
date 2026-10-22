WORKFLOW_PROFILES = {
    "interactive_lookup": "medium",
    "batch_tagging": "low",
    "policy_review": "high"
}

def get_reasoning_effort(workflow_name):
    return WORKFLOW_PROFILES.get(workflow_name, "medium")
