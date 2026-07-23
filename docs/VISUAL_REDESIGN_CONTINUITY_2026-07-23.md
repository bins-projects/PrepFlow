# PrepFlow Visual Redesign Continuity — 2026-07-23

This document preserves the authoritative direction for the unfinished PrepFlow visual redesign. The current home screen is a working visual-development canvas, not a completed design and not technical debt to remove casually.

## Protected working canvas

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

The stable public version remains available separately. Continue redesign work only on `docs/continuity-rebuild` until the new visual system is intentionally approved and merged.

## Latest completed visual milestone

```text
e5ed054  fix: stabilize half-width home composition
```

Verified behavior after this milestone:

- the reduced-width launcher and reference panel no longer collide;
- the PrepFlow logo and tagline remain separated and readable;
- the background reaches the bottom of the reduced-height viewport without dead space;
- all three books remain inside the visible composition;
- full-width rendering was checked after the change and was not regressed;
- `git diff --check` passed;
- local and private branch hashes matched after push.

The temporary book titles remain imperfect. Do not spend more time polishing those CSS titles because the books are scheduled for a sprite redesign.

## Current redesign state

- The home terminal/launcher is now dependable enough to use as the redesign canvas at full and reduced width.
- The first focused responsive-composition milestone is complete.
- The current book and button appearance is experimental and not yet fully matched to the approved pixel-art environment.
- The layered CSS files represent unfinished visual iterations. They must not be removed merely because they overlap.
- The current background and nurses still exist as one combined static image.

## Authoritative visual direction

- Preserve the current pixel-art background style.
- Keep the approved sunset-city environment as the visual reference.
- Rebuild books and buttons as reusable pixel-art sprites rather than ordinary flat interface cards.
- Use Pharm as the first book-sprite prototype, then apply the approved system consistently to Fundamentals and Med-Surg.
- Keep titles, question counts, selection state, and button labels as live HTML where practical. Do not bake changing text into artwork.
- Establish one consistent book silhouette, spine, cover, page depth, emblem area, hover state, and selected state before producing all three variants.
- Establish reusable button styling with consistent normal, hover, pressed, disabled, and selected states.

## Graphics production and file-format rule

Use transparent raster sprite assets for the principal illustrated pixel-art objects and characters.

Approved workflow:

1. Create and refine illustrated books, nurses, props, and similarly textured pixel-art assets as transparent PNG files during design and iteration.
2. After an asset is visually approved, an optimized transparent WebP version may be used in the shipped browser product when it preserves transparency, pixel fidelity, and intended appearance.
3. Reserve SVG for genuinely vector-like interface symbols, simple emblems, and clean scalable icons. Do not use SVG as the default format for textured illustrated books, nurses, or environment artwork.
4. Keep changing text and application state—titles, counts, chapter-selection status, button labels, and accessibility text—as live HTML.
5. Use CSS for positioning, sizing, responsive composition, hover/pressed/selected movement, glows, and state presentation. Do not use CSS gradients, pseudo-elements, or inline SVG to draw the principal final book or character artwork.
6. The current CSS-built books and inline SVG cover emblems are exploratory mockups only. They are not the intended final asset system.
7. Pharm is the proof-of-concept sprite. Preview the real transparent raster book asset first, adjust its crop/scale/placement, and do not treat that temporary artwork as the final approved Pharm design.

## Background and nurse assets

The currently approved home image contains both nurses and the sunset background in one static asset:

```text
web/images/pixel-home-stage.webp
```

Treat that image as the approved reference and do not casually regenerate, crop, substitute, or replace it.

Future asset work should separate:

1. the environment/background;
2. any lower environment extension or foreground needed for future compositions;
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

The focused reduced-width authority currently lives in:

```text
web/half-width-composition.css
```

Treat it as a layout-only layer. Do not use it to establish the permanent book artwork or final book typography.

## Change-control rules

- Do not disable, delete, consolidate, or reinterpret an existing visual layer solely because the CSS cascade is layered.
- Before removing an experimental layer, identify what visual decision it represents and compare the rendered result.
- Capture baseline screenshots before meaningful visual changes.
- Make one isolated visual change at a time.
- Verify full-window and reduced-window behavior after every change.
- Do not perform final CSS cleanup until the responsive composition, books, buttons, and reusable asset strategy are approved.
- Future chats must treat the user's recalled design intent in this document as authoritative unless newer committed evidence explicitly replaces it.

## Exact next visual milestone

Finalize Pharm as the first reusable book-sprite prototype without redesigning Fundamentals or Med-Surg.

Required sequence:

1. inspect the current Pharm card HTML, live text, and click behavior;
2. verify whether the previously approved transparent Pharm sprite asset is available;
3. if it is unavailable, ask Charlie to reattach that exact approved asset rather than regenerating it automatically;
4. place the sprite under a clear reusable asset path;
5. replace only the temporary Pharm book artwork with the real transparent raster sprite;
6. keep title, question count, chapter-selection status, data attributes, and click behavior as live application elements;
7. use CSS only for sprite placement, scale, interaction, and responsive behavior;
8. run the real browser at full and reduced width;
9. obtain Charlie's visual approval before applying the pattern to the other books.

Do not begin by polishing the temporary vertical title CSS, redrawing the book with CSS, redesigning all three books, consolidating the visual stylesheets, or separating the nurses from the background.

## Recommended continuation order

1. Finalize the Pharm book sprite as the reusable book pattern.
2. Apply the approved pattern to Fundamentals and Med-Surg.
3. Finalize reusable pixel-art button styling.
4. Reassess the background-extension and environment-layer strategy using the stable canvas.
5. Separate the background and nurses into reusable assets while preserving the approved character designs.
6. Create pose variants for other screens.
7. Test desktop, reduced-width, reduced-height, and narrow layouts.
8. Consolidate obsolete experimental CSS only after visual approval.
