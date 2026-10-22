import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const response = await client.responses.create({
  model: "gpt-4.1",
  input: [
    { role: "system", content: "You are a compliance analysis assistant for BlueVivo." },
    { role: "user", content: "Assess regulatory considerations for AI in healthcare in the EU." }
  ]
});

const outputText = response.output[0].content[0].text;
