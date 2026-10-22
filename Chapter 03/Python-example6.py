class ComplianceOrchestrator:
    def __init__(self, workflow_id):
        self.workflow_id = workflow_id
        self.state = repository.get_state(workflow_id)

    def execute(self):
        if self.state == "INITIATED":
            response = model_client.invoke(intake_context)
            repository.update_state(self.workflow_id, "DATA_ENRICHMENT")
