# PREPFLOW RESTART PACKET

## Purpose

This is the primary handoff for every new PrepFlow development session.

> **Mandatory first action:** Read this entire file before proposing a command or changing a PrepFlow file.

For visual or release work, also read:

```text
docs/ART_SYSTEM.md
docs/RELEASE_PRESERVATION_POLICY.md
docs/RELEASE_2026-07-24_BOOK_MILESTONE.md
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

`VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` describes the previous city-and-nurses homepage milestone. It is historical context, not the active implementation target.

The local repository at `~/projects/prepflow` is the active working copy. For visual work, the rendered local application is part of the source of truth.

---

# 1. Current Topology

## Active development

```text
Local repository: ~/projects/prepflow
Active branch: docs/continuity-rebuild
Private development repository: bins-projects/prepflow-dev
Public mirror repository: bins-projects/PrepFlow
Public mirror development branch: docs/continuity-rebuild
Verified synchronized development commit: 69ce6a70f8e8aead9afebc0c260b4572a6ab0fbd
```

Daily work continues on `docs/continuity-rebuild`, not on public `master` and not on a frozen release branch.

## Current public production

```text
Repository: bins-projects/PrepFlow
Branch: master
Observed public master after fetch: c58da62
Public site: https://bins-projects.github.io/PrepFlow/web/
```

The public site currently uses the older three-book homepage. It remains functional. Books can appear dimmed while a saved quiz is active; restarting or clearing the saved quiz restores the normal category-selection state.

## Previous frozen release

```text
Release source snapshot: 648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
Release branch: release/2026-07-24-book-milestone
Original public merge commit: 8e8e85b1e9b9604d257b6db52e9bb802fcb91fce
```

The previous release branch must remain preserved. Do not move, reuse, or continue ordinary development on it.

---

# 2. Authority Order

Use this order:

1. Charlie's explicit approval or correction.
2. The rendered local application for visual and interaction truth.
3. The local repository, active branch, working tree, and local-only files.
4. `docs/RESTART_PACKET.md` for current topology and resume procedure.
5. `docs/RELEASE_PRESERVATION_POLICY.md` for release, rollback, and protected-state rules.
6. `docs/ART_SYSTEM.md` for durable visual and asset-ownership rules.
7. The private development branch for the last committed development state.
8. The public mirror development branch for synchronization and release preparation.
9. Public `master` for the currently deployed production state.
10. Dated visual and release documents for historical context.

When sources conflict:

1. stop before modifying anything;
2. inspect `git status --short --branch` locally;
3. identify the newest relevant source;
4. inspect the rendered result;
5. ask Charlie when approval remains ambiguous;
6. update continuity after resolving the conflict.

Never overwrite newer local work merely because GitHub contains an older committed copy.

---

# 3. Local-First Development Rule

Use the local working copy to:

- inspect and edit application files;
- run automated tests;
- run the local browser server;
- verify real layout and behavior;
- preserve local visual experiments before commitment;
- inspect exact diffs before checkpoints and releases.

Use GitHub to:

- inspect committed baselines and history;
- make large documentation changes without long terminal heredocs;
- preserve verified checkpoints;
- synchronize intended remotes;
- create fixed release branches and pull requests;
- verify branch and release hashes.

For implementation work, do not reconstruct the project from repeated snippets when the real local files are available.

---

# 4. Product State

PrepFlow is a browser-centered nursing study application built around validated question Packs.

Active browser product:

```text
web/
```

Official starting Packs:

```text
packs/fundamentals.prepflow.json
packs/pharmacy.prepflow.json
packs/medical_surgical.prepflow.json
```

User-facing names:

```text
Fundamentals
Pharm
Medical-Surgical
```

Read exact question counts from the current Pack files rather than stale documentation.

The browser application is the active product. Removed Tkinter, PyInstaller, terminal-study, and separate desktop-study pathways must not be restored merely because they exist in history.

---

# 5. Current Hospital Homepage Milestone

The active local homepage is the PrepFlow Teaching Hospital exterior composition.

Authoritative runtime files:

```text
web/index.html
web/app.js
web/hospital-home.css
web/quiz-builder-screen.css
web/resume-rules.js
web/images/home-hospital/prepflow-home-background-final.png
```

Verified implementation commits:

```text
9975ddc feat: add hospital homepage quiz builder flow
e44d710 refine hospital homepage controls and branding
```

The local milestone currently provides:

- a locked 16:9 hospital exterior scene;
- architectural quiz and reference signs built into the composite background;
- a live left-sign launcher for new and saved quiz states;
- a live right-sign Drug Library control;
- a dedicated quiz-builder screen;
- the three approved subject books inside the builder;
- chapter selection with Back and Done navigation;
- quiz settings and Start Quiz inside the builder;
- saved-session text showing `Block X of Y`;
- Continue Quiz and Build a New Quiz actions;
- shared text-only command pulsing;
- a temporary live PrepFlow title and tagline;
- working quiz, rationale, save, resume, block-summary, and return-home behavior.

Temporary homepage branding:

```text
PrepFlow
Prepare. Practice. Progress.
```

The title and tagline are live HTML/CSS placeholders and can be replaced later without modifying the hospital artwork.

The architectural signs belong to the approved static composite. Live labels, actions, progress, hit areas, and changing state remain browser-owned HTML/CSS/JavaScript.

The three subject books remain separate transparent clickable assets. They now appear inside the dedicated quiz-builder screen rather than acting as the homepage's primary controls.

---

# 6. Nurse Status

No nurse separation, nurse sprite production, nurse animation, or hospital-interior nurse scene has been implemented in the hospital-homepage milestone.

The previous city-and-nurses homepage remains historical reference material only. Nurse work may be revisited later, but it is not the current next milestone and must not be started merely because older documentation proposed it.

---

# 7. Known Cleanup Debt

`web/hospital-home.css` is functionally and visually approved but contains a large layered override stack accumulated during iterative alignment and styling.

Verified integrity results:

- 1,860 lines;
- opening and closing braces balanced;
- comment openings and closings balanced;
- no terminal-paste artifacts found;
- all 72 automated tests passed;
- the real local browser workflow was visually and functionally approved.

A pre-cleanup safety copy exists outside the repository:

```text
~/prepflow-local-backups/hospital-home-pre-cleanup/
```

Cleanup is an integral part of the development process, not optional polish.

The stylesheet should be consolidated into one authoritative system covering:

- the 16:9 scene;
- left launcher placement;
- saved and unsaved launcher states;
- Drug Library placement;
- shared command-label animation;
- temporary homepage branding.

Do not casually delete or rewrite the working cascade. A cleanup milestone must:

1. begin from an external backup;
2. preserve the approved appearance and behavior;
3. verify all active states and hit areas;
4. test in the real browser;
5. run applicable automated tests;
6. inspect the focused diff;
7. commit cleanup separately from feature changes.

---

# 8. Untracked Hospital Artwork

The current working tree may contain untracked source and review assets such as:

```text
art/review/home-hospital/
docs/PrepFlow_Teaching_Hospital_Layered_Workflow_Brief.txt
web/images/home-hospital/hospital-background.png
web/images/home-hospital/prepflow-teaching-hospital-background-v1.png
web/images/home-hospital/signs/
```

The tracked runtime composite is:

```text
web/images/home-hospital/prepflow-home-background-final.png
```

Before release, classify every untracked file deliberately. Do not use `git add .`. Avoid committing duplicate runtime copies, temporary proofs, screenshots, or transfer artifacts.

The layered-workflow brief should be reviewed for accuracy before deciding whether to commit it as durable documentation.

---

# 9. Local Browser Workflow

Start the canonical server from the repository root:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Open:

```text
http://localhost:8004/web/
```

The server must run from `~/projects/prepflow`, not `~/projects/prepflow/web`, because the sibling `packs/` directory must also be served.

Hard refresh:

```text
Ctrl+Shift+R
```

Clean diagnostic origin:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

```text
http://localhost:8005/web/
```

Port 8005 is only a troubleshooting origin.

Troubleshooting order:

1. verify the server is running;
2. verify its working directory;
3. open the target asset directly by URL;
4. compare the direct asset with the homepage;
5. inspect the live DOM element and its children;
6. inspect pseudo-elements;
7. only then diagnose CSS, cache, or service-worker behavior.

---

# 10. Working Discipline

Standard loop:

```text
Read continuity
→ inspect local status
→ observe the real local application
→ identify one focused change
→ implement locally
→ test
→ inspect output and diff
→ clean up safely
→ document durable decisions
→ commit
→ push intended remotes
→ verify hashes
→ repeat
```

Permanent rules:

- one focused change at a time;
- when Charlie says `next`, provide the next executable step;
- do not ask for code already available through GitHub or the local project;
- do not perform speculative redesigns;
- do not claim tests, pushes, previews, merges, or approvals that were not verified;
- keep backup assets, screenshots, transfer archives, and temporary proofs out of production commits;
- protect privacy before public sharing or release;
- preserve exact approved source art;
- update continuity whenever a durable rule, release boundary, or active milestone changes;
- push every remote intended to remain synchronized and explicitly compare hashes;
- do not assume a plain `git push` updates both remotes;
- do not let exploratory override stacks become permanent architecture merely because they work.

---

# 11. Release Preservation and Rollback

The complete policy is:

```text
docs/RELEASE_PRESERVATION_POLICY.md
```

Use three protected states:

1. local active development;
2. synchronized remote development checkpoint;
3. frozen public release branch and tag.

For every major approved public update:

1. complete and test the milestone locally;
2. commit and push the development branch to both intended remotes;
3. verify local, private, and public-mirror development hashes;
4. create a uniquely named fixed release branch from the exact approved commit;
5. create an immutable release tag;
6. open a pull request from that release branch into public `master`;
7. inspect the exact release scope;
8. merge without rewriting prior release branches or tags;
9. verify GitHub Pages;
10. preserve the previous release until the new deployment is confirmed;
11. record the release boundary.

Never force-push public `master`, a frozen release branch, or a release tag.

---

# 12. End-of-Session Procedure

Before ending a substantial PrepFlow session:

1. inspect `git status --short --branch`;
2. classify every changed and untracked file;
3. remove or relocate temporary backups from the repository;
4. run applicable automated tests;
5. perform real-browser checks for affected behavior;
6. inspect the focused diff;
7. complete safe cleanup or record a protected cleanup milestone;
8. update supporting documentation;
9. update this restart packet when topology or milestones changed;
10. commit one coherent milestone;
11. push both development remotes when both should match;
12. verify local, private, and public-mirror hashes;
13. create a release branch only for an approved public chunk;
14. confirm a fresh chat can resume without relying on conversational memory.

---

# 13. Exact Current Resume State

Current verified development checkpoint:

```text
69ce6a70f8e8aead9afebc0c260b4572a6ab0fbd
```

That checkpoint includes:

- the complete hospital-homepage implementation commits;
- the homepage branding and command refinements;
- the release-preservation policy.

The three development copies were explicitly verified equal at that hash before this documentation update.

The immediate finishing sequence is:

1. update stale authoritative documentation for the hospital milestone;
2. pull and mirror each documentation commit so development hashes stay synchronized;
3. classify the remaining untracked hospital source and duplicate assets;
4. inspect the final milestone diff and privacy exposure;
5. rerun automated and browser verification after documentation and asset decisions;
6. create a final development checkpoint;
7. create a fixed hospital-homepage release branch and tag;
8. release through a pull request to public `master`;
9. verify the deployed site;
10. record the new production boundary.

Do not resume the obsolete nurse-separation milestone.

Do not treat the current stylesheet override stack as permanent finished architecture. Preserve the working result and keep consolidation recorded as a protected cleanup milestone.

---

# 14. Fresh-Chat Opening Instruction

Use this exact instruction:

> Continue PrepFlow from my local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. Read the full current `docs/RESTART_PACKET.md`, `docs/RELEASE_PRESERVATION_POLICY.md`, and `docs/ART_SYSTEM.md` before giving me a command. Inspect `git status --short --branch` first and inspect the rendered local application before visual changes. The current verified development state contains the approved PrepFlow Teaching Hospital homepage, dedicated quiz-builder workflow, saved-session `Block X of Y` state, Drug Library sign control, shared command pulsing, and temporary live PrepFlow title/tagline. The previous city-and-nurses milestone is historical; do not begin nurse separation. Cleanup is integral: `web/hospital-home.css` is visually approved but layered and must eventually be consolidated through a separate backed-up, browser-verified cleanup milestone. Preserve frozen releases according to `docs/RELEASE_PRESERVATION_POLICY.md`. Give me one executable step at a time, use the GitHub connector for large documentation rewrites, and never use `git add .` for the remaining untracked hospital assets.