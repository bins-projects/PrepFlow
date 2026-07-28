# PrepFlow Public Release — 2026-07-26 Hospital Homepage

## Release identity

```text
Release source commit: 0c69073444f55bf24eef3fa6598ffcdf4184964b
Frozen release branch: release/2026-07-26-hospital-homepage
Public pull request: bins-projects/PrepFlow#4
Public master merge commit: 587cf4c142f13daf2a2946711ef45c7d7e119584
Release date: 2026-07-26
```

The frozen release branch exists in both repositories and points to the exact tested source commit.

## What was released

- the PrepFlow Teaching Hospital homepage;
- the live Build Your Quiz launcher;
- the dedicated quiz-builder overlay;
- Fundamentals, Pharm, and Medical-Surgical book controls;
- Continue Quiz and Build a New Quiz flows;
- Drug Library control;
- save, resume, block-summary, and return-home behavior;
- updated architecture, art-system, continuity, restart, and release-policy documentation;
- a permanent pre-commit privacy gate for tracked project content.

## Verification completed

- `python -m pytest -q` completed with 72 passing tests;
- `git diff --check` passed for the release scope;
- added release content passed the privacy scan;
- the final local browser smoke test passed;
- local, private, and public release-branch hashes matched at `0c69073444f55bf24eef3fa6598ffcdf4184964b`;
- the public site was refreshed after merge and the project owner confirmed that the new hospital-homepage version was live.

## Preservation and rollback

The previous book-milestone release remains preserved as:

```text
release/2026-07-24-book-milestone
648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
```

Do not move, rewrite, or reuse either frozen release branch for ordinary development.

Active development continues on:

```text
docs/continuity-rebuild
```
