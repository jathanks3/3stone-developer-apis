# 3Stone API distribution kit

Public, secret-free assets for listing the 3Stone APIs on developer platforms.

## Postman

Import both files in `postman/`, then set the collection API-key variable locally. Never publish a real key in a collection, screenshot, example, or support message.

- `3stone-sentinel.postman_collection.json`
- `3stone-ledger.postman_collection.json`

The Sentinel collection contains a read-only deployed-site scan. The Ledger collection contains the full proposed-action lifecycle and saves the returned action ID into a collection variable.

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
3. Product Hunt launch page after three outside developers complete the quickstart
4. Zapier integration for Ledger after the public API workflow is stable

Current incremental platform spend target: $0. Do not enable sponsored placement or paid marketplace promotion without a separate budget decision.
