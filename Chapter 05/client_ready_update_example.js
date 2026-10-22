import OpenAI from "openai";

const client = new OpenAI();

const response1 = await client.responses.create({
  model: "gpt-5.4",
  instructions:
    "You are BlueVivo's engagement operations agent. Use clear consulting language.",
  input:
    "Draft a brief client update explaining that the pilot knowledge assistant is on track, " +
    "access controls are being validated, and performance testing begins next week."
});
console.log(response1.output_text);

const response2 = await client.responses.create({
  model: "gpt-5.4",
  previous_response_id: response1.id,
  instructions:
    "You are BlueVivo's engagement operations agent. Use clear consulting language.",
  input:
    "Now extract three internal action items from that update for the delivery team."
});
console.log(response2.output_text);
