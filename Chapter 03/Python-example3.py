response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "system", "content": "You are a BlueVivo regulatory risk analyst."},
        {"role": "user", "content": workflow_state["analysis_input"]}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "compliance_risk_assessment",
            "schema": {
                "type": "object",
                "properties": {
                    "risk_level": {
                        "type": "string",
                        "enum": ["Low", "Moderate", "High"]
                    },
                    "justification": {
                        "type": "string"
                    },
                    "recommended_action": {
                        "type": "string"
                    }
                },
                "required": ["risk_level", "justification", "recommended_action"]
            }
        }
    }
)
