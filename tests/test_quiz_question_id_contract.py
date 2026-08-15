from pathlib import Path


WEB = Path(__file__).parents[1] / "web"


def test_active_quiz_shows_review_and_neutral_skip_actions():
    html = (WEB / "index.html").read_text()
    script = (WEB / "app.js").read_text()
    rules = (WEB / "question-reference-rules.js").read_text()
    css = (WEB / "arcade-quiz.css").read_text()
    mobile_css = (WEB / "mobile-portrait.css").read_text()
    service_worker = (WEB / "sw.js").read_text()

    for element_id in ("quiz-question-id", "skip-question", "quiz-position"):
        assert f'id="{element_id}"' in html

    assert 'id="copy-question-id"' not in html
    assert 'id="copy-question-report"' not in html

    assert "currentQuestionReference().packPath" in script
    assert "displayQuestionReference(questionPack?.title, question.id)" in script
    assert 'skipQuestionButton.addEventListener("click", skipCurrentQuestion);' in script
    assert 'button.textContent = "Send for review"' in rules
    assert 'actions.insertBefore(button, skipButton)' in rules
    assert "Quiz-session position" in rules
    assert "Reference unavailable" in rules
    assert "• Ref ${Number(match[2])}" in rules
    for label in ("Pack:", "Chapter:", "Concise reference:", "Full PFQ ID:", "Question type:", "Stem:"):
        assert label in rules

    assert ".quiz-reference-bar" in css
    assert "grid-template-rows: auto auto auto minmax(0, 1fr) auto" in css
    assert "align-content: start" in css
    assert "user-select: text" in css
    assert "grid-row: 5" in mobile_css
    assert "prepflow-pwa-v10-review-skip" in service_worker
    assert '"./question-reference-rules.js"' in service_worker
    assert "20260815-review-skip-1" in html
