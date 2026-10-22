import OpenAI from "openai";

const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5.4",
  instructions:
    "You are BlueVivo's PMO support agent. Use tools for authoritative data.",
  input:
    "Check project BV-2042 and tell me whether leadership should be notified today.",
  tools: [
    {
      type: "function",
      name: "get_delivery_status",
      description: "Return the current delivery status for a BlueVivo project.",
      strict: true,
      parameters: {
        type: "object",
        properties: {
          project_code: { type: "string" }
        },
        required: ["project_code"],
        additionalProperties: false
      }
    }
  ]
});

for (const item of response.output) {
  if (item.type === "function_call" && item.name === "get_delivery_status") {
    const args = JSON.parse(item.arguments);

    const serviceResult = {
      project_code: args.project_code,
      status: "Yellow",
      risk_summary: "Validation delay remains within current contingency range.",
      leadership_notification_recommended: false
    };

    const followUp = await client.responses.create({
      model: "gpt-5.4",
      previous_response_id: response.id,
      input: [
        {
          type: "function_call_output",
          call_id: item.call_id,
          output: JSON.stringify(serviceResult)
        }
      ]
    });

    console.log(followUp.output_text);
  }
}
