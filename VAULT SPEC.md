# Binge Vault Specification

This document records the core structural rules for the from-scratch Binge vault.

## Media

Every actual media work receives a canonical record appropriate to its type.

### Series

    Show/
    ├── Season 01/
    │   ├── S01E01 - Episode Title/
    │   │   └── S01E01 - Episode Title.md
    │   └── S01E02 - Episode Title/
    │       └── S01E02 - Episode Title.md
    └── Show.md

### Movies

    Movie/
    └── Movie.md

### Documentary series

Use series-style seasons and episode folders when the production has a genuine episodic structure.

### Shorts and specials

Represent real shorts and specials explicitly. Do not discard them merely because they are outside a normal season.

## Naming

- Show and movie names use canonical titles where reliable sources support them.
- Seasons use canonical numbering where reliable metadata supports it.
- Episodes use `S01E01 - Episode Title`.
- Avoid arbitrary abbreviations, meaningless IDs, malformed names, and trailing whitespace.

## Metadata

Only verified or defensible metadata is written. Unknown fields remain unknown rather than being fabricated.

## Relationships

Use Markdown links, frontmatter, indexes, and franchise/universe pages for logical relationships. Do not over-nest physical folders solely to model relationships.

## Supporting files

Create folders such as `Sources`, `Images`, `Subtitles`, `Artwork`, `Scripts`, and `Captions` only when actual relevant files exist.

## Validation

Major batches must validate files, structure, links, metadata, duplicate identity, and navigation. Results belong in the Dev Log and Build Manifest.
