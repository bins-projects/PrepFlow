# PREPFLOW CONTINUITY REBUILD DECISION MAP

> Historical migration map rebuilt after the July 2026 forensic review. The active session state belongs in `docs/RESTART_PACKET.md`; durable architecture belongs in `docs/ARCHITECTURE_BIBLE.md`; visual rules belong in `docs/ART_SYSTEM.md`; release protection belongs in `docs/RELEASE_PRESERVATION_POLICY.md`.

## Purpose

This document connects:

1. what the repository contains;
2. what PrepFlow is intended to become;
3. how to move from the current implementation toward the approved architecture without losing working behavior.

It is a migration map, not a daily task list. No implementation should be deleted or substantially reorganized until its behavior, verification gate, and rollback path are understood.

---

# 1. Product Definition

PrepFlow is primarily a document-ingestion, sanitization, structuring, and study-library system.

Its defining purpose is:

> Take deliberately chosen educational material, clean and organize it, turn it into an authoritative independent PrepFlow Pack, and provide study tools that use that Pack.

The permanent flow is:

```text
Chosen educational source
        ↓
Source extraction
        ↓
Cleaning and sanitization
        ↓
Structure detection and parsing
        ↓
Normalization and validation
        ↓
Permanent PrepFlow question identity
        ↓
Independent authoritative Pack
        ↓
Browser study application
```

The visible quiz, hospital homepage, book interface, Drug Library, and future coaching features are ways of using the structured library. They are important product experiences, but they are not the underlying core.

---

# 2. Authority Model

PrepFlow does not independently fact-check an entire nursing curriculum before admitting material.

Approved rule:

> Material deliberately selected for import becomes authoritative study material inside its own Pack after it passes PrepFlow's cleaning, structural validation, and review process.

Each Pack remains its own authority boundary.

This means:

- sources are not silently blended into one universal truth database;
- chapter organization may follow the selected source;
- a contaminated, obsolete, or unwanted Pack can be deleted or rebuilt as a unit;
- the finished Pack is the study authority;
- the original source is temporary import material.

---

# 3. Canonical Study Record

A finished Pack requires:

- permanent Pack ID;
- user-facing title;
- format or schema version as needed;
- questions.

A finished question requires:

- permanent PrepFlow question ID;
- chapter;
- chapter title when useful;
- question type;
- stem;
- choices where applicable;
- correct answer or ordered answers;
- rationale.

Optional future enrichment may include concepts, medication classes, body systems, clinical relationships, and study tags. Optional enrichment must not block ordinary import.

Publisher, edition, page, Bloom level, difficulty, and detailed source provenance are not required in the finished study record.

---

# 4. Permanent Question Identity

Question identity must not depend on array position, display order, or neighboring questions.

Approved rule:

> A question receives a permanent PrepFlow identity that does not change merely because its display order, chapter position, or surrounding questions change.

Permanent identity supports:

- Pack rebuilds;
- saved sessions;
- corrections;
- duplicate detection;
- future analytics;
- medication or concept relationships;
- stable references across versions.

The implementation must eventually preserve existing IDs for unchanged questions and create new IDs only for genuinely new content.

---

# 5. Responsibility Map

## 5.1 Source adapters

Source adapters open a file format and return usable text or a neutral extraction structure.

Different source formats must feed one shared cleaning, detection, parsing, normalization, validation, and Pack-building pipeline.

Future DOCX, TXT, HTML, or OCR work must not create separate competing question engines.

## 5.2 Cleaner

The cleaner removes non-educational noise while preserving educational meaning.

It may remove:

- download-site contamination;
- repeated branding;
- page headers and footers;
- extraction artifacts;
- duplicated source blocks;
- narrowly evidenced source-specific noise.

It must not casually rewrite stems, choices, answers, or rationales.

## 5.3 Detector

Detection measures and reports source structure before parsing. It exposes uncertainty rather than hiding it.

## 5.4 Parser

The parser turns cleaned text into candidate question records. It owns recognition of chapter, question type, wrapped stems, choices, answers, rationales, and supported source structures.

It does not assign final permanent identity and does not control the GUI.

## 5.5 Normalizer

The normalizer converts supported parser output into one consistent compiler input shape. It must not become a second parser or invent educational content.

## 5.6 Validator

Validation decides whether candidate records are structurally safe to admit.

Severity model:

- **Fatal:** the Pack cannot safely be built.
- **Recoverable:** the affected question is quarantined or skipped while valid questions may proceed.
- **Advisory:** a concern is recorded but the question remains eligible.

Validation protects structural usability, not universal medical truth.

## 5.7 Deduplication

Only genuine exact duplicates should be removed automatically. Near-duplicates remain unless deliberately reviewed.

## 5.8 Pack compiler and library

The compiler receives normalized validated records, preserves or assigns permanent IDs, and builds the finished Pack.

The browser consumes finished Packs only. It does not parse private source files or repair malformed Pack content during a quiz.

## 5.9 Browser quiz behavior

The quiz behavior layer owns rules that must remain stable regardless of visual redesign:

- selected question pool;
- selected chapters across Packs;
- question order;
- block size;
- one question at a time;
- grading by question type;
- first-pass correct and missed tracking;
- review until mastered;
- block transitions;
- final first-pass result;
- save and resume meaning.

Behavior should become testable without depending on a specific screen layout or DOM structure.

## 5.10 Browser GUI

The GUI displays state and collects input. It owns the hospital homepage, quiz builder, books, chapter controls, answer controls, rationale presentation, results screens, responsive layout, and accessibility presentation.

The GUI must not independently invent scoring, review, or session rules.

---

# 6. Confirmed Current Implementation

## 6.1 Active compiler core

The active Python value remains the shared ingestion and compiler pipeline under `compiler/`.

Core responsibilities include importing, extracting, cleaning, detecting, parsing, normalizing, validating, building, exporting, identity, and diagnostics.

## 6.2 Active browser product

The active user-facing product is under:

```text
web/
```

The current browser provides:

- Pack loading;
- chapter selection across the three official Packs;
- question aggregation;
- block sessions;
- Multiple Choice and Multiple Response grading;
- first-pass tracking;
- review until mastered;
- save and resume;
- block summaries;
- hosted/PWA use;
- Drug Library access;
- the PrepFlow Teaching Hospital homepage;
- a dedicated quiz-builder flow.

Current hospital runtime files include:

```text
web/index.html
web/app.js
web/hospital-home.css
web/quiz-builder-screen.css
web/resume-rules.js
web/images/home-hospital/prepflow-home-background-final.png
```

The current homepage composition includes:

- a locked 16:9 hospital exterior;
- static architectural quiz and reference sign housings in the composite artwork;
- live browser-owned launcher text, state, hit areas, and actions;
- the three approved subject books inside the quiz builder;
- temporary live branding: `PrepFlow` and `Prepare. Practice. Progress.`;
- saved-session text using `Block X of Y`;
- Continue Quiz, Build a New Quiz, Build Your Quiz, and Drug Library controls.

No nurse sprites, nurse animation, or nurse-separation milestone has been implemented in the hospital homepage.

## 6.3 Current browser gaps

Known architectural or product gaps include:

- Completion and Ordered Response are not yet fully supported in the active quiz flow;
- shuffle behavior is not yet an explicit user choice;
- quiz rules and DOM control remain mixed in `web/app.js`;
- browser-level automated coverage remains limited;
- the offline contract is not yet fully explicit;
- the inner quiz-builder visual system still needs later refinement;
- permanent logo treatment remains deferred.

## 6.4 Pack library

The permanent tracked library contains:

- Fundamentals;
- Pharm;
- Medical-Surgical.

Exact counts must be read from the Pack files rather than copied from stale documentation.

## 6.5 Medication reference

The medication reference remains a separate browser feature. Long-term work may decouple master medication records from the Pharm-derived registry, but that is not part of the hospital-homepage release milestone.

## 6.6 Visual system

The active visual language is **PrepFlow Illustrated Pixel**.

The current hospital scene uses:

- cinematic modern illustrated pixel art;
- readable broad light and shadow masses;
- warm amber highlights;
- cool blue-purple dusk shadows;
- dark palette-related outlines;
- controlled architectural texture;
- static environment artwork separated from live application state.

The complete durable visual rules are in `docs/ART_SYSTEM.md`.

---

# 7. Current Cleanup Requirement

`web/hospital-home.css` contains a large layered override stack accumulated during iterative visual work.

Verified current state:

- 1,860 lines;
- balanced braces;
- balanced comments;
- no terminal-paste artifacts found;
- all 72 automated tests passed;
- real-browser interaction and visual checks passed.

Cleanup is integral to the process, not optional polish.

A protected consolidation milestone must:

1. begin from an external backup;
2. preserve the approved visual result;
3. consolidate duplicate and competing rules carefully;
4. verify unsaved and saved launcher states;
5. verify Drug Library placement and hit area;
6. verify command pulsing and temporary branding;
7. verify normal and fullscreen display;
8. run automated tests;
9. inspect the focused diff;
10. commit cleanup separately from feature work.

Do not perform a broad redesign while consolidating the stylesheet.

---

# 8. Repository and Artifact Boundaries

Approved boundary:

```text
Private chosen sources      → outside repository
Temporary import artifacts  → output/
Experiments                  → scratch/ or external backup
Approved source/review art   → art/source/ or art/review/
Finished authoritative data → packs/
Runtime browser assets       → web/images/
Product code and docs        → tracked
```

Before release, classify all untracked hospital artwork deliberately. Do not use `git add .`.

The tracked runtime hospital composite is:

```text
web/images/home-hospital/prepflow-home-background-final.png
```

Duplicate runtime copies, screenshots, transfer files, temporary proofs, and backup archives must not enter production commits.

---

# 9. Testing and Verification Strategy

Every structural or release step must define:

- behavior being protected;
- targeted tests;
- full test-suite result;
- browser smoke checks;
- visual-state checks when applicable;
- Pack validation checks when applicable;
- rollback commit or release boundary;
- remote synchronization status.

A smaller test count after deleting tests is not success unless the removed coverage has been replaced or deliberately declared obsolete.

The long-term direction is automatic verification on pushes and pull requests, independent of legacy desktop packaging.

---

# 10. Current Finishing and Release Sequence

The immediate migration priority is no longer the old city-and-nurse plan.

Current sequence:

## Stage A — Documentation baseline

- keep `RESTART_PACKET.md`, `ART_SYSTEM.md`, and `ARCHITECTURE_BIBLE.md` aligned with the hospital implementation;
- update this decision map;
- update README and changelog;
- mark dated city-and-nurse continuity as historical;
- review the hospital layered-workflow brief;
- document release preservation and rollback.

## Stage B — Asset classification

- inspect all untracked hospital artwork;
- retain only useful source or review assets;
- exclude duplicate runtime copies and temporary proofs;
- stage files intentionally.

## Stage C — Protected CSS consolidation

- create or verify the external backup;
- consolidate `web/hospital-home.css` without changing approved behavior;
- test all launcher states and browser modes;
- run the full automated suite;
- commit cleanup independently.

## Stage D — Final milestone verification

- run automated tests;
- perform the complete browser smoke test;
- verify no private or temporary artifacts are tracked;
- inspect the exact release diff;
- synchronize both development remotes and compare hashes.

## Stage E — Frozen hospital release

- create a uniquely named fixed release branch from the approved commit;
- create a release tag only after the release identity is deliberately chosen;
- open a pull request into public `master`;
- inspect the exact release scope;
- merge without rewriting prior release history;
- verify GitHub Pages;
- preserve the previous release until the new deployment is confirmed;
- record the final release boundary.

---

# 11. Later Architectural Sequence

After the hospital milestone is safely released, later work may proceed in focused stages:

1. strengthen browser behavior tests;
2. design and migrate permanent question identity;
3. separate quiz rules from DOM operations;
4. add Shuffle Questions and Keep Source Order choice;
5. add Completion and Ordered Response support;
6. remove verified legacy desktop and terminal pathways after equivalent behavior is protected;
7. remove the obsolete DOCX prototype route;
8. improve compiler quarantine and exact-duplicate handling;
9. define and test the offline contract;
10. refine the inner quiz-builder visual system;
11. add source adapters only from real use cases;
12. enrich medication and analytics features later;
13. evaluate browser-centered Windows and macOS wrappers later.

This sequence may change when evidence changes, but broad rewrites remain prohibited.

---

# 12. Deferred Feature Backlog

Deferred items include:

- permanent logo and branding treatment;
- inner quiz-builder visual rebuild;
- nurse characters or nurse animation;
- character-led coaching;
- cut scenes;
- multi-frame book-opening animation;
- DOCX and TXT adapters;
- OCR ingestion;
- complete first-install offline support;
- independent medication master library;
- richer concepts and analytics;
- downloadable Windows and macOS wrappers.

Deferred does not mean rejected. It means these items must not interrupt the current stabilization and release sequence.

---

# 13. Rejected or Superseded Directions

The following directions are rejected or superseded:

- preserving unreleased desktop compatibility as an architectural constraint;
- maintaining separate desktop and browser quiz engines indefinitely;
- keeping old code only because it may be useful someday;
- requiring detailed publisher and page provenance in every finished question;
- automatically deleting near-duplicate questions;
- building a separate parser for every book;
- starting with a broad rewrite;
- treating the old city-and-nurses homepage as the active visual target;
- starting nurse-sprite work merely because dated documentation once listed it next;
- flattening live application state into the hospital artwork;
- making exploratory CSS override stacks permanent without consolidation;
- force-pushing public master, frozen release branches, or release tags.

---

# 14. Release Preservation

The durable release policy is:

```text
docs/RELEASE_PRESERVATION_POLICY.md
```

Every major public update must preserve:

1. the active local development state;
2. a synchronized private and public-mirror development checkpoint;
3. a frozen release branch and tag for the approved public release.

The previous public release remains preserved until the replacement deployment is verified.

---

# 15. Change Control

Update this plan when the migration sequence, major cleanup boundary, or release strategy changes.

Do not place the next terminal command or transient branch hash here. Those belong in `docs/RESTART_PACKET.md`.

Historical evidence remains available in Git history, dated continuity documents, and the frozen tag `before-continuity-rebuild-2026-07-20`.
