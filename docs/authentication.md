# Authentication

## MCP

Use `https://app.rankability.com/mcp` with Streamable HTTP. OAuth discovery is available at:

- `https://app.rankability.com/.well-known/oauth-protected-resource/mcp`
- `https://app.rankability.com/.well-known/oauth-authorization-server`

The hosted service supports authorization code + PKCE S256, dynamic client registration, and refresh tokens. Let the MCP host complete the OAuth flow. Review the active organization and requested scopes before consenting. A connection stays bound to the organization that authorized it.

## Agent API

Create a scoped API key in Rankability Settings → API keys. Store it in your host's secrets or credentials system and send `Authorization: Bearer <your key>`. The starter collection uses an empty `apiKey` variable; supply it locally and do not sync or export its value.

For a Codex API-key fallback, set `RANKABILITY_API_KEY` in the environment that launches Codex and use:

```toml
[mcp_servers.rankability]
url = "https://app.rankability.com/mcp"
bearer_token_env_var = "RANKABILITY_API_KEY"
```

Grant only required scopes. The starter API reads require `clients:read`, `reporter:read`, `copywriter:read`, and `page_audit:read` as appropriate; `/usage` accepts a supported Agent API scope. A 401 needs authentication, while a 403 can indicate missing scope or account access. Revoke keys and connections through Rankability when no longer needed.
