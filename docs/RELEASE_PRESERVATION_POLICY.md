# PREPFLOW RELEASE PRESERVATION AND ROLLBACK POLICY

## Purpose

PrepFlow must always preserve the last known-good public release while a new milestone is developed, tested, documented, and released.

A major local revision must never replace the only recoverable working version.

## Protected States

PrepFlow uses three distinct protected states.

### 1. Local development

Active work is performed in the local PrepFlow working copy.

The normal development branch is:

```text
docs/continuity-rebuild
```

This state may contain unfinished or uncommitted work. It is not automatically safe for release.

### 2. Verified development checkpoint

After a coherent local milestone is approved:

1. run applicable automated tests;
2. verify the real browser workflow;
3. run the privacy and artifact scan;
4. inspect the working tree and focused diff;
5. commit the milestone;
6. push the development branch to the private development repository;
7. push the matching development branch to the public mirror;
8. fetch both remotes;
9. verify that local, private, and public-mirror development hashes match.

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

## Privacy and Artifact Gate

Privacy review is an upstream development requirement, not a final release-only task.

Before every commit and again before creating a release branch:

1. scan the focused diff and tracked files for personal names, personal email addresses, usernames, device names, absolute home-directory paths, and external backup locations;
2. replace personal names with role-based language such as `the user` or `the project owner`;
3. describe external backups without recording their personal filesystem paths;
4. verify that temporary files, source documents, screenshots, exports, credentials, and unrelated artifacts are not being committed;
5. inspect the exact staged diff before committing.

Do not place personal names, personal email addresses, usernames, device names, absolute home-directory paths, or exact external-backup paths in tracked project files. Use repository-relative paths, generic local-workspace language, and role-based references instead.

Required workflow:

```text
edit → test → privacy scan → inspect diff → commit → push
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
7. run the privacy and artifact scan;
8. inspect the final diff before committing.

When immediate cleanup would create unacceptable risk to a working release candidate, the current verified implementation may be preserved and released only after:

- structural integrity checks pass;
- known debt is documented explicitly;
- cleanup is recorded as a protected next milestone rather than forgotten.

## Current Hospital-Homepage Checkpoint

The current verified hospital-homepage development checkpoint is:

```text
6d1ce05705811177fe9aaa27df93d0c6982d67ee
```

It is present on:

```text
bins-projects/prepflow-dev:docs/continuity-rebuild
bins-projects/PrepFlow:docs/continuity-rebuild
```

The local, private, and public-mirror development hashes were explicitly verified equal after push.

The previous public release must remain preserved until the hospital-homepage release is independently verified on GitHub Pages.

## Change Control

Update this policy when the release topology, rollback method, branch naming convention, privacy gate, or preservation rules change.
