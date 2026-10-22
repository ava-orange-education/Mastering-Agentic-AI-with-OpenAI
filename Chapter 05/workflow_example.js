async function handleToolDecision(toolName, args, userContext) {
  const decision = authorizeToolCall(toolName, userContext.role);

  if (decision === "deny") {
    return { status: "blocked", reason: "Not authorized" };
  }

  if (decision === "require_approval") {
    return {
      status: "pending_approval",
      toolName,
      args,
      approverGroup: "bluevivo-governance-managers"
    };
  }

  return await executeApprovedTool(toolName, args, userContext);
}
