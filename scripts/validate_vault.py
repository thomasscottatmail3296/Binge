#!/usr/bin/env python3
"""Structural validator for the Binge Obsidian vault."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

REQUIRED = [
    "Directory/Directory.md",
    "01 - TV Shows/TV Shows.md",
    "02 - Movies/Movies.md",
    "03 - Documentaries/Documentaries.md",
    "04 - Franchises/Franchises.md",
    "05 - Shorts/Shorts.md",
    "06 - Collections/Collections.md",
    "07 - Data/Build Manifest.json",
    "07 - Data/inventory.json",
    "08 - Dev Log/Dev Log.md",
    "09 - Sources/Sources.md",
    "10 - Templates/Templates.md",
]

EPISODE_RE = re.compile(r"^S\d{2}E\d{2} - .+\.md$")
SEASON_RE = re.compile(r"^Season \d{2}$")

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"Missing JSON file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")
    return None

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

manifest = load_json(ROOT / "07 - Data/Build Manifest.json")
inventory = load_json(ROOT / "07 - Data/inventory.json")

if isinstance(manifest, dict):
    for key in ("project", "version", "latest_batch", "file_count", "markdown_count", "media_count", "episode_count", "validation"):
        if key not in manifest:
            errors.append(f"Build Manifest.json missing key: {key}")

if isinstance(inventory, dict):
    for key in ("project", "status", "media", "cover_groups", "notes"):
        if key not in inventory:
            errors.append(f"inventory.json missing key: {key}")
    if inventory.get("project") != "Binge":
        errors.append("inventory.json project must be Binge")
    if not isinstance(inventory.get("media", []), list):
        errors.append("inventory.json media must be an array")
    if not isinstance(inventory.get("cover_groups", []), list):
        errors.append("inventory.json cover_groups must be an array")

all_files = []
for path in ROOT.rglob("*"):
    if ".git" in path.parts:
        continue
    if path.is_file():
        all_files.append(path)
        rel = path.relative_to(ROOT)
        if path.name.startswith(" ") or path.name.endswith(" "):
            errors.append(f"Malformed filename whitespace: {rel}")
        if "  " in path.name:
            warnings.append(f"Double space in filename: {rel}")

markdown_files = [p for p in all_files if p.suffix.lower() == ".md"]

# Episode notes must be directly inside their matching episode folder.
episode_notes = []
for note in markdown_files:
    if EPISODE_RE.match(note.name):
        episode_notes.append(note)
        if note.parent.name != note.stem:
            errors.append(f"Episode note/folder mismatch: {note.relative_to(ROOT)}")
        if not SEASON_RE.match(note.parent.parent.name) and note.parent.parent.name != "Specials":
            warnings.append(f"Episode is not under a conventional season/specials folder: {note.relative_to(ROOT)}")

# Media count is derived from actual canonical media notes, excluding episode notes.
canonical_media = []
for note in markdown_files:
    if note.name in {"README.md", "VAULT SPEC.md", "Dev Log.md", "Directory.md"}:
        continue
    if note.parent.name in {
        "TV Shows", "Movies", "Documentaries", "Franchises",
        "Shorts", "Collections", "Data", "Sources", "Templates", "Inbox"
    }:
        continue
    if EPISODE_RE.match(note.name):
        continue
    canonical_media.append(note)

if isinstance(manifest, dict):
    actual_file_count = len(all_files)
    actual_markdown_count = len(markdown_files)
    actual_episode_count = len(episode_notes)
    if manifest.get("file_count") != actual_file_count:
        errors.append(f"Manifest file_count={manifest.get('file_count')} but actual={actual_file_count}")
    if manifest.get("markdown_count") != actual_markdown_count:
        errors.append(f"Manifest markdown_count={manifest.get('markdown_count')} but actual={actual_markdown_count}")
    if manifest.get("episode_count") != actual_episode_count:
        errors.append(f"Manifest episode_count={manifest.get('episode_count')} but actual={actual_episode_count}")

print(f"Binge validation: {len(errors)} error(s), {len(warnings)} warning(s)")
for item in errors:
    print(f"ERROR: {item}")
for item in warnings:
    print(f"WARNING: {item}")

sys.exit(1 if errors else 0)
