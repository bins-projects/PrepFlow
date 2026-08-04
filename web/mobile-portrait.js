(function () {
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

  function createSafeStudyModuleManifest(manifest) {
    const groups = manifest.groups.map((group) => {
      const chapters = group.chapters.map((chapter) => {
        const questionIds = chapter.question_ids.filter(
          (questionId) => !QUARANTINED_QUESTION_IDS.has(questionId)
        );

        return {
          ...chapter,
          expected_question_count: questionIds.length,
          question_ids: questionIds,
        };
      });

      return { ...group, chapters };
    });

    const expectedQuestionCount = groups.reduce(
      (groupTotal, group) => groupTotal + group.chapters.reduce(
        (chapterTotal, chapter) => chapterTotal + chapter.question_ids.length,
        0
      ),
      0
    );

    return {
      ...manifest,
      expected_question_count: expectedQuestionCount,
      groups,
    };
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
      typeof renderStudyModule !== "function"
      || typeof startSession !== "function"
      || typeof readSavedSession !== "function"
      || typeof showFinalSummary !== "function"
    ) {
      return;
    }

    const originalRenderStudyModule = renderStudyModule;
    renderStudyModule = function (manifest, container) {
      return originalRenderStudyModule(
        createSafeStudyModuleManifest(manifest),
        container
      );
    };

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
