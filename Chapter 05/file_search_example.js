import OpenAI from "openai";

const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5.4",
  instructions:
    "You are BlueVivo's solution architecture agent. " +
    "Use file search to ground your answer in internal standards.",
  input:
    "For a regulated healthcare client, what are the most important access-control considerations " +
    "for an internal knowledge assistant?",
  tools: [
    {
      type: "file_search",
      vector_store_ids: ["vs_bluevivo_architecture_standards"]
    }
  ]
});

console.log(response.output_text);
