import json
import os
import urllib.error
import urllib.request
import uuid

api_key = os.environ.get("THREESTONE_API_KEY")
if not api_key:
    raise SystemExit("Set THREESTONE_API_KEY in your server environment.")

request = urllib.request.Request(
    "https://one.3stoneai.com/v1/chat",
    data=json.dumps({
        "model": "3stone-auto",
        "input": "Explain exactly-once billing simply.",
        "max_output_tokens": 256,
    }).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Idempotency-Key": str(uuid.uuid4()),
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(request, timeout=120) as response:
        result = json.load(response)
        print(result["output_text"])
        print({"request_id": result["id"], "usage": result["usage"]})
except urllib.error.HTTPError as error:
    body = json.load(error)
    raise SystemExit(body.get("error", {}).get("message", f"HTTP {error.code}")) from error
