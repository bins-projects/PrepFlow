from pathlib import Path


def test_quiz_builder_renders_catalog_books_without_hardcoded_pack_buttons() -> None:
    html = Path("web/index.html").read_text(encoding="utf-8")
    script = Path("web/app.js").read_text(encoding="utf-8")
    service_worker = Path("web/sw.js").read_text(encoding="utf-8")

    assert 'class="subjects" aria-label="Quiz library" aria-live="polite"></section>' in html
    assert 'const PACK_CATALOG_PATH = "./data/pack-catalog.json"' in script
    assert "function renderBookCatalog(catalog)" in script
    assert "function bookButton(book)" in script
    assert 'button.className = `subject-card ${themed ? book.theme || "" : "generic-book"}`.trim();' in script
    assert 'chapterScreen.dataset.theme = button.dataset.theme || "generic";' in script
    assert "./data/pack-catalog.json" in service_worker
    assert 'importScripts("./pack-precache.js")' in service_worker
    assert "PREPFLOW_PACK_PRECACHE.urls" in service_worker
