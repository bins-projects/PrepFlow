# PREPFLOW RELEASE PRESERVATION AND ROLLBACK POLICY

## Purpose

PrepFlow must always preserve the last known-good public release while a new milestone is developed, tested, documented, and released.

A major local revision must never replace the only recoverable working version.

## Protected States

PrepFlow uses three distinct protected states.

### 1. Local development

Active work is performed in:

```text
~/projects/prepflow
```

The normal development branch is:

```text
docs/continuity-rebuild
```

This state may contain unfinished or uncommitted work. It is not automatically safe for release.

### 2. Verified development checkpoint

After a coherent local milestone is approved:

1. run applicable automated tests;
2. verify the real browser workflow;
3. inspect the working tree and focused diff;
4. commit the milestone;
5. push the development branch to the private development repository;
6. push the matching development branch to the public mirror;
7. fetch both remotes;
8. verify that local, private, and public-mirror development hashes match.

The private and public-mirror development branches should normally represent the same verified development commit.

### 3. Frozen public release

A public release must be created from the exact approved development commit.

For every substantial public update:

1. create a uniquely named release branch from the approved commit;
2. never continue ordinary development on that release branch;
3. preserve the previous release branch and tag;
4. open a pull request from the new fixed release branch into public `master`;
5. review the exact release scope;
6. merge the pull request;
7. verify the deployed GitHub Pages application;
8. tag the release when appropriate;
9. record the release source commit, release branch, merge commit, and deployment verification in continuity documentation.

Example release branch:

```text
release/2026-07-26-hospital-homepage
```

Example release tag:

```text
v0.9.0
```

## Rollback Rule

The previous public version must remain recoverable after every new release.

If a new public release fails, rollback may use:

- the previous frozen release branch;
- the previous release tag;
- the previous public merge commit;
- a new rollback branch created from the last known-good release source commit;
- individual file restoration from a verified earlier commit.

Do not rebuild the application from scratch when a known-good release exists in Git history.

## Prohibited Actions

Do not:

- force-push public `master`;
- force-push a frozen release branch;
- move or rewrite a release tag;
- use a release branch for ordinary development;
- delete the previous release merely because a newer release exists;
- publish directly from an uncommitted working tree;
- treat the private development repository as a separate product version that intentionally drifts from the public-mirror development branch.

## Cleanup and Release Safety

Cleanup is part of the development process, not optional polish.

Exploratory implementation may accumulate during visual or behavioral iteration, but approved work should eventually be consolidated into a clear authoritative implementation.

Before structural cleanup:

1. create an external backup;
2. preserve the verified checkpoint in Git;
3. define the exact behavior and appearance that must remain unchanged;
4. make cleanup a focused milestone;
5. rerun automated tests;
6. verify the real browser result;
7. inspect the final diff before committing.

When immediate cleanup would create unacceptable risk to a working release candidate, the current verified implementation may be preserved and released only after:

- structural integrity checks pass;
- known debt is documented explicitly;
- cleanup is recorded as a protected next milestone rather than forgotten.

## Current Hospital-Homepage Checkpoint

The hospital-homepage development checkpoint is:

```text
e44d710ef6901b7eb4347229a5fcd0c0f6db9835
```

It is present on:

```text
bins-projects/prepflow-dev:docs/continuity-rebuild
bins-projects/PrepFlow:docs/continuity-rebuild
```

The local, private, and public-mirror development hashes were explicitly verified equal after push.

The previous public release must remain preserved until the hospital-homepage release is independently verified on GitHub Pages.

## Change Control

Update this policy when the release topology, rollback method, branch naming convention, or preservation rules change.
