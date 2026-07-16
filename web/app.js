const SAVE_KEY = "prepflow.savedSession.v1";

const hero = document.querySelector(".hero");
const subjects = document.querySelector(".subjects");
const status = document.querySelector("#status");

const resumePanel = document.querySelector("#resume-panel");
const resumeDescription = document.querySelector("#resume-description");
const resumeSessionButton = document.querySelector("#resume-session");
const discardSessionButton = document.querySelector("#discard-session");

const chapterScreen = document.querySelector("#chapter-screen");
const chapterTitle = document.querySelector("#chapter-title");
const chapterList = document.querySelector("#chapter-list");
const selectionCount = document.querySelector("#selection-count");
const startButton = document.querySelector("#start-button");
const blockSizeSelect = document.querySelector("#block-size");

const quizScreen = document.querySelector("#quiz-screen");
const quizSubject = document.querySelector("#quiz-subject");
const quizPosition = document.querySelector("#quiz-position");
const quizProgress = document.querySelector("#quiz-progress");
const questionStem = document.querySelector("#question-stem");
const answerChoices = document.querySelector("#answer-choices");
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

function shuffle(items) {
  const copy = [...items];

  for (let index = copy.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[randomIndex]] = [copy[randomIndex], copy[index]];
  }

  return copy;
}

function readSavedSession() {
  try {
    const raw = localStorage.getItem(SAVE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
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
    version: 2,
    savedAt: new Date().toISOString(),
    screen,
    currentSubject,
    sessionQuestions,
    sessionBlockSize,
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

  if (!saved) {
    resumePanel.hidden = true;
    return;
  }

  const mode = saved.reviewMode ? "reviewing missed questions" : "in progress";

  resumeDescription.textContent =
    `${saved.currentSubject || "Custom Quiz"} — Block ${saved.blockNumber}, ${mode}.`;

  resumePanel.hidden = false;
}

function hideAllScreens() {
  hero.hidden = true;
  subjects.hidden = true;
  resumePanel.hidden = true;
  chapterScreen.hidden = true;
  quizScreen.hidden = true;
  blockSummary.hidden = true;
  status.hidden = true;
}

function updateSelectionStatus() {
  const selected = selectedChapters.size;

  selectionCount.textContent =
    `${selected} ${selected === 1 ? "chapter" : "chapters"} selected`;

  startButton.disabled = selected === 0;
}

function showSubjects() {
  hideAllScreens();

  hero.hidden = false;
  subjects.hidden = false;
  status.hidden = false;

  const selected = selectedChapters.size;
  status.textContent = selected
    ? `${selected} ${selected === 1 ? "chapter" : "chapters"} selected. Choose another category or return to your selected category to start.`
    : "Select a category to continue.";

  refreshResumePanel();
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

      const selectionKey = `${currentPackPath}|${key}`;
      checkbox.checked = selectedChapters.has(selectionKey);

      checkbox.addEventListener("change", () => {
        if (checkbox.checked) {
          selectedChapters.set(selectionKey, {
            packPath: currentPackPath,
            subject: currentSubject,
            chapterKey: key,
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

    hideAllScreens();
    chapterTitle.textContent = currentSubject;
    chapterScreen.hidden = false;

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

  return pack.questions[reference.questionIndex];
}

function totalBlockCount() {
  return Math.max(1, Math.ceil(sessionQuestions.length / sessionBlockSize));
}

function showQuestion() {
  const question = currentQuestion();
  const blockLength = blockEnd - blockStart;

  hideAllScreens();
  quizScreen.hidden = false;

  quizSubject.textContent = currentSubject;

  if (reviewMode) {
    quizPosition.textContent =
      `Block ${blockNumber} of ${totalBlockCount()} • Review • ${reviewQueue.length + 1} remaining`;

    quizProgress.max = Math.max(reviewQueue.length + 1, 1);
    quizProgress.value = 1;
  } else {
    const questionInBlock = questionIndex - blockStart + 1;

    quizPosition.textContent =
      `Block ${blockNumber} of ${totalBlockCount()} • Question ${questionInBlock} of ${blockLength}`;

    quizProgress.max = blockLength;
    quizProgress.value = questionInBlock;
  }

  questionStem.textContent = question.stem;
  answerChoices.hidden = false;
  answerChoices.replaceChildren();

  question.choices.forEach((choice) => {
    const label = document.createElement("label");
    label.className = "answer-choice";

    const radio = document.createElement("input");
    radio.type = "radio";
    radio.name = "answer";
    radio.value = choice.label;

    radio.addEventListener("change", () => {
      submitAnswer.disabled = false;
    });

    const text = document.createElement("span");
    text.textContent = `${choice.label}. ${choice.text}`;

    label.append(radio, text);
    answerChoices.append(label);
  });

  feedback.hidden = true;
  submitAnswer.hidden = false;
  submitAnswer.disabled = true;
  continueButton.hidden = true;

  quizScore.textContent =
    `First pass: ${firstPassCorrect} correct, ${firstPassMissed} missed`;

  saveSession("question");
}

function beginBlock() {
  blockEnd = Math.min(
    blockStart + sessionBlockSize,
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
  const percentage = totalQuestions
    ? Math.round((firstPassCorrect / totalQuestions) * 100)
    : 0;

  summaryTitle.textContent = "Quiz Complete";
  summaryScore.textContent = `First-pass score: ${percentage}%`;
  summaryMessage.textContent =
    `${firstPassCorrect} of ${totalQuestions} correct on the first attempt.`;

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

  if (mastered) {
    summaryTitle.textContent = `Block ${blockNumber} Mastered`;
    summaryScore.textContent =
      `First pass: ${blockCorrect} of ${blockLength} correct.`;
    summaryMessage.textContent =
      "All missed questions have now been answered correctly.";
  } else {
    summaryTitle.textContent = `Block ${blockNumber} Complete`;
    summaryScore.textContent =
      `First pass: ${blockCorrect} of ${blockLength} correct.`;
    summaryMessage.textContent =
      missedCount === 0
        ? "No review is needed."
        : `${missedCount} ${missedCount === 1 ? "question needs" : "questions need"} review.`;
  }

  if (!mastered && missedCount > 0) {
    summaryAction.textContent = "Review Missed Questions";
    summaryAction.dataset.action = "review";
  } else if (blockEnd < sessionQuestions.length) {
    summaryAction.textContent = "Start Next Block";
    summaryAction.dataset.action = "next-block";
  } else {
    summaryAction.textContent = "Finish Session";
    summaryAction.dataset.action = "finish";
  }

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

      pack.questions.forEach((question, index) => {
        const key = `${question.chapter}|${question.chapter_title}`;

        if (
          key === selection.chapterKey
          && ["mc", "multiple_choice"].includes(question.type)
        ) {
          selectedQuestions.push({
            packPath: selection.packPath,
            questionIndex: index,
          });
        }
      });
    }
  } catch (error) {
    status.hidden = false;
    status.textContent = error.message;
    return;
  }

  sessionQuestions = shuffle(selectedQuestions);

  if (sessionQuestions.length === 0) {
    status.hidden = false;
    status.textContent =
      "No Multiple Choice questions were found in that selection.";
    return;
  }

  currentSubject = "Custom Quiz";
  sessionBlockSize = Number(blockSizeSelect.value) || 15;

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
  const selected = answerChoices.querySelector(
    'input[name="answer"]:checked'
  );

  if (!selected) {
    return;
  }

  const question = currentQuestion();
  const correctAnswers = question.correct_answers.map(String);
  const isCorrect = correctAnswers.includes(selected.value);

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
      reviewQueue.push(currentReviewQuestion);
    } else {
      firstPassMissed += 1;
      blockMissed.push(sessionQuestions[questionIndex]);
    }
  }

  feedbackRationale.textContent = question.rationale || "";
  answerChoices.hidden = true;
  feedback.hidden = false;

  answerChoices.querySelectorAll("input").forEach((input) => {
    input.disabled = true;
  });

  quizScore.textContent =
    `First pass: ${firstPassCorrect} correct, ${firstPassMissed} missed`;

  submitAnswer.hidden = true;
  continueButton.hidden = false;
});

continueButton.addEventListener("click", () => {
  if (reviewMode) {
    if (reviewQueue.length === 0) {
      currentReviewQuestion = null;
      reviewMode = false;
      showBlockSummary(true);
      return;
    }

    currentReviewQuestion = reviewQueue.shift();
    showQuestion();
    return;
  }

  questionIndex += 1;

  if (questionIndex >= blockEnd) {
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

document.querySelectorAll(".subject-card").forEach((button) => {
  button.addEventListener("click", () => showChapters(button));
});

document.querySelector("#back-button").addEventListener("click", showSubjects);
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
    "Start over and permanently delete your saved quiz progress?"
  );

  if (!confirmed) {
    return;
  }

  clearSavedSession();
  selectedChapters.clear();
  showSubjects();
});

startButton.addEventListener("click", startQuiz);

showSubjects();

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./sw.js").catch((error) => {
      console.error("PrepFlow service worker registration failed:", error);
    });
  });
}
