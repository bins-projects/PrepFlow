from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "web" / "app.js"
index_path = root / "web" / "index.html"

app = app_path.read_text()
index = index_path.read_text()

old_index = '  <script src="saved-session-rules.js?v=20260721-1"></script>\n  <script src="app.js?v=20260721-phase-d-1"></script>'
new_index = '  <script src="saved-session-rules.js?v=20260721-1"></script>\n  <script src="review-rules.js?v=20260721-1"></script>\n  <script src="app.js?v=20260721-phase-d-1"></script>'

old_answer = '''    if (reviewMode) {
      reviewQueue.push(currentReviewQuestion);
    } else {
      firstPassMissed += 1;
      blockMissed.push(sessionQuestions[questionIndex]);
    }'''
new_answer = '''    if (reviewMode) {
      reviewQueue = PrepFlowReviewRules.queueAfterAnswer(
        reviewQueue,
        currentReviewQuestion,
        false
      );
    } else {
      firstPassMissed += 1;
      blockMissed.push(sessionQuestions[questionIndex]);
    }'''

old_continue = '''  if (reviewMode) {
    if (reviewQueue.length === 0) {
      currentReviewQuestion = null;
      reviewMode = false;
      showBlockSummary(true);
      return;
    }

    currentReviewQuestion = reviewQueue.shift();
    showQuestion();
    return;
  }'''
new_continue = '''  if (reviewMode) {
    const nextStep = PrepFlowReviewRules.nextReviewStep(reviewQueue);
    reviewQueue = nextStep.reviewQueue;
    currentReviewQuestion = nextStep.currentQuestion;

    if (nextStep.finished) {
      reviewMode = false;
      showBlockSummary(true);
      return;
    }

    showQuestion();
    return;
  }'''

for label, old, text in (
    ("index script insertion", old_index, index),
    ("review miss transition", old_answer, app),
    ("review continue transition", old_continue, app),
):
    if old not in text:
        raise SystemExit(f"Could not find expected {label} block; no files changed.")

index = index.replace(old_index, new_index, 1)
app = app.replace(old_answer, new_answer, 1)
app = app.replace(old_continue, new_continue, 1)

index_path.write_text(index)
app_path.write_text(app)
Path(__file__).unlink()
print("Phase D review-rule integration applied.")
