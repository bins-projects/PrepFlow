# PREPFLOW RESTART PACKET

## Purpose

This document is ChatGPT's operational bootloader.

The user pastes this into a new conversation whenever a previous chat has become slow, bloated, or has lost focus.

This document is **not** project documentation.

Its only purpose is to rapidly restore the current project state, operating rules, workflow, and immediate priority so work resumes efficiently.

---

# Source of Truth

The committed GitHub repository is the technical source of truth.

Memory is secondary.

If memory and GitHub disagree:

1. Inspect the committed repository.
2. Trust the committed implementation.
3. Update this Restart Packet if necessary.

Never begin architectural discussions from memory alone.

---

# GitHub-First Rule

Before asking the user for:

* terminal output
* source code
* file contents
* directory listings
* helper scripts

first ask:

> **Can the committed GitHub repository answer this?**

If yes:

Inspect GitHub.

Only request local information when:

* work has not been committed
* runtime behavior must be observed
* tests must be executed
* dependencies must be inspected
* GitHub genuinely cannot answer the question

GitHub inspection is the default workflow.

---

# Current Architecture

PrepFlow is a terminal-based study platform.

Architecture:

Private Source Material

↓

Compiler

↓

Canonical PrepFlow Packs

↓

Study Engine

The compiler exists only to produce canonical PrepFlow Packs.

The Study Engine consumes only canonical Packs.

Private source material intentionally remains outside the repository.

Architecture is considered stable.

Do not redesign without implementation evidence.

---

# Current Repository Goals

Current work is focused on producing a lean Version 1 repository.

The objective is not adding features.

The objective is reducing scaffolding until the remaining repository represents only the product.

Every remaining file should justify its existence.

Temporary build artifacts, obsolete documentation, migration utilities, and one-time tooling should disappear once their purpose has been fulfilled.

---

# Documentation Philosophy

Documentation should remain intentionally small.

Target structure:

README.md

ARCHITECTURE_BIBLE.md

RESTART_PACKET.md

V1_RELEASE_CHECKLIST.md

CHANGELOG.md

IDEAS.md

Everything else should either:

* merge into one of these documents
* or be removed.

Documentation should not duplicate itself.

Each document should have exactly one responsibility.

---

# Purpose of Each Document

README

Repository front page.

Explain what PrepFlow is, how to run it, and where to find additional information.

---

ARCHITECTURE_BIBLE

Permanent technical truth.

Contains:

* system architecture
* canonical data model
* compiler pipeline
* study engine
* repository structure
* architectural boundaries

Contains no temporary project status.

---

RESTART_PACKET

Operational bootloader for ChatGPT.

Contains:

* current workflow
* current operating rules
* current project focus
* startup procedure
* failure-mode reminders

Contains no implementation history beyond lessons that improve execution.

---

V1_RELEASE_CHECKLIST

Only unfinished Version 1 work.

No philosophy.

No brainstorming.

No future roadmap.

---

CHANGELOG

Append-only milestone history.

Not project status.

---

IDEAS

Parking lot for Version 2 and beyond.

Ideas never interrupt Version 1 execution.

---

# Startup Procedure

At the beginning of every PrepFlow session:

1. Inspect the committed GitHub repository.
2. Confirm repository health.
3. Compare documentation against implementation.
4. Identify the current Version 1 milestone.
5. Execute exactly one milestone.

Avoid reopening already-decided architectural discussions.

---

# Top-Down Assessment

A Top-Down Assessment means inspecting the committed GitHub repository.

It is not a file-by-file review.

It should produce:

* Repository Health
* Architecture
* Runtime
* Documentation
* Cleanup Candidates
* Exactly one recommended Version 1 milestone

Use GitHub to answer every question possible.

Only request local information when necessary.

---

# Failure Modes

## Logic Loops

Do not replace execution with repetitive inspection.

Examples:

* opening many files without making progress
* repeated grep searches
* repeatedly discussing decisions that have already been made
* expanding plans instead of implementing them

When work becomes repetitive:

Stop.

Return to the architectural question.

Choose the smallest executable action.

Execute.

---

## Feature Creep

Do not redesign working systems during Version 1.

Ideas belong in IDEAS.md.

Execution belongs in the current milestone.

---

## Documentation Growth

Avoid creating documents to explain temporary work.

Prefer improving an existing authoritative document.

Reduce duplication whenever possible.

---

# Current Priority

Finish documentation consolidation.

Verify the repository after cleanup.

Produce a clean, standalone Version 1.

Only after Version 1 is complete should planning and exploratory feature discussions become the primary workflow again.

---

# Operating Rules

Observe

↓

Inspect

↓

One focused change

↓

Compile

↓

Run

↓

Verify

↓

Commit

↓

Push

↓

Update documentation

↓

Repeat

One milestone at a time.

Architecture follows evidence.

GitHub is the source of truth.

Execution is preferred over discussion once the architectural decision has already been made.
    




This is a good point to capture the milestone. Since you're ready to stop, I wouldn't spend time editing multiple project documents tonight.

Instead, create one detailed handoff entry. Tomorrow, we can copy the relevant parts into `RESTART_PACKET.md`, `ARCHITECTURE_BIBLE.md`, or any other permanent document where they belong.

# PREPFLOW HANDOFF — STANDALONE PACKAGING MILESTONE

## Milestone Summary

This session successfully proved that PrepFlow can be packaged and launched as a standalone application rather than only as a Python project.

This is a major V1 milestone.

PrepFlow has now transitioned from:

> "Runs from the repository with Python."

to

> "Can be bundled into a distributable application."

No installer has been created yet, but the packaging pipeline has been proven.

---

# Repository State

Current commit:

`5d279b2`

Commit message:

> Support packaged PrepFlow builds and ignore PyInstaller artifacts

Repository was intentionally kept clean.

Only source changes were committed.

Generated build artifacts were excluded from version control.

`.gitignore` now ignores:

* build/
* dist/
* *.spec

This keeps future packaging builds from polluting commits.

---

# Packaging Investigation

Packaging approach selected:

PyInstaller (`--onedir`)

Reasoning:

* Smallest proof-of-concept
* Preserves dynamic Pack discovery
* Easy debugging
* Portable folder
* Future installer can wrap the same output

No GUI work was started.

No installer work was started.

No architecture redesign was performed.

---

# Packaging Bug #1

Initial packaged build launched but immediately failed with:

FileNotFoundError:
No PrepFlow packs found in packs/

Root cause:

`study/loader.py` assumed:

```python
PACKS_DIR = Path("packs")
```

This only works when the repository root is the working directory.

A packaged application does not necessarily execute from that location.

---

# Packaging Fix

Loader now detects whether PrepFlow is running:

* from source
* from a PyInstaller bundle

Source mode:

Uses repository root.

Packaged mode:

Uses the PyInstaller runtime bundle location (`sys._MEIPASS`) to locate bundled Packs.

This preserves existing development behavior while enabling standalone execution.

---

# Verification

Packaging process completed successfully.

PyInstaller build succeeded.

Application launched successfully.

Pack discovery worked.

Pack selection displayed:

* Medical-Surgical
* Pharmacy

This confirms:

* executable launches
* bundled data is located correctly
* loader fix is functioning

No further runtime issues were investigated this session.

---

# Current Distribution Status

Linux packaging has been proven.

Windows executable has NOT yet been built.

This is expected because PyInstaller is not a cross-compiler.

Windows build will occur from a Windows environment after remaining cleanup work.

---

# New Priority Order

The previous next milestone was:

Standalone executable.

That milestone has now been achieved as a proof-of-concept.

New priority order:

1. Privacy & Release Audit
2. Chapter display-name cleanup
3. Windows standalone build
4. Clean-machine testing
5. Beta distribution
6. Installer (optional)

---

# Privacy & Release Audit (Highest Priority)

Before ANY beta release:

Inspect and remove:

* personal names
* usernames
* email addresses
* machine paths
* repository metadata
* executable metadata
* documentation references
* screenshots
* generated Pack metadata
* Git author/history if appropriate

No classmate receives PrepFlow until this audit is complete.

---

# Remaining Cosmetic Cleanup

Observed during packaging verification:

Several Medical-Surgical chapter names still contain source-title remnants such as:

* "Linton:"
* truncated book titles
* partial source headers

These do not affect functionality.

They should be cleaned before beta testing because they are visible to users.

Compiler cleanup is expected to be straightforward and should regenerate the canonical Pack afterward.

---

# Development Rules Reaffirmed

Continue following:

Observe

↓

Inspect

↓

One focused change

↓

Build

↓

Run

↓

Verify

↓

Commit

↓

Push

↓

Repeat

Avoid speculative fixes.

Avoid architecture redesign.

Avoid logic loops.

Only fix observed problems.

---

# Current V1 Status

Compiler:

Stable.

Study Engine:

Stable.

Canonical Packs:

Stable.

Standalone packaging:

Proven.

Next milestone:

Privacy & Release Audit.

I think this is the right level of detail for a handoff: it captures **what changed, why it changed, how it was verified, and exactly where to resume** without cluttering the permanent documentation tonight. Tomorrow we can distill this into the Architecture Bible and Restart Packet where appropriate.
