(function () {
  function normalizeAnswers(rawAnswers) {
    const answers = Array.isArray(rawAnswers) ? rawAnswers : [rawAnswers];
    return answers
      .filter((answer) => answer !== null && answer !== undefined)
      .map((answer) => String(answer).trim().toUpperCase())
      .filter(Boolean);
  }

  function correctAnswersFor(question) {
    return normalizeAnswers(question.correct_answers ?? question.correct_answer ?? []);
  }

  function questionKind(question) {
    const questionType = question.type || question.question_type;
    if (questionType === "completion") return "text";
    if (questionType === "ordered_response") return "ordered";
    if (questionType === "multiple_response") return "multiple";
    return "single";
  }

  function isMultipleResponseQuestion(question) {
    const questionType = question.type || question.question_type;
    const correctAnswers = correctAnswersFor(question);
    const stem = String(question.stem || "");
    return (
      questionType === "multiple_response"
      || (["mc", "multiple_choice"].includes(questionType) && correctAnswers.length > 1)
      || /select all that apply/i.test(stem)
    );
  }

  function evaluateAnswer(question, selectedAnswers) {
    const correctAnswers = correctAnswersFor(question);
    const normalizedSelectedAnswers = normalizeAnswers(selectedAnswers);
    const kind = questionKind(question);
    const correctSet = new Set(correctAnswers);
    const selectedSet = new Set(normalizedSelectedAnswers);
    let isCorrect;
    if (kind === "ordered") {
      isCorrect = normalizedSelectedAnswers.length === correctAnswers.length
        && normalizedSelectedAnswers.every((answer, index) => answer === correctAnswers[index]);
    } else if (kind === "text") {
      isCorrect = normalizedSelectedAnswers.length === 1 && correctSet.has(normalizedSelectedAnswers[0]);
    } else {
      isCorrect = selectedSet.size === correctSet.size
        && [...selectedSet].every((answer) => correctSet.has(answer));
    }
    return { isCorrect, correctAnswers };
  }

  window.PrepFlowQuizRules = {
    normalizeAnswers,
    correctAnswersFor,
    questionKind,
    isMultipleResponseQuestion,
    evaluateAnswer,
  };
}());