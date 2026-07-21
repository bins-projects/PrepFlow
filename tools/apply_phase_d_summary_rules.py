from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "web" / "app.js"
index_path = root / "web" / "index.html"

app = app_path.read_text(encoding="utf-8")
index = index_path.read_text(encoding="utf-8")

old_summary = '''  if (!mastered && missedCount > 0) {
    summaryAction.textContent = "Review Missed Questions";
    summaryAction.dataset.action = "review";
  } else if (blockEnd < sessionQuestions.length) {
    summaryAction.textContent = "Start Next Block";
    summaryAction.dataset.action = "next-block";
  } else {
    summaryAction.textContent = "Finish Session";
    summaryAction.dataset.action = "finish";
  }
'''

new_summary = '''  const nextAction = PrepFlowSummaryRules.summaryAction({
    mastered,
    missedCount,
    hasMoreQuestions: blockEnd < sessionQuestions.length,
  });

  summaryAction.textContent = nextAction.label;
  summaryAction.dataset.action = nextAction.action;
'''

if old_summary not in app:
    raise SystemExit("Expected block-summary decision code was not found.")

app = app.replace(old_summary, new_summary, 1)

script_anchor = '  <script src="session-rules.js?v=20260721-1"></script>\n'
script_line = '  <script src="summary-rules.js?v=20260721-1"></script>\n'

if script_line not in index:
    if script_anchor not in index:
        raise SystemExit("Expected session-rules script anchor was not found.")
    index = index.replace(script_anchor, script_anchor + script_line, 1)

app_path.write_text(app, encoding="utf-8")
index_path.write_text(index, encoding="utf-8")
Path(__file__).unlink()

print("Phase D summary-rule integration applied.")
