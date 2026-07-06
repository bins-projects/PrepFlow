# PrepFlow Restart Packet

## Read First

Repository documentation is the source of truth.

Read these first, in order:

1. docs/PROJECT_STATE.md
2. docs/CHANGELOG.md
3. docs/VISION.md
4. docs/ARCHITECTURE_BIBLE.md
5. docs/DOMAIN_MODEL.md
6. docs/PACK_SPEC.md
7. docs/QUESTION_LIFECYCLE.md
8. docs/RESTART_PACKET.md

---

# Current Project Status

Project: PrepFlow

Version: 0.7.0

Sprint: 7 — Canonical Compiler Architecture

Status:

Sprint 7 is actively separating PrepFlow into clean architectural layers:

1. Import Layer
2. Canonical Compiler Pipeline
3. Application Layer

The production importers are complete and validated.

Current work focuses on compiler architecture, canonical objects, reusable pipeline design, and eventually connecting the Study Engine to canonical Packs.

---

# Major Architecture Direction

PrepFlow should be treated as:

## Library first

Core compiler behavior should live in reusable modules and functions.

## Application second

CLI, Study Engine, tests, future GUI, and future API should all call the same core library code.

---

# Current Architecture

## Import Layer

Responsible for turning source material into parsed question dictionaries.

Current inputs:

- DOCX
- Existing JSON question banks

Future inputs may include:

- PDF
- CSV
- AI-assisted imports

Current parsed outputs already exist in:

- output/medsurg_questions.json
- output/pharm_questions.json
- output/pharm_ch15_20_questions.json
- output/pharm_ch13_17_questions.json

---

## Canonical Compiler Pipeline

Current target pipeline:

Reader / Loader

↓

Tokenizer / Parser when needed

↓

Validator

↓

Deduplicator

↓

Builder

↓

Canonical Pack

↓

Exporter

---

# Completed Before This Session

## Production Importers

### Medical-Surgical Importer

Status:

Production Ready

### Pharmacy Importer

Status:

Production Ready

Validation:

- Chapters: 24
- Questions: 1076

---

## Canonical Domain Model

Implemented in:

compiler/models.py

Canonical dataclasses:

- Answer
- Origin
- Content
- Classification
- Metadata
- Question
- Pack

Design Rule:

Pack owns Questions.

Question does NOT own pack_id.

---

## Canonical Builder

Implemented in:

compiler/builder.py

Functions:

- build_question()
- build_questions()
- build_pack()

Purpose:

Convert parsed question dictionaries into canonical PrepFlow objects.

---

## Stable Question IDs

Implemented in:

compiler/ids.py

Format:

PFQ-000000001

PFQ-000000002

...

Publisher-independent.

---

## Schema Inspector

Implemented in:

tools/schema_inspector.py

Reports:

- field coverage
- question types
- choice counts
- answer counts

---

# Completed This Session

## Validator Diagnostics Improved

File:

compiler/validator.py

Validator now reports duplicate issues with both:

- the duplicate question
- the original question it duplicates

Examples:

- duplicate question number with original question number
- duplicate question text with original question number and stem preview

Validator still only diagnoses problems.

Validator does NOT repair source data.

---

## Deduplicator Added

File:

compiler/deduplicator.py

Added:

- DeduplicationResult dataclass
- deduplicate_questions()

Rules:

- Keep first occurrence
- Remove later duplicate question numbers
- Remove later duplicate stems
- Report every removal
- Do not repair missing source data

---

## Pipeline Added

File:

compiler/pipeline.py

Added:

- CompilationResult dataclass
- compile_questions()

Purpose:

Compile parsed question dictionaries into a canonical Pack through the canonical pipeline.

Current responsibility:

- Validate questions
- Return problems if validation fails
- Deduplicate questions
- Build canonical Questions
- Build canonical Pack
- Return CompilationResult

Pipeline does NOT know about:

- DOCX files
- JSON file paths
- command-line arguments
- printing
- sys.exit()

---

## CLI Partially Refactored

File:

compiler/cli.py

Current improvements:

- Supports DOCX input
- Supports JSON input
- Validation now happens before canonical building
- Deduplication stage inserted before building
- Duplicate removals are printed when present

Important:

The CLI still duplicates some pipeline behavior.

Next task is to refactor CLI so it calls compiler.pipeline.compile_questions() instead of running validation, deduplication, and building itself.

---

# Current Known Files Changed

Expected modified files:

- compiler/cli.py
- compiler/validator.py
- docs/RESTART_PACKET.md
- study/cli.py
- study/question.py

Expected new files:

- compiler/deduplicator.py
- compiler/pipeline.py

Expected untracked directory:

- exports/

Note:

study/cli.py and study/question.py contain intentional earlier Study Engine work, including command-line JSON loading and improved question formatting/parsing. Do not revert them unless specifically reviewing that work.

---

# Known Source Data Issues

## Question 80

Missing:

- correct answer
- rationale

Confirmed missing from source document.

This is NOT:

- parser bug
- builder bug
- validator bug

Source data requires repair or exclusion.

---

## Duplicate Question Block

Questions:

41–60

Validator reports:

- duplicate question numbers
- duplicate stems

Likely duplicated block inside original source document.

Investigate source before implementing aggressive automatic deduplication.

---

## Duplicate Stems

Questions:

117

156

Require investigation.

---

# Current Functional Scope

Do not add more sources or banks yet.

Initial target functionality:

## Source selection

- Pharm
- Med-Surg

## Chapter selection

- One chapter
- Multiple chapters
- All chapters

Deferred until later:

- topic search
- body system tagging
- mixed-source topic packs
- advanced filtering
- additional publishers/books

---

# Immediate Next Task

Refactor:

compiler/cli.py

Goal:

CLI should use:

compiler.pipeline.compile_questions()

Instead of duplicating:

- validate_questions()
- deduplicate_questions()
- build_questions()
- build_pack()

Desired structure:

DOCX path:

- read_docx()
- tokenize()
- parse_questions()
- compile_questions()
- print result

JSON path:

- load JSON
- compile_questions()
- print result

---

# Upcoming Sprint Objectives

1. Refactor CLI to call pipeline.compile_questions().
2. Add clean result-printing helpers for CompilationResult.
3. Add unit tests for:
   - validator
   - deduplicator
   - pipeline
   - builder
4. Build canonical exporter.
5. Connect Study Engine to exported canonical Packs.
6. Preserve source/chapter selection as the first Study Engine goal.
7. Do not expand to new banks until Pharm and Med-Surg selection works.

---

# Architecture Rules

Parser parses.

Validator validates.

Deduplicator deduplicates.

Builder builds.

Exporter exports.

Pack owns Questions.

Question never owns Pack.

Never silently repair source data.

Prefer diagnostics over hidden fixes.

Each compiler stage has exactly one responsibility.

Core logic should be reusable outside the CLI.

PrepFlow should be library-first.

---

# Development Workflow Rules

When modifying existing code:

1. Find the exact code.
2. Replace the exact code.
3. Save.
4. Compile.
5. Wait for confirmation before continuing.

Prefer replacing an entire file when performing significant refactoring.

Avoid vague instructions such as:

- near the top
- toward the bottom
- around line...

Use exact code landmarks instead.

---

# VS Code File Creation Rule

When creating a new file in VS Code:

Do NOT paste a path such as:

compiler/deduplicator.py

into the new-file prompt.

Instead:

1. Click the correct existing folder first.
2. Choose New File.
3. Enter only the filename.

Example:

Click compiler folder.

Create new file named:

deduplicator.py

Reason:

Pasting full paths into VS Code has caused accidental nested folders in prior sessions.

---

# Study Engine Protection Rule

Until compiler migration is complete:

Do not modify study/ files unless explicitly working on the Study Engine.

Known intentionally modified Study Engine files:

- study/cli.py
- study/question.py

These changes appear to be from earlier sessions and should be preserved unless reviewed directly.

---

# Session Completion Rule

Every coding session ends by completely replacing:

docs/RESTART_PACKET.md

The restart packet is NEVER appended to.

It is rewritten from scratch after reviewing:

- PROJECT_STATE.md
- CHANGELOG.md
- current architecture
- session accomplishments
- current objectives

The restart packet must always represent the current state of the project.

It is the primary bootstrap document for beginning every new ChatGPT development session.

---

# Documentation Responsibilities

VISION.md

Why PrepFlow exists.

Rarely changes.

ARCHITECTURE_BIBLE.md

How PrepFlow is designed.

Changes occasionally.

PROJECT_STATE.md

Current project status.

Updated at milestone completion.

CHANGELOG.md

Historical record.

Always appended.

Never rewritten.

RESTART_PACKET.md

Current working state.

Completely rewritten at the end of every coding session.

Single source of truth for resuming development.

---

# Before Closing This Session

Run:

python -m py_compile compiler/validator.py
python -m py_compile compiler/deduplicator.py
python -m py_compile compiler/pipeline.py
python -m py_compile compiler/cli.py

Then:

git status
git add .
git commit -m "Advance canonical compiler pipeline architecture"
git push