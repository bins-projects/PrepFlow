# PREPFLOW ARCHITECTURE BIBLE

> Durable authority for PrepFlow technical architecture. Current branch state, release hashes, temporary milestones, and the next executable task belong in `docs/RESTART_PACKET.md`.

---

# 1. Product Definition

PrepFlow is a browser-centered nursing study system built around cleaned, structured, validated question Packs.

Its permanent flow is:

```text
Chosen educational source
→ extraction
→ cleaning
→ structure detection and parsing
→ normalization and validation
→ permanent question identity
→ authoritative Pack
→ browser study application
```

The browser study experience, medication reference, artwork, and future coaching features consume the structured library. They do not replace the ingestion and Pack architecture.

---

# 2. Authority Model

Material deliberately selected for import becomes authoritative study material inside its own Pack after it passes PrepFlow cleaning, structural validation, and review.

Each Pack is an independent authority boundary. Packs are not silently blended into one universal truth database.

The finished Pack is the permanent study product. Original source files, extraction output, and source-specific contamination are temporary import material and must not become public runtime dependencies.

---

# 3. Core Data Model

## 3.1 Pack

A finished Pack requires:

- permanent Pack ID;
- user-facing title;
- schema or format version when needed;
- questions.

## 3.2 Question

A finished question requires:

- permanent PrepFlow question ID;
- chapter;
- chapter title when useful;
- question type;
- stem;
- choices where applicable;
- correct answer or ordered answers;
- rationale.

Optional enrichment may include concepts, medication classes, body systems, relationships, or study tags. Publisher, edition, page, Bloom level, and detailed source provenance are not required in the finished study record.

---

# 4. Permanent Question Identity

Question identity must not depend on array position, display order, chapter order, or neighboring questions.

Permanent identity must support:

- Pack rebuilds;
- saved sessions;
- corrections;
- duplicate detection;
- future analytics;
- stable references across versions.

The identity algorithm may evolve, but the same question should retain its identity across reorder and rebuild. Genuinely new content receives a new identity.

---

# 5. Ingestion Architecture

## 5.1 Source adapters

A source adapter opens one file format and returns usable text or a neutral extraction structure.

Different formats must feed one shared cleaning, detection, parsing, normalization, validation, and Pack-building pipeline. Do not build a separate compiler architecture for every source format.

## 5.2 Cleaning

Cleaning removes non-educational noise while preserving educational meaning. It may remove proven download-site contamination, repeated headers, footers, branding, broken extraction artifacts, and duplicated source blocks.

Cleaning must not casually rewrite stems, choices, answers, or rationales.

## 5.3 Detection and parsing

Detection reports source structure and uncertainty. Parsing converts cleaned source material into candidate questions and may recover chapters, wrapped stems, choices, answers, rationales, and supported question types.

Parsing does not define user-interface behavior or permanent identity.

## 5.4 Normalization and validation

Normalization converts supported parser output into one consistent compiler shape. It must not become a second parser or invent educational content.

Validation decides whether candidate records are structurally safe to admit.

Severity model:

- **Fatal:** the Pack cannot safely be built.
- **Recoverable:** the affected question is quarantined or skipped while valid questions proceed.
- **Advisory:** the concern is recorded but the question remains eligible.

Validation protects structural usability. It does not independently certify universal medical truth.

## 5.5 Deduplication

Only genuine exact duplicates should be removed automatically. Near-duplicates remain unless deliberately reviewed because similar questions may test different judgments or provide useful repetition.

## 5.6 Pack compilation

The compiler receives normalized validated candidates, preserves or assigns permanent IDs, builds the Pack, and exports only fields PrepFlow intentionally needs.

---

# 6. Pack Library

The permanent hierarchy is:

```text
Pack
└── Chapter
    └── Question
```

Each Pack is independently removable and rebuildable. The browser consumes finished Packs only; it does not parse private source files or repair malformed Pack content during a quiz.

---

# 7. Browser Study Architecture

The browser is the active compatibility target.

## 7.1 Quiz behavior layer

Quiz behavior owns rules that must remain stable across visual redesign:

- collect the selected question pool;
- support selected chapters across Packs;
- establish a stable session order;
- use configurable block sizes;
- present one question at a time;
- grade by question type;
- track first-pass results;
- review missed questions until mastered;
- transition between blocks;
- preserve save and resume meaning;
- display final first-pass results.

Quiz behavior should be testable without depending on a particular screen layout or DOM structure.

## 7.2 Browser GUI

The GUI displays state and collects user input. It owns:

- the hospital homepage;
- launcher controls;
- the dedicated quiz-builder screen;
- subject-book buttons;
- chapter selectors;
- quiz settings;
- answer controls;
- rationale presentation;
- progress and summary screens;
- medication-reference navigation;
- responsive presentation;
- accessibility presentation.

The GUI must not independently invent scoring, review, or session rules.

## 7.3 Save and resume

Saved state belongs to the browser study system and should preserve:

- selected question set;
- established question order;
- current position;
- block state and block number;
- first-pass score;
- missed questions;
- review queue;
- active screen or state.

The storage mechanism may evolve, but the behavioral meaning must remain stable.

## 7.4 Question types

The intended browser system supports:

- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response.

A valid Pack question type must not require revival of a separate legacy client.

---

# 8. Current Homepage Composition Architecture

The active homepage uses a locked 16:9 PrepFlow Teaching Hospital exterior composition.

The runtime composition separates static environmental art from live application state:

- the hospital exterior and architectural signs are static artwork;
- the left sign hosts live new-quiz and saved-session controls;
- the right sign hosts the live Drug Library control;
- the title and tagline are live HTML/CSS and are replaceable;
- the three subject books are separate transparent clickable assets inside the dedicated quiz builder;
- chapter state, quiz settings, progress, hit areas, and accessibility labels remain browser-owned.

The browser must preserve a clear distinction between permanent visual identity and changing application data.

## 8.1 Static artwork

Static artwork may own:

- environment;
- architecture;
- permanent architectural sign labels;
- material rendering;
- sunset and environmental lighting;
- noninteractive scenery.

Static artwork must not own:

- quiz status;
- progress;
- selected chapter counts;
- live command text;
- saved-session information;
- accessibility labels;
- click behavior.

## 8.2 Book assets

The three subject books remain separate transparent assets. They own permanent subject identity, cover artwork, icons, pages, spine, tabs, and permanent branding.

They must not contain changing totals, selection state, Pack paths, accessibility text, or interaction behavior.

## 8.3 Nurses and characters

No nurse sprite system is currently implemented in the hospital-homepage architecture.

Future characters may use reusable transparent assets when a specific screen or interaction justifies them. Older city-and-nurses plans are historical context, not an active architectural requirement.

## 8.4 HTML and JavaScript

HTML and JavaScript own:

- live launcher structure;
- quiz-builder structure;
- subject buttons and Pack paths;
- accessibility labels;
- selected chapter state;
- saved-session state;
- click and navigation behavior;
- enabled and disabled behavior;
- quiz and progress data.

## 8.5 CSS

CSS owns:

- placement and display size;
- responsive composition;
- scene-relative alignment;
- hover, focus, pressed, and disabled presentation;
- live glow and command animation;
- temporary title and tagline presentation.

CSS must not redraw principal final artwork with substitute gradients or pseudo-element illustrations.

---

# 9. Visual Cleanup and Change Control

Exploratory CSS may accumulate during visual iteration, but temporary override stacks must not become permanent architecture merely because they work.

Cleanup is an integral part of a visual milestone.

A structural cleanup must:

1. begin from a recoverable external backup;
2. preserve the approved rendered appearance and behavior;
3. retain active states, hit areas, and accessibility behavior;
4. be tested in the real browser;
5. run applicable automated tests;
6. inspect the focused diff;
7. be committed separately from unrelated feature work.

When immediate cleanup would place an approved milestone at high risk, preserve and verify the working state, document the debt explicitly, and schedule a protected cleanup milestone. Deferral does not convert the debt into approved permanent architecture.

Detailed visual rules belong in `docs/ART_SYSTEM.md`.

---

# 10. Offline Architecture

The service worker defines the browser application's offline promise.

The offline contract must be explicit: either the complete installed product is available on first offline use, or a narrower promise is documented and tested.

Shell files, Packs, scripts, styles, visual assets, and medication-reference data must not be assumed available offline merely because some were loaded previously.

---

# 11. Medication Reference

Medication reference is a separate library feature. It may use Pack relationships but should not be permanently gated by the Pharm Pack.

Long-term direction:

- stable independent medication records;
- mappings to Pharm, Med-Surg, Fundamentals, and future Packs;
- optional study and coaching relationships;
- no requirement that a valid medication exist in Pharm before it can exist in the reference library.

---

# 12. Testing and Verification

Tests protect active PrepFlow behavior, not obsolete implementations.

Required direction:

- maintain strong ingestion and compiler tests;
- maintain browser-centered tests for quiz behavior;
- validate Pack structure and identity rules;
- verify the real browser experience where automation is not practical;
- require passing tests and visual verification before release promotion.

Deleting old tests is safe only after equivalent active-product behavior is protected or deliberately rejected.

---

# 13. Legacy Code Policy

Unreleased desktop and terminal compatibility has no architectural authority.

Preserve valuable capabilities and behavior, not obsolete implementations.

The old Tkinter client, terminal client, PyInstaller pathway, desktop update system, and rigid DOCX prototype must not be restored merely because they exist in history.

Future DOCX support should be a source adapter feeding the shared ingestion pipeline.

---

# 14. Future Downloadable Applications

A future Windows or macOS application should package the cleaned browser-centered product rather than revive a separate study engine.

Platform packaging may differ, but Pack meaning, question identity, quiz rules, grading, scoring, review behavior, and save-state meaning must remain shared.

---

# 15. Repository and Release Boundaries

Permanent repository areas include:

- active compiler and ingestion code;
- finished Packs;
- browser application code and approved runtime assets;
- tests protecting active behavior;
- durable documentation.

The repository must not contain private source books, personal identifying information, scratch extraction files, generated release archives, obsolete temporary Packs, duplicate runtime assets, or one-time scripts that belong in the shared pipeline.

Release preservation is governed by:

```text
docs/RELEASE_PRESERVATION_POLICY.md
```

Use three protected states:

1. local active development;
2. synchronized remote development checkpoint;
3. frozen public release branch and tag.

Never force-push public `master`, frozen release branches, or release tags.

---

# 16. Architectural Principles

1. PrepFlow is a cleaning, structuring, and Pack-building system first.
2. Packs are independent authority boundaries.
3. The finished Pack is the permanent study product.
4. Question identity remains stable across reorder and rebuild.
5. Source formats share one ingestion pipeline after extraction.
6. Cleaning preserves educational meaning.
7. Detection exposes uncertainty.
8. Parsing recovers structure but does not control the GUI.
9. Validation protects structural usability, not universal medical truth.
10. Only genuine exact duplicates are removed automatically.
11. The browser is the active compatibility target.
12. Quiz behavior and GUI presentation have separate responsibilities.
13. Permanent artwork and changing application state have separate owners.
14. Cleanup is part of every substantial implementation milestone.
15. Legacy implementations may be removed when active value is absent.
16. Future downloads reuse the browser-centered product.
17. One focused change, test, verify, document, commit, and repeat.
18. Approved releases remain recoverable through frozen branches and tags.

---

# 17. Change Control

Update this document only when durable architecture changes.

Do not place current branch hashes, temporary milestone status, or the next executable task here. Those belong in `docs/RESTART_PACKET.md`.

Historical reasoning remains available in Git history, `docs/CONTINUITY_REBUILD_PLAN.md`, and the frozen continuity baseline.