import json
import os
import sys
import urllib.error
import urllib.request

api_key = os.environ.get("SENTINEL_API_KEY")
if not api_key:
    raise SystemExit("Set SENTINEL_API_KEY before running this example.")

target_url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
request = urllib.request.Request(
    "https://shield-api.3stoneai.com/api/v1/sentinel/scan",
    data=json.dumps({"url": target_url}).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(request, timeout=65) as response:
        print(json.dumps(json.load(response), indent=2))
except urllib.error.HTTPError as error:
    payload = json.load(error)
    raise SystemExit(payload.get("error", f"Request failed ({error.code})")) from error
