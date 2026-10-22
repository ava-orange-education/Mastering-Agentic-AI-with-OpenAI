def execute_workflow(workflow_id):
    state = repository.get_state(workflow_id)

    if state == "INITIATED":
        result = model_client.invoke(intake_context)
        repository.update_state(workflow_id, "DATA_ENRICHMENT")

    elif state == "DATA_ENRICHMENT":
        tool_result = tool_proxy.retrieve_policy(jurisdiction)
        repository.store_tool_result(workflow_id, tool_result)
        repository.update_state(workflow_id, "ANALYSIS_IN_PROGRESS")
