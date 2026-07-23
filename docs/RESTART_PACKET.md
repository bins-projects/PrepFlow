# PREPFLOW RESTART PACKET

## Purpose

This file is the single primary handoff for every new PrepFlow development session.

A new chat must begin here. Supporting documents may contain detailed architecture, history, or visual decisions, but they do not replace this packet. This packet identifies which supporting documents apply to the current milestone and what authority each one has.

The committed private repository is the technical source of truth. Local Git state and the rendered application must also be checked whenever work may be uncommitted, environment-specific, or visual.

---

# 1. Continuity Authority Hierarchy

Use this order:

1. `docs/RESTART_PACKET.md` — primary session handoff and authority index.
2. Current private-repository branch and latest commit — committed implementation truth.
3. Local branch, working-tree status, and local-only files — required when work may be uncommitted.
4. Supporting documents named by this packet for the active milestone.
5. The real rendered application and baseline screenshots for visual work.
6. Charlie's explicit approval or correction of design intent.
7. Historical documents and tags for context only.

When sources conflict:

1. stop before modifying anything;
2. identify which source is newer and relevant to the active area;
3. compare the implementation and rendered result;
4. ask Charlie when approval history remains ambiguous;
5. update this packet so the same ambiguity cannot recur.

Do not reinterpret, remove, or restore work merely because an older document differs.

---

# 2. Repository and Work Locations

## Stable public version

```text
Repository: bins-projects/PrepFlow
Branch: master
Latest verified public commit: 8987fdf  feat: load the 15 missing Pharm drug cards
```

The public version is the stable fallback. Do not modify or publish it during unfinished redesign work unless Charlie explicitly approves a release or merge.

## Active private development work

```text
Repository: bins-projects/prepflow-dev
Branch: docs/continuity-rebuild
```

Protected redesign-canvas checkpoint:

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

Latest completed responsive milestone:

```text
e5ed054  fix: stabilize half-width home composition
```

Latest visual-continuity update before this packet refresh:

```text
0624d32  docs: preserve Pharm sprite proof decisions
```

Frozen pre-rebuild reference:

```text
before-continuity-rebuild-2026-07-20
```

Use the frozen tag for historical context, not as permission to restore superseded behavior.

---

# 3. Supporting Documents and Their Roles

## Permanent architecture

```text
docs/ARCHITECTURE_BIBLE.md
```

Contains durable technical architecture and system boundaries.

## Continuity rebuild plan

```text
docs/CONTINUITY_REBUILD_PLAN.md
```

Contains the phased reconstruction plan and forensic reasoning. It is not the current session handoff.

## Historical detailed checkpoint

```text
docs/SESSION_CHECKPOINT_2026-07-20.md
```

Contains detailed completed work through the browser behavior extractions and later historical notes. Do not use an older “Exact next milestone” from that document when this packet names a newer active milestone.

## Current visual redesign authority

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

This document must be read in full before any visual, responsive, sprite, home-screen, book, button, background, or nurse-character work.

It now records:

- the completed half-width composition milestone;
- the approved pixel-art background direction;
- the transparent-raster sprite production workflow;
- the PNG/WebP/SVG division of responsibility;
- the Pharm-first reusable book-sprite plan;
- the successful real raster-sprite proof inside the live app;
- the decision to remove question totals from closed book covers;
- the warning that the temporary Pharm proof was recovered from a preview and is not final-quality source art;
- the rule against generating or flattening the full PrepFlow scene when working on one isolated asset;
- the dedicated local-server workflow and command-flow preferences;
- the exact next visual milestone.

---

# 4. Current Product and Architecture State

PrepFlow converts deliberately selected educational material into independent validated Packs and provides a browser-centered study application that uses those Packs.

Authoritative product flow:

```text
Chosen educational source
→ extraction adapter
→ cleaner
→ detector
→ parser
→ normalizer
→ validator
→ permanent question identity
→ authoritative Pack
→ browser study application
```

Active browser product:

```text
web/
```

Official starting Packs:

```text
packs/fundamentals.prepflow.json
packs/pharmacy.prepflow.json
packs/medical_surgical.prepflow.json
```

User-facing names:

```text
Fundamentals
Pharm
Medical-Surgical
```

Read exact question counts from the Pack files rather than relying on old documentation.

The legacy Tkinter desktop stack, PyInstaller configuration, old Windows workflow, and obsolete DOCX prototype were intentionally removed during the continuity rebuild. Do not restore them merely because they appear in history.

The browser behavior boundary work and permanent browser question-reference migration were completed on the private branch. The current active work is visual redesign, not another broad behavior extraction.

---

# 5. Current Visual Redesign State

The current home screen is an unfinished visual-development canvas. It is not a completed design and not technical debt to remove casually.

Approved and verified:

- preserve the pixel-art sunset-city background style;
- use the home terminal/launcher as the working canvas;
- the reduced-width launcher and reference panel no longer collide;
- the logo and tagline remain separated at reduced width;
- the environment reaches the bottom of the tested reduced-height viewport;
- full-width rendering was checked after the half-width change and was not regressed;
- use transparent raster sprites for principal illustrated books and characters;
- use PNG during design and iteration;
- optimized transparent WebP may be used after approval when fidelity is preserved;
- reserve SVG for clean vector-like symbols and interface icons;
- use CSS for placement, responsive behavior, movement, glow, and state—not for drawing the principal final book or character artwork;
- use Pharm as the first book-sprite prototype;
- apply the final approved pattern to Fundamentals and Med-Surg only afterward;
- keep changing application data as live HTML;
- do not display total question counts on closed home-screen books;
- show totals inside the opened book/chapter-selection experience instead;
- preserve live chapter-selection status, accessibility, data attributes, and click behavior;
- do not generate, redraw, or flatten the complete PrepFlow scene when working on one isolated asset.

Current approved reference asset:

```text
web/images/pixel-home-stage.webp
```

The background and two nurses are presently baked into that one static image. Do not crop, regenerate, substitute, or replace it casually.

The current CSS-built books and inline SVG emblems are exploratory placeholders. Their temporary vertical titles remain imperfect and should not receive more polish before sprite replacement.

A real transparent-raster Pharm book proof was successfully rendered inside the app. It proved the intended technical approach, but it was recovered from a prior preview, still contained a baked-in `1,238 QUESTIONS`, and is not the final source sprite. Temporary preview files were removed afterward. The last verified local state was clean and synchronized.

---

# 6. Required Startup Procedure

Before giving Charlie any modifying command in a new PrepFlow session:

1. Read this entire `docs/RESTART_PACKET.md` from the private repository.
2. Read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` in full for the current milestone.
3. Identify the stable public repository and active private repository named here.
4. Inspect the active private branch and latest commit.
5. Inspect local `git status --short --branch` before assuming local matches GitHub.
6. Determine whether local commits or uncommitted files exist.
7. Inspect committed files through GitHub before asking Charlie to paste their contents.
8. For visual work, run the actual local application unchanged and inspect a fresh baseline screenshot.
9. Compare the packet, Git state, visual document, rendered result, and Charlie's approval history.
10. State clearly before changing anything:
   - where the stable version lives;
   - where active work lives;
   - the current branch;
   - the protected checkpoint;
   - what is approved;
   - what is unfinished;
   - the single next focused action.
11. Resolve contradictions before recommending a modifying command.

GitHub-first rule:

Before asking Charlie to paste committed code, inspect the connected private repository. Request terminal output only for local state, runtime behavior, tests, ignored/generated artifacts, environment-specific behavior, or exact synchronization checks.

For visual work, GitHub inspection is necessary but not sufficient. The real browser rendering and baseline screenshot are part of the source of truth.

---

# 7. Local Browser Preview Workflow

Use a dedicated terminal for the Python server:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Leave that terminal running during previews.

Open:

```text
http://localhost:8004/web/
```

Use `Ctrl+Shift+R` for a hard refresh after visual changes.

The Python-server terminal printing request logs during refresh is normal.

Before blaming the service worker or CSS cascade, verify that port `8004` is actually running and serving the current `~/projects/prepflow` files. The current service worker uses a network-first fetch strategy.

---

# 8. Required Working Discipline

Standard loop:

```text
Observe
→ inspect committed code
→ inspect local status
→ run the real product unchanged when relevant
→ identify one focused change
→ implement
→ run targeted verification
→ inspect the real output
→ commit
→ push the intended private branch
→ verify hashes
→ update continuity documents
→ repeat
```

Permanent rules:

- one focused change at a time;
- do not ask for code already available through GitHub;
- do not make broad cleanup changes during visual iteration;
- do not manually repair generated Packs when the generic pipeline should be fixed;
- quarantine a small number of malformed source questions rather than broadening parser behavior recklessly;
- never claim a test, push, merge, runtime result, preview, cleanup, server state, or visual approval that was not verified;
- protect privacy before public release or sharing;
- when Charlie says `next`, treat the previous paste command as completed and provide the next executable step;
- do not repeat the previous command after `next`;
- when output is required, say clearly: `Paste the output here before continuing.`;
- for ordinary Bash commands, say only `Paste this`;
- identify the Python-server terminal only when the command must run there;
- stop and reassess when troubleshooting becomes repetitive rather than stacking additional guesses;
- do not generate the complete scene when the task concerns one isolated sprite or graphic element.

When work becomes repetitive, uncertain, or context-heavy:

1. stop changing files;
2. return to this packet and the active supporting document;
3. identify the unresolved decision;
4. inspect the smallest relevant evidence;
5. update continuity before starting a new chat.

---

# 9. Required End-of-Session Procedure

Before ending a substantial PrepFlow session:

1. Inspect `git status` and identify every changed or untracked file.
2. Ensure intended work is committed, or explicitly document why it remains uncommitted.
3. Run applicable tests and real-browser checks.
4. Push the active private branch when the milestone or checkpoint should be backed up.
5. Verify local and private remote hashes match.
6. Update the detailed supporting document for the active milestone.
7. Update this Restart Packet with current branch, latest commit, completed work, unfinished work, exact next step, and required supporting documents.
8. Replace stale current-state wording rather than stacking contradictory temporary handoffs.
9. Confirm that a fresh chat can orient itself from this packet without relying on conversational memory.
10. Push the documentation update and verify the private remote hash.

---

# 10. Verification and Rollback Rules

Every milestone must answer:

1. What exact behavior or visual element is changing?
2. What must remain unchanged?
3. Which automated or manual checks protect it?
4. What real-browser check is required?
5. What commit is the rollback point?
6. Which remotes should be synchronized when complete?

Prefer normal corrective or revert commits over casual history rewriting.

Important rollback references:

```text
before-continuity-rebuild-2026-07-20
8987fdf
f393626
e5ed054
```

---

# 11. Current Exact Resume State

Stable public work remains on:

```text
bins-projects/PrepFlow
master
```

Active redesign work remains on:

```text
bins-projects/prepflow-dev
docs/continuity-rebuild
```

Required detailed supporting document:

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

Current unfinished milestone:

> Create or recover a proper transparent Pharm book sprite based on the approved proof direction, remove the baked-in question total, verify the isolated asset before app insertion, then preview only Pharm while preserving live chapter-selection status and click behavior.

Do not begin by regenerating the whole scene, polishing temporary vertical title CSS, redrawing the book with CSS, redesigning all three books, consolidating visual stylesheets, separating the nurses from the background, or merging unfinished redesign work into public `master`.

---

# 12. Exact Next Step

1. Synchronize the local `docs/continuity-rebuild` branch with the latest private documentation commits.
2. Verify local and remote hashes and confirm the working tree is clean.
3. Read this packet and `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` in full.
4. Start the local server in its own terminal and verify `http://localhost:8004/web/` serves the current project.
5. Capture a clean full-width baseline.
6. Prepare the isolated transparent Pharm sprite outside the app first.
7. Verify that it is complete, has usable transparency, contains `PHARM` and the permanent emblem/branding as intended, contains no question total, and includes no background or full-scene content.
8. Inspect the committed Pharm card HTML and click behavior through GitHub.
9. Insert only the Pharm sprite and preserve live selection status, accessibility, data attributes, and click behavior.
10. Use CSS only for scale, placement, interaction, and responsive behavior.
11. Preview at full and reduced width.
12. Obtain Charlie's approval before committing the sprite or applying the pattern to Fundamentals and Med-Surg.

## What Charlie should say in a fresh chat

Use this exact instruction:

> Open the private PrepFlow repo `bins-projects/prepflow-dev` on branch `docs/continuity-rebuild`. Read `docs/RESTART_PACKET.md` first, then read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` in full. Follow their exact resume state before giving me any command.
