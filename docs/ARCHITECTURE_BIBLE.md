# ARCHITECTURE_BIBLE

## Purpose

This document defines the permanent architecture of PrepFlow.

Architectural decisions recorded here are considered stable unless explicitly revised.

---

# Design Philosophy

PrepFlow is a universal study engine.

The engine is independent of subject matter.

All study content is supplied through interchangeable Packs.

The application contains no nursing-specific logic.

The compiler converts source material into a normalized format that the study engine consumes.

---

# Core Hierarchy

PrepFlow

→ Pack

→ Section (optional)

→ Session

→ Block

→ Review Queue

---

# Core Objects

## Pack

A complete collection of study material for one subject.

Examples:

- Cardiac
- Respiratory
- Pharmacology
- Sports Rules
- History

A Pack owns:

- Questions
- Sections
- Metadata

---

## Section

Optional organization inside a Pack.

Examples:

Cardiac

- Hypertension
- Heart Failure
- Dysrhythmias

Not all Packs require Sections.

---

## Session

A temporary study instance.

Responsibilities:

- Generate shuffled order
- Create balanced Blocks
- Track scoring
- Track mastery
- Feed Review Queue

Sessions are not permanently saved in Version 1.

---

## Block

A balanced subset of questions.

Goals:

- Approximately 15 questions
- Even distribution across Sections
- Locked once created
- Presented sequentially

---

## Review Queue

Contains only questions missed on the first attempt.

Questions repeat until answered correctly.

First-attempt score never changes.

Mastery is tracked separately.

---

# Compiler Responsibilities

The compiler is responsible for:

- Reading source documents
- Parsing questions
- Validation
- Assigning permanent IDs
- Producing normalized JSON

The study engine never parses DOCX files directly.

---

# Study Engine Responsibilities

The study engine is responsible for:

- Loading compiled Packs
- Running Sessions
- Presenting questions
- Recording answers
- Calculating scores
- Managing Blocks
- Managing Review Queue

---

# Guiding Principles

- Engine first.
- Content second.
- Permanent Question IDs.
- Never generate questions.
- Normalize everything once.
- Reuse compiled data forever.
- Simple architecture over clever architecture.
- End users never require programming knowledge.

---

# Future Expansion

Architecture should support:

- Multiple Packs
- Multiple users
- Saved Sessions
- Statistics
- GUI
- Mobile interface
- Additional import formats
- Community-created Packs

---

This document should change rarely.

Behavior changes belong in PROJECT_STATE.md or CHANGELOG.md.