function getRateLimitPolicy(workflowType) {
  const policies = {
    client_advisory: {
      priority: "high",
      allowQueueing: true,
      maxAttempts: 3
    },
    internal_summary: {
      priority: "standard",
      allowQueueing: true,
      maxAttempts: 2
    },
    exploratory_research: {
      priority: "low",
      allowQueueing: false,
      maxAttempts: 1
    }
  };

  return policies[workflowType] || policies.exploratory_research;
}
