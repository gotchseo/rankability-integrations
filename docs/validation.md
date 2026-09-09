# Validation boundaries

Prepared 2026-09-08 against the Rankability Agent API documentation at source revision `936012fee` and live public OAuth discovery metadata.

Checks include manifest and JSON validation, known endpoint paths against the current API source, empty credentials and customer fixtures, and an unauthenticated MCP discovery check. The private application and its deployment were not changed.

Authenticated end-to-end testing in Claude, Cursor, Gemini, n8n, and Postman requires a user-authorized test workspace and account in each host. Do not describe these packages as platform approved or fully end-to-end tested based on structural validation. Directory submissions and approvals are tracked separately from this public package.

Validated with Claude Code 2.1.266 using its plugin and marketplace validators. The Postman collection and OpenAPI starter also passed their official JSON schemas. Registry publication was confirmed active on September 9, 2026; this does not establish approval by an AI platform directory.
