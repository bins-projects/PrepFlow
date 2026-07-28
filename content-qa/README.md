# PrepFlow Content QA Workflow

## Purpose

The Content QA system improves PrepFlow's import pipeline without changing question content through guesswork.

It exists to:

- detect parser failures
- detect extraction damage
- detect contamination
- isolate questionable content
- develop increasingly reliable importer rules

It is not an AI rewriting system.

## Core Principle

Every automatic repair must trace back to one or more human-verified examples.

AI may:

- identify suspicious content
- classify likely repair patterns
- help design detection and repair logic
- compare results from experimental rules

AI must not invent or rewrite imported question content.

Repairs should come from the original source material whenever possible.

## Intended Workflow

Source document
→ Import
→ QA scan
→ Flagged questions
→ Human source verification
→ Verified before-and-after examples
→ Pattern discovery
→ Experimental importer rule
→ Regression tests
→ Whole-Pack validation
→ Approved automatic repair

## Before-and-After Repair Corpus

Each source-verified repair should eventually be preserved as a permanent repair case.

A repair case should record:

- question ID
- affected field
- damaged imported text
- source-verified text
- repair category
- source location
- explanation of the extraction or parser failure

These examples serve as:

- documentation
- regression-test fixtures
- evidence supporting importer rules
- protection against future parser regressions

## Example

Damaged imported text:

    medication s
    as k
    administrationroute

Source-verified text:

    medications
    ask
    administration route

These individual examples are not automatically importer rules.

A rule should be considered only after multiple verified examples demonstrate a consistent and safely recognizable pattern.

## Conservative Rule Development

Recommended progression:

One verified example
→ ledger entry only

Several similar verified examples
→ candidate repair pattern

Consistent verified pattern
→ experimental rule and regression tests

Successful whole-Pack review
→ approved importer rule

Tests must include both:

- text the rule should repair
- valid text the rule must leave unchanged

## Future Repair Workbench

A future local QA workbench may:

- load one flagged question
- display it in plain quiz format
- display the stored answer and rationale
- show all QA findings and metadata
- compare imported text, source text, and verified repair
- export approved examples into the repair corpus
- preview proposed automatic changes without modifying the official Pack

The workbench would be a development and research tool, not part of the student-facing runtime.

## General-Purpose Goal

The core importer should remain domain-neutral.

It should recognize question structure and extraction problems rather than depend on nursing terminology.

The same workflow should eventually support reasonably structured question banks from unrelated subjects, including automotive, aviation, history, and other fields.

Domain-specific logic should be limited to optional terminology checks, publisher cleanup patterns, and similar supplemental validation.

## Success Criteria

The goal is not an importer that guesses how to repair every document.

The goal is an importer that:

- detects likely problems reliably
- repairs only well-understood patterns
- leaves uncertain cases for human review
- learns from verified examples
- becomes more accurate without becoming more reckless
