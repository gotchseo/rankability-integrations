# Rankability integrations

Connect your assistant or workflow to [Rankability](https://www.rankability.com/). Analyze SEO and AI visibility evidence for your business or clients, research keywords, work with content, and review audits through the hosted MCP server and Agent API.

- **MCP:** `https://app.rankability.com/mcp` (Streamable HTTP)
- **Agent API:** `https://app.rankability.com/api/agent/v1`
- **Setup:** [MCP guide](https://www.rankability.com/mcp-for-seo/) · [API guide](https://www.rankability.com/seo-api/) · [Help Center](https://help.rankability.com/)

A Rankability account with API access is required. OAuth is preferred. Permissions and data access belong to the organization authorized at connection time. This repository contains public configuration, guidance, and read-only API starter examples; the hosted service is operated by Rankability.

## Connect your assistant

### ChatGPT

Open the [Rankability plugin listing](https://chatgpt.com/plugins/plugin_asdk_app_6abcf76b7e6c8191852154b3b19d11c4), install it, and complete Rankability OAuth. Version 1.0.5 was verified publicly listed on November 4, 2026. Availability and permissions depend on your account and workspace.

### Claude

Open **Customize → Connectors → Discover** and search for **Rankability**. On November 4, 2026, the signed-in directory showed the Rankability community **plugin from Anthropic Directory**, version 0.2.1 with seven skills and one connector. An existing custom Rankability connector is a separate entry. Follow the plugin's setup flow and review the organization and scopes on the OAuth consent screen. If the plugin is unavailable to your account, use the custom remote MCP connection below. This observation does not establish a separate standalone connector listing or universal account availability.

Current directory readback, November 5, 2026: the same Anthropic Directory plugin now shows version 0.2.2 and the broader description for business owners, marketing teams, consultants and agencies. Seven skills and one connector remain. The November 4 observation above is historical.

### Other remote MCP clients

Add a custom remote connector with `https://app.rankability.com/mcp`, then complete Rankability OAuth.

### Claude Code plugin

```text
/plugin marketplace add gotchseo/rankability-integrations
/plugin install rankability@rankability
```

Use `/mcp` to authenticate the connection. The included `rankability-seo` skill guides evidence-backed workflows. This is Rankability's own marketplace; a public repository does not imply inclusion in a curated Claude directory.

### Gemini CLI extension

```sh
gemini extensions install https://github.com/gotchseo/rankability-integrations
```

Restart Gemini CLI, then use `/mcp auth rankability`. The extension uses the existing hosted server and includes no local executable server or automatic hooks.

### Cursor

Add the following to your MCP configuration and complete OAuth when prompted:

```json
{"mcpServers":{"rankability":{"url":"https://app.rankability.com/mcp"}}}
```

This repository also includes `.cursor-plugin/plugin.json` and `mcp.json` for plugin distribution.

See [Cursor submission preparation](docs/cursor-submission.md) for listing fields, the package builder, and the remaining authenticated acceptance checks. The native package is prepared; marketplace submission and approval have not been verified.

### Codex

The package includes `.codex-plugin/plugin.json` for plugin distribution. You can also connect the hosted server directly:

```sh
codex mcp add rankability --url https://app.rankability.com/mcp
codex mcp login rankability
```

If your client requires an API key, use a scoped key stored in its supported secret configuration. Never commit the key. See [authentication](docs/authentication.md).

## API and workflow starters

- [Postman collection](postman/rankability-read-only.postman_collection.json): usage, clients, Tracker summary, saved content, and saved audit reads.
- [Read-only OpenAPI starter](openapi.json): a deliberately bounded subset of the Agent API; see the current API guide for the full contract.
- [n8n saved Tracker summary](workflows/n8n/read-tracker-summary.json): import, select an HTTP Header Auth credential, and run manually.
- [API examples and automation recipes](docs/api-examples.md): HTTP examples for n8n, Make, and Zapier.

No credentials, sample customer responses, publishing actions, or paid scan requests are included. Read-only examples do not prove authentication or end-to-end behavior in every host; see [validation](docs/validation.md).

## OpenAI directory submission

The root `plugin.json` carries current OpenAI listing metadata and prepared review cases. The `.codex-plugin/plugin.json` remains available for local Codex installation. Build the public submission ZIP with `python3 scripts/build-openai-submission.py`. See [submission preparation](docs/openai-submission.md) for the remaining authenticated checks. A ZIP build or upload is not approval or publication.

Publication update, November 4, 2026: the publisher dashboard and public listing both confirm version 1.0.5 is published. Historical preparation notes are not the current publication status. Fresh-install and platform-specific acceptance tests remain separate evidence.

## Official MCP Registry

`io.github.gotchseo/rankability` version 1.0.1 was published and verified active/latest on November 4, 2026. [Registry record](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.gotchseo/rankability). Registry metadata does not imply approval in other directories.

## Support and policies

[Help Center](https://help.rankability.com/) · [Privacy](https://www.rankability.com/privacy/) · [Terms](https://www.rankability.com/terms/) · support@rankability.com

Report integration configuration bugs in this repository without posting credentials or private customer data. Rankability service use is governed by its terms. Repository material is copyright Rankability, Inc.; trademarks remain their owners' property.
