# PREPFLOW RESTART PACKET

## Purpose

This is the primary handoff for every new PrepFlow development session.

> **Mandatory first action:** Read this file before proposing a command or changing a PrepFlow file.

For visual or release work, also read:

```text
docs/ART_SYSTEM.md
docs/RELEASE_PRESERVATION_POLICY.md
docs/RELEASE_2026-07-24_BOOK_MILESTONE.md
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

`VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` is historical context for the previous city-and-nurses homepage. It is not the active implementation target.

---

# 1. Current Topology

```text
Local repository: ~/projects/prepflow
Active branch: docs/continuity-rebuild
Private development repository: bins-projects/prepflow-dev
Public mirror repository: bins-projects/PrepFlow
Public mirror development branch: docs/continuity-rebuild
Last explicitly verified synchronized development commit: 37ff1d609e5f91523cf30a41ecc5b651c050e98f
```

Daily work continues on `docs/continuity-rebuild`, not on public `master` and not on a frozen release branch.

Current public production:

```text
Repository: bins-projects/PrepFlow
Branch: master
Observed public master before the hospital release: c58da62
Public site: https://bins-projects.github.io/PrepFlow/web/
```

The public site currently uses the older three-book homepage until the hospital-homepage release is merged and deployed.

Previous frozen release:

```text
Release source snapshot: 648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
Release branch: release/2026-07-24-book-milestone
Original public merge commit: 8e8e85b1e9b9604d257b6db52e9bb802fcb91fce
```

Do not move, reuse, rewrite, or continue ordinary development on that frozen release branch.

---

# 2. Authority Order

Use this order:

1. Charlie's explicit approval or correction.
2. The rendered local application for visual and interaction truth.
3. The local repository and working tree.
4. This restart packet.
5. `docs/RELEASE_PRESERVATION_POLICY.md`.
6. `docs/ART_SYSTEM.md`.
7. The private development branch.
8. The public-mirror development branch.
9. Public `master` for deployed production.
10. Dated documents for historical context.

Never overwrite newer local work merely because GitHub contains an older committed copy.

---

# 3. Product State

PrepFlow is a browser-centered nursing study application built around validated question Packs.

Active browser product:

```text
web/
```

Official Packs:

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

Removed Tkinter, PyInstaller, terminal-study, and separate desktop-study pathways must not be restored merely because they exist in history.

---

# 4. Current Hospital Homepage Milestone

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

Key implementation commits:

```text
9975ddc feat: add hospital homepage quiz builder flow
e44d710 refine hospital homepage controls and branding
```

The milestone provides:

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
- temporary live PrepFlow title and tagline;
- working quiz, rationale, save, resume, block-summary, and return-home behavior.

Temporary homepage branding:

```text
PrepFlow
Prepare. Practice. Progress.
```

The architectural signs belong to the static composite. Live labels, actions, progress, hit areas, and changing state remain browser-owned HTML, CSS, and JavaScript.

The three subject books remain separate transparent clickable assets inside the quiz-builder screen.

---

# 5. Nurse Status

No nurse separation, nurse sprite production, nurse animation, or hospital-interior nurse scene has been implemented in this milestone.

The previous city-and-nurses homepage is historical reference material only. Do not resume nurse-separation work merely because an older document proposed it.

---

# 6. Known Cleanup Debt

`web/hospital-home.css` is functionally and visually approved but contains a large layered override stack accumulated during iterative alignment and styling.

Verified integrity before release preparation:

- 1,860 lines;
- balanced opening and closing braces;
- balanced comment openings and closings;
- no terminal-paste artifacts found;
- 72 automated tests passed;
- the real local browser workflow was visually and functionally approved.

A pre-cleanup safety copy exists outside the repository:

```text
~/prepflow-local-backups/hospital-home-pre-cleanup/
```

Cleanup is integral, but it must be a separate protected milestone. Do not casually rewrite the working cascade before release.

A cleanup milestone must:

1. begin from the external backup;
2. preserve approved appearance and behavior;
3. verify all active states and hit areas;
4. test in the real browser;
5. run automated tests;
6. inspect the focused diff;
7. commit cleanup separately from feature work.

---

# 7. Hospital Artwork Classification

The temporary layered-workflow transcript, duplicate background copies, review-art duplicates, and unused separate sign experiments were inspected and deliberately removed.

The authoritative tracked runtime composite is:

```text
web/images/home-hospital/prepflow-home-background-final.png
```

The working tree was verified clean after this classification. Do not restore the removed duplicate assets or obsolete workflow transcript without a specific historical need.

Never use `git add .` during release preparation.

---

# 8. Local Browser Workflow

Start the server from the repository root:

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

Diagnostic origin when needed:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

```text
http://localhost:8005/web/
```

---

# 9. Working Discipline

Standard loop:

```text
Read continuity
→ inspect local status
→ observe the real local application
→ make one focused change
→ test
→ inspect output and diff
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
- use the GitHub connector for substantial documentation changes rather than long terminal paste blocks.

---

# 10. Release Preservation and Rollback

The complete policy is:

```text
docs/RELEASE_PRESERVATION_POLICY.md
```

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
11. record the new release boundary.

Never force-push public `master`, a frozen release branch, or a release tag.

---

# 11. Immediate Finishing Sequence

1. synchronize this restart-packet correction locally and to the public mirror;
2. rerun automated tests;
3. perform a final real-browser smoke test;
4. inspect final status, diff, and privacy exposure;
5. create the final synchronized development checkpoint;
6. create a fixed hospital-homepage release branch;
7. choose and create the immutable release tag;
8. open and inspect the public release pull request;
9. merge and verify the deployed site;
10. record the new production boundary.

Do not resume the obsolete nurse-separation milestone.

Do not treat the current stylesheet override stack as permanent finished architecture. Preserve the working result and keep consolidation as a protected post-release cleanup milestone.

---

# 12. Fresh-Chat Opening Instruction

> Continue PrepFlow from my local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. Read the full current `docs/RESTART_PACKET.md`, `docs/RELEASE_PRESERVATION_POLICY.md`, and `docs/ART_SYSTEM.md` before giving me a command. Inspect `git status --short --branch` first and inspect the rendered local application before visual changes. The current development state contains the approved PrepFlow Teaching Hospital homepage, dedicated quiz-builder workflow, saved-session `Block X of Y` state, Drug Library sign control, shared command pulsing, and temporary live PrepFlow title/tagline. The previous city-and-nurses milestone is historical; do not begin nurse separation. `web/hospital-home.css` is visually approved but layered and must eventually be consolidated through a separate backed-up, browser-verified cleanup milestone. Preserve frozen releases according to `docs/RELEASE_PRESERVATION_POLICY.md`. Give one executable step at a time, use the GitHub connector for substantial documentation rewrites, and never use `git add .` during release preparation.
