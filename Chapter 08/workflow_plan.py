workflow_plan = [
    {
        "stage": "collect_context",
        "steps": [
            "retrieve_client_history",
            "retrieve_internal_guidance",
            "retrieve_project_notes"
        ],
        "execution": "parallel"
    },
    {
        "stage": "generate_response",
        "steps": [
            "create_advisory_draft"
        ],
        "execution": "sequential"
    },
    {
        "stage": "validate_response",
        "steps": [
            "check_governance_rules",
            "prepare_audit_record"
        ],
        "execution": "sequential"
    }
]
