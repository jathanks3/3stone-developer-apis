const baseUrl = "https://shield-api.3stoneai.com";
const apiKey = process.env.SENTINEL_API_KEY;

if (!apiKey) throw new Error("Set SENTINEL_API_KEY before running this example.");

const response = await fetch(`${baseUrl}/api/v1/sentinel/scan`, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ url: process.argv[2] ?? "https://example.com" }),
});

const result = await response.json();
if (!response.ok) throw new Error(result.error ?? `Request failed (${response.status})`);

console.log(JSON.stringify(result, null, 2));
