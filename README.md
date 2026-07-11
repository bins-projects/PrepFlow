# PrepFlow

PrepFlow helps students study more effectively by transforming educational content into validated, interactive study experiences focused on mastery rather than memorization.

PrepFlow is a terminal-based study platform that transforms educational source material into validated study packs and delivers those packs through an interactive study engine.

The project is designed around a simple architectural boundary:

```text
Private Source Material
        ↓
Compiler
        ↓
Canonical PrepFlow Packs
        ↓
Study Engine
```

The compiler produces canonical PrepFlow Packs.

The Study Engine consumes only those Packs.

Private source material intentionally remains outside the repository.

---

# Features

Current capabilities include:

* Canonical compilation pipeline
* Stable PrepFlow Pack format
* Dynamic Pack discovery
* Chapter selection
* Interactive study sessions
* Randomized question order
* Block-based study
* First-pass score tracking
* Review queue until mastery
* Support for multiple question types

---

# Repository Layout

```text
compiler/    Reusable compilation pipeline

study/       Interactive terminal Study Engine

packs/       Canonical PrepFlow study packs

docs/        Project documentation

tests/       Automated tests
```

---

# Quick Start

Create and activate a virtual environment.

Install the project requirements.

Run the Study Engine.

Select:

* a study pack
* one or more chapters
* begin studying

The Study Engine automatically:

* loads the selected Pack
* shuffles questions once
* tracks first-pass performance
* reviews missed questions until mastered

---

# Documentation

The repository intentionally maintains a small set of authoritative documents.

## README.md

Project overview.

## ARCHITECTURE_BIBLE.md

Permanent technical architecture.

## RESTART_PACKET.md

Operational bootloader for ChatGPT development sessions.

## V1_RELEASE_CHECKLIST.md

Remaining work required before Version 1.

## CHANGELOG.md

Project milestone history.

## IDEAS.md

Future enhancements that should not interrupt Version 1.

---

# Design Principles

PrepFlow is built around several core principles:

* Canonical data
* Explicit validation
* Stable question identity
* Separation of concerns
* Modular architecture
* Reusable study content
* Lean repository design

The repository should become simpler over time as temporary development scaffolding is removed.

---

# Current Status

PrepFlow is in active development toward Version 1.

The current focus is completing a clean, stable, standalone terminal application before expanding the feature set.

Version 1 emphasizes reliability, maintainability, and architectural stability over rapid feature growth.

---


