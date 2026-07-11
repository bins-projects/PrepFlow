# PREPFLOW RESTART PACKET

## Purpose

This document is ChatGPT's operational bootloader.

Charlie pastes this into a new conversation whenever a previous chat has become slow, bloated, or has lost focus.

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

Before asking Charlie for:

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
