# 🔥 PREPFLOW RESTART PACKET

This document is the operational restart guide for PrepFlow.

It should always reflect the **current** state of the project.

Completed history belongs in CHANGELOG.md.

GitHub is the technical source of truth.

---

# CURRENT PROJECT STATUS

PrepFlow is now a functioning terminal study application built around standardized PrepFlow Packs.

Current completed capabilities:

✓ Compiler pipeline
✓ Standard PrepFlow Pack format
✓ Pharmacy Pack
✓ Medical-Surgical Pack
✓ Dynamic Pack discovery
✓ Pack selection
✓ Chapter selection
✓ Study sessions
✓ Review queue
✓ Score tracking

Repository status:

✓ Clean
✓ Original source PDFs removed from project
✓ scratch/ ignored by Git
✓ Both GitHub mirrors synchronized

---

# PROJECT MISSION

PrepFlow is no longer simply a compiler.

PrepFlow is a study platform.

The compiler exists to generate canonical PrepFlow Packs.

The runtime application consumes only canonical Packs.

Private source material remains outside the project repository.

---

# CURRENT ARCHITECTURE

Private Source Material
        │
        ▼
Compiler
        │
        ▼
Canonical PrepFlow Packs
        │
        ▼
Study Engine
        │
        ▼
Pack Selection
        │
        ▼
Chapter Selection
        │
        ▼
Study Session
        │
        ▼
Review Queue

This architecture is considered stable.

Do not redesign without implementation evidence.

---

# EVERY DEVELOPMENT SESSION

## 1. Read this Restart Packet.

---

## 2. Perform a Top-Down Assessment.

Definition:

Top-Down Assessment means inspecting the committed GitHub mirror.

GitHub is the architectural source of truth.

Do not begin from memory.

Do not begin from local files unless debugging uncommitted work.

---

## 3. Repository Audit

Walk the project from the top down.

Inspect every major folder.

Inspect every project document.

Ask:

• Does this still serve a purpose?

• Has the project evolved beyond this?

• Is functionality duplicated elsewhere?

• Is this temporary?

Look for:

• obsolete scripts

• obsolete documents

• compatibility code

• dead architecture

• redundant outputs

• completed milestones that no longer belong

If something appears obsolete:

DO NOT DELETE IT.

Add it to a Cleanup Candidate list.

Only remove it after proving nothing depends on it.

The project should become simpler over time whenever possible.

---

## 4. Verify PROJECT_STATE.md

Confirm that PROJECT_STATE matches the committed GitHub repository.

If not:

Update PROJECT_STATE before writing code.

---

## 5. Review V1_RELEASE_CHECKLIST.md

Choose exactly ONE unchecked milestone.

Ignore future ideas.

---

## 6. Development Workflow

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

Update PROJECT_STATE

↓

Update RESTART_PACKET

↓

Repeat

---

# DEVELOPMENT RULES

GitHub is the source of truth.

Top-Down Assessment always means inspect the GitHub mirror.

One milestone at a time.

Architecture follows evidence.

Avoid speculative redesign.

Avoid feature creep.

Avoid logic loops.

Future ideas belong in IDEAS.md.

Do not optimize for hypothetical future requirements.

Prefer a functional product over architectural perfection.

---

# CURRENT VERSION 1 PRIORITIES

Current work is focused on completing the terminal version of PrepFlow.

Reference:

docs/V1_RELEASE_CHECKLIST.md

Do not begin Version 2 work until Version 1 is complete.

---

# CURRENT RUNTIME

Canonical runtime data:

packs/

    pharmacy.prepflow.json

    medical_surgical.prepflow.json

The Study Engine should consume only canonical PrepFlow Packs.

Original source material is intentionally excluded from the project.

---

# CLEANUP PHILOSOPHY

Temporary files should remain temporary.

Generated artifacts should remain reproducible.

The repository should become cleaner as the project matures.

Never keep historical files simply because they once had value.

---

# SUCCESS CRITERIA

Version 1 is complete when every item in:

docs/V1_RELEASE_CHECKLIST.md

has been completed and validated.

Only then should Version 2 planning begin.