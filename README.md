# PrepFlow

PrepFlow is a browser-based nursing study application built around organized question Packs.

It lets students build a quiz from selected nursing chapters, study one question at a time, review the correct answer and rationale, and repeat missed questions until they are mastered.

## Open PrepFlow

[Open PrepFlow in your browser](https://bins-projects.github.io/PrepFlow/web/)

No account is required. Study progress is stored locally in the browser on the device being used.

Clearing browser or site data may remove a saved session. A session saved in one browser or device does not automatically appear in another.

## Install as an App

PrepFlow can be installed from a supported browser so it opens in its own window.

### Chromebook or Chrome

1. Open PrepFlow in Chrome.
2. Select the install icon in the address bar.
3. Choose **Install**.
4. Open PrepFlow from the device launcher.

### Mac with Safari

1. Open PrepFlow in Safari.
2. Choose **File** and then **Add to Dock**.
3. Name it **PrepFlow** and select **Add**.
4. Open it from the Dock, Applications, or Spotlight.

## How to Build a Quiz

1. Open the PrepFlow Teaching Hospital homepage.
2. Select **Start Here!** or **Build Your Quiz**.
3. Choose Fundamentals, Pharm, or Medical-Surgical.
4. Select one or more chapters.
5. Use **Done** to return to the quiz builder.
6. Add chapters from other books when needed.
7. Choose the quiz settings and block size.
8. Start the quiz.

The three subject books are located inside the dedicated quiz-builder screen rather than acting as the homepage controls.

## Saved Sessions

PrepFlow automatically saves one unfinished session locally.

When a saved quiz exists, the hospital homepage shows:

- the current block as **Block X of Y**;
- **Continue Quiz**;
- **Build a New Quiz**.

Starting a new quiz replaces the existing saved session only after the user chooses that action.

## Study Library

PrepFlow currently includes:

- Fundamentals
- Pharm
- Medical-Surgical

The hospital homepage also provides access to the **Drug Library** through the References sign.

## Question Types

The PrepFlow library contains:

- Multiple Choice
- Multiple Response
- Completion
- Ordered Response

Browser support for individual question types may evolve as the active study interface is improved.

## Study Behavior

During a session, PrepFlow:

- presents one question at a time;
- gives immediate Correct or Incorrect feedback;
- shows the correct answer and rationale;
- tracks first-pass performance;
- places missed questions into a review queue;
- repeats missed questions until answered correctly;
- shows a block summary;
- displays final first-pass results after the session is complete.

Selected questions currently use one stable shuffled order for the session.

## Project Direction

PrepFlow also includes a compiler that turns deliberately selected educational source material into cleaned, structured, validated Packs.

The browser application is the active user-facing product. Future downloadable editions should reuse the browser-centered application rather than maintain a separate study system.

Internal architecture, art rules, release preservation, and development continuity are documented under `docs/`.
