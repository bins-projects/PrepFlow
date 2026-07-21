from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
app_path = ROOT / "web" / "app.js"
index_path = ROOT / "web" / "index.html"

app = app_path.read_text(encoding="utf-8")
index = index_path.read_text(encoding="utf-8")

replacements = [
    (
        "function totalBlockCount() {\n  return Math.max(1, Math.ceil(sessionQuestions.length / sessionBlockSize));\n}\n",
        "function totalBlockCount() {\n  return PrepFlowSessionRules.totalBlockCount(\n    sessionQuestions.length,\n    sessionBlockSize\n  );\n}\n",
    ),
    (
        "    const questionInBlock = questionIndex - blockStart + 1;",
        "    const questionInBlock = PrepFlowSessionRules.questionPosition(\n      questionIndex,\n      blockStart\n    );",
    ),
    (
        "  blockEnd = Math.min(\n    blockStart + sessionBlockSize,\n    sessionQuestions.length\n  );",
        "  blockEnd = PrepFlowSessionRules.blockEnd(\n    blockStart,\n    sessionBlockSize,\n    sessionQuestions.length\n  );",
    ),
    (
        "  const percentage = totalQuestions\n    ? Math.round((firstPassCorrect / totalQuestions) * 100)\n    : 0;",
        "  const percentage = PrepFlowSessionRules.firstPassPercentage(\n    firstPassCorrect,\n    totalQuestions\n  );",
    ),
]

for old, new in replacements:
    if old not in app:
        raise SystemExit(f"Expected app.js pattern not found:\n{old}")
    app = app.replace(old, new, 1)

script_marker = '  <script src="quiz-rules.js?v=20260721-1"></script>\n'
session_script = '  <script src="session-rules.js?v=20260721-1"></script>\n'

if session_script not in index:
    if script_marker not in index:
        raise SystemExit("quiz-rules script marker not found in web/index.html")
    index = index.replace(script_marker, script_marker + session_script, 1)

app_path.write_text(app, encoding="utf-8")
index_path.write_text(index, encoding="utf-8")
Path(__file__).unlink()
print("Phase D session-rule integration applied.")
