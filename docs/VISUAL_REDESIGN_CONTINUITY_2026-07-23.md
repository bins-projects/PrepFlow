# PrepFlow Visual Redesign Continuity — 2026-07-23

This document preserves the authoritative direction for the unfinished PrepFlow visual redesign. The current home screen is a working visual-development canvas, not a completed design and not technical debt to remove casually.

## Protected working canvas

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

The stable public version remains available separately. Continue redesign work only on `docs/continuity-rebuild` until the new visual system is intentionally approved and merged.

## Current redesign state

- The home terminal/launcher was being established as the working canvas for the redesign.
- Responsive scaling work was actively in progress and was not complete.
- The background should extend to the bottom of the viewport so reduced-height windows do not reveal dead space.
- The current book and button appearance is experimental and not yet fully matched to the approved pixel-art environment.
- The layered CSS files represent unfinished visual iterations. They must not be removed merely because they overlap.

## Authoritative visual direction

- Preserve the current pixel-art background style.
- Keep the approved sunset-city environment as the visual reference.
- Rebuild books and buttons as reusable pixel-art sprites rather than ordinary flat interface cards.
- Use Pharm as the first book-sprite prototype, then apply the approved system consistently to Fundamentals and Med-Surg.
- Keep titles, question counts, selection state, and button labels as live HTML where practical. Do not bake changing text into artwork.
- Establish one consistent book silhouette, spine, cover, page depth, emblem area, hover state, and selected state before producing all three variants.
- Establish reusable button styling with consistent normal, hover, pressed, disabled, and selected states.

## Background and nurse assets

The currently approved home image contains both nurses and the sunset background in one static asset:

```text
web/images/pixel-home-stage.webp
```

Treat that image as the approved reference and do not casually regenerate, crop, substitute, or replace it.

Future asset work should separate:

1. the environment/background;
2. the lower environment extension or foreground used to eliminate dead space;
3. reusable nurse character sprites.

The two nurses should retain consistent designs, proportions, palette, and pixel density while supporting different poses for different screens, such as home, studying, reference library, and quiz completion.

## Responsive composition rule

Do not solve scaling by independently adjusting unrelated pieces across several files without checking the complete composition. The final responsive system should use:

- one clear home-scene container;
- one approved desktop reference composition;
- proportional positioning inside that composition;
- a small number of intentional breakpoints;
- minimum readable sizes for live text and controls;
- deliberate reflow at narrow widths rather than accidental transform conflicts.

## Change-control rules

- Do not disable, delete, consolidate, or reinterpret an existing visual layer solely because the CSS cascade is layered.
- Before removing an experimental layer, identify what visual decision it represents and compare the rendered result.
- Capture baseline screenshots before meaningful visual changes.
- Make one isolated visual change at a time.
- Verify full-window and reduced-window behavior after every change.
- Do not perform final CSS cleanup until the responsive composition, books, buttons, and reusable asset strategy are approved.
- Future chats must treat the user's recalled design intent in this document as authoritative unless newer committed evidence explicitly replaces it.

## Recommended continuation order

1. Preserve and run the current home canvas unchanged.
2. Finish the reduced-window scaling and dead-space investigation without redesigning unrelated elements.
3. Establish the background-extension strategy.
4. Finalize the Pharm book sprite as the reusable book pattern.
5. Apply the pattern to Fundamentals and Med-Surg.
6. Finalize reusable pixel-art button styling.
7. Separate the background and nurses into reusable assets while preserving the approved character designs.
8. Create pose variants for other screens.
9. Test desktop, reduced-width, and narrow layouts.
10. Consolidate obsolete experimental CSS only after visual approval.
