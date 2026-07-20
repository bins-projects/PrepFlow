# PREPFLOW RESTART PACKET

> **Continuity note:** This Restart Packet was rebuilt after the July 2026 forensic architecture review. Earlier versions are preserved in Git history and in the frozen tag `before-continuity-rebuild-2026-07-20`. If a decision or omitted pathway seems unclear, inspect that preserved baseline before assuming information was accidentally lost. Historical documents explain how PrepFlow arrived here; this packet records the approved operating state from this point forward.
>
> Do not restore legacy behavior merely because it appears in an older document. The current Architecture Bible and this Restart Packet are the active authorities unless Charlie deliberately changes a decision.

## Purpose

This document is the operational handoff for resuming PrepFlow development.

It must answer:

1. What is PrepFlow?
2. What currently exists?
3. What architecture has been approved?
4. What is being kept, replaced, or removed?
5. What is the migration order?
6. What has already been completed?
7. What is the next safe step?
8. How is each step verified?
9. What is deferred?
10. How can work stop safely and resume later?

Permanent architectural truth belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

The full forensic findings, file classifications, and migration reasoning belong in:

```text
docs/CONTINUITY_REBUILD_DECISION_MAP.md
```

This packet should remain current and operational. It must not grow into another chronological diary of every completed session.

---

# 1. Source of Truth

## Repositories

```text
Private development repository:
bins-projects/prepflow-dev

Public repository:
bins-projects/PrepFlow
```

The private repository is the working source of truth during the continuity rebuild.

## Current development branch

```text
docs/continuity-rebuild
```

The branch was created from:

```text
8987fdf
```

Frozen pre-rebuild reference:

```text
before-continuity-rebuild-2026-07-20
```

That tag preserves the complete repository state before the continuity documentation rewrite.

## Documentation commits completed on this branch

```text
97b5fbb  docs: add continuity rebuild decision map
a49ea78  docs: rebuild architecture bible
```

The commit that replaces this Restart Packet follows those commits.

## GitHub-first rule

Before asking Charlie to paste committed code, repository trees, documentation, branches, or file contents, inspect GitHub first.

Request local terminal output only when it is needed for:

- uncommitted work;
- runtime behavior;
- local test execution;
- ignored/generated artifacts;
- private source material;
- environment-specific behavior;
- exact local and remote synchronization checks.

---

# 2. Current Product Definition

PrepFlow takes deliberately selected educational material, cleans and structures it, turns it into an authoritative independent Pack, and provides study tools that use that Pack.

The core flow is:

```text
Chosen source material
        ↓
Source adapter / extraction
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

The browser quiz, open-book interface, medication reference, characters, animations, and future coaching are ways of using the library. They are not separate educational architectures.

---

# 3. Authority and Content Rules

## Pack authority

A deliberately selected source becomes authoritative study material inside its own Pack after cleaning, structural validation, and review.

PrepFlow does not independently fact-check an entire nursing curriculum before content enters a Pack.

Each Pack is an independent authority boundary:

- sources are not silently reconciled into one universal truth database;
- one Pack can be removed or rebuilt without changing another;
- the original source is temporary import material;
- the finished Pack is the durable study product.

## Required Pack structure

```text
Pack
└── Chapter
    └── Question
```

Required question content:

- permanent PrepFlow question ID;
- chapter;
- chapter title when useful;
- question type;
- stem;
- choices when applicable;
- correct answer or ordered answers;
- rationale.

Publisher, edition, page, Bloom level, difficulty, and detailed source-provenance fields are not required merely because older models supported them.

Optional future tags may support concepts, medications, body systems, relationships, or coaching. They must not block ordinary imports.

## Source fidelity

- Preserve admitted educational content faithfully.
- Do not casually rewrite stems, choices, answers, or rationales.
- Remove contamination, branding, headers, footers, and extraction artifacts through the cleaner.
- Do not expose internal Pack filenames, IDs, JSON, compiler terms, or repository terminology in the user interface.

---

# 4. Approved Responsibility Map

## Source adapters

Open supported file formats and return usable text or a neutral extraction structure.

Current authoritative adapter:

- text-based PDF.

Future adapters:

- DOCX;
- TXT;
- possible HTML;
- OCR only as a separate later project.

All adapters must feed the same shared pipeline. Do not build separate question-processing systems for each file type.

## Extraction

Retrieves source content while preserving enough structure for later stages. It does not decide what is a question, answer, rationale, or contamination.

## Cleaner

Removes source noise and extraction artifacts while preserving educational meaning.

## Detector

Measures source structure and exposes uncertainty before parsing.

## Parser

Converts cleaned text into candidate question records and handles structures proven through real imports.

## Normalizer

Converts parser output into one consistent compiler input shape.

## Validator

Classifies problems as:

- fatal;
- recoverable;
- advisory.

The validator checks structural safety. It does not certify medical truth.

## Deduplication

Automatically remove only genuine exact duplicates. Keep near-duplicates because they may test different judgments or provide useful context-specific repetition.

## Pack compiler

Preserves or assigns permanent question identities, builds the Pack, and exports only intentionally retained fields.

## Pack library

Stores approved study content and is the permanent output of ingestion.

## Browser quiz behavior layer

Owns:

- selected question pool;
- cross-Pack chapter selection;
- Shuffle or Keep Source Order;
- stable session order;
- block size;
- grading;
- first-pass tracking;
- missed-question review until mastered;
- block transitions;
- final first-pass result;
- save/resume state meaning.

## Browser GUI

Owns display, controls, layout, animation, responsive behavior, and accessibility presentation. It must not independently invent scoring or session rules.

## Offline layer

Defines the actual offline promise and caches the files required to satisfy it.

## Future downloadable clients

Future Windows or macOS downloads should most likely package the cleaned browser-centered application. There is no requirement to preserve unreleased Tkinter compatibility.

---

# 5. Confirmed Current Implementation

## Active compiler pipeline

Core files include:

```text
compiler/importer.py
compiler/pdf_reader.py
compiler/cleaner.py
compiler/detector.py
compiler/source_parser.py
compiler/normalizer.py
compiler/validator.py
compiler/builder.py
compiler/exporter.py
compiler/pipeline.py
compiler/models.py
compiler/ids.py
compiler/diagnostics.py
```

Current authoritative flow:

```text
PDF
→ extraction
→ cleaner
→ detector
→ source parser
→ normalizer
→ validator
→ builder
→ exporter
→ Pack JSON
```

## Active browser product

The active user-facing product is under:

```text
web/
```

Confirmed browser capabilities include:

- Pack loading;
- chapter selection across Packs;
- full selected question pool;
- one-time shuffle;
- configurable blocks;
- one question at a time;
- Multiple Choice grading;
- Multiple Response exact-set grading;
- first-pass score tracking;
- missed-question review until mastered;
- final first-pass result;
- local save/resume;
- hosted/PWA use;
- layered arcade/open-book presentation;
- medication reference features.

Confirmed browser gaps from the audit:

- Completion and Ordered Response are not reliably part of the active browser quiz path inspected during the audit;
- shuffle cannot be disabled;
- quiz rules and DOM manipulation are mixed in `web/app.js`;
- strong browser-level automated coverage is missing;
- complete first-install offline support is not clearly guaranteed.

When later code or runtime evidence conflicts with this section, inspect the current implementation and update this packet rather than guessing.

## Official starting Packs

The permanent tracked library contains:

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

Read exact current counts directly from the Pack files. Do not copy counts from historical documentation without verification.

## Medication reference

The current medication registry is derived primarily from Pharm appearances and gatekeeps which card records load.

Approved later direction:

- independent master medication records;
- source mappings to Pharm, Med-Surg, Fundamentals, and future Packs;
- a valid medication must not require presence in the Pharm Pack.

This is deferred unless a current defect makes it urgent.

## Visual identity

Preserve the established visual language:

- dark navy foundation;
- bright blue, green, purple, pink, and gold accents;
- 16-bit/pixel styling;
- layered book presentation;
- category accents;
- reusable committed artwork;
- deliberate open-book quiz presentation.

Do not freeze creativity. New work should fit the established product and reuse approved assets where practical.

---

# 6. Permanent Question Identity

Current sequential IDs are formatted consistently but depend on export position. They are not stable enough for the long-term library.

Approved requirement:

> A question's PrepFlow ID must not change merely because questions before it are deleted, inserted, or reordered.

The design must support:

- assigning an identity once;
- recognizing the same question during a rebuild;
- preserving an identity through minor corrections;
- assigning a new identity only to genuinely new content;
- avoiding array-position dependence;
- detecting identity conflicts.

The exact algorithm remains an implementation decision and should be designed before changing Pack IDs.

Do not silently regenerate all IDs without a migration and verification plan.

---

# 7. Verified Legacy and Removal Candidates

Git history and the frozen tag preserve removed work.

## Old DOCX prototype route

Verified candidates:

```text
compiler/docx_reader.py
compiler/tokenizer.py
compiler/parser.py
DOCX-specific route inside compiler/cli.py
tests/test_parser.py
tests/test_ids.py
```

Reason:

- rigid source assumptions;
- separate obsolete path;
- little useful behavior not easily recreated;
- no proper shared cleaner/detector path;
- future DOCX should be an adapter feeding the authoritative pipeline.

## Old Python desktop and terminal study stack

Verified candidates after active browser behavior is protected:

```text
study/cli.py
study/gui.py
study/loader.py
study/question.py
study/review.py
study/save_state.py
study/scoring.py
study/selection.py
study/session.py
study/update_checker.py
study/version.py
PrepFlow.spec
.github/workflows/build-windows.yml
```

Related desktop-only tests may be removed only after retained behavior has equivalent active-product coverage or has been explicitly recorded as no longer required.

Reason:

- the browser is the active compatibility target;
- the browser does not consume this Python study stack;
- no released legacy installation requires preservation;
- future desktop packaging can wrap the browser product;
- preserving capabilities matters more than preserving obsolete implementations.

## Old visual experiment branch

```text
origin/feat/home-quiz-panel-clean
```

This branch contains old cover/stethoscope experiments and should not be merged wholesale. Git history preserves it as reference.

No other unmerged remote branch was found to contain hidden compiler, quiz-engine, medication, or architecture work.

---

# 8. Test and Verification State

The forensic inventory found:

- 18 test files;
- 108 standard function-style tests;
- strong compiler/import coverage;
- useful desktop behavior tests;
- empty `tests/test_ids.py`;
- empty `tests/test_parser.py`;
- no strong visible browser automation suite.

Historical test counts in old documents are not authoritative. Run the current suite and record the result whenever work resumes.

## Important warning

Deleting old tests can reduce the test count while still producing a green result.

Example:

```text
108 passed before deletion
65 passed after deletion
```

That does not prove the product is equally protected. It may mean safeguards disappeared.

Before removing a legacy implementation and its tests:

1. identify the behavior worth retaining;
2. protect it in the active browser or compiler layer where practical;
3. run targeted tests;
4. run the full suite;
5. perform the real browser smoke check;
6. inspect remaining references and imports.

## Planned CI direction

Replace the old manual Windows-build workflow with automatic verification on pushes and pull requests.

Initial CI should:

- install the supported Python environment;
- run the existing compiler tests;
- validate Pack files;
- fail on real structural regressions.

Later add browser checks as the browser behavior layer becomes testable.

---

# 9. Approved Migration Sequence

This is the default sequence. Change it only when implementation evidence shows a safer order.

## Phase A — Documentation foundation

Status: **Active and nearly complete**

1. Complete forensic audit. — Done.
2. Record decision map. — Done at `97b5fbb`.
3. Rebuild Architecture Bible. — Done at `a49ea78`.
4. Rebuild Restart Packet. — This commit.
5. Align README with real browser product.
6. Decide whether `QUESTION_LIFECYCLE.md` has any unique material; absorb useful content and remove the redundant file if appropriate.
7. Review the documentation diff as a unit.

No implementation deletion occurs during Phase A.

## Phase B — Verification foundation

1. Run the full existing test suite and record the current result.
2. Inspect Packs programmatically for schema validity, counts, IDs, types, and duplicate identities.
3. Add automatic push/PR verification using the existing tests.
4. Add the smallest practical browser behavior checks before deleting desktop behavior tests.
5. Write a repeatable browser smoke checklist.

## Phase C — Permanent identity design

1. Inventory current question IDs and references.
2. Choose the permanent identity strategy.
3. Define rebuild matching and conflict behavior.
4. Add tests before migration.
5. Migrate Packs in a controlled commit.
6. Verify save/resume and any reference mappings affected by IDs.

## Phase D — Browser behavior boundary

1. Identify pure quiz/session rules inside `web/app.js`.
2. Extract small testable behavior units without redesigning the GUI.
3. Preserve current working flow after each change.
4. Add the Shuffle versus Keep Source Order option.
5. Preserve source order when shuffle is disabled.

The shuffle setting is the first approved user-facing tweak after stable ground is established.

## Phase E — Browser question-type parity

1. Add Completion grading and controls to the active browser path.
2. Add Ordered Response grading and controls.
3. Preserve first-pass scoring, review behavior, save/resume, and source fidelity.
4. Add browser tests for all supported types.

## Phase F — Legacy removal

After browser behavior protections are adequate:

1. remove the unused Python study/desktop stack;
2. remove `PrepFlow.spec`;
3. remove the old Windows-build workflow;
4. remove obsolete desktop-only tests after retained rules are protected elsewhere;
5. run all tests and browser smoke checks;
6. search for dangling imports and references;
7. commit removal as a focused reversible milestone.

Then remove the rigid DOCX prototype path and its empty tests in a separate focused milestone.

## Phase G — Unified source adapters

1. preserve PDF as the first authoritative adapter;
2. rebuild DOCX as a real extraction adapter;
3. add TXT through the same boundary;
4. route all supported formats through the shared cleaner/detector/parser/compiler;
5. do not create book-specific permanent import architectures.

## Phase H — Offline and visual consolidation

1. define the offline promise;
2. inventory every required shell, Pack, visual, medication, and data asset;
3. update service-worker behavior and tests;
4. consolidate CSS only in visually safe increments;
5. preserve the approved visual identity and reusable art.

## Phase I — Deferred enrichment

Only after the foundation is stable:

- independent medication master library;
- optional topic/system/medication relationship tags;
- analytics and coaching;
- character animation and cut scenes;
- future Windows/macOS browser wrappers;
- user-facing import interface.

---

# 10. Verification and Rollback Rules

Every implementation milestone must answer:

1. What exact behavior is changing?
2. What must remain unchanged?
3. Which tests protect it?
4. What manual browser check is required?
5. What commit is the rollback point?
6. Are private and public remotes synchronized when the milestone is complete?

## Standard work loop

```text
Observe
→ Inspect GitHub
→ Define one focused change
→ Add or update tests when appropriate
→ Implement
→ Run targeted tests
→ Run full tests
→ Run the real browser product
→ Inspect output
→ Commit
→ Push private remote
→ Push public remote when appropriate
→ Verify remote hashes
→ Repeat
```

## Safe stopping rule

Do not stop in the middle of a destructive multi-file transition when practical.

A safe stopping point has:

- a coherent commit;
- passing applicable tests;
- known browser status;
- updated Restart Packet current-focus section when the active plan changed;
- no unexplained uncommitted files;
- exact next action recorded.

## Rollback references

Pre-documentation baseline:

```text
before-continuity-rebuild-2026-07-20
```

Documentation branch start:

```text
8987fdf
```

Never force-reset or rewrite shared history casually. Prefer a normal revert or a new corrective commit unless history rewriting is deliberately required.

---

# 11. Working Discipline

When Charlie says:

> next

provide the next executable step, not a menu of unrelated possibilities.

Other permanent working rules:

- one focused change at a time;
- inspect committed code before speculating;
- do not ask for code already available through GitHub;
- do not manually repair generated Packs when the generic pipeline should be fixed;
- quarantine a small number of malformed questions rather than broadening the parser recklessly;
- do not preserve ghost code merely because it once worked;
- do not delete working protections before replacing or consciously retiring them;
- use evidence from real imports and runtime behavior;
- protect privacy before public release or sharing;
- keep both intended Git remotes synchronized at completed milestones;
- do not claim a push, test, merge, or runtime result that has not been verified.

## Loop-prevention rule

When work becomes repetitive:

1. stop;
2. return to the active phase;
3. identify what decision is actually missing;
4. inspect the smallest relevant files;
5. choose one executable action;
6. test before expanding scope.

---

# 12. Deferred Ideas

These are preserved but are not active commitments:

- optional detailed topic tags;
- coaching based on missed concept clusters;
- independent medication master library and Pack mappings;
- animated character guidance;
- book-opening sequences and cut scenes;
- Windows and macOS packaged browser wrappers;
- user-facing PDF/DOCX/TXT import interface;
- OCR ingestion;
- additional Packs beyond the starting library;
- deeper analytics and adaptive recommendations.

Deferred does not mean rejected. It means do not interrupt the active architectural cleanup unless Charlie deliberately reprioritizes it.

---

# 13. Rejected or Superseded Directions

The following are not active requirements:

- preserving the Tkinter application for compatibility;
- rebuilding desktop parity before improving the browser;
- maintaining separate study engines for each platform;
- keeping the rigid old DOCX parser because it already exists;
- treating publisher/page provenance as required finished-Pack data;
- automatically deleting near-duplicate questions;
- making every optional future tag mandatory for import;
- keeping stale files in active directories merely as historical reference;
- merging `feat/home-quiz-panel-clean` wholesale;
- using test count alone as proof that protections were preserved.

---

# 14. Current Documentation Status

Completed on `docs/continuity-rebuild`:

- forensic audit;
- remote branch audit;
- approved responsibility map;
- approved browser-centered direction;
- approved Pack authority model;
- approved permanent question identity requirement;
- `docs/CONTINUITY_REBUILD_DECISION_MAP.md`;
- rebuilt `docs/ARCHITECTURE_BIBLE.md`;
- rebuilt `docs/RESTART_PACKET.md`.

Still required before implementation cleanup:

1. rewrite `README.md` so it describes the actual browser-centered product without obsolete Windows-release instructions;
2. review `docs/QUESTION_LIFECYCLE.md`, absorb any unique durable rule, and likely remove it as redundant;
3. compare the documentation set for contradictions;
4. inspect the branch diff;
5. run local tests after Charlie pulls the documentation commits;
6. commit any final documentation corrections;
7. merge the continuity documentation only after review.

No implementation files have been intentionally deleted or refactored during the documentation pass.

---

# 15. Exact Next Step

The next documentation action is:

> Rewrite `README.md` as a concise user-facing description of the browser application that only promises workflows currently supported and does not preserve obsolete desktop-download instructions.

After the README, review `QUESTION_LIFECYCLE.md` for absorption/removal.

Do not begin legacy-code deletion before the documentation set is reviewed and the verification foundation is started.

---

# 16. Startup Procedure for a New Session

At the start of the next PrepFlow session:

1. inspect `docs/RESTART_PACKET.md` in the private GitHub repository;
2. inspect the current branch and latest commit;
3. inspect `docs/ARCHITECTURE_BIBLE.md` and `docs/CONTINUITY_REBUILD_DECISION_MAP.md` only as needed;
4. verify whether the working branch is still `docs/continuity-rebuild` or whether the docs were merged;
5. inspect `git status` before giving commands that modify local files;
6. compare local, origin, and public hashes when relevant;
7. run the current test suite before destructive cleanup begins;
8. resume from the Exact Next Step or the newest explicitly recorded active milestone;
9. make one focused change;
10. test and commit before expanding scope.

If the current documents appear incomplete or a decision seems inexplicable, consult:

```text
before-continuity-rebuild-2026-07-20
```

Use that baseline for historical reasoning, not as permission to restore superseded behavior.

---

# 17. Current Resume Statement

> PrepFlow's July 2026 forensic audit is complete. The browser is the only active compatibility target. The authoritative core is the shared ingestion/compiler pipeline, independent Pack library, and browser study application. Packs are separate study-authority boundaries. Permanent question identity is a core requirement and must not depend on array order. The old Tkinter/terminal/PyInstaller stack and rigid DOCX prototype are verified removal candidates after active behavior is protected. The continuity rebuild is occurring on `docs/continuity-rebuild`, created from `8987fdf`, with the full pre-rebuild state preserved by tag `before-continuity-rebuild-2026-07-20`. The detailed decision map and Architecture Bible have been rebuilt. This Restart Packet now replaces the layered legacy handoff. No application code has been removed. The next action is to rewrite the README for the real browser-centered product, then absorb and likely remove the redundant Question Lifecycle document before reviewing the complete documentation diff.
