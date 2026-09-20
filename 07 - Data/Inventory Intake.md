# Inventory Intake

This document defines how the authoritative media inventory enters the Binge build.

## Authority

The media universe must come from the current project's authoritative to-add list or an explicit user-provided addition. Historical projects, previous conversations, model memory, or inferred titles are not valid substitutes.

## Accepted input

The authoritative inventory may be supplied as a plain-text title list, Markdown list, structured JSON/CSV file, an explicitly scoped cover-group instruction, or an explicit later addition from the user.

## Intake stages

1. Capture the supplied wording before normalization.
2. Classify likely TV, movie, documentary, short, special, miniseries, or collection/cover-group entries.
3. Normalize obvious formatting differences without changing identity.
4. Deduplicate using title, year, country, network/studio, cast, and production identity where available.
5. Expand cover groups only when their intended scope is clear.
6. Verify canonical title, type, year, season/episode structure, and relationships using reliable sources.
7. Approve only verified, non-duplicate media for canonical vault creation.

## Rules

- Do not silently expand an ambiguous phrase into unrelated media.
- Do not treat a franchise, universe, collection, or filmography label as a media record.
- Do not fabricate missing metadata.
- Preserve uncertainty when sources disagree.
- Do not create episode folders until the parent series and episode identity are established.
- Create supporting folders only when actual supporting material exists.

## Current status

The repository's canonical inventory.json is intentionally empty. No authoritative title list is currently stored in this repository.
