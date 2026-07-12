# PrepFlow Restart Packet

## Purpose

This document is the operational handoff point for continuing PrepFlow
work without losing project context.

This is not a replacement for the Architecture Bible. The Architecture
Bible contains permanent design decisions. This packet contains the
current project state, recent milestones, active problems, workflow
rules, and the exact mindset required to continue safely.

The goal is to prevent: - repeating solved problems - redesigning
working systems - losing architectural context during debugging -
getting trapped in small fixes without understanding the whole pipeline

------------------------------------------------------------------------

# First Action When Restarting Work

Before making changes:

## Perform a Top-Down Assessment

The committed GitHub repository is the source of truth.

Do not begin with random terminal debugging.

Review:

1.  Repository state
2.  Architecture documentation
3.  Restart Packet
4.  Current implementation structure
5.  Pipeline flow
6.  Tests
7.  Current milestone status

Understand the system before changing it.

The assessment should answer:

-   What is the current architecture?
-   What is already complete?
-   What changed recently?
-   What assumptions does each pipeline stage make?
-   Where does the problem actually originate?
-   Which layer owns the fix?

------------------------------------------------------------------------

# Current Stable Baseline

## Last Major Commit

Commit:

`b292d30`

Message:

`compiler: improve source cleanup parsing and validation`

Status:

-   Committed
-   Pushed
-   Stable baseline

------------------------------------------------------------------------

# Completed Compiler Work

## Cleaner Improvements

Completed:

-   Removed Stuvia contamination when branding replaced answer choices.
-   Removed contaminated section headers.
-   Prevented source branding from becoming educational content.

Example problem:

Before:

`COMPLETION Stuvia.com - The Marketplace...`

After:

`COMPLETION`

------------------------------------------------------------------------

## Source Parser Improvements

Completed:

-   Added recovery for missing A choices caused by PDF extraction.

Example:

Before:

`What is another term for seizure disorder? Epilepsy`

followed by:

`b. Enkephalin`

The parser now recognizes:

A. Epilepsy

B. Enkephalin

C. Narcolepsy

D. Neuropathy

------------------------------------------------------------------------

## Validator Improvements

Completed:

-   Duplicate question identity now accounts for question type.

Reason:

A chapter can legitimately contain:

-   Multiple Choice Question 1
-   Multiple Response Question 1
-   Completion Question 1

These are not duplicates.

------------------------------------------------------------------------

# Current Validation Status

Latest known:

-   Pharmacy compiler successfully processes source.
-   Test suite passed: 37 tests.

The compiler is no longer failing on the previous extraction issues.

------------------------------------------------------------------------

# Current Discovery

During Pharmacy validation:

Repeated source blocks were discovered.

Example:

Chapter 2 content appeared twice: - Multiple Choice block - Multiple
Response block

The active source tree no longer contains the previous deduplicator
module.

Current conclusion:

The duplicate warnings likely reveal a missing pipeline stage.

This is not primarily: - a parser failure - a validator failure - a
cleaner failure

------------------------------------------------------------------------

# Next Planned Milestone

Restore lightweight exact deduplication.

Correct location:

Extract ↓ Clean ↓ Parse ↓ Normalize ↓ Deduplicate ↓ Validate ↓ Build
Pack

------------------------------------------------------------------------

# Deduplication Rules (V1)

Only implement exact duplicate removal.

A duplicate should require matching educational content.

Do not use fuzzy matching yet.

Preserve: - similar questions testing different judgment - same topic
with different answer choices - clinically different scenarios

Do not: - hide source problems - modify parser behavior to remove
duplicates - weaken validator warnings

------------------------------------------------------------------------

# Workflow Rules

## One Focused Change

Follow:

Observe → Inspect → One focused change → Save → Test → Commit → Push

Do not stack unrelated changes.

------------------------------------------------------------------------

## Avoid Logic Loops

If debugging starts producing many small fixes:

Stop and ask:

-   Are we fixing symptoms?
-   Is the problem actually upstream?
-   Does the architecture already have a place for this?

------------------------------------------------------------------------

## Use the Repository First

For questions answerable by the committed repository:

Inspect the repository before requesting pasted files.

Only ask for local output when: - runtime behavior is needed -
uncommitted changes matter - dependencies/environment matter

------------------------------------------------------------------------

# Documentation Rules

Keep only two authoritative documents:

## ARCHITECTURE_BIBLE.md

Contains: - permanent architecture decisions - design rules - long-term
product requirements

## RESTART_PACKET.md

Contains: - current state - recent milestones - next action - known
problems - warnings for future continuation

Do not create additional overlapping handoff documents.

------------------------------------------------------------------------

# Current Local Notes

Separate local changes existed after compiler commit:

Study engine: - study/question.py - tests/test_question.py

These were intentionally separated from the compiler milestone.

Generated artifact: - packs/pharmacy-test.prepflow.json

Treat generated packs intentionally; do not commit artifacts without
deciding whether they are canonical project assets.

------------------------------------------------------------------------

# Core Project Principle

Do not optimize for fixing the current error message.

Optimize for preserving the integrity of the entire pipeline.

A small correct architectural fix is better than many local patches.