const apiKey = process.env.THREESTONE_API_KEY;
if (!apiKey) throw new Error("Set THREESTONE_API_KEY in your server environment.");

const response = await fetch("https://one.3stoneai.com/v1/chat", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Idempotency-Key": crypto.randomUUID(),
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "3stone-auto",
    input: "Explain exactly-once billing simply.",
    max_output_tokens: 256,
  }),
});

const result = await response.json();
if (!response.ok) throw new Error(result.error?.message ?? `HTTP ${response.status}`);
console.log(result.output_text);
console.log({ requestId: result.id, usage: result.usage });
