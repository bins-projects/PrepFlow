# PrepFlow Question Lifecycle

Version: 0.1

## Purpose

This document defines the complete lifecycle of a Question inside PrepFlow.

Every Question follows the same path regardless of its source.

---

## Stage 1 — Source

A Question begins in an external source.

Examples:

- PDF
- DOCX
- Text file
- AI-generated content
- Instructor-created content

---

## Stage 2 — Import

The Importer extracts raw content from the source.

Output:

Raw structured data.

---

## Stage 3 — Parse

The Parser identifies:

- stem
- answer choices
- correct answer
- rationale
- question type
- chapter
- section
- source metadata

Output:

Structured question data.

---

## Stage 4 — Compile

The Compiler converts parsed data into canonical PrepFlow Questions.

Responsibilities:

- Assign PrepFlow ID
- Build Question object
- Build Pack object
- Normalize fields
- Remove importer-specific assumptions

Output:

PrepFlow Pack

---

## Stage 5 — Validate

Validator verifies:

- required fields
- answer consistency
- duplicate IDs
- invalid structures
- parser artifacts
- watermark contamination

Output:

Validated Pack

---

## Stage 6 — Study

The Study Engine loads the Pack.

Responsibilities:

- Present Questions
- Grade responses
- Track progress
- Record attempts

---

## Stage 7 — Analytics

Question performance becomes available for:

- statistics
- adaptive learning
- concept mastery
- future recommendations

---

## Guiding Principle

A Question changes form during its lifecycle.

Its identity never changes.