# Batch 009 - Selected media identity verification

**Date:** 2026-09-20

## Scope

Targeted verification of ambiguous entries before canonical media folders and episode structures are generated. This batch intentionally does not create media folders yet.

## Verified changes

| ID | Title | Result |
|---|---|---|
| extra-gear | Extra Gear | Confirmed as a British online television companion series to Top Gear; 4 series / 24 episodes; first aired 2016. Recorded as a web series and ended. |
| sassy-the-sasquatch | Sassy the Sasquatch | Confirmed as a 2022 animated web/TV series with 6 main episodes in Season 1. Recorded as a web series and ended. |
| the-backrooms | The Backrooms | Confirmed as Kane Pixels' YouTube web series beginning in 2022. Kept as a web series rather than treating the title as a generic creepypasta entry. |
| president-curtis | President Curtis | Confirmed as the Rick and Morty spin-off created for Adult Swim and associated with 2026. Recorded as a TV series. |
| minecraft-story-mode | Minecraft: Story Mode | Confirmed by Telltale as an episodic narrative game rather than a television production. The inventory remains retained because it was explicitly supplied, but its `media_type` now records the game nature so it is not silently treated as conventional TV. |

## Sources consulted

- Wikipedia — Extra Gear: British online television series, 4 series / 24 episodes, 2016–2019.
- IMDb — Extra Gear: TV series with 24 episodes across 4 seasons.
- Tubi — Sassy the Sasquatch: 2022, one season, three-part presentation.
- IMDb / TheTVDB — Sassy the Sasquatch: six-episode Season 1 and a separate special/behind-the-scenes entry.
- Wikipedia — Backrooms web series: Kane Pixels' YouTube series, first aired 2022.
- Wikipedia / IMDb — President Curtis: Adult Swim animated Rick and Morty spin-off associated with 2026.
- Telltale Community — Minecraft: Story Mode: explicitly described as a Telltale Games series/game with episodic releases.
- Minecraft Wiki — Minecraft: Story Mode episode lists for both seasons.

## Structural decision

No physical folders were created from these classifications yet. Episode creation remains gated on broader title/episode verification so the vault does not need to be rebuilt after avoidable identity errors.

## Validation

- Inventory remains at 406 media records.
- No new media titles were introduced.
- No exact duplicate records were introduced.
- No supporting asset folders were fabricated.
- The five selected records now carry additional identity/type metadata.
- Full inventory verification remains incomplete.

## Known issues

- Several Marvel entries still require production-type and same-title identity verification.
- Several supplied titles remain ambiguous and need source matching before folder creation.
- Minecraft: Story Mode needs a final decision on whether game content belongs in the physical media tree or a dedicated non-video-media area; no structural move was made in this batch.

## Next steps

Continue identity verification in grouped batches, prioritizing:
1. same-title Marvel productions and Marvel short/special boundaries;
2. Doctor Who / Star Trek unusual episode and special structures;
3. ambiguous supplied titles;
4. future/scheduled releases;
5. then begin canonical media record creation once the verified inventory is stable.
