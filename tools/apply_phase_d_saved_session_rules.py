from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "web" / "app.js"
index_path = root / "web" / "index.html"

app = app_path.read_text(encoding="utf-8")
index = index_path.read_text(encoding="utf-8")

old_reader = '''function readSavedSession() {
  try {
    const raw = localStorage.getItem(SAVE_KEY);
    const saved = raw ? JSON.parse(raw) : null;

    if (saved && saved.version !== 3) {
      localStorage.removeItem(SAVE_KEY);
      return null;
    }

    return saved;
  } catch {
    localStorage.removeItem(SAVE_KEY);
    return null;
  }
}
'''

new_reader = '''function readSavedSession() {
  const raw = localStorage.getItem(SAVE_KEY);
  const result = PrepFlowSavedSessionRules.parseSavedSession(raw, 3);

  if (result.shouldClear) {
    localStorage.removeItem(SAVE_KEY);
  }

  return result.saved;
}
'''

if old_reader not in app:
    raise SystemExit("Expected saved-session reader was not found.")

app = app.replace(old_reader, new_reader, 1)

script_anchor = '  <script src="summary-rules.js?v=20260721-1"></script>\n'
script_line = '  <script src="saved-session-rules.js?v=20260721-1"></script>\n'

if script_line not in index:
    if script_anchor not in index:
        raise SystemExit("Expected summary-rules script anchor was not found.")
    index = index.replace(script_anchor, script_anchor + script_line, 1)

app_path.write_text(app, encoding="utf-8")
index_path.write_text(index, encoding="utf-8")
Path(__file__).unlink()

print("Phase D saved-session integration applied.")
