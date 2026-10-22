import OpenAI from "openai";

const client = new OpenAI();

const stream = await client.responses.create({
  model: "gpt-5.4",
  input: [
    {
      role: "user",
      content:
        "Summarize the current BlueVivo pilot status for the weekly operations call."
    }
  ],
  stream: true
});

for await (const event of stream) {
  console.log(event);
}
