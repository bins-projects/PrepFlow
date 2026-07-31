const SAVE_KEY = "prepflow.savedSession.v1";

const hero = document.querySelector(".hero");
const subjects = document.querySelector(".subjects");
const status = document.querySelector("#status");
const homeLauncher = document.querySelector("#home-launcher");
const quizBuilderScreen = document.querySelector("#quiz-builder-screen");
const openQuizBuilderButton = document.querySelector("#open-quiz-builder");
const closeQuizBuilderButton = document.querySelector("#close-quiz-builder");
const doneChaptersButton = document.querySelector("#done-chapters");
const quizBuilderOpenBook = document.querySelector("#quiz-builder-openbook");

const resumePanel = document.querySelector("#resume-panel");
const resumeDescription = document.querySelector("#resume-description");
const resumeSessionButton = document.querySelector("#resume-session");
const discardSessionButton = document.querySelector("#discard-session");

const chapterScreen = document.querySelector("#chapter-screen");
const chapterTitle = document.querySelector("#chapter-title");
const chapterList = document.querySelector("#chapter-list");
const selectionCount = document.querySelector("#selection-count");
const selectedChapterSummary = document.querySelector("#selected-chapter-summary");
const selectedQuestionSummary = document.querySelector("#selected-question-summary");
const selectedChapterNumbers = document.querySelector("#selected-chapter-numbers");
const startButton = document.querySelector("#start-button");
const blockSizeSelect = document.querySelector("#block-size");

const quizBuilder = document.querySelector("#quiz-builder");
const builderSelectionCount = document.querySelector("#builder-selection-count");
const builderBookCount = document.querySelector("#builder-book-count");
const globalBlockSizeSelect = document.querySelector("#global-block-size");
const shuffleQuestionsToggle = document.querySelector("#shuffle-questions");
const clearSelectionsButton = document.querySelector("#clear-selections");
const buildQuizButton = document.querySelector("#build-quiz");

const quizScreen = document.querySelector("#quiz-screen");
const quizSubject = document.querySelector("#quiz-subject");
const quizPosition = document.querySelector("#quiz-position");
const quizProgress = document.querySelector("#quiz-progress");
const questionStem = document.querySelector("#question-stem");
const answerChoices = document.querySelector("#answer-choices");
const responsePageLabel = document.querySelector("#response-page-label");
const feedback = document.querySelector("#feedback");
const feedbackResult = document.querySelector("#feedback-result");
const feedbackRationale = document.querySelector("#feedback-rationale");
const quizScore = document.querySelector("#quiz-score");
const submitAnswer = document.querySelector("#submit-answer");
const continueButton = document.querySelector("#continue-button");

const blockSummary = document.querySelector("#block-summary");
const summaryTitle = document.querySelector("#summary-title");
const summaryScore = document.querySelector("#summary-score");
const summaryMessage = document.querySelector("#summary-message");
const summaryAction = document.querySelector("#summary-action");
const summaryExit = document.querySelector("#summary-exit");

let currentSubject = null;
let currentPack = null;
let currentPackPath = null;

const loadedPacks = new Map();
const selectedChapters = new Map();

let sessionQuestions = [];
let sessionBlockSize = 15;
let sessionShuffleQuestions = true;

let blockStart = 0;
let blockEnd = 0;
let questionIndex = 0;
let blockNumber = 1;

let firstPassCorrect = 0;
let firstPassMissed = 0;
let blockCorrect = 0;
let blockMissed = [];

let reviewQueue = [];
let reviewMode = false;
let currentReviewQuestion = null;
let questionSubmissionState = "idle";

function readSavedSession() {
  const raw = localStorage.getItem(SAVE_KEY);
  const result = PrepFlowSavedSessionRules.parseSavedSession(raw, 3);

  if (result.shouldClear) {
    localStorage.removeItem(SAVE_KEY);
  }

  return result.saved;
}

function clearSavedSession() {
  localStorage.removeItem(SAVE_KEY);
  refreshResumePanel();
}

function saveSession(screen) {
  if (sessionQuestions.length === 0) {
    return;
  }

  const state = {
    version: 3,
    savedAt: new Date().toISOString(),
    screen,
    currentSubject,
    sessionQuestions,
    sessionBlockSize,
    sessionShuffleQuestions,
    blockStart,
    blockEnd,
    questionIndex,
    blockNumber,
    firstPassCorrect,
    firstPassMissed,
    blockCorrect,
    blockMissed,
    reviewQueue,
    reviewMode,
    currentReviewQuestion,
  };

  localStorage.setItem(SAVE_KEY, JSON.stringify(state));
}

function refreshResumePanel() {
  const saved = readSavedSession();
  const hasSavedSession = Boolean(saved);

  quizBuilder.hidden = hasSavedSession;
  resumePanel.hidden = !hasSavedSession;

  if (!saved) {
    resumeDescription.textContent = "";
    return;
  }

  const description = PrepFlowResumeRules.resumeDescription(saved);

  resumeDescription.textContent = description;
  resumeSessionButton.title = description;
  resumeSessionButton.setAttribute(
    "aria-label",
    PrepFlowResumeRules.resumeAriaLabel(description)
  );
}

function hideAllScreens() {
  hero.hidden = true;
  subjects.hidden = true;
  homeLauncher.hidden = true;
  quizBuilderScreen.hidden = true;
  quizBuilder.hidden = true;
  resumePanel.hidden = true;
  chapterScreen.hidden = true;
  quizScreen.hidden = true;
  blockSummary.hidden = true;
  status.hidden = true;
}

function updateSelectionStatus() {
  const totalSelected = selectedChapters.size;

  const allSelections = [...selectedChapters.values()];
  const currentBookSelections = allSelections.filter(
    (selection) => selection.packPath === currentPackPath
  );

  const currentBookSelected = currentBookSelections.length;

  const selectedPackPaths = new Set(
    allSelections.map((selection) => selection.packPath)
  );
  const selectedBooks = selectedPackPaths.size;

  const totalChapterSelectionText =
    PrepFlowSelectionRules.chapterSelectionText(totalSelected);

  const currentBookChapterSelectionText =
    PrepFlowSelectionRules.chapterSelectionText(currentBookSelected);

  const currentBookQuestions = currentBookSelections.reduce(
    (total, selection) => total + (selection.questionCount || 0),
    0
  );

  selectionCount.textContent = currentBookChapterSelectionText;
  selectedChapterSummary.textContent =
    currentBookChapterSelectionText;
  selectedQuestionSummary.textContent =
    `${currentBookQuestions.toLocaleString()} ${
      currentBookQuestions === 1 ? "question" : "questions"
    } selected`;

  const currentBookChapterNumbers = currentBookSelections
    .map((selection) => String(selection.chapterKey).split("|", 1)[0])
    .filter(Boolean);

  const visibleChapterNumbers = currentBookChapterNumbers.slice(0, 5);
  const remainingChapterCount =
    currentBookChapterNumbers.length - visibleChapterNumbers.length;

  selectedChapterNumbers.textContent =
    visibleChapterNumbers.length === 0
      ? "Selected: none"
      : `Selected: ${visibleChapterNumbers.join(", ")}${
          remainingChapterCount > 0
            ? ` +${remainingChapterCount} more`
            : ""
        }`;

  builderSelectionCount.textContent =
    totalChapterSelectionText;
  builderBookCount.textContent =
    PrepFlowSelectionRules.bookSelectionText(
      totalSelected,
      selectedBooks
    );

  startButton.disabled = totalSelected === 0;
  buildQuizButton.disabled = totalSelected === 0;
  clearSelectionsButton.disabled = totalSelected === 0;

  document.querySelectorAll(".subject-card").forEach((book) => {
    const packPath = book.dataset.pack;
    const count = [...selectedChapters.values()].filter(
      (selection) => selection.packPath === packPath
    ).length;

    let badge = book.querySelector(".book-selected-count");

    if (!badge) {
      badge = document.createElement("span");
      badge.className = "book-selected-count";
      book.append(badge);
    }

    badge.textContent = count > 0 ? PrepFlowSelectionRules.bookBadgeText(count) : "";

    book.classList.toggle("has-selections", count > 0);
  });
}

function showSubjects() {
  document.body.classList.remove(
    "book-open",
    "real-book-chapters"
  );
  hideAllScreens();

  hero.hidden = false;
  homeLauncher.hidden = false;
  status.hidden = true;

  const selected = selectedChapters.size;
  status.textContent = PrepFlowSelectionRules.homeStatusText(selected);

  refreshResumePanel();
}

function showQuizBuilder() {
  document.body.classList.remove(
    "book-open",
    "real-book-chapters"
  );
  document.body.classList.add("builder-open");

  hideAllScreens();

  quizBuilderScreen.hidden = false;
  subjects.hidden = false;

  updateSelectionStatus();
}

async function loadPack(packPath) {
  if (loadedPacks.has(packPath)) {
    return loadedPacks.get(packPath);
  }

  const response = await fetch(packPath);

  if (!response.ok) {
    throw new Error(`Could not load study category: ${response.status}`);
  }

  const pack = await response.json();
  loadedPacks.set(packPath, pack);
  return pack;
}

async function showChapters(button) {
  status.textContent = "Loading chapters…";

  try {
    currentPackPath = button.dataset.pack;
    currentPack = await loadPack(currentPackPath);
    currentSubject = button.dataset.subject;

    const chapters = new Map();

    currentPack.questions.forEach((question) => {
      const key = `${question.chapter}|${question.chapter_title}`;
      const existing = chapters.get(key);

      if (existing) {
        existing.count += 1;
      } else {
        chapters.set(key, {
          number: question.chapter,
          title: question.chapter_title || "Untitled Chapter",
          count: 1,
        });
      }
    });

    chapterList.replaceChildren();

    chapters.forEach((chapter, key) => {
      const label = document.createElement("label");
      label.className = "chapter-option";

      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.value = key;
      checkbox.dataset.questionCount = chapter.count;

      const selectionKey = `${currentPackPath}|${key}`;
      checkbox.checked = selectedChapters.has(selectionKey);

      checkbox.addEventListener("change", () => {
        if (checkbox.checked) {
          selectedChapters.set(selectionKey, {
            packPath: currentPackPath,
            subject: currentSubject,
            chapterKey: key,
            questionCount: chapter.count,
          });
        } else {
          selectedChapters.delete(selectionKey);
        }

        updateSelectionStatus();
      });

      const text = document.createElement("span");
      text.className = "chapter-option-text";

      const name = document.createElement("span");
      name.className = "chapter-name";
      name.textContent = `Chapter ${chapter.number}: ${chapter.title}`;

      const count = document.createElement("span");
      count.className = "chapter-count";
      count.textContent = `${chapter.count.toLocaleString()} questions`;

      text.append(name, count);
      label.append(checkbox, text);
      chapterList.append(label);
    });

    chapterTitle.textContent = currentSubject;
    chapterScreen.dataset.theme =
      button.classList.contains("fundamentals") ? "fundamentals" :
      button.classList.contains("pharm") ? "pharm" :
      "med-surg";

    const usesRealOpenBook = true;

    chapterScreen.hidden = false;

    if (usesRealOpenBook) {
      /*
        Keep the approved nursing-station scene visible beneath the real
        open-book chapter interface.
      */
      quizBuilderScreen.hidden = false;
      document.body.classList.add(
        "builder-open",
        "book-open",
        "real-book-chapters"
      );
    } else {
      quizBuilderScreen.hidden = true;
      document.body.classList.remove(
        "builder-open",
        "real-book-chapters"
      );
      document.body.classList.add("book-open");
    }

    status.hidden = true;
    chapterList.scrollTop = 0;

    updateSelectionStatus();
  } catch (error) {
    status.hidden = false;
    status.textContent = error.message;
  }
}

function currentQuestionReference() {
  return reviewMode ? currentReviewQuestion : sessionQuestions[questionIndex];
}

function currentQuestion() {
  const reference = currentQuestionReference();
  const pack = loadedPacks.get(reference.packPath);

  if (!pack) {
    throw new Error(`Study category is not loaded: ${reference.packPath}`);
  }

  const question = pack.questions.find(
    (candidate) => candidate.id === reference.questionId
  );

  if (!question) {
    throw new Error(
      `Question is not available: ${reference.questionId}`
    );
  }

  return question;
}

function totalBlockCount() {
  return PrepFlowSessionRules.totalBlockCount(
    sessionQuestions.length,
    sessionBlockSize
  );
}

function showQuestion() {
  const question = currentQuestion();
  const isMultipleResponse = PrepFlowQuizRules.isMultipleResponseQuestion(question);
  const blockLength = blockEnd - blockStart;

  questionSubmissionState = "idle";

  hideAllScreens();
  quizScreen.hidden = false;

  quizSubject.textContent = currentSubject;

  if (reviewMode) {
    quizPosition.textContent = PrepFlowDisplayRules.quizPositionText({
      blockNumber,
      totalBlocks: totalBlockCount(),
      reviewMode: true,
      reviewRemaining: reviewQueue.length + 1,
      questionInBlock: null,
      blockLength,
    });

    quizProgress.max = Math.max(reviewQueue.length + 1, 1);
    quizProgress.value = 1;
  } else {
    const questionInBlock = PrepFlowSessionRules.questionPosition(
      questionIndex,
      blockStart
    );

    quizPosition.textContent = PrepFlowDisplayRules.quizPositionText({
      blockNumber,
      totalBlocks: totalBlockCount(),
      reviewMode: false,
      reviewRemaining: null,
      questionInBlock,
      blockLength,
    });

    quizProgress.max = blockLength;
    quizProgress.value = questionInBlock;
  }

  questionStem.textContent = question.stem;
  responsePageLabel.textContent = isMultipleResponse
    ? "Select All That Apply"
    : "Choose Your Answer";
  answerChoices.hidden = false;
  answerChoices.replaceChildren();

  question.choices.forEach((choice) => {
    const label = document.createElement("label");
    label.className = "answer-choice";

    const input = document.createElement("input");
    input.type = isMultipleResponse ? "checkbox" : "radio";
    input.name = "answer";
    input.value = choice.label;

    input.addEventListener("change", () => {
      submitAnswer.disabled =
        answerChoices.querySelectorAll('input[name="answer"]:checked').length === 0;
    });

    const text = document.createElement("span");
    text.textContent = `${choice.label}. ${choice.text}`;

    label.append(input, text);
    answerChoices.append(label);
  });

  feedback.hidden = true;
  submitAnswer.hidden = false;
  submitAnswer.disabled = true;
  continueButton.hidden = true;

  quizScore.textContent = PrepFlowDisplayRules.runningScoreText(
    firstPassCorrect,
    firstPassMissed
  );

  saveSession("question");

  document.dispatchEvent(new CustomEvent("prepflow:question-shown", {
    detail: {
      questionType: question.type || question.question_type,
      packPath: currentQuestionReference().packPath,
    },
  }));
}

function beginBlock() {
  blockEnd = PrepFlowSessionRules.blockEnd(
    blockStart,
    sessionBlockSize,
    sessionQuestions.length
  );

  questionIndex = blockStart;
  blockCorrect = 0;
  blockMissed = [];
  reviewQueue = [];
  reviewMode = false;
  currentReviewQuestion = null;

  showQuestion();
}

function showFinalSummary() {
  hideAllScreens();
  blockSummary.hidden = false;

  const totalQuestions = sessionQuestions.length;
  const percentage = PrepFlowSessionRules.firstPassPercentage(
    firstPassCorrect,
    totalQuestions
  );

  summaryTitle.textContent = "Quiz Complete";
  summaryScore.textContent = PrepFlowDisplayRules.finalScoreText(percentage);
  summaryMessage.textContent = PrepFlowDisplayRules.finalMessage(
    firstPassCorrect,
    totalQuestions
  );

  summaryAction.textContent = "Return Home";
  summaryAction.dataset.action = "return-home";
  summaryExit.hidden = true;

  clearSavedSession();
}

function showBlockSummary(mastered = false) {
  summaryExit.hidden = false;
  hideAllScreens();
  blockSummary.hidden = false;

  const blockLength = blockEnd - blockStart;
  const missedCount = blockMissed.length;

  summaryTitle.textContent = PrepFlowDisplayRules.blockTitle(
    blockNumber,
    mastered
  );
  summaryScore.textContent = PrepFlowDisplayRules.firstPassBlockScoreText(
    blockCorrect,
    blockLength
  );
  summaryMessage.textContent = PrepFlowDisplayRules.blockMessage(
    missedCount,
    mastered
  );

  const nextAction = PrepFlowSummaryRules.summaryAction({
    mastered,
    missedCount,
    hasMoreQuestions: blockEnd < sessionQuestions.length,
  });

  summaryAction.textContent = nextAction.label;
  summaryAction.dataset.action = nextAction.action;

  saveSession(mastered ? "mastered-summary" : "block-summary");
}

function startReview() {
  reviewMode = true;
  reviewQueue = [...blockMissed];
  currentReviewQuestion = reviewQueue.shift();
  showQuestion();
}

async function startQuiz() {
  const selectedQuestions = [];

  try {
    for (const selection of selectedChapters.values()) {
      const pack = await loadPack(selection.packPath);

      pack.questions.forEach((question) => {
        const key = `${question.chapter}|${question.chapter_title}`;

        if (
          key === selection.chapterKey
          && [
            "mc",
            "multiple_choice",
            "multiple_response",
          ].includes(question.type || question.question_type)
        ) {
          selectedQuestions.push({
            packPath: selection.packPath,
            questionId: question.id,
          });
        }
      });
    }
  } catch (error) {
    status.hidden = false;
    status.textContent = error.message;
    return;
  }

  sessionShuffleQuestions = shuffleQuestionsToggle.checked;
  sessionQuestions = PrepFlowOrderRules.orderQuestions(
    selectedQuestions,
    sessionShuffleQuestions
  );

  if (sessionQuestions.length === 0) {
    status.hidden = false;
    status.textContent =
      "No Multiple Choice or Multiple Response questions were found in that selection.";
    return;
  }

  currentSubject = "Custom Quiz";
  sessionBlockSize = Number(globalBlockSizeSelect.value) || 15;

  blockStart = 0;
  blockNumber = 1;
  firstPassCorrect = 0;
  firstPassMissed = 0;

  beginBlock();
}

async function resumeSavedSession() {
  const saved = readSavedSession();

  if (!saved) {
    showSubjects();
    return;
  }

  try {
    currentSubject = saved.currentSubject || "Custom Quiz";
    sessionQuestions = saved.sessionQuestions || [];
    sessionShuffleQuestions = saved.sessionShuffleQuestions !== false;
    shuffleQuestionsToggle.checked = sessionShuffleQuestions;

    const packPaths = new Set(
      sessionQuestions
        .map((reference) => reference && reference.packPath)
        .filter(Boolean)
    );

    for (const packPath of packPaths) {
      await loadPack(packPath);
    }

    sessionBlockSize = saved.sessionBlockSize;
    blockStart = saved.blockStart;
    blockEnd = saved.blockEnd;
    questionIndex = saved.questionIndex;
    blockNumber = saved.blockNumber;

    firstPassCorrect = saved.firstPassCorrect;
    firstPassMissed = saved.firstPassMissed;
    blockCorrect = saved.blockCorrect;
    blockMissed = saved.blockMissed || [];

    reviewQueue = saved.reviewQueue || [];
    reviewMode = Boolean(saved.reviewMode);
    currentReviewQuestion = saved.currentReviewQuestion;

    if (
      saved.screen === "block-summary"
      || saved.screen === "mastered-summary"
    ) {
      showBlockSummary(saved.screen === "mastered-summary");
    } else {
      showQuestion();
    }
  } catch (error) {
    clearSavedSession();
    showSubjects();
    status.textContent = `Saved session could not be restored: ${error.message}`;
  }
}

submitAnswer.addEventListener("click", () => {
  if (questionSubmissionState !== "idle") {
    return;
  }

  const selected = answerChoices.querySelectorAll(
    'input[name="answer"]:checked'
  );

  if (selected.length === 0) {
    return;
  }

  questionSubmissionState = "grading";
  submitAnswer.disabled = true;

  let scoringStarted = false;

  try {
    const question = currentQuestion();
    const selectedAnswers = Array.from(selected, (input) => input.value);
    const { isCorrect, correctAnswers } =
      PrepFlowQuizRules.evaluateAnswer(question, selectedAnswers);

    scoringStarted = true;

    if (isCorrect) {
      feedbackResult.textContent = "Correct!";

      if (!reviewMode) {
        firstPassCorrect += 1;
        blockCorrect += 1;
      }
    } else {
      feedbackResult.textContent =
        `Incorrect. Correct answer: ${correctAnswers.join(", ")}`;

      if (reviewMode) {
        reviewQueue = PrepFlowReviewRules.queueAfterAnswer(
          reviewQueue,
          currentReviewQuestion,
          false
        );
      } else {
        firstPassMissed += 1;
        blockMissed.push(sessionQuestions[questionIndex]);
      }
    }

    questionSubmissionState = "submitted";
    feedbackRationale.textContent = question.rationale || "";

    document.dispatchEvent(new CustomEvent("prepflow:answer-graded", {
      detail: {
        isCorrect,
        selectedAnswers,
        correctAnswers,
        choices: question.choices.map((choice) => ({
          label: choice.label,
          text: choice.text,
        })),
        multipleResponse: PrepFlowQuizRules.isMultipleResponseQuestion(question),
      },
    }));
    answerChoices.hidden = true;
    feedback.hidden = false;

    answerChoices.querySelectorAll("input").forEach((input) => {
      input.disabled = true;
    });

    quizScore.textContent = PrepFlowDisplayRules.runningScoreText(
      firstPassCorrect,
      firstPassMissed
    );

    submitAnswer.hidden = true;
    continueButton.hidden = false;
  } catch (error) {
    if (!scoringStarted) {
      questionSubmissionState = "idle";
      submitAnswer.disabled = false;
    }

    throw error;
  }
});

continueButton.addEventListener("click", () => {
  if (reviewMode) {
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
  }

  const nextStep = PrepFlowNavigationRules.nextQuestionStep(
    questionIndex,
    blockEnd
  );
  questionIndex = nextStep.questionIndex;

  if (nextStep.blockComplete) {
    showBlockSummary(false);
    return;
  }

  showQuestion();
});

summaryAction.addEventListener("click", () => {
  const action = summaryAction.dataset.action;

  if (action === "review") {
    startReview();
    return;
  }

  if (action === "next-block") {
    blockStart = blockEnd;
    blockNumber += 1;
    beginBlock();
    return;
  }

  if (action === "finish") {
    showFinalSummary();
    return;
  }

  clearSavedSession();
  selectedChapters.clear();
  showSubjects();
});

openQuizBuilderButton.addEventListener("click", showQuizBuilder);
closeQuizBuilderButton.addEventListener("click", () => {
  document.body.classList.remove("builder-open");
  showSubjects();
});
doneChaptersButton.addEventListener("click", showQuizBuilder);

const BOOK_LAUNCH_DURATION_MS = 1150;
const OPEN_BOOK_REVEAL_MS = 760;
const OPEN_BOOK_TOTAL_MS = 1500;
const BOOK_CLOSE_DURATION_MS = 760;
const MOBILE_BOOK_LAUNCH_DURATION_MS = 240;
const MOBILE_BOOK_CLOSE_DURATION_MS = 220;

let bookLaunchInProgress = false;
let bookCloseInProgress = false;
let activeBookButton = null;

function wait(milliseconds) {
  return new Promise((resolve) => window.setTimeout(resolve, milliseconds));
}

function usesMobilePortraitPresentation() {
  return (
    document.documentElement.classList.contains("mobile-portrait")
    && window.matchMedia(
      "(max-width: 760px) and (orientation: portrait)"
    ).matches
  );
}

async function launchBook(button) {
  if (bookLaunchInProgress) {
    return;
  }

  activeBookButton = button;

  const usesMobileTransition = usesMobilePortraitPresentation();
  const usesOpenBookTransition = !usesMobileTransition;

  bookLaunchInProgress = true;
  document.body.classList.add("book-launching");
  button.classList.add("is-launching");
  button.setAttribute("aria-busy", "true");

  try {
    if (usesMobileTransition) {
      await wait(MOBILE_BOOK_LAUNCH_DURATION_MS);
    } else if (usesOpenBookTransition) {
      await wait(OPEN_BOOK_REVEAL_MS);

      quizBuilderOpenBook.hidden = false;

      /*
        Allow the browser to establish the hidden starting state before
        activating the fade-and-settle transition.
      */
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          document.body.classList.add("book-opening");
        });
      });

      await wait(
        OPEN_BOOK_TOTAL_MS - OPEN_BOOK_REVEAL_MS
      );
    } else {
      await wait(BOOK_LAUNCH_DURATION_MS);
    }

    await showChapters(button);
  } finally {
    button.classList.remove("is-launching");
    button.removeAttribute("aria-busy");

    document.body.classList.remove(
      "book-launching",
      "book-opening"
    );

    quizBuilderOpenBook.hidden = true;
    bookLaunchInProgress = false;
  }
}

document.querySelectorAll(".subject-card").forEach((button) => {
  button.addEventListener("click", () => launchBook(button));
});

async function closeCurrentBook() {
  if (bookCloseInProgress || bookLaunchInProgress) {
    return;
  }

  const usesRealOpenBook =
    document.body.classList.contains("real-book-chapters");

  if (!usesRealOpenBook || !activeBookButton) {
    showQuizBuilder();
    activeBookButton = null;
    return;
  }

  bookCloseInProgress = true;

  document.body.classList.add("book-closing");
  activeBookButton.classList.add("is-closing");
  activeBookButton.setAttribute("aria-busy", "true");

  try {
    await wait(
      usesMobilePortraitPresentation()
        ? MOBILE_BOOK_CLOSE_DURATION_MS
        : BOOK_CLOSE_DURATION_MS
    );
    showQuizBuilder();
  } finally {
    document.body.classList.remove("book-closing");
    activeBookButton.classList.remove("is-closing");
    activeBookButton.removeAttribute("aria-busy");

    activeBookButton = null;
    bookCloseInProgress = false;
  }
}

document.querySelector("#back-button").addEventListener(
  "click",
  closeCurrentBook
);
document.querySelector("#exit-quiz").addEventListener("click", showSubjects);
document.querySelector("#summary-exit").addEventListener("click", showSubjects);

document.querySelector("#select-all").addEventListener("click", () => {
  chapterList.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.checked = true;

    const selectionKey = `${currentPackPath}|${checkbox.value}`;
    selectedChapters.set(selectionKey, {
      packPath: currentPackPath,
      subject: currentSubject,
      chapterKey: checkbox.value,
      questionCount: Number(checkbox.dataset.questionCount || 0),
    });
  });

  updateSelectionStatus();
});

document.querySelector("#clear-all").addEventListener("click", () => {
  chapterList.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.checked = false;
    selectedChapters.delete(`${currentPackPath}|${checkbox.value}`);
  });

  updateSelectionStatus();
});

resumeSessionButton.addEventListener("click", resumeSavedSession);

discardSessionButton.addEventListener("click", () => {
  const confirmed = window.confirm(
    "Starting a new quiz will replace your saved quiz progress. Continue?"
  );

  if (!confirmed) {
    return;
  }

  clearSavedSession();
  selectedChapters.clear();
  showQuizBuilder();
});

startButton.addEventListener("click", startQuiz);
buildQuizButton.addEventListener("click", startQuiz);

globalBlockSizeSelect.addEventListener("change", () => {
  blockSizeSelect.value = globalBlockSizeSelect.value;
});

clearSelectionsButton.addEventListener("click", () => {
  selectedChapters.clear();
  updateSelectionStatus();
});

showSubjects();
updateSelectionStatus();

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./sw.js").catch((error) => {
      console.error("PrepFlow service worker registration failed:", error);
    });
  });
}
