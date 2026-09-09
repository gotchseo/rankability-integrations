# API examples and automation recipes

Use a scoped API key from Rankability Settings → API keys. Store it in your workflow tool's credential store. These are read-only starter recipes; importing a recipe does not make it a native or verified platform integration.

## Read saved Tracker evidence

```sh
curl --fail-with-body 'https://app.rankability.com/api/agent/v1/reporter/summary' \
  -H "Authorization: Bearer ${RANKABILITY_API_KEY}" \
  -H 'Accept: application/json'
```

Required scope: `reporter:read`. The response is saved workspace evidence, not a fresh scan. Keep source dates, missing values, and platform distinctions in downstream reporting.

## Read the usage contract

```sh
curl --fail-with-body 'https://app.rankability.com/api/agent/v1/usage' \
  -H "Authorization: Bearer ${RANKABILITY_API_KEY}"
```

Read usage before any future on-demand workflow. It may represent pooled usage or outcome allowances. Use the current contract's estimate/preflight route for paid operations, and do not invent action prices.

## n8n

Import `workflows/n8n/read-tracker-summary.json`, configure HTTP Header Auth (`Authorization`, `Bearer <key>`), and run manually. No destination receives the response until you add one. Do not activate a recurring schedule until you have reviewed the data and the desired frequency.

## Make

Create an HTTP request module with method GET, URL `https://app.rankability.com/api/agent/v1/reporter/summary`, and the Authorization header stored in Make's protected credential configuration. Parse the JSON response. Run once and inspect its structure before mapping selected fields to the destination the user authorized. The HTTP recipe is not a native Make app or an approved public template.

## Zapier

Use an authenticated HTTP/API request step with GET to `https://app.rankability.com/api/agent/v1/reporter/summary`. Supply the bearer credential through the product's supported protected auth configuration. Confirm the response before mapping fields. The HTTP recipe is not a native Zapier integration or an approved Zap template.

## Errors and durable actions

Inspect `X-Request-Id` for support without exposing credentials or response contents. Stop and correct 400/401/403 errors. For 429/503, honor `Retry-After` and any `retry_at` with a bounded retry policy. If adding an action later, use a stable idempotency key for that logical request, persist the returned job ID, and poll the documented status route. Never retry a paid create request with a new key merely because the first response was lost.
