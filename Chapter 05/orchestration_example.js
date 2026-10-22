import OpenAI from "openai";
import pg from "pg";

const client = new OpenAI();
const db = new pg.Client({
  host: "localhost",
  port: 5432,
  database: "bluevivo",
  user: "app_user",
  password: "secret"
});

await db.connect();

// Step 1: fetch structured memory
const result = await db.query(
  `SELECT project_code, client_name, compliance_profile, summary
   FROM engagement_memory
   WHERE project_code = $1`,
  ["BV-2042"]
);

const engagement = result.rows[0];

// Step 2: ask the model to generate a recommendation,
// allowing it to use file search over the engagement memory store
const response = await client.responses.create({
  model: "gpt-5.4",
  instructions:
    "You are BlueVivo's delivery architecture agent. " +
    "Use the database facts as authoritative. Use retrieved documents as supporting evidence.",
  input:
    `Project code: ${engagement.project_code}
     Client: ${engagement.client_name}
     Compliance profile: ${engagement.compliance_profile}
     Summary: ${engagement.summary}

     Recommend the next three implementation priorities for this engagement.`,
  tools: [
    {
      type: "file_search",
      vector_store_ids: ["vs_1234567890"]
    }
  ]
});
console.log(response.output_text);
