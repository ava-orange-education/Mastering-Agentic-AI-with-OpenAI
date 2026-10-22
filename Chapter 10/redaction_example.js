function redactSensitiveFields(text) {
  return text
    .replace(/\b\d{3}-\d{2}-\d{4}\b/g, "[REDACTED_ID]")
    .replace(/\b\d{16}\b/g, "[REDACTED_ACCOUNT_NUMBER]")
    .replace(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi, "[REDACTED_EMAIL]");
}

const retrievedClientNote = `
Client contact: maria.santos@example.com
Account number: 1234567812345678
The client requested a summary of implementation risks.
`;

const safeContext = redactSensitiveFields(retrievedClientNote);

// safeContext can now be evaluated by downstream workflow logic
// before being included in a model request.
