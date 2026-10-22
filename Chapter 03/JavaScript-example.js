import express from "express";
import OpenAI from "openai";

const app = express();
app.use(express.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.post("/compliance-assessment", async (req, res) => {
  if (!req.body.analysis_input) {
    return res.status(400).json({ error: "Missing analysis input" });
  }

  try {
    const response = await client.responses.create({
      model: "gpt-4.1",
      input: [
        {
          role: "system",
          content: "You are a regulatory analyst operating within BlueVivo's governance framework."
        },
        {
          role: "user",
          content: req.body.analysis_input
        }
      ]
    });

    const outputText = response.output[0].content[0].text;
    res.json({ assessment: outputText });

  } catch (error) {
    res.status(500).json({ error: "Model invocation failed" });
  }
});

app.listen(3000, () => {
  console.log("Service running on port 3000");
});
