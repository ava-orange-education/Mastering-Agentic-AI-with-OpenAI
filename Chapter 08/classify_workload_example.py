def classify_workload(request):
    if request["workflow_type"] == "client_advisory":
        return {
            "priority": "high",
            "max_concurrent_steps": 2,
            "requires_audit_log": True
        }

    if request["workflow_type"] == "internal_summary":
        return {
            "priority": "standard",
            "max_concurrent_steps": 4,
            "requires_audit_log": True
        }

    return {
        "priority": "low",
        "max_concurrent_steps": 1,
        "requires_audit_log": False
    }
