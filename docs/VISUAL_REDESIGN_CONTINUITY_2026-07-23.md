# PrepFlow Visual Redesign Continuity — 2026-07-23

> **CURRENT LOCAL AUTHORITY:** The three approved transparent PNG books are installed and working in the local repository. This is newer than the last committed GitHub state. Do not resume from the older Pharm-only proof milestone.

This document is the authoritative detailed handoff for the unfinished PrepFlow visual redesign. The current home screen is a working visual-development canvas, not a completed design and not technical debt to remove casually.

## Protected working canvas

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

Continue redesign work only on `docs/continuity-rebuild` until the new visual system is intentionally approved and merged. The stable public version remains separate.

## Latest completed visual milestone

On 2026-07-23, all three Charlie-approved transparent PNG book assets were installed into the real local application and verified in the browser.

Approved assets:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

Implementation files:

```text
web/index.html
web/approved-book-buttons.css
```

Verified result:

- the three approved PNG books render on the home screen;
- the old CSS-drawn book bodies and inline SVG cover emblems are no longer visible;
- the existing `.subject-card` JavaScript hook remains intact;
- all three books open their chapter-selection screens;
- the layout shown in the 2026-07-23 local browser verification is visually approved by Charlie.

This milestone is local and uncommitted at the time of this documentation pass.

## Current redesign state

- The approved sunset-city background and nurses remain one combined static image.
- The closed-book artwork is now real transparent raster artwork for all three subjects, not a Pharm-only proof.
- Live application behavior remains in HTML and JavaScript.
- The new presentation layer is `web/approved-book-buttons.css`, loaded after the existing home-layout styles.
- Do not remove the `.subject-card` class; JavaScript uses it to disable books during saved sessions, update selection badges, and open chapter screens.
- Do not infer that every historical `.subject-card` rule is active or requires an architecture rebuild merely because `grep` finds it. Inspect the actual local markup, load order, final rendered result, and behavior.

## Authoritative visual direction

- Preserve the current pixel-art sunset-city background style.
- Keep the approved sunset-city environment as the visual reference.
- Rebuild books and buttons as reusable pixel-art sprites rather than ordinary flat interface cards.
- Use Pharm as the first book-sprite prototype, then apply the approved system consistently to Fundamentals and Med-Surg.
- Establish one consistent book silhouette, spine, cover, page depth, emblem area, hover state, and selected state before producing all three variants.
- Establish reusable button styling with consistent normal, hover, pressed, disabled, and selected states.
- Do not generate, redraw, or flatten the complete PrepFlow scene when working on one book, button, character, or other isolated asset.

## Graphics production and file-format rule

Use transparent raster sprite assets for the principal illustrated pixel-art objects and characters.

Approved workflow:

1. Create and refine illustrated books, nurses, props, and similarly textured pixel-art assets as transparent PNG files during design and iteration.
2. After an asset is visually approved, an optimized transparent WebP version may be used in the shipped browser product when it preserves transparency, pixel fidelity, and intended appearance.
3. Reserve SVG for genuinely vector-like interface symbols, simple emblems, and clean scalable icons. Do not use SVG as the default format for textured illustrated books, nurses, or environment artwork.
4. Use CSS for positioning, sizing, responsive composition, hover/pressed/selected movement, glows, and state presentation. Do not use CSS gradients, pseudo-elements, or inline SVG to draw the principal final book or character artwork.
5. The approved home-screen book artwork is now the three transparent PNG assets named above. Do not restore the previous CSS-built books or inline SVG cover emblems.
6. Keep live selection status, accessibility text, Pack paths, and click behavior outside the artwork.
7. Never substitute a generated full-screen screenshot or flattened scene for a transparent isolated sprite.

## Permanent artwork versus live application data

The artwork may contain permanent subject identity such as:

- `PHARM`;
- a capsule or medication emblem;
- permanent PrepFlow branding when it belongs to the book design.

Changing library and application data must remain outside the artwork as live HTML. This includes:

- chapter-selection status;
- button labels;
- accessibility text;
- changing counts or progress;
- data attributes and click behavior.

### Closed-book question-count decision

Do **not** display total question counts on the closed books on the home screen.

Reasoning:

- users choose a book by subject, not by which Pack has the largest total;
- totals clutter the artwork and compete with the visual hierarchy;
- the information is more useful after the book is opened.

Show relevant totals inside the opened book/chapter-selection experience instead. The live chapter-selection status may remain beneath or near each closed book.

The temporary Pharm proof recovered during the 2026-07-23 session had `1,238 QUESTIONS` baked into the image. That proof is useful only for layout testing. The next Pharm asset must remove that baked-in count.

## Superseded Pharm-proof warning

The earlier Pharm-only proof and its baked-in `1,238 QUESTIONS` limitation are historical context only. It is no longer the active milestone. The current approved Pharm PNG installed with the other two books does not display the closed-book total.

Do not instruct Charlie to recreate, crop, or recover the old proof. Use the current local approved assets.

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

Treat it as a layout-only layer. Do not use it to establish permanent book artwork or final book typography.

## Local browser-preview workflow

Run the local server from its own dedicated terminal:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Leave that terminal running while previewing. The server terminal printing a request log during page loads and hard refreshes is normal.

Open:

```text
http://localhost:8004/web/
```

Use `Ctrl+Shift+R` for a hard refresh after visual changes.

Before diagnosing CSS, image, or cache behavior, verify the server is actually running and serving the current project. Do not assume the service worker is responsible. The current `web/sw.js` uses a network-first fetch strategy.

## Proven multi-file local workflow

The successful 2026-07-23 repair used the actual local `web/` working copy rather than repeated terminal snippets or GitHub-only inspection. Preserve this workflow for future multi-file visual work:

1. treat `~/projects/prepflow` as the active working source;
2. when direct local access is unavailable, package the smallest relevant local folder or file set;
3. inspect the uploaded local snapshot directly;
4. make one focused change and return only modified files with project-relative paths;
5. apply the package locally;
6. run the real local application and verify the rendered result and behavior;
7. document the proven result;
8. commit and push only afterward.

Do not reconstruct a multi-file visual feature from repeated `grep`, `sed`, and pasted excerpts when one local archive can expose the actual working copy. Do not switch the editing target to GitHub during local iteration.

## Command-flow preference

- When Charlie says `next`, treat the previous paste command as completed and continue to the next executable step.
- Do not repeat the previous command.
- When terminal output is genuinely required, say clearly: `Paste the output here before continuing.`
- Ordinary commands should be introduced with `Paste this`.
- Identify the Python-server terminal only when a command must run there.

## Change-control rules

- Do not disable, delete, consolidate, or reinterpret an existing visual layer solely because the CSS cascade is layered.
- Before removing an experimental layer, identify what visual decision it represents and compare the rendered result.
- Capture baseline screenshots before meaningful visual changes.
- Make one isolated visual change at a time.
- Verify full-window and reduced-window behavior after every change.
- Do not perform final CSS cleanup until the responsive composition, books, buttons, and reusable asset strategy are approved.
- Never claim a preview, test, server state, cleanup, or approval that was not verified.
- Stop and reassess when troubleshooting becomes repetitive rather than stacking additional guesses.
- Future chats must treat Charlie's explicit design corrections in this document as authoritative unless newer committed evidence replaces them.

## Exact next visual milestone

Finish verification and commit the already-approved three-book replacement.

Required sequence:

1. begin from the current local `docs/continuity-rebuild` working copy;
2. verify `git status --short --branch`;
3. run the server from `~/projects/prepflow`, not from `web/`;
4. verify the approved books at full width and reduced width;
5. select chapters from each book and verify live selection badges;
6. run the existing automated tests;
7. inspect the focused diff;
8. keep transfer archives and backups out of the commit;
9. commit the book replacement;
10. push and verify the intended private remote.

Do not begin another book redesign, return to a Pharm-only prototype, rebuild the stylesheet architecture, polish obsolete CSS-drawn covers, or replace the approved PNGs without Charlie's explicit request.

## Recommended continuation order

1. Complete responsive and behavior verification for the approved three-book replacement.
2. Commit and synchronize the verified local milestone.
3. Finalize reusable pixel-art button styling only if Charlie wants further button changes.
4. Reassess the background-extension and environment-layer strategy using the stable canvas.
5. Separate the background and nurses into reusable assets while preserving the approved character designs.
6. Create pose variants for other screens.
7. Test desktop, reduced-width, reduced-height, and narrow layouts.
8. Consolidate obsolete experimental CSS only after visual approval and only with a focused evidence-based plan.
