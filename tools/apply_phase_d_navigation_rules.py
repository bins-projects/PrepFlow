from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "web" / "app.js"
index_path = root / "web" / "index.html"

app = app_path.read_text(encoding="utf-8")
old = '''  questionIndex += 1;

  if (questionIndex >= blockEnd) {
    showBlockSummary(false);
    return;
  }

  showQuestion();
'''
new = '''  const nextStep = PrepFlowNavigationRules.nextQuestionStep(
    questionIndex,
    blockEnd
  );
  questionIndex = nextStep.questionIndex;

  if (nextStep.blockComplete) {
    showBlockSummary(false);
    return;
  }

  showQuestion();
'''
if old not in app:
    raise SystemExit("Expected question navigation block was not found in web/app.js")
app_path.write_text(app.replace(old, new, 1), encoding="utf-8")

index = index_path.read_text(encoding="utf-8")
old_script = '  <script src="review-rules.js?v=20260721-1"></script>\n'
new_script = old_script + '  <script src="navigation-rules.js?v=20260721-1"></script>\n'
if old_script not in index:
    raise SystemExit("Expected review-rules script tag was not found in web/index.html")
index_path.write_text(index.replace(old_script, new_script, 1), encoding="utf-8")

Path(__file__).unlink()
print("Phase D navigation-rule integration applied.")
