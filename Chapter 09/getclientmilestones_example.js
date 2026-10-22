async function getClientMilestones({ user, clientId }) {
  if (!user.allowedClientIds.includes(clientId)) {
    throw new Error("Access denied.");
  }

  const token = process.env.PROJECT_API_TOKEN;

  if (!token) {
    throw new Error("Project API token is not configured.");
  }

  const apiResponse = await fetch(
    `https://projects.internal.example/clients/${clientId}/milestones`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
        "Accept": "application/json"
      }
    }
  );

  if (!apiResponse.ok) {
    throw new Error("Unable to retrieve project milestones.");
  }

  const milestones = await apiResponse.json();

  return milestones.map(item => ({
    title: item.title,
    status: item.status,
    dueDate: item.dueDate
  }));
}
