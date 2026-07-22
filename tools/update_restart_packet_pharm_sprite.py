from pathlib import Path

path = Path("docs/RESTART_PACKET.md")
text = path.read_text()
marker = "# 17. Current Resume Statement"
if marker not in text:
    raise SystemExit("Current Resume Statement section not found")

prefix = text.split(marker, 1)[0].rstrip()
replacement = r'''# 17. Temporary Session Handoff — Pharm Book Sprite

> **Disposable continuity note:** This section exists only to preserve unfinished work between chat instances. Replace it whenever a newer handoff is created. Delete it once the unfinished work below is completed and the Restart Packet has been updated with the next current state.

## Mandatory startup instruction

Read this entire handoff before taking any action.

Do not rely on conversational memory alone. Inspect the private GitHub repository, the current branch, the latest commit, and the local working-tree status before giving Charlie any modifying command.

When a PrepFlow session becomes context-heavy, repetitive, error-prone, or visibly unreliable, stop making changes and replace this temporary handoff before beginning a fresh chat. This continuity process is mandatory.

## Current task

Replace the temporary CSS-built Pharm book with the approved real pixel-art sprite inside the actual PrepFlow browser application.

The approved Pharm sprite is a transparent PNG depicting:

- a dark green modern pharmacology textbook;
- a three-quarter pixel-art view;
- visible page block, binding, tabs, highlights, and restrained wear;
- the word `PHARM` on the cover;
- a green-and-white capsule emblem.

The sprite was approved as a strong starting asset.

## Critical workflow rule

Never generate a picture or mockup of the PrepFlow interface.

All interface previews must come from:

1. changing the real repository code;
2. loading the real browser application at `http://localhost:8000/web/`;
3. reviewing screenshots of that actual running page.

Image generation is allowed only for standalone reusable assets such as sprites, icons, characters, or environment artwork. It must never be used to imitate or recreate the application screen.

## Current asset state

The approved Pharm PNG is not yet committed to the repository and is not yet loaded by the application.

A later generated picture of the entire application was a mistake, was cancelled, and must not be used.

A proposed downloadable installer was also the wrong workflow and must not be used.

The previous direct GitHub image-upload attempt was blocked. Do not claim that the sprite was installed.

If the approved PNG is unavailable in the new chat, ask Charlie to reattach that exact sprite image before proceeding. Do not regenerate it unless Charlie explicitly requests a revision.

## Current repository and branch

Private repository:

```text
bins-projects/prepflow-dev
```

Working branch:

```text
docs/continuity-rebuild
```

The most recent remote helper commit created during the launcher-only correction was:

```text
dea443b7453f2df145a2e5f206d80838e25f184b
```

Do not assume the local tree is clean. Inspect `git status` first.

## Launcher and responsive-layout state

The launcher box was reduced and repositioned in a launcher-only correction.

Do not resume broad responsive tuning yet.

The temporary CSS books distort or mangle live text when scaled. Stop scaling those temporary cards as complete objects.

The intended long-term structure is:

- reusable book sprite artwork;
- live chapter-selection status kept as real HTML text;
- no transforms that distort live lettering;
- responsive scaling applied to the sprite image, not to an entire text-filled card.

## Exact next step

1. Inspect the current GitHub branch and relevant home-page HTML/CSS.
2. Inspect local `git status`.
3. Confirm access to the approved transparent Pharm PNG.
4. Add the PNG as a real asset under an appropriate path such as `web/assets/books/pharm-book.png`.
5. Replace only the Pharm card's temporary book artwork with an actual `<img>` using that asset.
6. Preserve the Pharm button's existing functionality and data attributes.
7. Keep the question count and chapter-selection status as separate live HTML text.
8. Do not modify Fundamentals or Med-Surg during this preview.
9. Do not generate any picture of the page.
10. Have Charlie open the real browser page and judge the sprite in context before further design work.

## Working discipline

```text
Observe
→ inspect GitHub
→ inspect local status
→ one focused change
→ run the real browser
→ visually review
→ test
→ commit
→ push
```

Charlie pastes commands rather than typing them. Give one short executable command at a time. Never ask Charlie to repeat terminal output or screenshot information that is already visible.
'''

path.write_text(prefix + "\n\n---\n\n" + replacement.strip() + "\n")
Path(__file__).unlink()
print("Restart Packet temporary handoff replaced; updater removed.")
