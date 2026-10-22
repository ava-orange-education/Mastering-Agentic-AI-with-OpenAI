import logging
import time
import uuid

logging.basicConfig(level=logging.INFO, format="%(message)s")

def log_event(workflow_run_id, stage, component, status, duration_ms=None, metadata=None):
    record = {
        "workflow_run_id": workflow_run_id,
        "stage": stage,
        "component": component,
        "status": status,
        "duration_ms": duration_ms,
        "metadata": metadata or {}
    }
    logging.info(record)

workflow_run_id = f"wf_{uuid.uuid4().hex[:8]}"

start = time.time()
log_event(workflow_run_id, "intake", "advisory_api", "started")

# Placeholder for workflow logic
time.sleep(0.2)

duration_ms = int((time.time() - start) * 1000)
log_event(
    workflow_run_id,
    "intake",
    "advisory_api",
    "completed",
    duration_ms,
    {"request_type": "governance_review"}
)
