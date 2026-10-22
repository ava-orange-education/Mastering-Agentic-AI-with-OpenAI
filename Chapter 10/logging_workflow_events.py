from datetime import datetime, timezone
import uuid

def create_audit_event(
    workflow_id,
    event_type,
    user_id,
    policy_profile,
    details=None
):
    return {
        "event_id": str(uuid.uuid4()),
        "workflow_id": workflow_id,
        "event_type": event_type,
        "user_id": user_id,
        "policy_profile": policy_profile,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "details": details or {}
    }

workflow_id = str(uuid.uuid4())

audit_events = []

audit_events.append(create_audit_event(
    workflow_id=workflow_id,
    event_type="workflow_started",
    user_id="user_1842",
    policy_profile="client_confidential_review",
    details={
        "workflow_name": "client_risk_summary",
        "risk_level": "moderate",
        "human_review_required": True
    }
))

audit_events.append(create_audit_event(
    workflow_id=workflow_id,
    event_type="retrieval_completed",
    user_id="user_1842",
    policy_profile="client_confidential_review",
    details={
        "source_count": 4,
        "source_types": ["approved_knowledge_base", "client_repository"],
        "restricted_sources_excluded": True
    }
))

audit_events.append(create_audit_event(
    workflow_id=workflow_id,
    event_type="human_review_required",
    user_id="user_1842",
    policy_profile="client_confidential_review",
    details={
        "reason": "client_facing_output",
        "required_reviewer_role": "engagement_manager"
    }
))
