function authorizeClientAccess(user, clientId) {
  return user.allowedClientIds.includes(clientId);
}

function getAllowedTools(user) {
  const tools = ["summarize_document", "search_client_knowledge"];

  if (user.roles.includes("ProjectManager")) {
    tools.push("draft_status_update");
  }

  if (user.roles.includes("OperationsAdmin")) {
    tools.push("review_workflow_metrics");
  }

  return tools;
}

app.post("/agent/client-summary", async (req, res) => {
  const user = req.authenticatedUser;
  const { clientId, requestText } = req.body;

  if (!authorizeClientAccess(user, clientId)) {
    return res.status(403).json({ error: "Access denied." });
  }

  const allowedTools = getAllowedTools(user);

  const approvedDocuments = await documentService.getDocumentsForClient({
    clientId,
    userId: user.id
  });

  const response = await openai.responses.create({
    model: "gpt-4.1",
    input: [
      {
        role: "system",
        content: "You assist with approved BlueVivo client workflows."
      },
      {
        role: "user",
        content: requestText
      }
    ],
    tools: allowedTools.map(name => toolRegistry[name]),
    metadata: {
      user_id: user.id,
      client_id: clientId,
      workflow: "client-summary"
    }
  });

  res.json({ result: response.output_text });
});
