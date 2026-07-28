# QUIZ BUILDER INTERIOR CHECKPOINT — 2026-07-27

## Status

The visually approved Quiz Builder interior milestone is preserved in commit
`5897f0d7fbb334cdc7eebaad73d1cbd3292a4a82` on
`docs/continuity-rebuild` and was synchronized to both development remotes.

The current local working tree contains a focused follow-up fix that locks the
book and shelf-plaque layers together across browser sizes. It is not yet
committed or pushed.

## Implemented and approved

- The Quiz Builder is a separate full-screen application state rather than a
  transparent homepage overlay.
- The complete nursing-station scene is contained as a 16:9 coordinate plane.
- The hospital homepage is hidden while the Quiz Builder is open.
- Three new transparent closed-book assets are seated on one measured counter
  baseline.
- Clicking a book centers and enlarges its artwork, dims the other books, holds,
  pulses once, and then runs the existing chapter-opening behavior.
- Three decorative shelf-front plaques identify the subjects without becoming
  buttons or enlarging the book hit areas.
- Existing Pack paths, accessibility labels, chapter state, selected-book state,
  and mixed-Pack quiz construction remain browser-owned and functional.

## Runtime assets

Background:

```text
web/images/quiz-builder/prepflow-nursing-station-quiz-builder.png
```

Closed books:

```text
web/images/quiz-builder/books/fundamentals-closed.png
web/images/quiz-builder/books/pharm-closed.png
web/images/quiz-builder/books/medsurg-closed.png
```

All book canvases are `896 × 1200`.

Measured visible alpha geometry:

```text
Fundamentals: 774 × 1067; bottom padding 68 px
Pharm:        774 × 1066; bottom padding 68 px
Med-Surg:     774 × 1068; bottom padding 67 px
```

The older assets under `web/images/book-sprite-preview/` are historical and are
not authoritative for this interior.

## Approved book geometry

Shared resting rules:

```text
width: 9.6%
top: auto
bottom: 47.2%
transform-origin: bottom center
```

Shared station-center coordinates:

```text
Fundamentals: 25.9%
Pharm:        49.6%
Med-Surg:     73.3%
```

Each `9.6%`-wide book card derives its left edge from the shared station center:

```text
left: calc(station center - 4.8%)
```

The decorative plaque for that subject uses the same station center directly.

The narrow wooden strip visible beneath the books is intentional and provides
the depth cue that they are resting on the counter.

## Approved launch interaction

Authority:

```text
web/app.js
BOOK_LAUNCH_DURATION_MS = 1150
```

Each subject uses the same sequence:

```text
move to center → enlarge → dim other books → hold → pulse → open chapters
```

The artwork moves while the subject-card button remains fixed at the shelf
station. Only one launch may run at a time.

## Approved shelf plaques

The plaques are separate decorative HTML/CSS elements:

```text
aria-hidden="true"
pointer-events: none
```

They use an upper flange, main face, and lower return to appear wrapped around
the shelf edge.

Approved row position:

```text
top: 58%
```

Each plaque uses the same shared station-center variable as its corresponding
book. Books and plaques therefore remain horizontally locked while the 16:9
scene changes rendered size.

The uniform aged-brass/light-enamel treatment with dark lettering is approved.
Subject color coding was tested and superseded.

## Durable geometry and CSS rules

For scene-bound objects that share one painted physical surface:

1. measure the rendered scene surface;
2. inspect transparent padding and visible alpha bounds;
3. establish one shared baseline;
4. establish shared station anchors for objects that must remain aligned;
5. verify both the visual result and rendered element boxes at multiple sizes;
6. reset inherited global constraints that alter the scene coordinate plane;
7. keep one authoritative current CSS rule.

The responsive drift was caused by the global homepage rule
`.subjects { max-width: calc(100vw - 48px) !important; }` shrinking only the
Quiz Builder book layer. The authoritative Quiz Builder `.subjects` rule now
uses `max-width: none !important`, so the book and plaque layers both occupy the
complete 16:9 scene plane.

When a new adjustment replaces an earlier experimental rule for the same
element, remove or replace the superseded rule instead of stacking another
override. An earlier rule remains only when it intentionally serves a distinct
breakpoint, state, or interaction.

## Deferred work

- redesign the chapter-selection screen;
- create approved open-book chapter states;
- standardize and finish the lower Quiz Builder controls in scene coordinates;
- continue rebuilding later quiz layers inward without redesigning unrelated
  behavior.

## Local working files

Current follow-up modifications:

```text
web/index.html
web/quiz-builder-screen.css
```

The application logic and runtime artwork are already preserved in the
synchronized `5897f0d` checkpoint.

Local safety copy:

```text
web/quiz-builder-screen.css.before-nursing-station
```

The safety copy is not a runtime dependency and must not enter the production
commit without an explicit decision.

## Verification completed for the responsive-lock follow-up

- book and plaque centers were measured from the rendered browser elements;
- the narrower inherited book coordinate layer was identified and corrected;
- books and plaques remain locked while resizing the 16:9 scene;
- Fundamentals, Pharm, and Med-Surg launch and open their correct chapter lists;
- Return to Hospital, Clear Selections, and Build Quiz remain functional;
- the complete automated suite passes: `72 passed`.

Still required before commit:

- inspect the final focused diff;
- run the privacy and artifact scan;
- stage files explicitly; never use `git add .`.

## Push destination after approval

Commit on:

```text
docs/continuity-rebuild
```

Then push the identical commit to:

```text
origin/docs/continuity-rebuild
public/docs/continuity-rebuild
```

Fetch both remotes and verify that local, private, and public-mirror hashes are
equal. Do not push this milestone directly to `master`.
