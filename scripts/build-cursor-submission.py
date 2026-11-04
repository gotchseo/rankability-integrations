#!/usr/bin/env python3
"""Validate and package the native Cursor plugin with an explicit file allowlist."""
import argparse
import hashlib
import json
import re
import struct
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('dist/rankability-cursor.zip'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / '.cursor-plugin/plugin.json').read_text())
    require(re.fullmatch(r'[a-z0-9]+(?:[-.][a-z0-9]+)*', manifest['name']), 'Invalid name')
    require(re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']), 'Invalid version')
    require(manifest['author']['name'] == 'Rankability', 'Unexpected publisher')
    require(bool(manifest['description'].strip()), 'Missing description')
    require(manifest['skills'] == './skills/', 'Review changed skill paths')
    require(manifest['mcpServers'] == './mcp.json', 'Review changed MCP path')
    require(manifest['logo'] == 'assets/icon.png', 'Review changed logo')
    config = json.loads((root / 'mcp.json').read_text())
    require(config['mcpServers'] == {'rankability': {'type': 'streamable-http', 'url': 'https://app.rankability.com/mcp'}}, 'Unexpected endpoint, executable, or credentials')
    files = ['.cursor-plugin/plugin.json', 'mcp.json', 'assets/icon.png', 'skills/rankability-seo/SKILL.md', 'README.md']
    for name in files:
        path = root / name
        require(path.is_file() and not path.is_symlink(), 'Missing or linked asset: ' + name)
        require(root in path.resolve().parents, 'Path escapes package')
    skill = (root / files[3]).read_text()
    require(skill.startswith('---\n'), 'Missing skill frontmatter')
    frontmatter = skill.split('---', 2)[1]
    require(re.search(r'^name: rankability-seo$', frontmatter, re.M), 'Invalid skill name')
    require(re.search(r'^description: \S.+$', frontmatter, re.M), 'Missing skill description')
    png = (root / 'assets/icon.png').read_bytes()
    require(png[:8] == b'\x89PNG\r\n\x1a\n', 'Invalid PNG signature')
    width, height = struct.unpack('>II', png[16:24])
    require(width == height and width >= 48, 'Logo must be square and at least 48px')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, 'w', ZIP_DEFLATED) as archive:
        for name in files:
            archive.write(root / name, name)
    with ZipFile(args.output) as archive:
        require(archive.testzip() is None and sorted(archive.namelist()) == sorted(files), 'ZIP verification failed')
    receipt = {'plugin': manifest['name'], 'version': manifest['version'], 'format': 'native Cursor', 'structural_validation': 'passed', 'authenticated_cursor_test': 'not_run', 'marketplace_submission': 'not_submitted', 'logo_dimensions': [width, height], 'files': files, 'sha256': hashlib.sha256(args.output.read_bytes()).hexdigest()}
    args.output.with_suffix('.validation.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
