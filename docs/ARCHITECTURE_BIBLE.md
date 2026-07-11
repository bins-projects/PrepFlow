# PREPFLOW ARCHITECTURE BIBLE

## Purpose

This document defines the permanent technical architecture of PrepFlow.

It is the authoritative explanation of:

* what PrepFlow is
* how its components are separated
* how study content moves through the system
* what a PrepFlow Pack contains
* what belongs in the repository
* which architectural boundaries should remain stable

This document contains no temporary project status, sprint history, current milestone, or future feature list.

Those concerns belong elsewhere.

---

# Mission

PrepFlow is a reliable, modular study platform that transforms educational source material into validated study packs and delivers those packs through an interactive study engine.

PrepFlow prioritizes:

* reliability before features
* simple, maintainable code
* explicit validation
* stable question identity
* separation of concerns
* reusable study content
* end-user operation without programming knowledge

---

# System Architecture

PrepFlow has three architectural layers:

```text
Private Source Material
        ↓
Compiler
        ↓
Canonical PrepFlow Packs
        ↓
Study Engine
```

Each layer has a separate responsibility.

The layers communicate through defined data boundaries rather than direct dependencies on one another’s internal implementation.

---

# 1. Private Source Material

Private source material is the original educational content used to build PrepFlow Packs.

Examples may include:

* PDF question banks
* DOCX documents
* structured JSON
* instructor-created material
* other authorized educational sources

Private source material intentionally remains outside the repository.

The repository should not depend on the continued presence of the original source files after a valid Pack has been created.

Source-specific extraction, cleaning, and preparation may be required before content enters the canonical compiler.

These preparation steps are not part of the Study Engine.

One-time import or migration tools should not remain permanent architectural components after their purpose has been fulfilled.

---

# 2. Compiler

## Responsibility

The compiler transforms supported structured question data into validated canonical PrepFlow objects and, when requested, exports a lean PrepFlow Pack.

The compiler is reusable application code.

It does not contain study-session behavior.

It does not present questions to learners.

It does not track scores or mastery.

---

## Compiler Pipeline

The current reusable compiler pipeline is:

```text
Reader or Loader
        ↓
Tokenizer and Parser when required
        ↓
Normalizer
        ↓
Validator
        ↓
Recoverable-question filtering
        ↓
Deduplicator
        ↓
Canonical Question Builder
        ↓
Canonical Pack Builder
        ↓
PrepFlow Pack Exporter
```

Not every source uses every stage.

For example, structured input may enter after source-specific extraction and parsing, while DOCX input may require the reader, tokenizer, and parser.

---

## Reader and Loader

The Reader or Loader obtains source content for compilation.

Its responsibility is access and extraction.

It should not silently repair invalid questions or contain study-engine behavior.

---

## Tokenizer

The Tokenizer converts document content into tokens that can be interpreted by a parser.

It is used only by source formats that require tokenization.

---

## Parser

The Parser identifies structured question fields such as:

* stem
* choices
* correct answer
* rationale
* question type
* chapter
* section
* source question number
* available metadata

The Parser produces structured source-derived question dictionaries.

It does not create canonical PrepFlow objects.

---

## Normalizer

The Normalizer converts supported input variations into one compiler input schema.

Normalization occurs before validation.

Later stages should not repeatedly translate source-specific field names or structures.

Normalize once.

Use the normalized representation throughout the remaining compiler pipeline.

---

## Validator

The Validator detects structural problems and returns typed diagnostics.

Possible findings include:

* missing stem
* missing choices when choices are required
* missing correct answer
* missing rationale
* unsupported or missing question type
* malformed answer structure
* duplicate identifiers
* parser artifacts
* source contamination

Diagnostics may be classified by severity.

Fatal problems prevent the Pack from being built.

Recoverable problems allow the affected question to be skipped while valid questions continue through the pipeline.

Advisory findings report concerns without silently changing source meaning.

The Validator reports problems.

It does not invent missing educational content.

---

## Source Cleaning and Contamination Control

Source cleaning is not one operation.

It may include:

* text extraction
* formatting normalization
* removal of non-question blocks
* removal of page headers and footers
* removal of download-site branding
* removal of watermark fragments
* repair of split structural headings
* verification of final parsed output

Removing non-question blocks does not guarantee that all source contamination has been removed.

Residual branding or header fragments may survive inside otherwise valid question blocks.

Therefore, final Pack validation must include explicit searches for known source artifacts and branding rather than assuming structural extraction removed them.

Cleaning should remove contamination without rewriting legitimate question content.

---

## Deduplicator

The Deduplicator removes records identified as duplicates according to compiler rules.

Its responsibilities include:

* keeping the first accepted occurrence
* removing later duplicate records
* reporting what was removed
* preserving valid distinct questions

Deduplication must not silently collapse questions merely because they discuss the same topic.

Questions testing different clinical judgments remain separate questions.

---

## Builder

The Builder creates canonical PrepFlow domain objects.

It creates:

* canonical `Question` objects
* canonical `Pack` objects

The Builder receives normalized, validated, accepted question data.

It does not parse raw documents.

It does not run study sessions.

---

## Exporter

The Exporter converts the rich canonical Pack into the lean JSON format consumed by PrepFlow applications.

The exported file uses the extension:

```text
.prepflow.json
```

The exported Pack is the stable interface between content compilation and study delivery.

---

# 3. Canonical Domain Model

The compiler uses a rich internal domain model.

The primary objects are:

```text
Pack
 └── Question
      ├── Origin
      ├── Content
      ├── Answer
      ├── Classification
      └── Metadata
```

---

## Pack

A canonical Pack represents a complete collection of compiled Questions.

A Pack owns its Questions.

A Question does not own its Pack.

Canonical Pack information may include:

* Pack ID
* title
* version
* schema version
* creation information
* source information
* Questions

---

## Question

A canonical Question represents one standardized assessment item.

Its identity remains stable after compilation.

A canonical Question contains:

* stable PrepFlow ID
* version
* origin
* learner-facing content
* answer
* optional classification
* developer-facing metadata

---

## Origin

Origin records where the Question came from before PrepFlow standardized it.

Possible fields include:

* publisher
* book
* edition
* chapter
* section
* source page
* source identifier

Origin is provenance.

It must not control Study Engine behavior.

---

## Content

Content contains learner-facing material:

* stem
* choices
* rationale

---

## Answer

Answer contains:

* question type
* accepted answer value

Question types currently represented in production Packs include:

* multiple choice
* multiple response
* completion
* ordered response

---

## Classification

Classification supports optional grouping and future analysis.

Possible fields include:

* concepts
* tags
* body system
* difficulty
* Bloom level

Classification is optional and should not be required for basic Pack delivery.

---

## Metadata

Metadata contains developer-facing information.

Possible fields include:

* compiler version
* validation state
* creation information
* notes
* preserved source metadata

Metadata must not be required for basic question presentation unless explicitly added to the Pack contract.

---

# Canonical PrepFlow Pack Format

## Purpose

A PrepFlow Pack is the serialized application-facing study format.

It is the only study-content format the Study Engine consumes.

The Study Engine does not consume:

* original PDFs
* DOCX source files
* parser output
* temporary extraction files
* compiler-internal dataclasses

---

## Pack-Level Contract

A valid PrepFlow Pack contains:

```json
{
  "format": "prepflow_pack",
  "version": "1.0",
  "pack_id": "example_pack",
  "title": "Example Pack",
  "questions": []
}
```

Required Pack-level fields:

* `format`
* `version`
* `pack_id`
* `title`
* `questions`

The `format` value identifies the file as a PrepFlow Pack.

The current format marker is:

```text
prepflow_pack
```

---

## Question-Level Contract

A study-ready question contains the fields required to identify, present, grade, and explain it.

Core fields are:

```json
{
  "id": "source-ch01-multiple_choice-q001",
  "chapter": 1,
  "type": "multiple_choice",
  "stem": "Question text",
  "choices": [
    {
      "label": "A",
      "text": "Choice text"
    }
  ],
  "correct_answers": ["A"],
  "rationale": "Explanation"
}
```

Production Packs may also preserve useful fields such as:

* `source`
* `chapter_title`
* `section`
* `source_question_number`
* `metadata`

These fields improve display, traceability, or future analysis but do not change the separation between the Pack and its original source.

---

## Stable Question IDs

Question IDs are assigned during content preparation or compilation and must remain stable across repeated builds when the source question has not changed.

IDs should be:

* deterministic
* unique within the Pack
* independent of temporary file location
* independent of display order
* understandable enough for diagnostics

A typical ID contains:

* source
* chapter
* question type
* stable sequence

Example:

```text
medsurg-ch34-multiple_choice-q001
```

Question order may change during study.

Question identity must not.

---

## Pack Boundary

The PrepFlow Pack is the architectural boundary between the compiler and the Study Engine.

This boundary is stable.

The compiler may change internally without changing study delivery, provided it continues producing valid Packs.

The Study Engine may change internally without changing import logic, provided it continues consuming valid Packs.

Neither system should reach across this boundary to depend on the other system’s private implementation.

---

# 4. Study Engine

## Responsibility

The Study Engine delivers questions from valid PrepFlow Packs.

It is responsible for:

* Pack discovery
* Pack loading
* chapter selection
* randomized session creation
* block-based presentation
* answer checking
* first-attempt scoring
* missed-question review
* mastery progression

The Study Engine does not compile source material.

It does not parse private question banks.

It does not repair invalid Packs.

---

## Pack Discovery

The Study Engine discovers files matching:

```text
packs/*.prepflow.json
```

It reads Pack metadata for display and ignores files that do not identify themselves with the expected PrepFlow format marker.

This makes Packs interchangeable.

The Study Engine does not contain hard-coded nursing sources.

---

## Pack Loading

The loader reads the selected Pack and verifies its format marker.

An invalid Pack should fail clearly rather than being interpreted as an unrelated JSON file.

---

## Pack Selection

Available Packs are presented dynamically from the `packs/` directory.

Adding another valid Pack should not require nursing-specific changes to the Study Engine.

---

## Chapter Selection

The Study Engine supports:

* the entire selected Pack
* one chapter
* multiple chapters

Chapter filtering uses chapter values stored in Pack questions.

When available, `chapter_title` is used for display.

---

## Session Creation

A session receives the selected questions and copies them into session state.

Questions are shuffled once when the session begins.

The session then advances sequentially through that fixed shuffled order.

The default block size is approximately 15 questions.

---

## Question Presentation

The Study Engine presents:

* session or block position
* question stem
* answer choices when present
* answer prompt

The answer checker compares the learner’s normalized response with the accepted answer set.

For multiple-response questions, answer order is not significant unless the question type explicitly requires ordered response behavior.

---

## First-Attempt Scoring

First-attempt performance is recorded separately from review performance.

A question missed on the first attempt remains a first-attempt miss even after it is mastered in review.

Review does not rewrite the first-pass score.

---

## Review Queue

Missed questions enter the Review Queue.

At the end of a completed block, queued questions are presented again.

A question answered incorrectly during review returns to the queue.

Review continues until all queued questions are answered correctly.

This produces two distinct measures:

* first-pass performance
* eventual mastery

---

# Repository Architecture

The repository is intended to contain only durable product code, canonical Packs, tests, and authoritative documentation.

The major permanent areas are:

```text
compiler/
docs/
packs/
study/
tests/
README.md
requirements.txt
```

---

## `compiler/`

Reusable compilation components.

Contains the canonical compiler pipeline and domain model.

---

## `packs/`

Canonical PrepFlow Packs consumed by the Study Engine.

Current production Packs include:

* Pharmacy
* Medical-Surgical

Packs are product data, not private source material.

---

## `study/`

Interactive terminal Study Engine.

Contains Pack loading, session management, question presentation, scoring, and review behavior.

---

## `tests/`

Automated verification of compiler and Study Engine behavior.

Tests protect the stable architectural boundaries and expected runtime behavior.

---

## `docs/`

Authoritative project documents.

The intended documentation set is:

* `ARCHITECTURE_BIBLE.md`
* `RESTART_PACKET.md`
* `V1_RELEASE_CHECKLIST.md`
* `CHANGELOG.md`
* `IDEAS.md`

Technical architecture belongs here in the Architecture Bible rather than being duplicated across multiple specification documents.

---

# What Does Not Belong in the Repository

Unless a continuing architectural need is demonstrated, the repository should not retain:

* private source banks
* temporary extraction output
* exported study documents
* one-time migration scripts
* obsolete import scaffolding
* course-specific temporary study packets
* duplicate documentation
* old project-status documents
* downloaded branding or watermark artifacts
* generated files that are not canonical product assets

Temporary resources may be useful during development without becoming permanent project structure.

---

# Architectural Rules

## Canonical Packs Are the Interface

The compiler produces Packs.

The Study Engine consumes Packs.

This boundary should not be bypassed.

---

## Private Sources Stay Private

The application must remain usable without committing original source material.

---

## Applications Contain No Nursing-Specific Logic

The Study Engine should work with any valid PrepFlow Pack.

Source and subject differences belong in Pack data, not application control flow.

---

## Normalize Once

Source-specific schema translation belongs in normalization or pre-compilation preparation.

Later stages should consume a consistent structure.

---

## Validate Explicitly

Invalid structures and contamination should produce visible diagnostics or failed validation.

Do not hide errors through silent repair.

---

## Preserve Educational Meaning

Cleaning and normalization may remove artifacts and standardize structure.

They must not casually rewrite the meaning of:

* stems
* choices
* correct answers
* rationales

---

## Stable Identity

Question identity should survive export, reordering, session shuffling, and future application changes.

---

## Separate First-Pass Performance from Mastery

Correcting a missed question during review demonstrates mastery.

It does not alter the historical first-attempt result.

---

## Keep the Repository Lean

A file remains only when removing it would cost the architecture, product, validation, or meaningful history.

Past usefulness alone is not sufficient reason for permanent retention.

---

## Architecture Follows Evidence

Do not redesign working systems based only on speculation.

Architectural changes require implementation evidence showing that the current boundary or model no longer serves the product.

---

# Current Stable Decisions

The following decisions are considered stable unless implementation evidence requires revision:

1. PrepFlow remains divided into source preparation, compiler, Pack, and Study Engine layers.

2. Canonical PrepFlow Packs remain the interface between compilation and study delivery.

3. The Study Engine consumes only Pack data.

4. Private source material remains outside the repository.

5. Pack discovery is dynamic rather than hard-coded by subject.

6. Chapter selection is driven by Pack metadata.

7. Questions are shuffled once per session.

8. First-pass scoring remains separate from review mastery.

9. Missed questions repeat until mastered.

10. The repository should become smaller and simpler as temporary scaffolding is retired.

---

# Change Control

This document describes permanent technical truth.

Update it only when:

* implementation changes an architectural boundary
* the canonical Pack contract changes
* a core component gains or loses responsibility
* repository structure changes in a durable way
* a previously stable architectural decision is intentionally revised

Do not update it merely because:

* a temporary task was completed
* the current milestone changed
* a bug was fixed without architectural impact
* an idea was proposed
* a development session ended

Current work belongs in `V1_RELEASE_CHECKLIST.md`.

Historical milestones belong in `CHANGELOG.md`.

Deferred ideas belong in `IDEAS.md`.

ChatGPT operating context belongs in `RESTART_PACKET.md`.
