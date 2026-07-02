# PrepFlow Changelog

This changelog tracks meaningful project milestones beginning with Version 0.6.0.

Earlier development history remains available through Git commit history.

---

# Version 0.6.0 — Sprint 6
Date: July 2026

## Repository

- Reorganized project documentation.
- Centralized documentation under `docs/`.
- Established PROJECT_STATE.md as the source of truth.
- Standardized project organization and session workflow.

## Compiler

- Implemented question validation framework.
- Added duplicate question number detection.
- Added duplicate question stem detection.
- Added validation for:
  - Missing stems
  - Missing answer choices
  - Missing correct answers
  - Missing rationales
  - Missing question types
- Compiler now displays validation errors before aborting compilation.
- Added developer duplicate detection utility.

## Study Engine

- Stable block progression.
- Review queue implemented.
- Session manager implemented.
- Running score tracking.
- Randomized question ordering.
- Block completion flow operational.

## Development Workflow

- Standardized Git workflow.
- Standardized end-of-session documentation updates.
- Introduced repository-based project documentation.

---

Future releases should be added above this line.