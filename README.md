# 3Stone Developer APIs

Official examples and machine-readable contracts for the production 3Stone APIs.

| API | Use it when | Start |
| --- | --- | --- |
| [3Stone API](https://www.3stoneai.com/api) | You need chat, research, file understanding, images, editable Office files, documents, music, video, or interactive tools behind one key and prepaid balance. | [Open Developer Mode](https://one.3stoneai.com/developer) |
| [Shield](https://www.3stoneai.com/shield/api) | You need machine-readable accessibility findings in CI or a delivery workflow. | [Get a key](https://shield-api.3stoneai.com/signup?edition=shield_api_starter) |
| [Sentinel](https://www.3stoneai.com/sentinel) | You need to check an AI-built app for exposed Supabase paths or browser-bundled secrets. | [Get a key](https://shield-api.3stoneai.com/signup?edition=sentinel) |
| [Ledger](https://www.3stoneai.com/ledger) | You need an agent to propose a risky action and wait for an explicit decision. | [Get a key](https://shield-api.3stoneai.com/signup?edition=ledger) |

3Stone API base URL: `https://one.3stoneai.com`

Shield, Sentinel, and Ledger base URL: `https://shield-api.3stoneai.com`

All paid endpoints use a bearer key. Keep keys in a secrets manager and never ship them to browser or mobile client code.

```bash
curl https://one.3stoneai.com/v1/chat \
  -H "Authorization: Bearer $THREESTONE_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"model":"3stone-auto","input":"Explain exactly-once billing simply.","max_output_tokens":256}'
```

See the [production documentation](https://www.3stoneai.com/developers/docs) for authentication, billing, errors, limits, jobs, and every currently available capability.

```bash
curl -X POST https://shield-api.3stoneai.com/api/v1/sentinel/scan \
  -H "Authorization: Bearer $SENTINEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'
```

## OpenAPI

The `openapi/` directory contains OpenAPI 3.1 contracts for 3Stone API and the focused infrastructure APIs. These files are suitable for documentation tools, SDK generation, contract testing, and API directories.

## Postman

Import the files in `postman/`, then set the collection API-key variable locally. Never publish a real key in a collection, screenshot, example, or support message.

- `3stone-sentinel.postman_collection.json`
- `3stone-ledger.postman_collection.json`
- `3stone-shield.postman_collection.json`

Sentinel and Shield contain read-only scan quickstarts. Ledger contains the proposed-action lifecycle and saves the returned action ID into a collection variable.

## Working examples

- `examples/3stone-api-node.mjs` and `examples/3stone-api-python.py` call the main 3Stone API and poll durable creation jobs.
- `examples/node.mjs` and `examples/python.py` cover the focused infrastructure APIs.

Both examples read credentials from environment variables. They do not contain keys.

See [TUTORIALS.md](./TUTORIALS.md) for a Next.js server route, durable artifact jobs, source-backed research, and safe backend patterns for mobile and no-code products.

## Marketplace positioning

### Sentinel API

**Tagline:** Find exposed data paths and browser-bundled secrets in AI-built apps.

**Short description:** Sentinel runs narrow, read-only checks against a deployed web app for exposed Supabase data, missing RLS signals, and secrets present in browser JavaScript. It returns evidence and prioritized actions without storing exposed row contents.

### Ledger API

**Tagline:** Put approval gates and an independent action record in front of AI agents.

**Short description:** Ledger records proposed agent actions, applies a caller-defined risk threshold, holds risky actions for an explicit decision, and records caller-reported execution outcomes. It does not execute or reverse production actions.

## Publishing order

1. Postman Public API Network
2. RapidAPI public listings
3. APIs.guru OpenAPI Directory
4. Product Hunt after outside developers complete the quickstart
5. Ledger automation integrations after the public workflow is stable

Current incremental platform spend target: $0. Do not enable sponsored placement or paid marketplace promotion without a separate budget decision.

## Support and responsible use

Email [jathan@3stoneai.com](mailto:jathan@3stoneai.com). Sentinel performs narrow, read-only checks and is not a penetration test. Shield's automated results cannot evaluate every WCAG success criterion and are not a compliance guarantee. Ledger records decisions and caller-reported outcomes; it never executes or reverses an action.
