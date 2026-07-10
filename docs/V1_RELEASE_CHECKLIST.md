# PrepFlow Version 1 Release Checklist

> Goal: Deliver a polished terminal-based PrepFlow application that is complete, stable, and easy for end users to use. New ideas belong in `IDEAS.md` unless they are required for Version 1.

---

# Development Rules

These rules take precedence during Version 1 development.

- Top-down assessment **always** means inspecting the committed GitHub mirror.
- GitHub is the technical source of truth.
- Observe → Inspect → One focused change → Compile → Test → Commit → Push.
- Do not redesign working architecture without evidence.
- Build a functional product before adding polish.
- Future ideas go into `IDEAS.md`, not the current milestone.
- Finish the current milestone before starting another.

---

# Core Engine

- [x] Compiler pipeline
- [x] Standard PrepFlow Pack format
- [x] Runtime Pack loader
- [x] Dynamic Pack discovery
- [x] Pack selection
- [x] Chapter selection
- [x] Question session engine
- [x] Review queue
- [x] Score tracking

---

# User Experience

- [ ] Main menu
- [ ] Graceful Exit
- [ ] Restart Session
- [ ] Return to Pack Selection
- [ ] Better invalid-input handling
- [ ] Session summary
- [ ] Progress display
- [ ] Startup banner / title screen

---

# Runtime Reliability

- [ ] Pack validation before loading
- [ ] Friendly error messages
- [ ] Missing Pack handling
- [ ] Invalid chapter handling
- [ ] General robustness testing

---

# Packaging

- [ ] Standalone Windows executable
- [ ] Standalone Linux executable
- [ ] Packaging instructions
- [ ] End-user README

---

# Documentation

- [ ] Architecture Bible current
- [ ] PROJECT_STATE.md current
- [ ] RESTART_PACKET.md current
- [ ] CHANGELOG.md updated

---

# Testing

## Pharmacy

- [x] Entire Pack
- [x] Single Chapter
- [x] Multiple Chapters

## Medical-Surgical

- [x] Entire Pack
- [x] Single Chapter
- [x] Multiple Chapters

---

# Deferred Until Version 2

- [ ] Saved progress
- [ ] Long-term statistics
- [ ] Search
- [ ] Favorites
- [ ] Difficulty modes
- [ ] Mixed Pack mode
- [ ] GUI
- [ ] Mobile version
- [ ] Cloud sync

---

# Definition of Done

PrepFlow Version 1 is complete when:

- A user can launch the program without modifying code.
- A user can choose a Pack.
- A user can choose one or more Chapters.
- The study session runs reliably.
- Review questions work correctly.
- The application exits cleanly.
- The application can be packaged and distributed without source PDFs.