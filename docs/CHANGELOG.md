# PrepFlow Changelog

This document records major project milestones. Minor edits and intermediate work are preserved in Git history.

## Version 1.0.0 — Desktop Application Proof

Date: 2026-07-12

### Desktop Application

- Added a standalone Tkinter desktop interface around the existing Study Engine.
- Added a PrepFlow home screen with Fundamentals, Pharmacy, and Medical-Surgical.
- Added dynamic Pack discovery and user-facing subject names.
- Added chapter selection with multi-select, Select All, and Clear All.
- Added mixed-chapter study sessions with one shuffle per session.
- Preserved 15-question blocks with correctly sized shorter final blocks.
- Preserved first-pass scoring and missed-question mastery review.
- Added support for Multiple Choice, Multiple Response, Completion, and Ordered Response.
- Added drag-and-drop controls for Ordered Response questions.
- Added scrollable question content with fixed Submit and Continue controls.

### Session Persistence

- Added a single overwriteable local autosave slot.
- Added automatic saving whenever a new question opens.
- Added Continue Saved Quiz to the home screen.
- Preserved shuffled order, current position, score, block state, missed questions, and review state.
- Added a temporary Progress saved notification.
- Added automatic save deletion after session completion.

### Packaging

- Updated the PyInstaller specification to launch the desktop GUI.
- Bundled the three official PrepFlow Packs.
- Successfully built and tested a standalone Linux x86-64 application.
- Verified the packaged application launches without Python or terminal interaction.
- Verified subject selection, chapter selection, quiz flow, autosave, and resume in the packaged build.

### Privacy and Validation

- Verified no personal names, personal email addresses, personal home paths, or recovery-bundle references remain in tracked project files.
- Verified all reachable Git commits use the anonymous PrepFlow Git identity.
- Scanned the packaged Linux release for personal identifying information.
- Confirmed both Git remotes were synchronized at commit `81160bd`.
- Confirmed the working tree was clean.
- Confirmed all 53 automated tests passed.

---

## Version 0.8.0 — Release Preparation

Date: 2026-07-11

### Packaging

- Proved standalone Linux packaging with PyInstaller.
- Added packaged-runtime Pack discovery.
- Excluded generated PyInstaller build artifacts from Git.

### Privacy

- Replaced personal Git author and committer metadata with the PrepFlow identity.
- Removed personal identifying information from reachable Git history.
- Removed historical private source and scratch artifacts.
- Verified sanitized history across the private repository and public mirror.

### Canonical Packs

- Removed residual TCPDF source branding from the Pharmacy Pack.
- Cleaned 527 malformed Medical-Surgical chapter-title occurrences.
- Preserved all 1,435 Medical-Surgical questions.
- Verified zero remaining malformed Medical-Surgical chapter names.

### Validation

- Confirmed both Git remotes match the sanitized local history.
- Confirmed canonical Pack JSON remains valid.
- Existing automated tests pass.

---

## Sprint 6 — Pack Validation
# Version 0.6.2

Date: 2026-07-03

## Sprint 6 — Pharmacy Production Importer Complete

### Added

- Created `tools/import_pharm_bank.py`
- Added Pharmacy production importer
- Added ORDERING section detection
- Added ordered question type support
- Improved question boundary detection
- Added importer validation reporting

### Fixed

- Fixed duplicate completion question generation
- Fixed Chapter 13 ORDERING parsing
- Fixed completion answer extraction
- Fixed completion rationale extraction
- Eliminated duplicate IDs
- Eliminated invalid question records

### Validation

Pharmacy Test Bank

- Chapters: 24
- Questions: 1076

Question Types

- Multiple Choice: 963
- SATA: 73
- Completion: 39
- Ordered: 1

Validation Results

- Missing Answers: 0
- Missing Rationales: 0
- Duplicate IDs: 0
- Invalid Questions: 0

Status

✅ Pharmacy production importer complete.
v0.6.1

- Added Med-Surg PDF importer
- Added pypdf integration
- Implemented chapter detection
- Implemented inventory generation
- Added JSON inventory export
- Added source_banks ignore rules
- Verified 63 chapters from Med-Surg bank

- Fixed validator crash caused by duplicate stem tracking.
- Improved compiler validation output with grouped problem reporting.
- Added clearer duplicate question number reporting.
- - Validation reports now group multiple issues under each affected question.
---

# Version 0.6.0 — Sprint 6 Documentation Refresh

## Repository

- Reorganized all project documentation into the `docs/` directory.
- Established `PROJECT_STATE.md` as the primary source of truth.
- Added `RESTART_PACKET.md` for starting new ChatGPT sessions.
- Added `SESSION_CHECKLIST.md` for standardized end-of-session workflow.
- Simplified project documentation structure.
- Removed duplicate documentation files.
- Standardized repository organization.

---

## Compiler

Completed features:

- DOCX document loader
- Tokenizer
- Question parser
- JSON artifact generation
- Validation framework
- Duplicate question number detection
- Duplicate question text detection
- Missing question stem detection
- Missing answer choice detection
- Missing correct answer detection
- Missing rationale detection
- Missing question type detection
- Graceful compiler failure when validation errors are found
- Human-readable validation reporting

---

## Study Engine

Completed features:

- Interactive terminal quiz
- Block mode
- Session manager
- Running score
- Review queue
- Progress tracking
- Rationales
- Question randomization

---

## Documentation

Current documentation system:

- PROJECT_STATE.md
- CHANGELOG.md
- VISION.md
- RESTART_PACKET.md
- SESSION_CHECKLIST.md
- ARCHITECTURE.md
- PACK_SPEC.md
- IDEAS.md

# Version 0.7.0

Sprint 7 — Canonical Compiler Architecture

---

## Compiler

Major architectural refactor completed.

Implemented:

- Reusable compiler pipeline
- Dedicated normalization stage
- Library-first compiler architecture
- CLI orchestration layer

Added:

- compiler/normalizer.py

Pipeline now consists of:

- Reader / Loader
- Tokenizer (DOCX)
- Parser (DOCX)
- Normalizer
- Validator
- Deduplicator
- Builder
- Canonical Pack

Validation, deduplication, and canonical object creation now occur inside the compiler pipeline instead of the CLI.

---

## Architecture

Introduced explicit compiler data representations:

- Parsed Question
- Normalized Question
- Canonical Question

Schema compatibility is now handled exclusively by the Normalizer.

Applications consume compiler functionality rather than implementing compiler logic directly.

---

## Validation

Validator updated to validate normalized compiler input.

Duplicate question numbers are now evaluated within chapter scope.

Known remaining validation failures are confirmed source-data issues:

- Duplicate block (Questions 41–60)
- Missing correct answer and rationale (Question 80)
- Duplicate stems (Questions 117 and 156)

---

## Documentation

Updated:

- ARCHITECTURE_BIBLE.md
- PROJECT_STATE.md

Compiler architecture documentation now reflects the implemented library-first design.

---
---

Future releases should be added above this line.