# Cursor submission packet

Updated November 5, 2026. Metadata version 1.0.1 and package validation are complete; authenticated Cursor acceptance, publisher access and marketplace submission remain outstanding. The November 4 preparation is historical; no marketplace approval is inferred.

## Submission fields

- Publisher: Rankability (business publisher; confirm the signed-in account has authority).
- Name: Rankability
- Identifier: `rankability`
- Native Cursor package version: `1.0.1`
- Repository: https://github.com/gotchseo/rankability-integrations
- Plugin directory: repository root
- Manifest: `.cursor-plugin/plugin.json`
- Homepage: https://www.rankability.com/mcp-for-seo/
- Support: https://help.rankability.com/ and support@rankability.com
- Privacy: https://www.rankability.com/privacy/
- Terms: https://www.rankability.com/terms/
- Logo: `assets/icon.png`
- Suggested category: Data & Analytics, if offered; otherwise select the closest marketing/SEO category.
- Keywords: SEO, AI visibility, AEO, GEO, keyword research, content, Rankability.
- Short description: SEO research, AI visibility, content, and audits through your Rankability workspace.

Long description:

Connect Cursor to your Rankability workspace to review saved rankings, AI mentions and citations, content projects, and page or site audits. Research keywords and prioritize improvements using evidence for your business or clients. Built for business owners, in-house marketing teams, consultants and agencies. The plugin includes the rankability-seo skill and Rankability's hosted MCP connection. OAuth sign-in and a Rankability account with the necessary API access are required. Access is scoped to the connected organization. Research, scans, content generation, and other changes use the account's allowances and require appropriate authorization. A directory installation does not grant additional Rankability permissions.

## Package and validation

Run `python3 scripts/build-cursor-submission.py --output dist/rankability-cursor.zip`. The native Cursor ZIP includes exactly the Cursor manifest, MCP configuration, public icon, SEO skill, and README. It excludes Git metadata, credentials, private customer data, and unrelated platform review materials. A JSON validation receipt accompanies the archive.

The public repository supports both Cursor's native manifest and the portable root manifest. Both now use an explicit Streamable HTTP transport in `mcp.json`. OpenAI's builder validates the same configuration. The native package version and OpenAI package version are independently tracked; do not infer approval from either version number.

## Local acceptance before submission

Use a dedicated sample-data Rankability organization in Cursor. Record date, Cursor version, plugin version/commit, and pass/fail evidence for each case. No case below has been executed in Cursor during this preparation.

1. Install locally, confirm the rankability-seo skill and one remote MCP server appear, and complete OAuth. Verify the connected organization is the intended sample account.
2. Prompt: “Show the clients available in my connected Rankability account. Do not change anything.” Expect only authorized clients.
3. Prompt: “Summarize the sample client's saved SEO and AI visibility results. Do not start a scan.” Expect evidence references, freshness, and clear distinction between rankings, mentions, citations, and missing data.
4. Prompt: “Review the sample client's latest completed page audit and prioritize three fixes. Do not run another audit.” Expect saved findings without a new crawl.
5. Prompt: “Estimate one site audit's usage impact for the sample website, but do not start it.” Expect estimation only and no usage-bearing work.
6. Check inaccessible records and a client with no saved results: expect an access boundary or explicit missing-data result, without invented evidence.
7. Reconnect/restart Cursor and confirm OAuth works; verify disconnect/revoke stops access. Coordinate revocation with the sample account owner.

## Portal steps

The submission portal is https://cursor.com/marketplace/publish. On November 4 it required sign-in to apply as a plugin publisher. Sign in with the publisher account, confirm company identity, and check existing applications before creating another. Review any developer terms as the account owner. Submit the public repository only after the preparation change is merged and local acceptance is recorded. Cursor manually reviews marketplace plugins. Record the application ID, submission date, reviewer feedback, and eventual listing URL in the distribution tracker.

References: https://cursor.com/docs/reference/plugins and https://cursor.com/docs/plugins
