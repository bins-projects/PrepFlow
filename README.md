# PrepFlow

PrepFlow is a Python application for compiling educational content into validated study packs and delivering those packs through an interactive command-line study engine.

---

# Current Status

**Version:** 0.6.0

**Current Sprint:** Sprint 6 – Pack Validation

**Development Status:** Active

---

# Components

## Compiler

Responsible for:

- Loading source documents
- Tokenizing content
- Parsing questions
- Validating question packs
- Exporting standardized JSON

Current validation includes:

- Duplicate question numbers
- Duplicate question text
- Missing stems
- Missing answer choices
- Missing correct answers
- Missing rationales
- Missing question types

---

## Study Engine

Features include:

- Randomized question order
- Block mode
- Review queue
- Running score
- Session manager
- Rationales
- Progress tracking

---

# Repository Layout

```text
compiler/
study/
tools/
tests/
data/
output/
docs/
```

---

# Documentation

Project documentation is located in:

```
docs/
```

Primary documents:

- PROJECT_STATE.md
- CHANGELOG.md
- VISION.md

---

# Typical Development Workflow

1. Build one feature.
2. Test it.
3. Review changes.
4. Commit.
5. Push.
6. Update documentation.
7. Verify working tree clean.

---

# Current Goal

Finish Sprint 6 by completing the Pack Validation system before continuing Study Engine improvements.

---

# Version Roadmap

0.6.x — Validation

0.7.x — Compiler Completion

0.8.x — Study Engine Polish

0.9.x — Beta

1.0 — Initial Release