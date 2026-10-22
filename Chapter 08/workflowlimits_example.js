const workflowLimits = {
  internal_summary: {
    maxActive: 25,
    queueAllowed: true
  },
  client_advisory: {
    maxActive: 8,
    queueAllowed: true
  },
  exploratory_research: {
    maxActive: 5,
    queueAllowed: false
  }
};

function getWorkflowLimit(workflowType) {
  return workflowLimits[workflowType] || {
    maxActive: 3,
    queueAllowed: false
  };
}
