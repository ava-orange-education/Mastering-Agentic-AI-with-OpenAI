import OpenAI from "openai";

const client = new OpenAI();

export async function draftPolicySummary(prompt, sourceText, effort = "medium") {
  const response = await client.responses.create({
    model: "gpt-5",
    reasoning: { effort },
    input: [
      {
        role: "system",
        content:
          "You are a BlueVivo internal policy analysis assistant. " +
          "Summarize clearly and avoid unsupported claims."
      },
      {
        role: "user",
        content: `Task: ${prompt}\n\nSource Material:\n${sourceText}`
      }
    ]
  });

  return response.output_text;
}
