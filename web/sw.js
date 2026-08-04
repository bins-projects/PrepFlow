const CACHE_NAME = "prepflow-pwa-v5-final-exam-completion";

const APP_FILES = [
  "./",
  "./index.html",
  "./styles.css",
  "./app.js",
  "./study-module-rules.js",
  "./data/study-modules/catalog.json",
  "./data/study-modules/combined-nursing-final-review.json",
  "./drug-reference.css",
  "./drug-reference.js",
  "./drug-reference-batch-loader.js",
  "./mobile-portrait.css",
  "./mobile-portrait.js",
  "./mobile-quiz-builder.js",
  "./mobile-quiz-flow.js",
  "./images/drug-reference/prepflow-medication-room-reference-station.png",
  "./images/home-hospital/prepflow-mobile-home-background.png",
  "./images/quiz-builder/prepflow-mobile-quiz-builder-background.png",
  "./images/quiz-builder/prepflow-mobile-chapter-clipboard.png",
  "./manifest.webmanifest",
  "./icons/prepflow-192.png",
  "./icons/prepflow-512.png",
  "../packs/fundamentals.prepflow.json",
  "../packs/pharmacy.prepflow.json",
  "../packs/medical_surgical.prepflow.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_FILES))
  );

  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(
        names
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      )
    )
  );

  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response.ok) {
          const copy = response.clone();

          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, copy);
          });
        }

        return response;
      })
      .catch(() => caches.match(event.request))
  );
});
