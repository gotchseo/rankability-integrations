#!/usr/bin/env python3
"""Build an allowlisted public plugin ZIP; never bundle a checkout or credentials."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZIP_DEFLATED, ZipFile


def https(value):
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("dist/rankability-openai.zip"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "plugin.json").read_text())
    codex = json.loads((root / ".codex-plugin/plugin.json").read_text())
    openai = manifest["extensions"]["com.openai"]
    interface = openai["interface"]
    assert manifest["name"] == codex["name"] == "rankability"
    assert manifest["version"] == codex["version"]
    for field, value in codex["interface"].items():
        assert interface[field] == value, f"Portable/Codex metadata diverged: {field}"
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        assert https(interface[field]), f"Invalid listing URL: {field}"
    for field, maximum in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000)):
        assert 0 < len(interface[field]) <= maximum, field
    prompts = interface["defaultPrompt"]
    assert 1 <= len(prompts) <= 3 and len(set(prompts)) == len(prompts)
    assert all(0 < len(prompt) <= 128 for prompt in prompts)
    cases = openai["review"]["test_cases"]
    assert len(cases["positive"]) == 5 and len(cases["negative"]) == 3
    for kind, entries in cases.items():
        for case in entries:
            required = ["description", "prompt", "expected_behavior"]
            if kind == "positive":
                required.append("tools_triggered")
            assert all(case.get(field, "").strip() for field in required)
    assert not {"test_credentials", "reviewer_instructions"} & openai["review"].keys()
    if openai["review"].get("demo_recording_url"):
        assert https(openai["review"]["demo_recording_url"])
    mcp = json.loads((root / "mcp.json").read_text())
    assert list(mcp["mcpServers"]) == ["rankability"]
    server = mcp["mcpServers"]["rankability"]
    assert server == {"url": "https://app.rankability.com/mcp"}, "Unexpected MCP config; review before packaging"
    # Use the documented portable transport declaration only in the submission;
    # retain existing Cursor configuration in the repository.
    mcp = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
        "mcpServers": {"rankability": {"type": "streamable-http", **server}},
    }
    files = ["assets/icon.png", "skills/rankability-seo/SKILL.md"]
    assert interface["logo"] == interface["composerIcon"] == "./assets/icon.png"
    for name in files:
        path = root / name
        assert path.is_file() and not path.is_symlink(), name
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.writestr("plugin.json", json.dumps(manifest, indent=2) + "\n")
        archive.writestr("mcp.json", json.dumps(mcp, indent=2) + "\n")
        for name in files:
            archive.write(root / name, name)
    with ZipFile(output) as archive:
        assert archive.testzip() is None
        assert sorted(archive.namelist()) == sorted(["plugin.json", "mcp.json", *files])
    print(f"Package built: {output}")
    print("Structural checks passed. This does not certify authenticated tests, recording, review or publication.")
    if not openai["review"].get("demo_recording_url"):
        print("Not ready for final review: add the actual accessible walkthrough recording after execution.")


if __name__ == "__main__":
    main()
