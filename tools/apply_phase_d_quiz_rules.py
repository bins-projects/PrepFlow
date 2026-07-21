from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "web" / "app.js"
INDEX = ROOT / "web" / "index.html"
SELF = Path(__file__).resolve()

app = APP.read_text(encoding="utf-8")
index = INDEX.read_text(encoding="utf-8")

old_function = '''function normalizedCorrectAnswers(question) {
  const rawAnswers =
    question.correct_answers ?? question.correct_answer ?? [];

  return (
    Array.isArray(rawAnswers)
      ? rawAnswers
      : [rawAnswers]
  )
    .filter((answer) => answer !== null && answer !== undefined)
    .map((answer) => String(answer).trim().toUpperCase())
    .filter(Boolean);
}

'''
if old_function not in app:
    raise SystemExit("Expected normalizedCorrectAnswers function was not found.")
app = app.replace(old_function, "", 1)

old_multiple_response = "  const correctAnswers = normalizedCorrectAnswers(question);"
new_multiple_response = "  const correctAnswers = PrepFlowQuizRules.correctAnswersFor(question);"
if old_multiple_response not in app:
    raise SystemExit("Expected multiple-response grading reference was not found.")
app = app.replace(old_multiple_response, new_multiple_response, 1)

old_grading = '''  const question = currentQuestion();
  const correctAnswers = normalizedCorrectAnswers(question);

  const selectedAnswers = Array.from(
    selected,
    (input) => String(input.value).trim().toUpperCase()
  );

  const selectedSet = new Set(selectedAnswers);
  const correctSet = new Set(correctAnswers);
  const isCorrect =
    selectedSet.size === correctSet.size
    && [...selectedSet].every((answer) => correctSet.has(answer));
'''
new_grading = '''  const question = currentQuestion();
  const selectedAnswers = Array.from(selected, (input) => input.value);
  const { isCorrect, correctAnswers } =
    PrepFlowQuizRules.evaluateAnswer(question, selectedAnswers);
'''
if old_grading not in app:
    raise SystemExit("Expected submit-answer grading block was not found.")
app = app.replace(old_grading, new_grading, 1)

old_script = '  <script src="app.js?v=20260719-sata-1"></script>'
new_scripts = '''  <script src="quiz-rules.js?v=20260721-1"></script>
  <script src="app.js?v=20260721-phase-d-1"></script>'''
if old_script not in index:
    raise SystemExit("Expected app.js script tag was not found.")
index = index.replace(old_script, new_scripts, 1)

APP.write_text(app, encoding="utf-8")
INDEX.write_text(index, encoding="utf-8")
SELF.unlink()

print("Phase D quiz-rule integration applied.")
