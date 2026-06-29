# PACK_SPEC

## Purpose

A Pack is the unit of study distributed to PrepFlow.

Every Pack must compile into the same standardized format regardless of the original source material.

---

# Pack Requirements

Every Pack contains:

- Metadata
- Questions
- Permanent Question IDs
- Optional Sections

The study engine never relies on the original source document after compilation.

---

# Metadata

Each Pack should define:

- Title
- Subject
- Version
- Author (optional)
- Description
- Creation Date

---

# Questions

Each question must contain:

- Permanent ID
- Question Type
- Prompt
- Answer Choices (if applicable)
- Correct Answer(s)
- Rationale
- Section (optional)

Question IDs must never change after publication.

---

# Supported Question Types

Version 1 supports:

- Multiple Choice
- Select All That Apply (SATA)
- Ordered Response

Future versions may include:

- Drag and Drop
- Hot Spot
- Case Study
- Image-Based Questions

---

# Validation Rules

Before a Pack is published:

- No duplicate Question IDs
- No duplicate questions
- Every question has an answer
- Every question has a rationale
- Question type is recognized
- Pack metadata is complete

---

# Compiler Output

Every Pack compiles into normalized JSON.

The study engine only consumes compiled Packs.

---

# Versioning

Pack versions are independent of PrepFlow versions.

Updating a Pack should not require changing the study engine.

---

This specification defines the contract between Pack creators and the PrepFlow engine.