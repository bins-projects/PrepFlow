# PREPFLOW VERSION 1 RELEASE CHECKLIST

## Purpose

This document contains only the remaining work required before PrepFlow
Version 1 is distributed for beta testing.

Completed milestones belong in `CHANGELOG.md`.

Future platform and interface work belongs in `IDEAS.md`.

Architecture belongs in `ARCHITECTURE_BIBLE.md`.

---

# Completed Version 1 Foundation

The following Version 1 foundations are complete and recorded in the
CHANGELOG:

* Generic compiler pipeline proven across three starting sources.
* Fundamentals, Pharmacy, and Medical-Surgical canonical Packs.
* Stable desktop study interface.
* Subject and multi-chapter selection.
* All four supported question types.
* Fifteen-question blocks and shorter final blocks.
* First-pass scoring and missed-question mastery review.
* Automatic single-slot save and resume.
* Standalone Linux x86-64 packaging proof.
* Repository and packaged-release privacy scans.
* Fifty-three passing automated tests.

---

# Remaining Release Work

## Documentation

☐ Review and update the public README for the actual desktop workflow

☐ Review `IDEAS.md` and move any completed items to the CHANGELOG

☐ Confirm the Restart Packet reflects the latest committed milestone

## Release Validation

☐ Perform a fresh-clone installation and build test

☐ Perform a clean packaged-application smoke test from the release archive

☐ Confirm generated `build/` and `dist/` files remain untracked

☐ Confirm the packaged application contains only the three intended starting categories

## Distribution

☐ Create the Linux x86-64 release archive

☐ Write short Linux extraction and launch instructions

☐ Decide whether the Linux proof build is suitable for limited beta distribution

☐ Build and test separate releases on each additional supported desktop operating system

## Version Control

☐ Commit final Version 1 release documentation

☐ Push the private repository

☐ Push the public mirror

☐ Confirm both remote branch hashes match

☐ Create the Version 1 release tag

## Future Platform Track

The iPad-compatible frontend is a later platform milestone. A normal
macOS desktop build will not run on iPadOS. The proven PrepFlow Packs,
study rules, scoring behavior, mastery flow, and save-state design should
be reused when that frontend begins.

---

# Definition of Done

PrepFlow Version 1 is ready for limited beta distribution when:

* the repository documentation accurately describes the working product;
* a fresh environment can build the application;
* the release archive passes a clean smoke test;
* privacy validation remains clean;
* both Git remotes match;
* and the Version 1 release is tagged.
