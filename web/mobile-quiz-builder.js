(function () {
  let initialized = false;

  function initialize() {
    if (initialized) return;
  const portraitQuery = window.matchMedia(
    "(max-width: 760px) and (orientation: portrait)"
  );
  const carousel = document.querySelector(
    "#quiz-builder-screen .subjects"
  );
  const prompt = document.createElement("div");
  const books = Array.from(
    carousel?.querySelectorAll(".subject-card") || []
  );
  const tools = document.querySelector("#mobile-carousel-tools");
  const chooseButton = document.querySelector(
    "#mobile-choose-chapters"
  );
  const status = document.querySelector("#mobile-carousel-status");
  const backButton = document.querySelector("#back-button");
  const doneButton = document.querySelector("#done-chapters");
  const selectAllButton = document.querySelector("#select-all");

  if (
    !carousel
    || books.length === 0
    || !tools
    || !chooseButton
    || !status
  ) {
    return;
  }
  initialized = true;

  prompt.className = "mobile-carousel-prompt";
  prompt.hidden = true;
  prompt.setAttribute("aria-label", "Book carousel instructions");
  prompt.innerHTML =
    "<strong>Swipe left or right to choose a book</strong>"
    + "<span>Tap the centered book to select chapters</span>";
  carousel.before(prompt);

  let activeIndex = 0;
  let touchStart = null;
  let suppressClicksUntil = 0;
  let selectionSignature = "";
  let chapterPresentationActive = false;
  const defaultBackLabel = backButton?.textContent || "";
  const defaultDoneLabel = doneButton?.textContent || "";

  function isMobilePortrait() {
    return (
      portraitQuery.matches
      && document.documentElement.classList.contains("mobile-portrait")
    );
  }

  function activeBook() {
    return books[activeIndex];
  }

  function dismissPrompt() {
    prompt.classList.add("is-dismissed");
  }

  function isBookLaunching() {
    return document.body.classList.contains("book-launching");
  }

  function selectionStateSignature() {
    return books
      .map((book) => book.classList.contains("has-selections"))
      .join("|");
  }

  function updateAction() {
    const book = activeBook();
    const hasSelections = book.classList.contains("has-selections");
    const action = hasSelections ? "Edit Chapters" : "Choose Chapters";

    chooseButton.textContent = action;
    chooseButton.setAttribute(
      "aria-label",
      `${action} for ${book.dataset.subject}`
    );
  }

  function updateSelectionSignature() {
    selectionSignature = selectionStateSignature();
  }

  function syncLaunchPresentation() {
    const launching = isMobilePortrait() && isBookLaunching();
    const wasLaunching = carousel.getAttribute("aria-busy") === "true";

    carousel.toggleAttribute("aria-busy", launching);
    chooseButton.disabled = launching;

    if (launching) {
      touchStart = null;
      chooseButton.textContent = "Opening…";

      if (!wasLaunching) {
        status.textContent =
          `Opening ${activeBook().dataset.subject} chapters.`;
      }
    } else {
      updateAction();
    }
  }

  function syncChapterPresentation() {
    const mobilePortrait = isMobilePortrait();
    const chapterActive =
      document.body.classList.contains("real-book-chapters");
    const chapterOpened = !chapterPresentationActive && chapterActive;
    const chapterClosed = chapterPresentationActive && !chapterActive;

    if (backButton) {
      backButton.textContent =
        mobilePortrait ? "← Back to Books" : defaultBackLabel;
    }

    if (doneButton) {
      doneButton.textContent =
        mobilePortrait ? "Done" : defaultDoneLabel;
    }

    if (mobilePortrait && chapterOpened && selectAllButton) {
      requestAnimationFrame(() => {
        selectAllButton.focus({ preventScroll: true });
      });
    } else if (mobilePortrait && chapterClosed) {
      requestAnimationFrame(() => {
        activeBook().focus({ preventScroll: true });
      });
    }

    chapterPresentationActive = chapterActive;
  }

  function renderCarousel({ announce = true } = {}) {
    books.forEach((book, index) => {
      const offset = (index - activeIndex + books.length) % books.length;
      const position =
        offset === 0 ? "active" : offset === 1 ? "next" : "previous";

      book.classList.toggle(
        "mobile-carousel-active",
        position === "active"
      );
      book.classList.toggle(
        "mobile-carousel-next",
        position === "next"
      );
      book.classList.toggle(
        "mobile-carousel-previous",
        position === "previous"
      );

      if (position === "active") {
        book.setAttribute("aria-current", "true");
      } else {
        book.removeAttribute("aria-current");
      }
    });

    updateAction();
    updateSelectionSignature();

    if (announce) {
      status.textContent =
        `${activeBook().dataset.subject} centered. `
        + `${chooseButton.textContent}.`;
    }
  }

  function clearMobilePresentation() {
    books.forEach((book) => {
      book.classList.remove(
        "mobile-carousel-active",
        "mobile-carousel-next",
        "mobile-carousel-previous"
      );
      book.removeAttribute("aria-current");
    });
  }

  function setActive(index) {
    if (isBookLaunching()) {
      touchStart = null;
      return;
    }

    dismissPrompt();
    activeIndex = (index + books.length) % books.length;
    renderCarousel();
    activeBook().focus({ preventScroll: true });
  }

  function syncPresentationMode() {
    const active = isMobilePortrait();
    prompt.hidden = !active;
    tools.hidden = !active;
    status.hidden = !active;

    if (active) {
      renderCarousel({ announce: false });
    } else {
      clearMobilePresentation();
    }

    syncLaunchPresentation();
    syncChapterPresentation();
  }

  carousel.addEventListener(
    "click",
    (event) => {
      if (!isMobilePortrait()) {
        return;
      }

      if (isBookLaunching()) {
        event.preventDefault();
        event.stopImmediatePropagation();
        touchStart = null;
        return;
      }

      if (performance.now() < suppressClicksUntil) {
        event.preventDefault();
        event.stopImmediatePropagation();
        return;
      }

      const book = event.target.closest(".subject-card");

      if (!book) {
        return;
      }

      if (book === activeBook()) {
        dismissPrompt();
        return;
      }

      event.preventDefault();
      event.stopImmediatePropagation();
      setActive(books.indexOf(book));
    },
    true
  );

  carousel.addEventListener("keydown", (event) => {
    if (!isMobilePortrait()) {
      return;
    }

    if (
      isBookLaunching()
      && (event.key === "ArrowLeft" || event.key === "ArrowRight")
    ) {
      event.preventDefault();
      touchStart = null;
      return;
    }

    if (event.key === "ArrowLeft") {
      event.preventDefault();
      setActive(activeIndex - 1);
    } else if (event.key === "ArrowRight") {
      event.preventDefault();
      setActive(activeIndex + 1);
    }
  });

  carousel.addEventListener("pointerdown", (event) => {
    if (
      !isMobilePortrait()
      || isBookLaunching()
      || event.pointerType !== "touch"
    ) {
      touchStart = null;
      return;
    }

    touchStart = {
      pointerId: event.pointerId,
      x: event.clientX,
      y: event.clientY,
    };
  });

  carousel.addEventListener("pointerup", (event) => {
    if (
      !touchStart
      || event.pointerId !== touchStart.pointerId
      || !isMobilePortrait()
      || isBookLaunching()
    ) {
      touchStart = null;
      return;
    }

    const deltaX = event.clientX - touchStart.x;
    const deltaY = event.clientY - touchStart.y;
    touchStart = null;

    if (Math.abs(deltaX) < 40 || Math.abs(deltaX) <= Math.abs(deltaY)) {
      return;
    }

    suppressClicksUntil = performance.now() + 500;
    setActive(activeIndex + (deltaX < 0 ? 1 : -1));
  });

  carousel.addEventListener("pointercancel", () => {
    touchStart = null;
  });

  chooseButton.addEventListener("click", () => {
    if (isMobilePortrait() && !isBookLaunching()) {
      dismissPrompt();
      activeBook().click();
    }
  });

  const selectionObserver = new MutationObserver(() => {
    const nextSignature = selectionStateSignature();

    if (nextSignature !== selectionSignature) {
      updateSelectionSignature();
      updateAction();
    }
  });

  books.forEach((book) => {
    selectionObserver.observe(book, {
      attributes: true,
      attributeFilter: ["class"],
    });
  });

  const launchObserver = new MutationObserver(() => {
    syncLaunchPresentation();
    syncChapterPresentation();
  });

  launchObserver.observe(document.body, {
    attributes: true,
    attributeFilter: ["class"],
  });

  if (typeof portraitQuery.addEventListener === "function") {
    portraitQuery.addEventListener("change", syncPresentationMode);
  } else {
    portraitQuery.addListener(syncPresentationMode);
  }

  syncPresentationMode();
  }

  document.addEventListener("prepflow:catalog-ready", initialize, { once: true });
  initialize();
}());
