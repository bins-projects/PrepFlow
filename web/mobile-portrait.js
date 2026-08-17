(function () {
  const unifiedPhoneTest = new URLSearchParams(window.location.search).get("unified") === "1";
  const initialPhoneQuery = window.matchMedia(
    "(max-width: 820px) and (pointer: coarse)"
  );

  if (unifiedPhoneTest && initialPhoneQuery.matches) {
    const viewport = document.querySelector('meta[name="viewport"]');
    if (viewport) {
      viewport.setAttribute(
        "content",
        "width=1200, initial-scale=1, viewport-fit=cover"
      );
    }

    document.documentElement.dataset.unifiedPhoneUi = "true";

    const unifiedPhoneStyle = document.createElement("style");
    unifiedPhoneStyle.id = "unified-phone-ui-styles";
    unifiedPhoneStyle.textContent = `
      html[data-unified-phone-ui="true"] #quiz-screen.quiz-screen:not([hidden]) {
        box-sizing: border-box !important;
        padding:
          max(env(safe-area-inset-top), 12px)
          max(env(safe-area-inset-right), 12px)
          max(env(safe-area-inset-bottom), 12px)
          max(env(safe-area-inset-left), 12px) !important;
      }

      html[data-unified-phone-ui="true"] #quiz-screen .quiz-book {
        transform-origin: center center !important;
      }

      html[data-unified-phone-ui="true"] #phone-orientation-hint {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 50%;
        top: max(env(safe-area-inset-top), 12px);
        transform: translateX(-50%);
        padding: 7px 12px;
        border: 1px solid rgba(220, 174, 73, .72);
        border-radius: 999px;
        color: #fff1bd;
        background: rgba(9, 10, 42, .86);
        font: 800 12px/1.15 Arial, Helvetica, sans-serif;
        letter-spacing: .02em;
        box-shadow: 0 3px 10px rgba(0, 0, 0, .28);
        pointer-events: none;
      }

      @media (orientation: portrait) {
        html[data-unified-phone-ui="true"] body:has(#quiz-screen:not([hidden])) #phone-orientation-hint {
          display: block;
        }
      }
    `;
    document.head.appendChild(unifiedPhoneStyle);

    function ensureOrientationHint() {
      if (document.getElementById("phone-orientation-hint")) return;
      const hint = document.createElement("div");
      hint.id = "phone-orientation-hint";
      hint.setAttribute("aria-hidden", "true");
      hint.textContent = "Rotate to landscape for the full book view";
      document.body.appendChild(hint);
    }

    function fitQuizBookToPhoneViewport() {
      const book = document.querySelector("#quiz-screen .quiz-book");
      if (!book) return;

      const viewportWidth = window.visualViewport?.width || window.innerWidth;
      const viewportHeight = window.visualViewport?.height || window.innerHeight;
      const horizontalRoom = Math.max(320, viewportWidth - 40);
      const verticalRoom = Math.max(260, viewportHeight - 44);
      const bookRatio = 1.72;
      const fittedWidth = Math.min(horizontalRoom, verticalRoom * bookRatio, 1420);
      const fittedHeight = fittedWidth / bookRatio;

      book.style.setProperty("width", `${fittedWidth}px`, "important");
      book.style.setProperty("height", `${fittedHeight}px`, "important");
    }

    function syncPhoneQuizLayout() {
      ensureOrientationHint();
      fitQuizBookToPhoneViewport();
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", syncPhoneQuizLayout, { once: true });
    } else {
      syncPhoneQuizLayout();
    }

    window.addEventListener("resize", syncPhoneQuizLayout);
    window.addEventListener("orientationchange", syncPhoneQuizLayout);
    window.visualViewport?.addEventListener("resize", syncPhoneQuizLayout);
  }

  const portraitQuery = window.matchMedia(
    "(max-width: 760px) and (orientation: portrait)"
  );

  function syncMobilePortraitMode() {
    document.documentElement.classList.toggle(
      "mobile-portrait",
      portraitQuery.matches
    );
  }

  syncMobilePortraitMode();

  if (typeof portraitQuery.addEventListener === "function") {
    portraitQuery.addEventListener("change", syncMobilePortraitMode);
  } else {
    portraitQuery.addListener(syncMobilePortraitMode);
  }
}());

(function () {
  const QUARANTINED_QUESTION_IDS = new Set([
    "PFQ-fundamentals-000000937",
  ]);

  function isQuarantinedReference(reference) {
    return Boolean(
      reference
      && QUARANTINED_QUESTION_IDS.has(reference.questionId)
    );
  }

  function filterReferences(references) {
    return Array.isArray(references)
      ? references.filter((reference) => !isQuarantinedReference(reference))
      : [];
  }

  function installFinalSummaryPresentation() {
    if (document.querySelector("#prepflow-final-summary-mobile-fix")) {
      return;
    }

    const style = document.createElement("style");
    style.id = "prepflow-final-summary-mobile-fix";
    style.textContent = `
      html.mobile-portrait #block-summary[data-summary-state="final"]:not([hidden]) {
        position: fixed !important;
        z-index: 140 !important;
        inset: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 1rem !important;
        width: 100% !important;
        max-width: none !important;
        min-height: 100dvh !important;
        margin: 0 !important;
        padding: max(2rem, env(safe-area-inset-top)) 1.25rem max(2rem, env(safe-area-inset-bottom)) !important;
        border: 0 !important;
        border-radius: 0 !important;
        background:
          linear-gradient(rgba(3, 9, 29, .76), rgba(3, 9, 29, .86)),
          url("images/quiz-builder/prepflow-mobile-quiz-builder-background.png") center / cover no-repeat !important;
        box-shadow: none !important;
        overflow-y: auto !important;
      }

      html.mobile-portrait #block-summary[data-summary-state="final"]:not([hidden]) > * {
        width: min(100%, 32rem) !important;
        margin-inline: auto !important;
      }

      html.mobile-portrait #block-summary[data-summary-state="final"] #summary-title {
        color: #fff7dc !important;
        font-size: clamp(2rem, 10vw, 3rem) !important;
        line-height: 1.05 !important;
        text-shadow: 3px 3px 0 #111a36 !important;
      }

      html.mobile-portrait #block-summary[data-summary-state="final"] #summary-score,
      html.mobile-portrait #block-summary[data-summary-state="final"] #summary-message {
        padding: .9rem 1rem !important;
        border: 2px solid #315fa8 !important;
        background: rgba(248, 241, 220, .96) !important;
        color: #172540 !important;
        font-family: Arial, Helvetica, sans-serif !important;
        text-align: center !important;
      }

      html.mobile-portrait #block-summary[data-summary-state="final"] #summary-action {
        min-height: 3.25rem !important;
        border-color: #5de5ff !important;
        background: #101936 !important;
        color: #fff !important;
      }
    `;
    document.head.append(style);
  }

  function installQuizLifecycleSafeguards() {
    if (
      typeof startSession !== "function"
      || typeof readSavedSession !== "function"
      || typeof showFinalSummary !== "function"
    ) {
      return;
    }

    const originalStartSession = startSession;
    startSession = async function (questionReferences, ...args) {
      return originalStartSession(filterReferences(questionReferences), ...args);
    };

    const originalReadSavedSession = readSavedSession;
    readSavedSession = function () {
      const saved = originalReadSavedSession();

      if (!saved || !Array.isArray(saved.sessionQuestions)) {
        return saved;
      }

      const originalQuestions = saved.sessionQuestions;
      const sessionQuestions = filterReferences(originalQuestions);
      const blockMissed = filterReferences(saved.blockMissed);
      const reviewQueue = filterReferences(saved.reviewQueue);
      const currentReviewWasQuarantined = isQuarantinedReference(
        saved.currentReviewQuestion
      );
      const currentQuestionWasQuarantined = isQuarantinedReference(
        originalQuestions[Number(saved.questionIndex) || 0]
      );

      if (
        sessionQuestions.length === originalQuestions.length
        && blockMissed.length === (saved.blockMissed || []).length
        && reviewQueue.length === (saved.reviewQueue || []).length
        && !currentReviewWasQuarantined
      ) {
        return saved;
      }

      const removedBefore = (boundary) => originalQuestions
        .slice(0, Math.max(0, Number(boundary) || 0))
        .filter(isQuarantinedReference)
        .length;

      const cleaned = {
        ...saved,
        sessionQuestions,
        blockStart: Math.max(
          0,
          (Number(saved.blockStart) || 0) - removedBefore(saved.blockStart)
        ),
        blockEnd: Math.max(
          0,
          (Number(saved.blockEnd) || 0) - removedBefore(saved.blockEnd)
        ),
        questionIndex: Math.max(
          0,
          (Number(saved.questionIndex) || 0) - removedBefore(saved.questionIndex)
        ),
        blockMissed,
        reviewQueue,
        currentReviewQuestion: currentReviewWasQuarantined
          ? null
          : saved.currentReviewQuestion,
        firstPassMissed: Math.max(
          0,
          (Number(saved.firstPassMissed) || 0)
          - ((saved.blockMissed || []).length - blockMissed.length)
        ),
        screen: currentQuestionWasQuarantined || currentReviewWasQuarantined
          ? "question"
          : saved.screen,
      };

      cleaned.blockStart = Math.min(cleaned.blockStart, sessionQuestions.length);
      cleaned.blockEnd = Math.min(
        Math.max(cleaned.blockStart, cleaned.blockEnd),
        sessionQuestions.length
      );
      cleaned.questionIndex = Math.min(
        cleaned.questionIndex,
        sessionQuestions.length
      );

      localStorage.setItem(SAVE_KEY, JSON.stringify(cleaned));
      return cleaned;
    };

    const originalShowFinalSummary = showFinalSummary;
    showFinalSummary = function () {
      originalShowFinalSummary();

      selectedChapters.clear();
      updateSelectionStatus();

      quizBuilder.hidden = true;
      resumePanel.hidden = true;
      blockSummary.hidden = false;
    };
  }

  document.addEventListener("DOMContentLoaded", () => {
    installFinalSummaryPresentation();
    installQuizLifecycleSafeguards();
  }, { once: true });
}());
