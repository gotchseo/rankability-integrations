# OpenAI submission preparation

Updated October 1, 2026 against the [submission guide](https://developers.openai.com/plugins/deploy/submission) and [plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines).

Run `python3 scripts/build-openai-submission.py`. The ZIP contains only the portable manifest, one remote MCP connection, the public icon and the SEO skill. It excludes Git metadata, private source, local configuration, reviewer credentials and test receipts. The root manifest is authoritative for OpenAI; keep its shared listing fields synchronized with the local Codex manifest. The builder checks that alignment.

The five positive and three negative cases are expected behaviors, not passed tests. Do not submit until each case has been executed in ChatGPT against a dedicated non-admin reviewer organization with sample data and the real walkthrough has been recorded. The dedicated reviewer organization is **Claude Review**. Its sample client is named **Rankability**, with a completed Tracker report, a completed Page Auditor report and saved content projects. These records have been inspected in the Rankability application; that inspection does not replace authenticated ChatGPT tool tests. Keep the account usable for later reviews. Enter its credentials and sign-in instructions only in the secure portal review details, never in this repository or ZIP.

Use normal OAuth consent with the least permissions required by the test workflows. The `kb:read` discovery-only grant lists tools and public help; it cannot read sample workspaces. Confirm actual read and estimation scopes from the current Agent API. Do not grant admin access or connect customer/internal workspaces to make a test pass.

Before uploading, verify that the deployed `consult_serena` schema accepts only a client ID and focused question, with no prior-turn array. The private application fix must be released through Rankability's existing Replit path before a portal scan can see it. Re-enumerate deployed tools instead of copying historical counts. Annotation justifications are no longer required; explicit boolean annotations remain required.

Resume the existing Rankability portal draft. Add the real accessible video URL as `extensions.com.openai.review.demo_recording_url` and rebuild when available. Do not insert placeholder URLs or record synthetic screenshots as live acceptance. Preserve the existing selected developer identity and country availability unless the owner changes them. Review the current domain challenge rather than replacing another plugin's token.

Record tool arguments, returned sample record references, results and confirmation behavior for all cases. Check desktop and mobile ChatGPT. Review listing privacy, third-party data handling and consequential actions against the current guidelines. Only attest to verified behavior. Submission starts review; publish separately after approval and the product launch workflow.

Launch coordination: https://github.com/gotchseo/rankability-app/issues/1558.
