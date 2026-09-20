# Data

Machine-readable project data lives here.

## Files

- inventory.json — canonical staged media inventory.
- inventory.schema.json — schema for the inventory structure.
- media.schema.json — schema for individual media records.
- Build Manifest.json — machine-readable build state and validation summary.
- Inventory Intake.md — rules for bringing the authoritative media list into the project.

## Inventory rule

inventory.json must be populated only from the authoritative to-add list supplied for this build or an explicit later addition.

Do not reconstruct the inventory from historical projects, previous conversations, model memory, or guesses.

Before canonical media folders are created, inventory entries should be normalized, deduplicated, classified, and verified.
