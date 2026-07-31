(function () {
  const root = document.documentElement;
  const quizScreen = document.querySelector("#quiz-screen");
  const quizBook = quizScreen.querySelector(".quiz-book");
  const questionHeading = document.querySelector("#question-stem");
  const responseHeading = document.querySelector("#response-page-label");
  const instruction = document.querySelector("#mobile-question-instruction");
  const answers = document.querySelector("#answer-choices");
  const feedbackHeading = document.querySelector("#feedback-result");
  const answerReview = document.querySelector("#mobile-answer-review");
  const submit = document.querySelector("#submit-answer");
  const continueButton = document.querySelector("#continue-button");
  const exitQuiz = document.querySelector("#exit-quiz");
  const viewAnswers = document.querySelector("#mobile-view-answers");
  const backQuestion = document.querySelector("#mobile-back-question");
  const viewQuestion = document.querySelector("#mobile-view-question");
  const backFeedback = document.querySelector("#mobile-back-feedback");
  const portraitQuery = window.matchMedia(
    "(max-width: 760px) and (orientation: portrait)"
  );
  const states = new Set(["question", "answers", "feedback", "review"]);
  const semanticAttributes = [
    [quizBook, ["role", "aria-label"]],
    [questionHeading, ["tabindex"]],
    [responseHeading, ["tabindex", "role", "aria-level"]],
    [feedbackHeading, ["tabindex"]],
  ];
  const originalAttributes = new Map();

  semanticAttributes.forEach(([element, attributes]) => {
    const values = new Map();
    attributes.forEach((attribute) => {
      values.set(attribute, element.getAttribute(attribute));
    });
    originalAttributes.set(element, values);
  });

  let state = "question";
  let gradedResult = null;
  let desktopFeedbackText = "";
  let answerInstruction = "Choose one answer";
  let subjectAccent = "fundamentals";
  let resultState = "";
  let transitionGeneration = 0;
  let focusFrame = null;
  let announcementFrame = null;
  let busyTimer = null;
  let unitRevealFrame = null;

  const clipboardImage = new Image();
  const clipboardReady = new Promise((resolve) => {
    let settled = false;

    function finish() {
      if (settled) return;
      settled = true;
      resolve();
    }

    function finishAfterDecode() {
      if (typeof clipboardImage.decode !== "function") {
        finish();
        return;
      }

      clipboardImage.decode().then(finish, finish);
    }

    clipboardImage.addEventListener("load", finishAfterDecode, { once: true });
    clipboardImage.addEventListener("error", finish, { once: true });
    clipboardImage.decoding = "async";
    clipboardImage.src =
      "images/quiz-builder/prepflow-mobile-chapter-clipboard.png";

    if (clipboardImage.complete && clipboardImage.naturalWidth > 0) {
      finishAfterDecode();
    }
  });

  const announcer = document.createElement("div");
  announcer.className = "sr-only mobile-quiz-announcer";
  quizScreen.append(announcer);

  function isPortraitQuiz() {
    return portraitQuery.matches
      && root.classList.contains("mobile-portrait")
      && !quizScreen.hidden;
  }

  function restoreAttribute(element, attribute) {
    const original = originalAttributes.get(element).get(attribute);

    if (original === null) {
      element.removeAttribute(attribute);
    } else {
      element.setAttribute(attribute, original);
    }
  }

  function invalidateDeferredWork() {
    transitionGeneration += 1;

    if (focusFrame !== null) {
      window.cancelAnimationFrame(focusFrame);
      focusFrame = null;
    }

    if (announcementFrame !== null) {
      window.cancelAnimationFrame(announcementFrame);
      announcementFrame = null;
    }

    if (busyTimer !== null) {
      window.clearTimeout(busyTimer);
      busyTimer = null;
    }

    if (unitRevealFrame !== null) {
      window.cancelAnimationFrame(unitRevealFrame);
      unitRevealFrame = null;
    }

    quizBook.removeAttribute("aria-busy");
    return transitionGeneration;
  }

  function concealMobileUnit() {
    if (unitRevealFrame !== null) {
      window.cancelAnimationFrame(unitRevealFrame);
      unitRevealFrame = null;
    }
    quizScreen.classList.remove("mobile-quiz-unit-visible");
  }

  function revealMobileUnit(expectedGeneration) {
    clipboardReady.then(() => {
      if (
        expectedGeneration !== transitionGeneration
        || !isPortraitQuiz()
      ) {
        return;
      }

      unitRevealFrame = window.requestAnimationFrame(() => {
        unitRevealFrame = null;
        if (
          expectedGeneration === transitionGeneration
          && isPortraitQuiz()
        ) {
          quizScreen.classList.add("mobile-quiz-unit-visible");
        }
      });
    });
  }

  function targetCanReceiveFocus(target) {
    if (!target || target.hidden || target.disabled) return false;
    if (target.closest('[aria-hidden="true"]')) return false;

    const style = window.getComputedStyle(target);
    return style.display !== "none" && style.visibility !== "hidden";
  }

  function focusForState(expectedState, generation) {
    focusFrame = window.requestAnimationFrame(() => {
      focusFrame = null;

      if (
        generation !== transitionGeneration
        || !isPortraitQuiz()
        || state !== expectedState
        || quizBook.dataset.mobileState !== expectedState
      ) {
        return;
      }

      const target = expectedState === "answers"
        ? responseHeading
        : expectedState === "feedback"
          ? feedbackHeading
          : questionHeading;

      if (targetCanReceiveFocus(target)) {
        target.focus({ preventScroll: true });
      }
    });
  }

  function applyMobileSemantics() {
    quizBook.setAttribute("role", "region");
    quizBook.setAttribute("aria-label", "Quiz clipboard");
    questionHeading.tabIndex = -1;
    responseHeading.tabIndex = -1;
    responseHeading.setAttribute("role", "heading");
    responseHeading.setAttribute("aria-level", "2");
    feedbackHeading.tabIndex = -1;
    announcer.setAttribute("aria-live", "polite");
    announcer.setAttribute("aria-atomic", "true");
  }

  function removeMobileSemantics() {
    semanticAttributes.forEach(([element, attributes]) => {
      attributes.forEach((attribute) => restoreAttribute(element, attribute));
    });
    announcer.removeAttribute("aria-live");
    announcer.removeAttribute("aria-atomic");
    delete quizBook.dataset.mobileState;
    delete quizBook.dataset.mobileResult;
    delete quizBook.dataset.subjectAccent;
    quizBook.removeAttribute("aria-busy");
    concealMobileUnit();
  }

  function syncMobileControls() {
    instruction.hidden = false;
    backFeedback.hidden = state !== "review";
    viewAnswers.hidden = state === "review";
    backQuestion.hidden = state !== "answers";
    viewQuestion.hidden = state !== "feedback";
    answerReview.hidden = state !== "feedback";
  }

  function hideMobileControls() {
    instruction.hidden = true;
    viewAnswers.hidden = true;
    backFeedback.hidden = true;
    backQuestion.hidden = true;
    viewQuestion.hidden = true;
    answerReview.hidden = true;
  }

  function announceState(generation) {
    const message = {
      question: "Question",
      answers: answerInstruction,
      feedback: feedbackHeading.textContent || "Feedback and rationale",
      review: "Question review",
    }[state];

    announcer.textContent = "";
    announcementFrame = window.requestAnimationFrame(() => {
      announcementFrame = null;

      if (generation === transitionGeneration && isPortraitQuiz()) {
        announcer.textContent = message;
      }
    });
  }

  function setState(nextState, options = {}) {
    if (!states.has(nextState)) return;

    state = nextState;
    const generation = invalidateDeferredWork();
    if (!isPortraitQuiz()) return;

    applyMobileSemantics();
    quizBook.dataset.mobileState = state;
    quizBook.dataset.subjectAccent = subjectAccent;
    if (resultState) quizBook.dataset.mobileResult = resultState;
    quizBook.setAttribute("aria-busy", "true");
    syncMobileControls();
    announceState(generation);

    busyTimer = window.setTimeout(() => {
      busyTimer = null;
      if (generation === transitionGeneration && isPortraitQuiz()) {
        quizBook.removeAttribute("aria-busy");
      }
    }, 260);

    if (options.focus !== false) {
      focusForState(state, generation);
    }
  }

  function normalizeLabel(label) {
    return String(label).trim().toUpperCase();
  }

  function fullChoiceText(label, choices) {
    const normalizedLabel = normalizeLabel(label);
    const choice = choices.find(
      (item) => normalizeLabel(item.label) === normalizedLabel
    );
    return choice ? `${choice.label}. ${choice.text}` : String(label);
  }

  function addReviewSection(title, labels, choices) {
    const section = document.createElement("section");
    const heading = document.createElement("h4");
    const list = document.createElement("ul");
    heading.textContent = title;
    labels.forEach((label) => {
      const item = document.createElement("li");
      item.textContent = fullChoiceText(label, choices);
      list.append(item);
    });
    section.append(heading, list);
    answerReview.append(section);
  }

  document.addEventListener("prepflow:question-shown", (event) => {
    invalidateDeferredWork();
    gradedResult = null;
    desktopFeedbackText = "";
    resultState = "";
    answerReview.replaceChildren();
    answerInstruction = event.detail.questionType === "multiple_response"
      ? "Select all that apply"
      : "Choose one answer";
    instruction.textContent = answerInstruction;
    const packPath = event.detail.packPath || "";
    subjectAccent = packPath.includes("pharmacy")
      ? "pharm"
      : packPath.includes("medical_surgical")
        ? "med-surg"
        : "fundamentals";
    setState("question", { focus: false });
  });

  document.addEventListener("prepflow:answer-graded", (event) => {
    const result = event.detail;
    gradedResult = result;
    desktopFeedbackText = feedbackHeading.textContent;
    resultState = result.isCorrect ? "correct" : "incorrect";
    answerReview.replaceChildren();

    if (isPortraitQuiz()) {
      feedbackHeading.textContent = result.isCorrect ? "Correct" : "Incorrect";
    }

    addReviewSection(
      result.multipleResponse ? "Your selections" : "Your answer",
      result.selectedAnswers,
      result.choices
    );

    if (!result.isCorrect) {
      addReviewSection(
        result.multipleResponse ? "Correct selections" : "Correct answer",
        result.correctAnswers,
        result.choices
      );
    }

    setState("feedback");
  });

  viewAnswers.addEventListener("click", () => setState("answers"));
  backQuestion.addEventListener("click", () => setState("question"));
  viewQuestion.addEventListener("click", () => setState("review"));
  backFeedback.addEventListener("click", () => setState("feedback"));
  exitQuiz.addEventListener("click", invalidateDeferredWork, true);
  submit.addEventListener("click", () => {
    if (!submit.disabled && isPortraitQuiz()) {
      quizBook.setAttribute("aria-busy", "true");
    }
  });
  continueButton.addEventListener("click", invalidateDeferredWork, true);

  function syncPortraitSemantics() {
    invalidateDeferredWork();

    if (isPortraitQuiz()) {
      applyMobileSemantics();
      responseHeading.textContent = answerInstruction;
      if (gradedResult) {
        feedbackHeading.textContent = gradedResult.isCorrect
          ? "Correct"
          : "Incorrect";
      }
      setState(state, { focus: false });
      revealMobileUnit(transitionGeneration);
    } else {
      removeMobileSemantics();
      hideMobileControls();
      responseHeading.textContent = answerInstruction === "Select all that apply"
        ? "Select All That Apply"
        : "Choose Your Answer";
      if (desktopFeedbackText) feedbackHeading.textContent = desktopFeedbackText;
    }
  }

  if (typeof portraitQuery.addEventListener === "function") {
    portraitQuery.addEventListener("change", syncPortraitSemantics);
  } else {
    portraitQuery.addListener(syncPortraitSemantics);
  }

  const presentationObserver = new MutationObserver(syncPortraitSemantics);
  presentationObserver.observe(quizScreen, {
    attributes: true,
    attributeFilter: ["hidden"],
  });
  presentationObserver.observe(root, {
    attributes: true,
    attributeFilter: ["class"],
  });
  syncPortraitSemantics();
}());
