from pathlib import Path

checkpoint = Path("docs/SESSION_CHECKPOINT_2026-07-20.md")
text = checkpoint.read_text(encoding="utf-8")

marker = "### Backlog addition\n"
section = """### Eighth Phase D extraction completed

Completed at:

```text
87e631e  refactor: extract browser selection rules
```

Implemented:

- added `web/selection-rules.js` with pure chapter-count, book-count, per-book badge, and home-status text formatting;
- added `web/selection-rules.test.html` with nine singular, plural, empty, and populated display cases;
- loaded the selection rules before `web/app.js`;
- updated the live selection UI to use the tested text helpers;
- removed the temporary integration helper after use.

Verification completed:

- all nine selection-rule browser tests passed;
- all 72 Python tests passed;
- `git diff --check` passed;
- a live selection click-through was not performed for this extraction;
- local, private, and public branch heads all matched commit `87e631e`;
- working tree was clean.

"""

if section not in text:
    if marker not in text:
        raise SystemExit("Checkpoint marker not found.")
    text = text.replace(marker, section + marker, 1)

old_next = "Continue Phase D with another read-only inspection of `web/app.js`. Extract only the next smallest pure behavior unit that can be tested without changing visible browser flow. Prefer a narrowly scoped selection-status or display-text helper. Do not begin a broad rewrite. The visible question-reference item remains a separate small UI backlog change."
new_next = "Continue Phase D with another read-only inspection of `web/app.js`. Extract only the next smallest pure behavior unit that can be tested without changing visible browser flow. Prefer a narrowly scoped resume-description, score-text, or other display helper. Do not begin a broad rewrite. The visible question-reference item remains a separate small UI backlog change."

if old_next in text:
    text = text.replace(old_next, new_next, 1)
elif new_next not in text:
    raise SystemExit("Exact-next milestone text not found.")

checkpoint.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("Selection milestone checkpoint update applied.")
