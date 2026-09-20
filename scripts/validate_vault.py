#!/usr/bin/env python3
"""Basic structural validator for the Binge Obsidian vault."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

required = [
    "Directory/Directory.md",
    "01 - TV Shows/TV Shows.md",
    "02 - Movies/Movies.md",
    "03 - Documentaries/Documentaries.md",
    "04 - Franchises/Franchises.md",
    "05 - Shorts/Shorts.md",
    "06 - Collections/Collections.md",
    "07 - Data/Build Manifest.json",
    "08 - Dev Log/Dev Log.md",
    "09 - Sources/Sources.md",
    "10 - Templates/Templates.md",
]

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

manifest_path = ROOT / "07 - Data/Build Manifest.json"
if manifest_path.is_file():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            errors.append("Build Manifest.json must contain an object")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid Build Manifest.json: {exc}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.name.endswith(" ") or path.name.startswith(" "):
        errors.append(f"Malformed filename whitespace: {path.relative_to(ROOT)}")
    if "  " in path.name:
        warnings.append(f"Double space in filename: {path.relative_to(ROOT)}")

# Every episode note must live inside an episode directory with the same stem.
episode_pattern = re.compile(r"^S\\d{2}E\\d{2} - .+\\.md$")
for note in ROOT.rglob("*.md"):
    if episode_pattern.match(note.name):
        if note.parent.name != note.stem:
            errors.append(f"Episode note/folder mismatch: {note.relative_to(ROOT)}")

print(f"Binge validation: {len(errors)} error(s), {len(warnings)} warning(s)")
for item in errors:
    print(f"ERROR: {item}")
for item in warnings:
    print(f"WARNING: {item}")

sys.exit(1 if errors else 0)
