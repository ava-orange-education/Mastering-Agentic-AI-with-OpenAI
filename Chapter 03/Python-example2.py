conversation = [
    {"role": "system", "content": "You are a regulatory analysis agent operating within BlueVivo's governance framework."},
    {"role": "user", "content": workflow_state["initial_request"]},
    {"role": "assistant", "content": workflow_state["prior_analysis_summary"]},
    {"role": "tool", "content": workflow_state["policy_retrieval_result"]}
]

response = client.responses.create(
    model="gpt-4.1",
    input=conversation
)
