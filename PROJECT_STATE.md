# PROJECT_STATE

Last Updated:
Sprint 4 Documentation Phase

---

# Current Milestone

Sprint 4 – Initial Study Engine Foundation

Status:
Documentation in progress.
---

# Current Repository Status

Git Status:
Working tree clean before documentation.

Current major folders:

```
compiler/
study/
docs/
output/
data/
tests/
```

---

# Completed Features

## Compiler

- DOCX Reader
- Tokenizer
- Parser
- Validator
- Permanent Question IDs
- JSON Export Pipeline

Output:

```
output/03_questions.json
```

---

## Study Engine

Implemented:

- Load compiled question bank
- Display questions
- Format answer choices
- Accept user answers
- Grade responses
- Display rationale
- Advance through session
- Hidden ScoreTracker

Current limitations:

- Questions presented sequentially
- No block engine
- No review queue
- No session manager

---

# Locked Product Decisions

PrepFlow is a universal study engine.

Content is provided through Packs.

The engine itself contains no subject-specific logic.

Core hierarchy:

PrepFlow
→ Pack
→ Section (optional)
→ Session
→ Block
→ Review Queue

Question IDs are permanent.

Questions are never generated.

The compiler is the single source of truth.

---

# Immediate Next Objectives

1. Finish project documentation.
2. Commit documentation.
3. Build Session Manager.
4. Build Balanced Block Engine.
5. Build Review Queue.
6. Implement Shuffle-once session generation.
7. Preserve first-attempt scoring.

---

# Long-Term Roadmap

Compiler ✓

Study Engine Foundation ✓

Documentation ← CURRENT

Session Manager

Block Engine

Review Queue

Pack Manager

Statistics

Save/Resume Sessions

GUI

Pack Creator

Public Release

---

# Notes

The Project Bible is the human-readable project resume.

PROJECT_STATE.md is the repository's living development log.

This file should be updated at the end of every coding session.