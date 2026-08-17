(() => {
  const startButton = document.querySelector("#build-quiz");
  if (!startButton) return;

  let lastTouchActivation = 0;

  document.addEventListener("pointerup", (event) => {
    if (event.pointerType !== "touch" && event.pointerType !== "pen") return;
    if (startButton.disabled || startButton.hidden) return;

    const rect = startButton.getBoundingClientRect();
    const inside = event.clientX >= rect.left && event.clientX <= rect.right && event.clientY >= rect.top && event.clientY <= rect.bottom;
    if (!inside) return;

    const now = performance.now();
    if (now - lastTouchActivation < 700) return;
    lastTouchActivation = now;

    event.preventDefault();
    startButton.click();
  }, true);
})();
