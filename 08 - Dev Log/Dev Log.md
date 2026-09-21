# Dev Log

This folder records meaningful Binge build batches.

## Batch 011 — Marvel specials, pilots, and legacy television-film verification

**Date:** 2026-09-20  
**Scope:** Continue Marvel identity verification, focusing on LEGO Marvel entries, legacy television films/compilations, pilot/special boundaries, and same-production duplicates.

- Verified LEGO Marvel Avengers: Code Red (2023) and LEGO Marvel Avengers: Mission Demolition (2024) as animated specials.
- Verified LEGO Marvel Avengers: Strange Tails (2025) as an animated series with a season/episode structure.
- Verified Dr. Strange (1978), The Death of the Incredible Hulk (1990), and The Return of the Incredible Hulk (1977) as distinct television-film productions.
- Reclassified The Incredible Hulk: Married (1978) as a television special.
- Verified Spider-Man Strikes Back (1978) and Spider-Man: The Dragon's Challenge (1981) as feature-length compilations of Amazing Spider-Man episodes.
- Verified Blade: House of Chthon as the feature-length pilot/DVD presentation of Blade: The Series.
- Verified Nightman: World Premiere as the two-part 1997 television pilot and retained it as a special/pilot.
- Deduplicated the supplied Inhumans movie record because its IMAX release consisted of the first two episodes of the same 2017 television series rather than a separate production.
- No new titles were introduced.
- No physical media or episode folders were created.

### Validation

- Inventory media count: **405**
- Episode count: **0**
- Physical media folders: **0**
- Supporting asset folders: **0**
- No speculative titles added.

### Next step

Continue remaining Marvel same-title and short/special boundaries, then proceed toward broader inventory verification before canonical media-folder generation.

# Dev Log

This folder records meaningful Binge build batches.

## Batch 008 — Initial targeted external verification

**Date:** 2026-09-20  
**Scope:** Begin external verification of captured media identities and correct production collisions before canonical folder construction.

- Added targeted verification notes in `08 - Dev Log/Batch 008 - Initial external verification.md`.
- Corrected the How to Train Your Dragon collision: the 2010 animated film and 2025 live-action film are distinct productions and are now separate inventory records. citeturn1search0turn0search0
- Verified Incredibles 3 as a scheduled Pixar film for June 16, 2028. citeturn1search1
- Updated Toy Story 5 to released/2026 based on Disney's official film listing. citeturn1search6
- Updated Scream 7 to released/2026 based on Paramount's current listing. citeturn1search15
- Reclassified The Punisher: One Last Kill as a special presentation based on Marvel's official catalogue. citeturn0search12
- No episode structures were generated yet; systematic verification continues before large-scale folder creation.

## Batch 007 — Capture authoritative inventory

**Date:** 2026-09-20  
**Scope:** Capture the user-supplied authoritative media lists, expand the supplied cover groups, and remove duplicate copies without importing anything from the referenced “existing source” material.

### Inventory capture

- Captured the television/series list, existing films, and existing documentaries.
- Captured the explicit Superwog: Son of a Donkey item as its own media record.
- Materialized the supplied Star Trek, Toy Story, The Incredibles, How to Train Your Dragon, Mario, Scream, Avatar, Marvel, and David Attenborough cover expansions.
- Did not use the “existing source” wording as an inventory source.
- Did not infer unrelated titles.
- Retained explicitly named future/scheduled projects rather than inventing unnamed projects.

### Deduplication

- Removed exact duplicate copies where the same production appeared in both a base list and an expansion.
- Preserved distinct productions that share a display title, including the separate Scream films and separate same-title Marvel film/television/short productions.
- Inventory now contains **405 media records**.

### Current inventory counts

- TV / series: 156
- Movies: 203
- Documentaries: 27
- Shorts: 17
- Specials: 2
- Total: 405

### Validation status

- Inventory schema remains compatible with the current data model.
- No episode folders or media folders have been created yet.
- No supporting asset folders have been fabricated.
- Metadata has not yet been externally verified at this stage.

### Next step

Externally verify and normalize the captured inventory, resolve any remaining production-identity ambiguities, then begin canonical media record creation and episode expansion.

## Batch 006 — Manifest reconciliation after inventory-intake foundation

**Date:** 2026-09-20  
**Scope:** Reconcile machine-readable build counts with the repository after Batch 005 and verify that no speculative media entered the project.

- Updated 07 - Data/Build Manifest.json to reflect the current repository tree.
- Updated latest batch to 6.
- Corrected repository totals to 25 files and 20 Markdown files.
- Confirmed media count remains 0.
- Confirmed episode count remains 0.
- Confirmed no cover-group records have been introduced.
- Confirmed the authoritative inventory remains intentionally empty.
- No media folders, episode folders, or fabricated metadata were created.

### Validation

Current repository contains the complete initialization/data-intake foundation plus the Batch 005 intake documentation. The manifest now matches the tree state.

### Known blocker

The authoritative to-add media list is still not present in the current project inputs. Media construction must not begin until that inventory is supplied.

### Next step

Once the authoritative inventory exists, capture it in 07 - Data/inventory.json, then normalize, deduplicate, classify, research, and verify it before canonical media creation.

## Batch 005 — Inventory intake contract

**Date:** 2026-09-20  
**Scope:** Establish a precise intake contract for the authoritative media inventory without creating speculative media.

- Added 07 - Data/Inventory Intake.md.
- Expanded 07 - Data/README.md to document the complete inventory pipeline.
- Defined capture, classification, normalization, deduplication, cover-group expansion, verification, and approval stages.
- Explicitly documented that historical projects, previous conversations, model memory, and inferred titles are not valid inventory sources for this from-scratch build.

## Batch 004 — Validator consistency correction

**Date:** 2026-09-20  
**Scope:** Reconcile manifest counts with the actual repository tree and strengthen inventory validation.

- Corrected manifest counts to 20 total files and 16 Markdown files.
- Added schema files to validator required-file checks.
- Added duplicate inventory-ID detection.
- Added required ID/title checks for future inventory records.
- Added manifest-to-inventory media count validation.
- No media or episode records created.

## Batch 003 — Data schema and validator hardening

**Date:** 2026-09-20  
**Scope:** Strengthen the from-scratch foundation without inventing media inventory.

- Added machine-readable media and inventory schemas.
- Hardened the structural validator and fixed episode-pattern matching.
- Added manifest count consistency checks.
- Added inventory structure checks.
- No media or episode records were created.
- The authoritative media/to-add list is still not present in the current project inputs.

## Batch 002 — Foundation validation

**Date:** 2026-09-20  
**Scope:** Initial machine-readable inventory staging and structural validation.

- Added 07 - Data/inventory.json as the canonical inventory staging file.
- Added 07 - Data/README.md documenting inventory rules.
- Added the initial scripts/validate_vault.py validator.
- Added the Batch 002 report.
- Corrected the manifest counts to reflect the actual 15-file foundation.
- Media inventory intentionally remains empty; no historical media was imported.

## Batch 001 — Initialize Binge media architecture

**Date:** 2026-09-20  
**Scope:** From-scratch vault foundation.

- Established canonical root organization for TV shows, movies, documentaries, franchises, shorts, collections, data, Dev Log, sources, templates, and inbox work.
- Added the human-facing Directory and media-type landing pages.
- Added the initial machine-readable Build Manifest.
- Added the persistent Dev Log.
- Deliberately did not create media records, episode folders, fake supporting directories, speculative metadata, or plugin configuration.

## Batch 009 — Selected media identity verification

**Date:** 2026-09-20  
**Scope:** Targeted external verification of ambiguous web, animated-series, and non-TV entries before physical media construction.

- Verified Extra Gear as a British online Top Gear companion series (4 series / 24 episodes) and recorded it as a web series.
- Verified Sassy the Sasquatch as a 2022 animated web/TV series and recorded its six-episode first season.
- Verified The Backrooms as Kane Pixels' YouTube web series beginning in 2022.
- Verified President Curtis as the Adult Swim Rick and Morty spin-off associated with 2026.
- Verified Minecraft: Story Mode as an episodic narrative game; retained it because it was explicitly supplied, while recording its non-TV nature in media_type.
- Added the detailed Batch 009 verification report.
- No media folders or episode folders were generated in this batch.

### Validation

- Inventory remains at 406 media records.
- No new titles were introduced.
- No exact duplicate records were introduced.
- No supporting asset folders were fabricated.
- Full inventory verification remains incomplete.

### Known issues

- Marvel same-title productions and short/special boundaries still require systematic verification.
- Several ambiguous supplied titles still require source matching.
- Minecraft: Story Mode requires a later structural decision about non-video game content; no move was made yet.

### Next step

Continue grouped identity verification, then begin canonical media record creation only after the inventory is sufficiently stable.


## Batch 010 — Verify Marvel legacy film identities

**Date:** 2026-09-20  
**Scope:** Verify Marvel legacy television films, feature films, and Marvel Rising special boundaries before physical media construction.

- Distinguished Captain America (1979) from Captain America (1990).
- Verified Captain America II: Death Too Soon (1979) as a separate television film.
- Verified The Fantastic Four (1994) as an officially unreleased completed feature film.
- Verified Generation X (1996), Nick Fury: Agent of S.H.I.E.L.D. (1998), Spider-Man (1977), and The Incredible Hulk (1977) as television-film productions.
- Verified Man-Thing (2005) as a feature-length Marvel production with a U.S. television premiere.
- Verified The Punisher (1989) as a distinct feature film.
- Verified Marvel Rising: Secret Warriors as an animated television film and Chasing Ghosts, Heart of Iron, and Battle of the Bands as animated specials.
- Changed those three Marvel Rising entries from `short` to `special` in the inventory.
- No new titles were added and no duplicate productions were merged.

### Validation

- Inventory remains 406 media records.
- No media or episode folders were created.
- No supporting asset folders were fabricated.
- Verification remains incomplete.

### Next step

Continue Marvel identity verification, especially LEGO entries, remaining direct-to-video/television productions, animated-series boundaries, and same-title productions.


## Batch 012 — Remaining Hulk television-film verification

**Date:** 2026-09-20

- Verified **The Incredible Hulk Returns** as the 1988 television film.
- Verified **The Trial of the Incredible Hulk** as the 1989 television film.
- Confirmed these are distinct from the 1977 **The Return of the Incredible Hulk** pilot sequel.
- Existing metadata for **The Death of the Incredible Hulk** (1990) and **The Incredible Hulk: Married** (1978 special) was retained.
- Inventory remains at 405 media records.
- No physical media or episode folders were generated.
- No speculative titles were added.

### Next step
Continue remaining Marvel same-title and short/special/direct-to-video verification before canonical media-folder generation.


## Batch 013 — Marvel short-form identity verification

**Date:** 2026-09-20

- Identified the supplied **Captain America** short-form record as the 1944 Republic Pictures theatrical serial.
- Identified the supplied **Spider-Man** short-form record as the 1978 Toei theatrical production.
- Both remain separate from same-title television and feature productions.
- Inventory remains at 405 media records.
- No physical media or episode folders were generated.
- No speculative titles were added.

### Next step
Continue Marvel boundary verification and then broaden verification to the remaining authoritative inventory before physical vault generation.


## Batch 014 — Marvel same-title film verification

**Date:** 2026-09-21

- Distinguished the 1994 unreleased *The Fantastic Four* from the 2005 released *Fantastic Four*.
- Distinguished the 2004 *The Punisher* from the 1989 feature film and the *The Punisher* television series.
- Identified the supplied *The Incredible Hulk* feature record as the 2008 film, separate from the 1977 television film.
- Identified the supplied *Spider-Man* feature record as the 2002 film, separate from the 1977 television film and 1978 Toei production.
- Inventory remains at 405 media records.
- No speculative titles added.

### Next step
Continue Marvel boundary verification, then move into broader inventory verification before physical vault generation.


## Batch 015 — Marvel pilot and special verification

**Date:** 2026-09-21

- Corrected *Blade: House of Chthon* to 2006 and retained its feature-length television-pilot classification.
- Confirmed *The Punisher: One Last Kill* as a 2026 television special.
- Checked the Marvel Rising special/short boundary without expanding the authoritative inventory beyond supplied titles.
- Inventory remains at 405 media records.
- No speculative media added.

### Next step
Move from the remaining Marvel edge cases into broader verification of the authoritative inventory, prioritizing ambiguous titles and future/scheduled records.


## Batch 016 — Recent series verification

**Date:** 2026-09-21

- Verified *The Summer Hikaru Died* as a 2025 anime series; Season 1 has 12 episodes.
- Verified *The War Between the Land and the Sea* as a 2025 five-episode television miniseries.
- Began broader non-Marvel verification after the Marvel identity pass.
- Inventory remains at 405 media records.
- No speculative media added and no physical media folders generated.

### Next step
Continue systematic verification of ambiguous series, miniseries, web series, and unusual episode structures across the authoritative inventory.


## Batch 017 — Web and animated series verification

**Date:** 2026-09-21

- Verified *Extra Gear* as a distinct *Top Gear* online companion/web series.
- Verified *Sassy the Sasquatch* as a 2022 six-part animated series; did not add its later behind-the-scenes special because it was not in the authoritative inventory.
- Verified *The Backrooms* as Kane Parsons' ongoing web series.
- Verified *President Curtis* as a distinct 2026 Adult Swim animated series.
- Inventory remains at 405 media records.
- No speculative media added.

### Next step
Continue verification of unusual series, future/scheduled titles, documentary/special boundaries, and episode-level metadata.


## Batch 018 — Current feature film verification

**Date:** 2026-09-21

- Verified *Project Hail Mary* as released in 2026.
- Verified *Avatar: Fire and Ash* as released in 2025.
- Verified *Spider-Man: Brand New Day* as released in 2026.
- Kept *Avengers: Doomsday* as scheduled for December 18, 2026.
- Inventory remains at 405 media records.
- No speculative media added.

### Next step
Continue current-date verification of scheduled titles and non-standard documentaries, specials, and miniseries.
