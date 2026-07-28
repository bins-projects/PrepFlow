# Quiz Builder Open-Book Checkpoint — 2026-07-28

## Status

The shared Quiz Builder open-book chapter interface is visually approved and working locally on branch `docs/continuity-rebuild`.

This checkpoint builds on the synchronized nursing-station interior preserved in commit `53d18865c8276a3cca2fd464d7e593acd1da2042`.

## Implemented behavior

All three subject books now share one open-book interaction:

- Fundamentals
- Pharm
- Medical-Surgical

Each closed book:

1. leaves its nursing-station shelf;
2. travels to the shared center preview position;
3. enlarges;
4. hands off to the transparent open-book artwork;
5. displays that subject's chapters;
6. closes and returns to its original shelf through the shared Back control.

The animation is an approved browser illusion using the closed-cover and open-book PNG assets. It is not a frame-by-frame page-turn animation.

## Chapter interface

The shared interior provides:

- one responsive 16:9 book coordinate plane;
- five complete visible chapter rows at supported window sizes;
- natural scrolling for additional chapters;
- whole-card checkbox selection;
- persistent illuminated selected state;
- raised and illuminated mouse hover;
- keyboard-visible focus treatment;
- per-book chapter and question totals;
- up to five selected chapter numbers followed by `+N more`;
- selection preservation when returning to the shelf;
- combined cross-book totals in the nursing-station builder footer.

The open-book summary always reports only the currently open subject. The builder footer reports the combined selection across all subjects.

## Navigation rule

`Back to Quiz Builder` is the authoritative return control for the open-book interior.

It:

- preserves chapter selections;
- uses the shared close-book action;
- returns the active cover to the correct shelf;
- uses a visually approved 2.2-second attention pulse;
- remains steadily illuminated on hover or keyboard focus.

The older `Done — Return to Builder` control remains hidden in the real open-book state and should not be restored as a duplicate return action.

## Runtime asset

The only new open-book runtime asset is:

```text
web/images/quiz-builder/books/quizbook-transparent.png
```

The discarded opaque exports `openbook.png` and `quizbook.png` were removed before commit because they were unused duplicates.

## Primary implementation files

```text
web/app.js
web/index.html
web/quiz-builder-screen.css
web/images/quiz-builder/books/quizbook-transparent.png
```

## CSS cleanup completed

Before preservation, the open-book CSS was consolidated:

- selected-card appearance and animation were combined into one rule;
- unreachable styling for hidden legacy controls was removed;
- the redundant open-book mobile override was removed;
- closing animation scales now use the same subject-specific variables as opening;
- authoritative open-book selectors were verified;
- `git diff --check` passed.

This cleanup applies only to the new open-book work. Older nursing-station and homepage CSS cleanup remains a separate protected milestone.

## Verification

Completed locally:

- Fundamentals open, select, scroll, close, and reopen;
- Pharm open, select, scroll, close, and reopen;
- Medical-Surgical open, select, scroll, close, and reopen;
- per-book summaries;
- combined builder totals;
- wide and narrow responsive comparison;
- selection preservation;
- 72 automated tests passed;
- `git diff --check` passed.

## Deferred work

Do not treat the following as part of this completed milestone:

- true frame-based book opening or page-turn artwork;
- deletion of the hidden legacy HTML controls;
- broad consolidation of older Quiz Builder CSS;
- consolidation of `web/hospital-home.css`;
- mobile-specific redesign beyond the current responsive 16:9 behavior.

These may be reconsidered as separate backed-up milestones.
