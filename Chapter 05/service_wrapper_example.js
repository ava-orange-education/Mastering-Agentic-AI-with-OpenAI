import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function getEngagementStatus(projectCode, userContext) {
  // Security check before any downstream call
  if (!userContext.permissions.includes("engagement.read")) {
    throw new Error("Unauthorized");
  }

  const response = await fetch(
    `https://internal.bluevivo.local/engagements/${projectCode}/status`,
    {
      headers: {
        "Authorization": `Bearer ${process.env.BLUEVIVO_SERVICE_TOKEN}`,
        "X-User-Id": userContext.userId
      }
    }
  );

  if (!response.ok) {
    throw new Error("Status service unavailable");
  }

  return await response.json();
}
