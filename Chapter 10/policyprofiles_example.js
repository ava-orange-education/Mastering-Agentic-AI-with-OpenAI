const policyProfiles = {
  internal_standard: {
    allowedDataSources: ["internal_kb"],
    allowedTools: ["search_knowledge_base"],
    humanReviewRequired: false,
    retainTrace: true
  },
  client_confidential: {
    allowedDataSources: ["approved_kb", "client_repository"],
    allowedTools: ["search_knowledge_base", "retrieve_client_docs"],
    humanReviewRequired: true,
    retainTrace: true
  }
};

function selectPolicyProfile({ workflowType, dataClassification }) {
  if (workflowType === "client_summary" && dataClassification === "confidential") {
    return policyProfiles.client_confidential;
  }

  return policyProfiles.internal_standard;
}

function authorizeWorkflow(user, workflowType) {
  if (!user.roles.includes("consultant") && workflowType === "client_summary") {
    throw new Error("User is not authorized to run this workflow.");
  }
}

function validateDataSource(profile, requestedSource) {
  if (!profile.allowedDataSources.includes(requestedSource)) {
    throw new Error("Requested data source is not permitted for this policy profile.");
  }
}

const user = {
  id: "user_1842",
  roles: ["consultant"]
};

const request = {
  workflowType: "client_summary",
  dataClassification: "confidential",
  requestedSource: "client_repository"
};

authorizeWorkflow(user, request.workflowType);

const profile = selectPolicyProfile(request);

validateDataSource(profile, request.requestedSource);
