(() => {
  const launch = document.querySelector("#open-drug-reference");
  const screen = document.querySelector("#drug-reference-screen");
  const close = document.querySelector("#close-drug-reference");
  const searchInput = document.querySelector("#drug-reference-search");
  const filter = document.querySelector("#drug-reference-filter");
  const results = document.querySelector("#drug-reference-results");
  const detail = document.querySelector("#drug-reference-detail");
  const detailCard = document.querySelector("#drug-reference-card");
  const backToResults = document.querySelector("#back-to-drug-results");
  const tabs = [...document.querySelectorAll("[data-reference-tab]")];

  if (!launch || !screen) return;

  const referenceLaunch = document.querySelector(".reference-launch");
  const originalHideAllScreens = window.hideAllScreens;
  const originalShowSubjects = window.showSubjects;

  let entries = [];
  let activeTab = "search";
  let selectedId = null;
  let resultsScrollPosition = 0;
  const recentStorageKey = "prepflow.drugReference.recentIds";
  const recentLimit = 5;

  const routeAliases = {
    pill: "oral", pills: "oral", tablet: "oral", tablets: "oral",
    capsule: "oral", capsules: "oral", liquid: "oral", syrup: "oral",
    iv: "iv", intravenous: "iv", infusion: "iv",
    shot: "injection", shots: "injection", injectable: "injection",
    cream: "topical", ointment: "topical", lotion: "topical", gel: "topical",
    patch: "transdermal", inhaler: "inhaled", inhaled: "inhaled",
    nebulizer: "inhaled", nebulized: "inhaled",
    "eye drops": "ophthalmic", eye: "ophthalmic",
    "ear drops": "otic", ear: "otic", nasal: "nasal"
  };

  function normalized(value) {
    return String(value || "").toLocaleLowerCase().replace(/\s+/g, " ").trim();
  }

  function isMobilePortrait() {
    return document.documentElement.classList.contains("mobile-portrait");
  }

  function searchTerms(entry) {
    return [
      entry.genericName,
      ...(entry.pharmSpellings || []),
      ...(entry.brandNames || []),
      ...(entry.drugClasses || []),
      ...(entry.bodySystems || []),
      ...(entry.routes || []),
      ...(entry.dosageForms || []),
    ].map(normalized).join(" ");
  }

  function valuesForTab(entry) {
    if (activeTab === "class") return entry.drugClasses || [];
    if (activeTab === "system") return entry.bodySystems || [];
    if (activeTab === "route") return entry.routes || [];
    if (activeTab === "az") return [entry.genericName.charAt(0).toUpperCase()];
    return [];
  }

  function populateFilter() {
    const label = {
      search: "All medications",
      az: "All letters",
      class: "All drug classes",
      system: "All body systems",
      route: "All routes",
    }[activeTab];

    const values = new Set();
    entries.forEach((entry) => valuesForTab(entry).forEach((value) => value && values.add(value)));
    filter.replaceChildren(new Option(label, ""));
    [...values].sort((a, b) => a.localeCompare(b)).forEach((value) => filter.append(new Option(value, value)));
    filter.hidden = activeTab === "search";
  }

  function filteredEntries() {
    let query = normalized(searchInput.value);
    Object.entries(routeAliases).forEach(([alias, replacement]) => {
      query = query.replace(new RegExp(`\\b${alias}\\b`, "g"), replacement);
    });

    const selectedFilter = filter.value;
    return entries.filter((entry) => {
      const matchesSearch = !query || query.split(" ").every((term) => searchTerms(entry).includes(term));
      const matchesFilter = !selectedFilter || valuesForTab(entry).includes(selectedFilter);
      return matchesSearch && matchesFilter;
    });
  }

  function renderResults() {
    const matches = filteredEntries();
    results.replaceChildren();

    const count = document.createElement("p");
    count.className = "drug-reference-count";
    count.textContent = `${matches.length} ${matches.length === 1 ? "medication" : "medications"}`;
    results.append(count);

    if (!matches.length && !isMobilePortrait()) {
      const empty = document.createElement("div");
      empty.className = "drug-reference-no-results";
      empty.innerHTML = "<strong>No medications match.</strong><p>Check the spelling, clear the current filter, or try a generic name, trade name, class, body system, route, or dosage form.</p>";
      results.append(empty);
      if (!isMobilePortrait()) renderReferenceIndex(true);
      return;
    }

    matches.forEach((entry) => {
      const button = document.createElement("button");
      button.className = "drug-result";
      button.classList.toggle("active", entry.id === selectedId);
      button.type = "button";
      button.setAttribute("aria-pressed", String(entry.id === selectedId));
      button.setAttribute("aria-label", `${entry.genericName}; ${(entry.brandNames || []).join(", ") || "generic entry"}; routes ${(entry.routes || []).join(", ") || "not listed"}`);
      button.innerHTML = `
        ${isMobilePortrait() ? "" : `<span class="drug-result-check" aria-hidden="true">${entry.id === selectedId ? "✓" : ""}</span>`}
        <strong>${entry.genericName}</strong>
        <span>${(entry.brandNames || []).join(", ") || "Generic entry"}</span>
        <small>${(entry.routes || []).join(" • ")}</small>
      `;
      button.addEventListener("click", () => {
        resultsScrollPosition = results.scrollTop;
        selectedId = entry.id;
        if (!isMobilePortrait()) rememberOpenedMedication(entry.id);
        renderResults();
        renderDetail(entry);
        screen.classList.add("showing-drug-card");
        detail.scrollTop = 0;
        if (isMobilePortrait()) backToResults.focus({ preventScroll: true });
      });
      results.append(button);
    });
  }

  function storedRecentIds() {
    try {
      const value = JSON.parse(localStorage.getItem(recentStorageKey) || "[]");
      return Array.isArray(value) ? value.filter((id) => typeof id === "string") : [];
    } catch (_error) {
      return [];
    }
  }

  function rememberOpenedMedication(id) {
    const ids = [id, ...storedRecentIds().filter((storedId) => storedId !== id)].slice(0, recentLimit);
    try {
      localStorage.setItem(recentStorageKey, JSON.stringify(ids));
    } catch (_error) {
      // The reference remains fully usable when storage is unavailable.
    }
  }

  function openMedicationById(id) {
    const entry = entries.find((candidate) => candidate.id === id);
    if (!entry) return;
    selectedId = entry.id;
    rememberOpenedMedication(entry.id);
    renderResults();
    renderDetail(entry);
    detail.scrollTop = 0;
  }

  function renderReferenceIndex(noResults = false) {
    if (isMobilePortrait()) return;

    const recentEntries = storedRecentIds()
      .map((id) => entries.find((entry) => entry.id === id))
      .filter(Boolean)
      .slice(0, recentLimit);
    const recentMarkup = recentEntries.length ? `
      <section class="reference-index-recents" aria-labelledby="recent-medications-heading">
        <div class="reference-index-section-heading">
          <h4 id="recent-medications-heading">Recently Viewed</h4>
          <button class="continue-last-card" type="button" data-open-drug-id="${recentEntries[0].id}">Continue Last Card</button>
        </div>
        <div class="reference-index-recent-list">
          ${recentEntries.map((entry) => `<button type="button" data-open-drug-id="${entry.id}"><strong>${entry.genericName}</strong><span>${(entry.brandNames || []).join(", ") || "Generic entry"}</span></button>`).join("")}
        </div>
      </section>` : "";

    detailCard.innerHTML = `
      <article class="reference-index ${noResults ? "reference-index-no-results" : ""}">
        <p class="reference-index-kicker">Clinical study reference</p>
        <h3>Drug Reference Index</h3>
        <p class="reference-index-count"><strong>${entries.length}</strong> medications available</p>
        <p class="reference-index-guidance">Search by generic or trade name, drug class, body system, route, or dosage form. You can also choose a browse view above, then select a medication from the index.</p>
        <div class="reference-index-browse" aria-label="Browse medication reference">
          ${tabs.slice(1).map((tab) => `<button type="button" data-open-reference-tab="${tab.dataset.referenceTab}">${tab.textContent}</button>`).join("")}
        </div>
        ${recentMarkup}
        <p class="reference-index-safety"><strong>Study reference:</strong> Verify medication orders, current clinical guidance, institutional policy, allergies, contraindications, and patient-specific factors before administration.</p>
      </article>`;

    detailCard.querySelectorAll("[data-open-drug-id]").forEach((button) => {
      button.addEventListener("click", () => openMedicationById(button.dataset.openDrugId));
    });
    detailCard.querySelectorAll("[data-open-reference-tab]").forEach((button) => {
      button.addEventListener("click", () => activateTab(button.dataset.openReferenceTab));
    });
  }

  function valueOrPending(value) {
    return value || "Pending verified drug-card content.";
  }

  function compactSection(title, value, className = "") {
    return `<section class="quick-card-section ${className}"><h4>${title}</h4><p>${valueOrPending(value)}</p></section>`;
  }

  function detailSection(title, value) {
    return `<details class="drug-card-detail"><summary>${title}</summary><p>${valueOrPending(value)}</p></details>`;
  }

  function renderDetail(entry) {
    const card = entry.card || {};
    const brands = (entry.brandNames || []).join(", ") || "No common trade name listed";
    const primaryRoute = (entry.routes || [])[0] || "Route pending";
    const primaryForm = (entry.dosageForms || [])[0] || "Form pending";
    const classes = (entry.drugClasses || []).join(" • ") || "Class pending";
    const systems = (entry.bodySystems || []).join(" • ") || "System pending";

    detailCard.innerHTML = `
      <article class="nursing-drug-card">
        <header class="nursing-drug-header">
          <div>
            <h3>${entry.genericName}</h3>
            <p class="trade-names">Trade names: ${brands}</p>
          </div>
          <span class="drug-card-status">${entry.cardStatus}</span>
        </header>

        <div class="drug-identity-strip">
          <span><strong>Class</strong>${classes}</span>
          <span><strong>Body system</strong>${systems}</span>
        </div>

        <section class="drug-use-panel">
          <h4>What it is used for</h4>
          <p>${valueOrPending(card.indications)}</p>
        </section>

        <section class="usual-dose-panel">
          <div>
            <span class="panel-label">Usual route</span>
            <strong>${primaryRoute}</strong>
            <small>${primaryForm}</small>
          </div>
          <div>
            <span class="panel-label">Typical dosing</span>
            <p>${valueOrPending(card.dosing)}</p>
          </div>
        </section>

        <section class="safety-alert-panel">
          <h4>Major warning</h4>
          <p>${valueOrPending(card.warnings)}</p>
        </section>

        <section class="do-not-give-panel">
          <h4>Do not give if</h4>
          <p>${valueOrPending(card.contraindications)}</p>
        </section>

        <div class="side-effect-grid">
          ${compactSection("Common side effects", card.commonAdverseEffects, "common-effects")}
          ${compactSection("Serious side effects", card.seriousAdverseEffects, "serious-effects")}
        </div>

        <div class="nursing-priority-grid">
          ${compactSection("Key nursing checks", card.monitoring, "nursing-checks")}
          ${compactSection("Patient teaching", card.patientTeaching, "patient-teaching")}
          ${compactSection("Food and nutrition", card.nutrition, "food-notes")}
        </div>

        <section class="more-drug-details">
          <h4>More details</h4>
          ${detailSection("How it works", card.mechanism)}
          ${detailSection("Full dosing and administration", `${valueOrPending(card.dosing)} ${valueOrPending(card.routeAdministration)}`)}
          ${detailSection("Drug interactions", card.interactions)}
        </section>
      </article>
    `;
  }

  function showResults() {
    screen.classList.remove("showing-drug-card");
    requestAnimationFrame(() => {
      results.scrollTop = resultsScrollPosition;
      const selectedResult = results.querySelector(".drug-result.active");
      if (selectedResult) selectedResult.focus({ preventScroll: true });
      else searchInput.focus({ preventScroll: true });
    });
  }

  async function loadReference() {
    if (entries.length) return;

    const cacheVersion = "20260719-warfarin-1";
    const [registryResponse, cardsResponse] = await Promise.all([
      fetch(`./data/drug-reference.json?v=${cacheVersion}`, { cache: "no-store" }),
      fetch(`./data/drug-reference-cards.json?v=${cacheVersion}`, { cache: "no-store" }),
    ]);

    if (!registryResponse.ok) throw new Error(`Could not load drug reference: ${registryResponse.status}`);

    const payload = await registryResponse.json();
    const cardPayload = cardsResponse.ok ? await cardsResponse.json() : { cards: {} };
    const cards = cardPayload.cards || {};

    entries = (payload.entries || []).map((entry) => {
      const override = cards[entry.id];
      if (!override) return entry;
      return {
        ...entry,
        ...override,
        card: { ...(entry.card || {}), ...(override.card || {}) },
      };
    });
  }

  function hideHomeReferenceLaunch() {
    if (referenceLaunch) referenceLaunch.hidden = true;
  }

  function showHomeReferenceLaunch() {
    if (referenceLaunch) referenceLaunch.hidden = false;
  }

  window.hideAllScreens = function patchedHideAllScreens() {
    originalHideAllScreens();
    screen.hidden = true;
    hideHomeReferenceLaunch();
  };

  window.showSubjects = function patchedShowSubjects() {
    originalShowSubjects();
    screen.hidden = true;
    showHomeReferenceLaunch();
  };

  async function openReference() {
    try {
      window.hideAllScreens();
      await loadReference();
      screen.hidden = false;
      screen.classList.remove("showing-drug-card");
      populateFilter();
      renderResults();
      if (!isMobilePortrait()) renderReferenceIndex();
      searchInput.focus();
    } catch (error) {
      window.showSubjects();
      const status = document.querySelector("#status");
      status.hidden = false;
      status.textContent = error.message;
    }
  }

  launch.addEventListener("click", openReference);
  close.addEventListener("click", window.showSubjects);
  searchInput.addEventListener("input", renderResults);
  filter.addEventListener("change", renderResults);
  backToResults.addEventListener("click", showResults);

  function activateTab(tabName) {
    activeTab = tabName;
    tabs.forEach((candidate) => {
      const isActive = candidate.dataset.referenceTab === tabName;
      candidate.classList.toggle("active", isActive);
      candidate.setAttribute("aria-pressed", String(isActive));
    });
    populateFilter();
    renderResults();
  }

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      activateTab(tab.dataset.referenceTab);
    });
  });

  showHomeReferenceLaunch();
})();
