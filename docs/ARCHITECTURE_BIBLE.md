# PREPFLOW ARCHITECTURE BIBLE

## Purpose

This document defines PrepFlow's permanent technical architecture.

It contains only long-term architectural truth.

It does **not** contain:

- temporary milestones
- sprint notes
- bugs
- handoff information
- current priorities

Those belong in the Restart Packet.

---

# Mission

PrepFlow converts educational source material into validated, canonical PrepFlow Packs that can be studied through a common Study Engine.

The long-term user experience is simple:

> Select a source file, choose a Pack name, and let PrepFlow make it study-able.

---

# Core Architecture

```
Private Source
      │
      ▼
Source Adapter
      │
      ▼
Extract
      │
      ▼
Clean
      │
      ▼
Detect
      │
      ▼
Parse
      │
      ▼
Normalize
      │
      ▼
Validate
      │
      ▼
Deduplicate
      │
      ▼
Canonical Pack Builder
      │
      ▼
PrepFlow Pack
      │
      ▼
Study Engine
```

Each stage has exactly one responsibility.

No stage should perform the work of another.

---

# Source Material

PrepFlow is designed to support multiple source formats.

Examples include:

- PDF
- DOCX
- TXT
- JSON
- future OCR sources

Private source material always remains outside the repository.

Generated canonical Packs are the permanent product.

---

# Source Adapters

A source adapter knows how to read a particular file format.

Current implementation:

- Text-based PDF

Future adapters may include:

- DOCX
- Plain text
- OCR
- Structured JSON

Adapters only extract data.

They never parse questions.

---

# Extraction

Extraction converts a supported source into raw text.

Current artifact:

```
output/imports/<pack-id>/01_raw.txt
```

Extraction intentionally preserves source noise.

Cleaning is responsible for removing it.

---

# Cleaning

Cleaning removes extraction artifacts while preserving educational meaning.

Cleaning may remove:

- branding
- download notices
- watermark fragments
- repeated page headers
- repeated page footers
- duplicate chapter indexes
- formatting artifacts
- repeated URLs

Cleaning must never intentionally rewrite:

- question stems
- answer choices
- correct answers
- rationales

Current artifact:

```
output/imports/<pack-id>/02_clean.txt
```

---

# Detection

Detection observes the cleaned document before parsing.

Its job is to measure—not interpret.

Examples include:

- chapter count
- section headers
- answer markers
- metadata markers
- question-like blocks
- unknown structures

Detection generates an import report.

Current artifact:

```
output/imports/<pack-id>/03_detection.json
```

Detection should expose uncertainty rather than hide it.

---

# Parsing

The parser converts cleaned text into structured source-derived question records.

The parser identifies:

- chapter
- chapter title
- section
- source question number
- question type
- stem
- choices
- answer
- rationale
- metadata

The parser does **not** create canonical PrepFlow Questions.

---

# Canonical Compiler

The compiler converts parsed source questions into canonical PrepFlow Questions.

Its permanent stages are:

```
Normalize
    ↓
Validate
    ↓
Recover invalid questions
    ↓
Deduplicate
    ↓
Assign stable IDs
    ↓
Build canonical Pack
    ↓
Export
```

---

# Normalization

Normalization converts supported parser output into one internal schema.

All later compiler stages consume the normalized representation.

---

# Validation

Validation reports:

- missing stems
- missing answers
- missing rationales
- unsupported question types
- malformed structures
- duplicate IDs
- parser failures
- remaining source contamination

Validation reports problems.

It never invents educational content.

---

# Deduplication

Deduplication removes only true duplicates.

Questions testing different clinical judgment must remain.

Every removal should be explainable.

---

# Stable IDs

Question IDs must be:

- deterministic
- repeatable
- unique
- independent of file location
- independent of display order

Repeated compilation of unchanged source should produce identical IDs.

---

# Export

Canonical Packs are exported as:

```
*.prepflow.json
```

Canonical Packs form the permanent interface between the compiler and the Study Engine.

---

# Study Engine

The Study Engine consumes canonical Packs only.

Responsibilities include:

- Pack discovery
- chapter selection
- randomized sessions
- answer checking
- scoring
- review queue
- mastery tracking

The Study Engine never reads private source material.

It never parses PDFs.

It never repairs invalid Packs.

---

# Dynamic Packs

Every valid Pack placed inside:

```
packs/
```

must automatically appear in the Pack selection screen.

Adding a new subject must not require Study Engine code changes.

---

# User Import Workflow

The long-term workflow should become:

> Import and Create Module

The user should:

1. choose a source file;
2. choose a Pack name;
3. begin import;
4. review the import report;
5. receive a validated PrepFlow Pack.

The interface is a wrapper around the compiler pipeline.

It must not replace compiler stages.

---

# Repository Structure

Permanent repository areas include:

```
compiler/
study/
packs/
docs/
tests/
```

The repository must not contain:

- private source books
- scratch extraction files
- recovery repositories
- obsolete import scripts
- personal identifying information
- generated build artifacts

---

# Architectural Principles

1. Private source remains private.
2. Source adapters are format-aware, not subject-aware.
3. The importer is generic.
4. The compiler is generic.
5. Canonical Packs are the only Study Engine input.
6. Study Engine behavior is Pack-driven.
7. IDs remain deterministic.
8. Validation reports uncertainty.
9. Cleaning preserves educational meaning.
10. Architecture follows evidence from real imports.
11. One focused change → test → commit → repeat.

---

# Change Control

Only update this document when permanent architecture changes.

Never place temporary milestones or current work here.

Those belong in the Restart Packet.