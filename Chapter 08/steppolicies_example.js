const stepPolicies = {
  retrieveClientContext: {
    required: true,
    retryable: true,
    maxAttempts: 3
  },
  enrichWithMarketNotes: {
    required: false,
    retryable: true,
    maxAttempts: 2
  },
  validateGovernanceRules: {
    required: true,
    retryable: false,
    escalateOnFailure: true
  }
};

function shouldContinue(stepName, failed) {
  const policy = stepPolicies[stepName];

  if (!failed) {
    return true;
  }

  return policy && policy.required === false;
}
