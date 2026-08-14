(function () {
  "use strict";

  const STABLE_ID = /^PFQ-([a-z0-9_]+)-(\d{9})$/i;
  const TYPE_LABELS = {
    mc: "Multiple choice",
    multiple_choice: "Multiple choice",
    multiple_response: "Select all that apply",
    completion: "Fill in the blank",
    ordered_response: "Ordered response",
  };

  function stableReference(packTitle, questionId) {
    const fullId = typeof questionId === "string" ? questionId : "";
    const match = STABLE_ID.exec(fullId);
    if (!match) {
      return { available: false, concise: "Reference unavailable", fullId: "" };
    }
    return {
      available: true,
      concise: `${String(packTitle || "Pack").trim()} • Ref ${Number(match[2])}`,
      fullId,
    };
  }

  function questionTypeLabel(question) {
    const stored = question?.type || question?.question_type || "";
    return TYPE_LABELS[stored] || String(stored || "Unknown");
  }

  function reportText({ packTitle, question, progress }) {
    const reference = stableReference(packTitle, question?.id);
    const chapterTitle = String(question?.chapter_title || "").trim();
    const chapter = question?.chapter == null
      ? "Chapter unavailable"
      : `Chapter ${question.chapter}${chapterTitle ? `: ${chapterTitle}` : ""}`;
    return [
      `Pack: ${packTitle}`,
      `Chapter: ${chapter}`,
      `Concise reference: ${reference.concise}`,
      `Full PFQ ID: ${reference.available ? reference.fullId : "Reference unavailable"}`,
      `Question type: ${questionTypeLabel(question)}`,
      `Stem: ${String(question?.stem || "")}`,
      `Quiz-session position: ${progress}`,
    ].join("\n");
  }

  window.PrepFlowQuestionReferenceRules = {
    reportText,
    stableReference,
    questionTypeLabel,
  };
}());
