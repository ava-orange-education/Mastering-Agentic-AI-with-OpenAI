const tools = [
  {
    type: "function",
    function: {
      name: "retrieve_regulatory_policy",
      description: "Retrieve jurisdiction-specific policy data from BlueVivo knowledge systems",
      parameters: {
        type: "object",
        properties: {
          jurisdiction: { type: "string" }
        },
        required: ["jurisdiction"]
      }
    }
  }
];
