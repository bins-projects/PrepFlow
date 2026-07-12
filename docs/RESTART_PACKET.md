# PREPFLOW RESTART PACKET

## Purpose

This document is ChatGPT’s operational bootloader for resuming PrepFlow development.

It restores:

- the current project state;
- permanent working rules;
- the latest verified milestones;
- the active cold-import experiment;
- the exact next implementation target.

This is not the permanent architecture document.

Permanent technical truth belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

The committed GitHub repository is the technical source of truth.

Memory and this packet are secondary.

If the packet conflicts with the committed repository:

1. inspect the committed repository;
2. trust the committed implementation;
3. correct this packet.

---

# Source of Truth

Primary technical source:

```text
Private repository:
https://github.com/bins-projects/prepflow

Public mirror:
https://github.com/bins-projects/PF-O
```

Expected branch:

```text
master
```

Both remotes should normally point to the same commit.

Before requesting terminal output, pasted code, local files, or helper scripts, first ask:

> Can the committed GitHub repository answer this?

Use GitHub first whenever the required information is committed.

Request local inspection only when:

- work is uncommitted;
- runtime behavior must be observed;
- tests must run;
- dependencies must be inspected;
- private source material must be examined;
- generated import artifacts are intentionally untracked;
- GitHub genuinely cannot answer.

---

# Working Discipline

PrepFlow development follows:

```text
Observe
   ↓
Inspect
   ↓
One focused change
   ↓
Save
   ↓
Compile or Build
   ↓
Run
   ↓
Verify
   ↓
Commit
   ↓
Push private remote
   ↓
Push public mirror
   ↓
Repeat
```

Do not:

- make several speculative changes at once;
- redesign working architecture during debugging;
- create a separate importer for every book;
- reopen architectural decisions without implementation evidence;
- collect endless diagnostics instead of executing;
- introduce a graphical interface before the underlying pipeline works;
- allow ideas to interrupt the current Version 1 milestone.

When Charlie says:

> next

perform or provide exactly the next executable step.

Do not merely describe the next step.

---

# Focus and Loop Prevention

If work becomes repetitive or confusing:

1. stop;
2. return to the current architectural boundary;
3. identify the smallest executable action;
4. execute it;
5. verify before continuing.

Warning signs of a logic loop include:

- repeated `grep` commands without a new decision;
- inspecting the same files repeatedly;
- proposing multiple architectures;
- expanding the plan instead of implementing the current stage;
- repeatedly explaining why the project is important;
- creating abstractions before testing a real source;
- asking Charlie to paste information already available from GitHub.

The current work is evidence-driven.

Real source material determines importer requirements.

---

# Permanent Product Goal

PrepFlow’s main purpose is:

> Give PrepFlow educational source material and make it study-able.

The user should eventually be able to choose a source and use a simple action such as:

> Import and Create Module

The intended user workflow is:

1. choose a source file;
2. enter or confirm the module title;
3. enter or confirm the Pack ID;
4. start import;
5. allow PrepFlow to extract, clean, detect, parse, validate, and build;
6. review an import report;
7. receive a canonical PrepFlow Pack;
8. see the new Pack on the home screen;
9. select chapters;
10. begin studying.

The user should not need to understand Python scripts or compiler internals.

The interface must wrap a proven compiler pipeline.

Do not build the button before the full pipeline works end-to-end.

---

# Permanent Architecture

PrepFlow’s stable architecture is:

```text
Private Source Material
        ↓
Source Adapter
        ↓
Extract
        ↓
Clean
        ↓
Detect Structure
        ↓
Parse
        ↓
Normalize
        ↓
Validate
        ↓
Recover usable questions
        ↓
Deduplicate
        ↓
Assign stable IDs
        ↓
Build canonical Pack
        ↓
Export
        ↓
PrepFlow Study Engine
```

The importer is:

- format-aware;
- subject-agnostic.

PrepFlow must not require separate permanent importers such as:

```text
import_pharmacy.py
import_medsurg.py
import_maternity.py
import_pediatrics.py
import_auto_repair.py
```

Pharmacy, Medical-Surgical, Fundamentals, Maternity, and other subjects are Pack content and metadata.

They are not separate application architectures.

---

# Repository Boundaries

Permanent product areas are:

```text
compiler/
study/
packs/
tests/
docs/
README.md
requirements.txt
```

The repository must not contain:

- copyrighted private source PDFs;
- private DOCX source files;
- scratch extraction files;
- recovered pre-anonymization repositories;
- temporary importer snapshots;
- personal identifying information;
- personal email addresses;
- personal machine paths embedded in project content;
- PyInstaller build output;
- executable artifacts;
- obsolete one-time book-specific scripts.

Private source files should remain outside the repository.

Current source storage convention:

```text
~/projects/prepflow-sources/
```

Generated cold-import artifacts currently live under:

```text
output/imports/<pack-id>/
```

These are working artifacts and should not automatically be committed.

---

# Git and Privacy State

The repository history was rewritten before beta release.

All reachable commit author and committer metadata was replaced with:

```text
PrepFlow <bins-projects@users.noreply.github.com>
```

Historical personal identifiers were removed.

Historical private or temporary paths removed from reachable Git history include:

```text
cardiac questions.docx
scratch/medsurg_clean.txt
scratch/medsurg_module_test.json
scratch/medsurg_raw.txt
scratch/pharm_clean.txt
scratch/pharm_module.json
scratch/pharm_module_preview.json
scratch/pharm_raw.txt
```

Local, private, and public branch hashes were verified after the rewrite.

The pre-anonymization recovery bundle is stored at:

```text
~/projects/prepflow-before-anonymization.bundle
```

This bundle contains:

- the original commit history;
- Charlie’s former author name;
- Charlie’s personal email;
- deleted historical scratch data;
- deleted historical source files.

It must remain private.

It must never be:

- uploaded to GitHub;
- included in a release;
- sent to classmates;
- placed inside the repository;
- packaged with PrepFlow.

It may be deleted later when Charlie is fully confident the sanitized history is no longer needed.

The terminal prompt:

```text
charliekeila@penguin
```

is only the local Linux username and Chromebook Linux hostname.

It is not Git commit identity and is not automatically published.

---

# Current Repository State

Latest confirmed committed importer milestone:

```text
9435a41 Add generic source cleaning and structure detection
```

At that milestone:

- local `master` was clean;
- private `origin/master` was pushed;
- public `public/master` was pushed.

Before resuming, verify GitHub rather than assuming this commit is still current.

---

# Completed Major Milestones

## Canonical Compiler and Packs

PrepFlow has canonical production Packs for:

```text
packs/pharmacy.prepflow.json
packs/medical_surgical.prepflow.json
```

Pharmacy pipeline was previously proven through:

```text
PDF
→ Extract
→ Clean
→ Parse
→ Write
→ Canonical PrepFlow Pack
```

Pharmacy Pack contains approximately:

```text
1,084 questions
```

Medical-Surgical Pack contains:

```text
1,435 questions
```

Supported question types include:

- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response.

Known residual source branding was removed from the committed Packs.

The Pharmacy Pack’s remaining TCPDF fragment was removed.

A subsequent branding scan returned no remaining known strings such as:

- Stuvia;
- Downloaded by;
- Powered by TCPDF;
- Distribution of this document is illegal;
- Want to earn;
- Docsity notices.

---

## Medical-Surgical Chapter Cleanup

Medical-Surgical chapter display names originally contained source-title fragments such as:

```text
Linton:
Medical-
Medical-Surgical
```

The committed Pack was cleaned.

Results:

```text
527 chapter-title occurrences corrected
1,435 questions preserved
0 malformed chapter display names remaining
JSON remained valid
```

Examples corrected include:

```text
Acute Lower Respiratory Tract Disorders Linton:
→ Acute Lower Respiratory Tract Disorders

Cerebrovascular Accident Linton: Medical-
→ Cerebrovascular Accident

Medical-Surgical Patients: Individuals, Families, and
→ Medical-Surgical Patients: Individuals, Families, and Communities

Spinal Cord Injury Linton: Medical-Surgical
→ Spinal Cord Injury
```

Important lesson:

Removing unwanted question or answer blocks is not enough.

Branding and source-header cleanup require separate final-output validation.

---

## Study Engine

The Study Engine currently supports:

- dynamic Pack discovery;
- Pack selection;
- chapter selection;
- randomized question order;
- block-based study sessions;
- first-pass scoring;
- missed-question review;
- review until mastery;
- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response.

Any valid canonical Pack added to:

```text
packs/*.prepflow.json
```

should appear dynamically in Pack selection.

Adding a subject must not require Study Engine changes.

---

## Standalone Packaging

Linux standalone packaging was proven with PyInstaller using an on-directory build.

The packaged runtime successfully:

- launched;
- located bundled Packs;
- displayed Medical-Surgical;
- displayed Pharmacy.

The loader was corrected to support:

- source execution from the repository;
- packaged execution using PyInstaller’s runtime bundle location.

Ignored packaging artifacts include:

```text
build/
dist/
*.spec
```

A Windows executable has not yet been built.

PyInstaller is not a cross-compiler, so Windows packaging requires a Windows environment.

Do not begin beta distribution until all release checks are satisfied.

---

# Recovered Importer History

During cleanup, the original prototype PDF importer tools were removed from the active repository.

This unintentionally removed an integral proven capability.

The tools were not lost.

They were recovered from:

```text
~/projects/prepflow-before-anonymization.bundle
```

Recovery repository:

```text
~/projects/prepflow-importer-recovery
```

Recovered snapshot:

```text
~/projects/prepflow-importer-snapshot
```

Recovered historical files included:

```text
tools/build_source_module.py
tools/clean_pharm_text.py
tools/extract_text.py
tools/find_duplicates.py
tools/import_medsurg_bank.py
tools/import_pharm_bank.py
tools/parse_pharm_module.py
tools/schema_inspector.py
tools/write_source_module.py
```

The last functional historical importer state inspected was:

```text
3334f04 Validate source pipeline on medical surgical bank
```

The recovered scripts proved:

- PDF text extraction;
- cleaning;
- chapter splitting;
- section detection;
- numbered-question splitting;
- choice parsing;
- answer extraction;
- rationale extraction;
- metadata collection;
- Pack writing.

However, the recovered scripts were partially book-specific.

They included hardcoded:

- source paths;
- output paths;
- source names;
- ID prefixes;
- Pharmacy or Med-Surg assumptions.

Decision:

> Recover the proven behavior, but do not restore the book-specific architecture.

The permanent importer is being rebuilt inside `compiler/` as generic, tested components.

---

# Current Generic Importer Components

## PDF Source Adapter

Committed file:

```text
compiler/pdf_reader.py
```

Purpose:

- accept a text-based PDF;
- extract text faithfully;
- reject missing sources;
- reject non-PDF inputs;
- report PDFs with no extractable text.

Dependency:

```text
pypdf==6.14.2
```

Scanned-image PDFs are not yet supported.

They may require a future OCR adapter.

Do not add OCR until a real source proves it is needed.

---

## Import Orchestrator

Committed file:

```text
compiler/importer.py
```

Current responsibilities:

- validate import request;
- validate Pack ID;
- detect source type;
- call the correct source adapter;
- create an import workspace;
- preserve raw extraction;
- run cleaning;
- preserve cleaned text;
- run structure detection;
- preserve detection report.

Current request model includes:

```text
source_path
pack_id
title
workspace_root
```

Pack IDs currently allow lowercase letters, numbers, hyphens, and underscores.

---

## Generic Cleaner

Committed file:

```text
compiler/cleaner.py
```

Current proven generic behaviors include:

- removing full-line Docsity notices;
- removing inline Docsity notices while preserving legitimate metadata;
- removing known Stuvia/TCPDF/download notice patterns;
- collapsing excessive blank lines;
- removing a leading table-of-contents-style chapter index when the real first chapter repeats later.

The cleaner must remain conservative.

It should remove extraction contamination without casually rewriting:

- stems;
- choices;
- correct answers;
- rationales;
- educational metadata.

Current cleaned artifact:

```text
output/imports/<pack-id>/02_clean.txt
```

---

## Structure Detector

Committed file:

```text
compiler/detector.py
```

The detector currently reports:

- chapter-heading count;
- question-like start count;
- recognized section headers;
- recognized answer markers;
- recognized metadata markers.

Recognized section headers currently include:

```text
MULTIPLE CHOICE
MULTIPLE RESPONSE
COMPLETION
ORDERING
```

Recognized answer marker:

```text
ANS:
```

Recognized metadata markers include:

```text
DIF:
OBJ:
TOP:
MSC:
KEY:
NCLEX:
```

The detector does not parse questions.

It measures available structure.

Current artifact:

```text
output/imports/<pack-id>/03_detection.json
```

---

# Cold Import Experiment

The first completely unseen source selected for the new generic importer is a Fundamentals of Nursing test bank.

Private source path:

```text
~/projects/prepflow-sources/docsity-test-bank-for-fundamentals-of-nursing-active-learning-for-collaborative-practice-3rd-edi-11.pdf
```

This PDF must never be committed.

Desired module:

```text
Pack ID: fundamentals
Title: Fundamentals of Nursing
```

The cold import must begin from the original PDF.

Do not manually pre-clean or convert it before testing PrepFlow.

The purpose is to determine whether PrepFlow can truly:

> accept a source and make it study-able.

---

# Cold Import Progress

The unseen Fundamentals PDF successfully completed:

```text
PDF
   ↓
Extract
   ↓
Clean
   ↓
Detect
```

Raw extraction results:

```text
Characters extracted: 1,162,282
Artifact: output/imports/fundamentals/01_raw.txt
```

The raw text included:

- Docsity branding;
- Docsity URLs;
- a leading chapter table of contents;
- repeated chapter headings;
- real test-bank content;
- answer markers;
- metadata markers.

The generic cleaner removed:

- full-line Docsity notices;
- inline Docsity share notices;
- the leading duplicate chapter index;
- excess blank lines.

Verification:

```text
Docsity remaining after cleaning: 0
```

Clean artifact:

```text
output/imports/fundamentals/02_clean.txt
```

---

# Fundamentals Detection Results

Initial detection incorrectly reported:

```text
85 chapter-like headings
```

Investigation proved:

- chapters 1–42 appeared in a leading chapter index;
- chapters 1–42 appeared again as real content;
- the cover line `Chapter 1-42 Latest Version` was falsely counted.

Generic fixes were implemented:

1. remove a leading sequential chapter index when the first chapter repeats later;
2. exclude chapter-range lines from chapter-heading counts.

Final verified detection:

```text
chapter_count=42
section_headers=('MULTIPLE CHOICE', 'MULTIPLE RESPONSE')
answer_markers=('ANS:',)
metadata_markers=('DIF:', 'OBJ:', 'TOP:', 'MSC:')
question_count=1046
```

The detector identified approximately:

```text
1,046 question-like starts
```

This count is evidence, not yet the final parsed-question total.

No Fundamentals-specific cleaner or importer was created.

All changes were generic.

---

# Automated Tests

The latest reported test run after detector refinement was:

```text
17 passing
```

Tests now cover at least:

- Multiple Response answer-order behavior;
- Ordered Response order preservation;
- PDF adapter missing-file rejection;
- PDF adapter non-PDF rejection;
- source-type detection;
- invalid Pack ID rejection;
- raw artifact writing;
- clean artifact writing;
- detection report writing;
- Docsity line removal;
- inline Docsity removal;
- normal-content preservation;
- leading chapter-index removal;
- chapter-range exclusion;
- extract-to-clean integration;
- basic structure detection.

At startup, rerun:

```bash
python3 -m pytest -v
```

Trust the current output over the historical count in this packet.

---

# Exact Current Pipeline State

Completed:

```text
Source selection
      ↓
PDF source adapter
      ↓
Raw extraction
      ↓
Generic cleaning
      ↓
Generic structure detection
```

Not yet implemented for the new generic importer:

```text
Generic parsing
      ↓
Parser diagnostics/report
      ↓
Canonical normalization
      ↓
Validation
      ↓
Recovery/filtering
      ↓
Deduplication
      ↓
Stable ID assignment
      ↓
Pack build
      ↓
Deterministic rebuild comparison
      ↓
Study Engine verification
```

---

# Exact Next Milestone

The next implementation milestone is:

> Build the generic parser and continue the Fundamentals cold import.

Do not perform another top-down architecture discussion unless the committed repository reveals a conflict.

Do not build UI yet.

Do not add another source adapter yet.

Do not create a Fundamentals-specific parser.

The parser must use real evidence from:

```text
output/imports/fundamentals/02_clean.txt
```

The next session should inspect representative real boundaries for:

- chapter heading;
- section heading;
- numbered question start;
- choices;
- `ANS:`;
- rationale;
- metadata;
- transition to the next question.

Then implement the smallest useful generic parsing stage.

---

# Parser Responsibilities

The generic parser should produce structured source-derived question dictionaries.

Expected fields include:

```text
chapter
chapter_title
section
source_question_number
question_type
stem
choices
answer
rationale
metadata
```

Parsing and canonicalization are separate responsibilities.

The parser should not:

- assign final canonical IDs prematurely;
- export the final Pack directly;
- invent missing answers;
- invent missing rationales;
- silently discard unknown structures;
- contain subject names in control flow.

The parser should preserve enough raw context to diagnose failures.

---

# Parser Strategy

Proceed incrementally.

Recommended sequence:

1. inspect one complete real Multiple Choice question block;
2. inspect one real Multiple Response question block;
3. identify chapter boundaries;
4. identify section boundaries;
5. split numbered question blocks;
6. parse one supported block into a source-derived structure;
7. write tests from the real observed grammar;
8. run against the full cleaned source;
9. produce counts and diagnostics;
10. improve one observed failure at a time.

Do not attempt the entire parser in one speculative change.

---

# Parser Report Requirement

The generic parser should eventually produce a report containing evidence such as:

```text
chapters parsed
question blocks detected
questions parsed successfully
Multiple Choice count
Multiple Response count
Completion count
Ordered Response count
unknown section count
missing stem count
missing choices count
missing answer count
missing rationale count
metadata-marker count
unparsed block count
```

The purpose is measurable trust.

PrepFlow should expose uncertainty rather than silently generate a bad Pack.

---

# Determinism Requirement

After the Fundamentals Pack is successfully built:

1. build it once;
2. save the output hash;
3. build it again from unchanged input;
4. compare outputs;
5. confirm stable IDs;
6. confirm identical canonical content.

An unchanged source must produce deterministic output.

---

# Fundamentals Completion Criteria

The cold Fundamentals import is complete only when:

- the original PDF enters the generic pipeline;
- branding and extraction noise are cleaned;
- exactly 42 real chapters are represented;
- question structures are parsed;
- unsupported structures are explicitly reported;
- answers and rationales are preserved;
- validation results are acceptable;
- IDs are stable;
- two builds match;
- `packs/fundamentals.prepflow.json` is produced;
- the Pack appears in Study Engine selection;
- chapter selection works;
- sample questions can be completed correctly;
- no private source material is committed.

Only then should Fundamentals be considered a core Pack.

---

# Core Pack Direction

Pharmacy and Medical-Surgical were the first production sources.

They are not a permanent two-Pack scope limit.

Charlie has additional important books intended for the core library.

Possible future subjects may include:

- Fundamentals;
- Maternity;
- Pediatrics;
- Mental Health;
- other nursing subjects;
- non-nursing educational material.

Every new core source should pass the same standards:

- generic import where possible;
- explicit diagnostics;
- preserved educational fidelity;
- valid canonical Pack;
- stable IDs;
- runtime verification;
- no private source leakage.

The Study Engine should remain subject-neutral.

---

# User-Facing Import Requirement

After the underlying pipeline works end-to-end, create an easy import workflow.

Possible interface wording:

```text
Import and Create Module
```

The user should not need to:

- manually create source folders;
- run Python heredocs;
- understand extraction stages;
- execute separate cleaner scripts;
- write Pack JSON;
- know compiler module names.

The user-facing workflow should collect:

```text
Source file
Module title
Pack ID
```

Then display progress such as:

```text
Extracting
Cleaning
Detecting structure
Parsing
Validating
Building Pack
```

The final screen should provide:

- import summary;
- warnings;
- error locations;
- question counts;
- chapter counts;
- output Pack location;
- option to study the Pack.

This is a core usability requirement.

It is not the next coding milestone.

---

# Documentation State

The Architecture Bible was replaced at this stopping point to reflect the permanent importer architecture.

The Restart Packet is being replaced with this document.

After saving both documents:

1. run tests;
2. run `git diff --check`;
3. inspect the diff stat;
4. commit both;
5. push both remotes;
6. confirm a clean working tree;
7. stop.

The README should not yet document a polished import command because the end-to-end command/interface does not exist.

Update the README when users can actually run the supported import workflow.

---

# Version 1 Checklist Philosophy

`docs/V1_RELEASE_CHECKLIST.md` should contain only unfinished Version 1 work.

Completed milestones belong in:

```text
docs/CHANGELOG.md
```

Permanent architecture belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

Operational handoff belongs here.

Future ideas belong in:

```text
docs/IDEAS.md
```

Do not allow documentation to duplicate itself.

---

# Immediate Stopping Procedure

After replacing the Architecture Bible and Restart Packet, run:

```bash
python3 -m pytest -v
git diff --check
git diff --stat
```

If tests pass and the documentation diff is valid:

```bash
git add docs/ARCHITECTURE_BIBLE.md docs/RESTART_PACKET.md

git commit -m "Refresh architecture and importer handoff"

git push origin master
git push public master

git status
```

Expected final state:

```text
On branch master
nothing to commit, working tree clean
```

Do not continue into parser implementation during this stopping procedure.

---

# Startup Procedure for the Next Session

At the beginning of the next PrepFlow session:

1. inspect the committed public GitHub mirror;
2. verify the current branch and latest commit;
3. compare the Architecture Bible to implementation;
4. verify working-tree cleanliness;
5. run the automated test suite;
6. confirm the private Fundamentals PDF still exists outside the repository;
7. confirm `02_clean.txt` is available or regenerate it;
8. inspect representative parser boundaries;
9. implement exactly one generic parser improvement;
10. test, commit, and push.

The first terminal inspection should focus on real cleaned Fundamentals text around:

```text
Chapter
MULTIPLE CHOICE
1.
a.
b.
ANS:
DIF:
OBJ:
TOP:
MSC:
```

The next implementation target is the generic parser.

---

# Exact Resume Statement

Resume PrepFlow from this statement:

> The generic importer is committed through PDF extraction, generic cleaning, and generic structure detection. A completely unseen Fundamentals PDF successfully produced clean text with zero remaining Docsity notices and a correct 42-chapter detection report. Approximately 1,046 question-like starts were detected, with Multiple Choice and Multiple Response sections plus ANS, DIF, OBJ, TOP, and MSC markers. The next milestone is to inspect real cleaned question boundaries and implement the first small, generic parser stage without adding book-specific logic.

---# Current Milestone Update: Pharmacy Compiler Validation

## Completed

Commit:
- b292d30 — compiler: improve source cleanup parsing and validation

Verified:
- Pharmacy source pipeline runs.
- Parser recovers missing A choices caused by extraction.
- Cleaner removes source contamination.
- Validator duplicate identity includes question type.
- 37 tests passing.

## Current Discovery

During Pharmacy validation, duplicate source blocks were detected.

Important:
This appears to be a missing pipeline stage, not a parser failure.

Current intended flow:

Extract
↓
Clean
↓
Parse
↓
Normalize
↓
Deduplicate
↓
Validate
↓
Build Pack

## Next Focused Milestone

Implement lightweight exact deduplication.

Rules:
- Remove exact duplicates only.
- Preserve clinically different questions.
- Do not solve duplicates by weakening validation.
- Do not redesign the parser.

Use top-down assessment before implementation.

# Final Operating Reminder

One focused change at a time.

Use GitHub first.

Let real sources provide evidence.

Do not create subject-specific importers.

Do not build the user-facing button before the pipeline works.

Do not lose educational fidelity for convenience.

When Charlie says:

> next

perform the next executable step.