(function () {
  "use strict";

  const STABLE_ID = /^PFQ-([a-z0-9_]+)-(\d{9})$/i;
  const REVIEW_CONFIG_PATH = "./data/review-service.json";
  const TYPE_LABELS = {
    mc: "Multiple choice",
    multiple_choice: "Multiple choice",
    multiple_response: "Select all that apply",
    completion: "Fill in the blank",
    ordered_response: "Ordered response",
  };
  const sentThisSession = new Set();
  let reviewEndpoint = "";
  let reviewConfigLoaded = false;

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

  function currentQuestionId() {
    const node = document.querySelector("#quiz-question-id");
    const fullId = String(node?.title || "").trim();
    return STABLE_ID.test(fullId) ? fullId : "";
  }

  function showStatus(message) {
    const node = document.querySelector("#question-copy-status");
    if (!node) return;
    node.textContent = message;
    window.setTimeout(() => {
      if (node.textContent === message) node.textContent = "";
    }, 2500);
  }

  function updateReviewButton(button) {
    if (!button) return;
    const questionId = currentQuestionId();
    const sent = sentThisSession.has(questionId);
    button.textContent = sent ? "Sent for review" : "Send for review";
    button.disabled = !questionId || !reviewEndpoint || sent;
    button.title = !reviewConfigLoaded
      ? "Checking review service…"
      : !reviewEndpoint
        ? "Review service is not configured yet."
        : sent
          ? `${questionId} was sent for review.`
          : questionId
            ? `Send ${questionId} for review`
            : "Reference unavailable";
  }

  async function loadReviewConfig(button) {
    try {
      const response = await fetch(REVIEW_CONFIG_PATH, { cache: "no-store" });
      if (!response.ok) throw new Error(`Review config unavailable: ${response.status}`);
      const config = await response.json();
      reviewEndpoint = String(config?.endpoint || "").trim().replace(/\/$/, "");
    } catch (error) {
      console.warn("PrepFlow review service config unavailable:", error);
      reviewEndpoint = "";
    } finally {
      reviewConfigLoaded = true;
      updateReviewButton(button);
    }
  }

  async function sendForReview(button) {
    const questionId = currentQuestionId();
    if (!questionId || !reviewEndpoint || sentThisSession.has(questionId)) return;

    button.disabled = true;
    button.textContent = "Sending…";

    try {
      const response = await fetch(`${reviewEndpoint}/reports`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ question_id: questionId }),
      });
      const payload = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(payload.error || `Review request failed: ${response.status}`);
      sentThisSession.add(questionId);
      showStatus(payload.status === "already_submitted" ? "Already sent for review." : "Sent for review.");
    } catch (error) {
      showStatus(error.message || "Could not send for review.");
    } finally {
      updateReviewButton(button);
    }
  }

  function installReviewButton() {
    const actions = document.querySelector(".quiz-reference-actions");
    if (!actions || document.querySelector("#send-question-review")) return;

    const button = document.createElement("button");
    button.id = "send-question-review";
    button.type = "button";
    button.className = "quiz-reference-action";
    button.textContent = "Send for review";
    button.disabled = true;
    button.addEventListener("click", () => { void sendForReview(button); });
    actions.append(button);

    document.addEventListener("prepflow:question-shown", () => updateReviewButton(button));
    void loadReviewConfig(button);
  }

  window.PrepFlowQuestionReferenceRules = {
    reportText,
    stableReference,
    questionTypeLabel,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", installReviewButton, { once: true });
  } else {
    installReviewButton();
  }
}());
