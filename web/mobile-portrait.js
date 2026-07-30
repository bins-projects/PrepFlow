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
