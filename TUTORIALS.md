# 3Stone API integration patterns

All examples run on the server. Never expose `THREESTONE_API_KEY` in browser or mobile code.

## Next.js route handler

```ts
export async function POST(request: Request) {
  const { prompt } = await request.json();
  const response = await fetch("https://one.3stoneai.com/v1/chat", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.THREESTONE_API_KEY}`,
      "Idempotency-Key": crypto.randomUUID(),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ model: "3stone-auto", input: prompt }),
  });
  return new Response(response.body, { status: response.status, headers: { "Content-Type": "application/json" } });
}
```

This pattern also fits Vercel Functions. Set the key as a server-side environment variable.

## Durable creation job

```js
const headers = {
  Authorization: `Bearer ${process.env.THREESTONE_API_KEY}`,
  "Content-Type": "application/json",
};

const submitted = await fetch("https://one.3stoneai.com/v1/presentations", {
  method: "POST",
  headers: { ...headers, "Idempotency-Key": crypto.randomUUID() },
  body: JSON.stringify({ prompt: "Create a concise editable project update deck." }),
}).then((response) => response.json());

let job;
do {
  await new Promise((resolve) => setTimeout(resolve, 1500));
  job = await fetch(`https://one.3stoneai.com/v1/jobs/${submitted.job_id}`, { headers }).then((response) => response.json());
} while (["queued", "provider_starting", "running"].includes(job.status));

if (job.status !== "completed") throw new Error(`Job stopped: ${job.error?.code}`);

const artifact = await fetch(`https://one.3stoneai.com/v1/jobs/${submitted.job_id}/artifact`, { headers });
```

Use `/v1/spreadsheets`, `/v1/images`, or `/v1/video` with the same job pattern. Do not retry a `reconciliation_required` job blindly.

## Research with sources

```python
import json, os, urllib.request, uuid

request = urllib.request.Request(
    "https://one.3stoneai.com/v1/research",
    data=json.dumps({"query": "Research current battery recycling policy and cite primary sources."}).encode(),
    headers={
        "Authorization": f"Bearer {os.environ['THREESTONE_API_KEY']}",
        "Idempotency-Key": str(uuid.uuid4()),
        "Content-Type": "application/json",
    },
    method="POST",
)
with urllib.request.urlopen(request, timeout=120) as response:
    result = json.load(response)
    print(result["output_text"])
    for source in result.get("sources", []):
        print(source["url"])
```

## Lovable, no-code, and mobile products

Put the 3Stone call behind your own authenticated backend or server function. The client sends the user prompt to your backend; the backend authorizes the user, adds the secret key and idempotency key, submits the 3Stone request, and returns only the safe result/job state. Persist the 3Stone request and job IDs so reconnecting clients can resume without duplicate work.
