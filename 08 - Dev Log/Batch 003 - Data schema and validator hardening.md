# Batch 003 — Data schema and validator hardening

**Date:** 2026-09-20  
**Scope:** Strengthen the from-scratch foundation without inventing media inventory.

## Changes

- Added a machine-readable media-record JSON Schema.
- Added a machine-readable inventory JSON Schema.
- Hardened the structural validator.
- Corrected episode filename matching so canonical `S01E01 - Title.md` notes are actually recognized.
- Added required-file checks for the canonical inventory.
- Added manifest consistency checks for total files, Markdown files, and episode notes.
- Added basic validation of inventory top-level structure and project identity.
- Added warnings for episode notes placed outside conventional season/specials folders.
- Updated the Build Manifest for Batch 003.

## Media impact

- Media records created: 0.
- Episode records created: 0.
- No speculative titles or metadata were added.
- The authoritative to-add inventory is still absent from the current project inputs, so historical media lists were not imported.

## Validation

The validator is now designed to derive file and episode counts from the working tree and compare them with the manifest. The schema files define the intended machine-readable shape for future inventory and media records.

## Known limitations

- JSON Schema files are definitions; a full JSON-Schema engine is not yet required by the lightweight validator.
- Wikilink resolution, frontmatter/YAML validation, Dataview references, and duplicate media identity checks will be added when actual media records exist.
- External metadata verification has not started because there is no authoritative media inventory to research.

## Next steps

1. Obtain the authoritative media/to-add list in the current project inputs.
2. Normalize and deduplicate that inventory.
3. Expand cover groups only where their intended scope is clear.
4. Research and verify individual media before creation.
5. Build canonical media and episode structures in meaningful batches.
