from pathlib import Path

index_path = Path("web/index.html")
index = index_path.read_text()

replacements = {
'''        <span class="subject-icon" aria-hidden="true">✚</span>''': '''        <span class="subject-icon cover-emblem fundamentals-emblem" aria-hidden="true">
          <svg viewBox="0 0 120 120" role="img" aria-label="Medical staff">
            <path d="M60 14v92M38 30h44M43 42c0 10 34 10 34 22S43 76 43 88s34 12 34 22" fill="none" stroke="currentColor" stroke-width="8" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="M29 29h62v13H29z" fill="currentColor"/>
          </svg>
        </span>''',
'''        <span class="subject-icon heart-icon" aria-hidden="true">♥</span>''': '''        <span class="subject-icon cover-emblem pharm-emblem" aria-hidden="true">
          <svg viewBox="0 0 120 120" role="img" aria-label="Medication bottle and capsule">
            <rect x="19" y="37" width="42" height="58" rx="5" fill="none" stroke="currentColor" stroke-width="7"/>
            <rect x="25" y="25" width="30" height="14" fill="currentColor"/>
            <path d="M33 63h14M40 56v14" stroke="currentColor" stroke-width="6" stroke-linecap="square"/>
            <g transform="rotate(-38 83 69)">
              <rect x="67" y="45" width="32" height="50" rx="16" fill="none" stroke="currentColor" stroke-width="7"/>
              <path d="M67 70h32" stroke="currentColor" stroke-width="7"/>
            </g>
          </svg>
        </span>''',
'''        <span class="subject-icon" aria-hidden="true">⚕</span>''': '''        <span class="subject-icon cover-emblem medsurg-emblem" aria-hidden="true">
          <svg viewBox="0 0 120 120" role="img" aria-label="Stethoscope">
            <path d="M30 18v34c0 17 12 29 28 29s28-12 28-29V18" fill="none" stroke="currentColor" stroke-width="8" stroke-linecap="square"/>
            <path d="M22 18h16M78 18h16" stroke="currentColor" stroke-width="8"/>
            <path d="M58 81v8c0 12 8 20 20 20 10 0 18-6 20-16" fill="none" stroke="currentColor" stroke-width="8"/>
            <circle cx="98" cy="88" r="10" fill="none" stroke="currentColor" stroke-width="7"/>
          </svg>
        </span>'''
}

for old, new in replacements.items():
    if old not in index:
        raise SystemExit(f"Expected cover icon not found: {old}")
    index = index.replace(old, new, 1)

index_path.write_text(index)

app_path = Path("web/app.js")
app = app_path.read_text()
old = '''    badge.textContent = PrepFlowSelectionRules.bookBadgeText(count);\n\n    book.classList.toggle("has-selections", count > 0);'''
new = '''    badge.textContent = PrepFlowSelectionRules.bookBadgeText(count);\n\n    const action = book.querySelector(".card-action");\n    if (action) {\n      action.textContent = count === 1\n        ? "1 chapter selected"\n        : `${count} chapters selected`;\n    }\n\n    book.classList.toggle("has-selections", count > 0);'''
if old not in app:
    raise SystemExit("Book selection status block not found")
app = app.replace(old, new, 1)
app_path.write_text(app)

css_path = Path("web/book-shelf.css")
css = css_path.read_text()
css += r'''

/* Recovered vertical cover hierarchy. */
.subject-card {
  min-height: 270px !important;
  padding: 28px 18px 54px 52px !important;
  overflow: hidden !important;
}

.subject-card::after {
  display: none !important;
}

.subject-card .cover-emblem {
  position: absolute !important;
  top: 46px !important;
  right: 19px !important;
  left: auto !important;
  width: 104px !important;
  height: 118px !important;
  margin: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
  color: var(--card-accent) !important;
}

.subject-card .cover-emblem svg {
  width: 100%;
  height: 100%;
  overflow: visible;
  filter: drop-shadow(4px 4px 0 #030718) drop-shadow(0 0 8px color-mix(in srgb, var(--card-accent) 38%, transparent));
}

.subject-copy {
  position: static !important;
  margin: 0 !important;
}

.subject-copy::before {
  content: "PREPFLOW" !important;
  position: absolute !important;
  top: 14px !important;
  left: 38px !important;
  margin: 0 !important;
  color: var(--card-accent) !important;
  font: 900 .56rem "Courier New", monospace !important;
  letter-spacing: .17em !important;
  text-align: left !important;
}

.subject-card .subject-name {
  position: absolute !important;
  top: 44px !important;
  bottom: 50px !important;
  left: 35px !important;
  width: 18px !important;
  min-height: 0 !important;
  margin: 0 !important;
  writing-mode: vertical-rl !important;
  transform: rotate(180deg) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  color: #f7fbff !important;
  font: italic 900 .88rem "Courier New", monospace !important;
  letter-spacing: .055em !important;
  line-height: 1 !important;
  text-align: center !important;
  text-shadow: 3px 3px 0 #030718 !important;
}

.subject-card .subject-name::before,
.subject-card .subject-name::after {
  display: none !important;
}

.subject-card .question-count {
  position: absolute !important;
  right: 16px !important;
  bottom: 48px !important;
  left: 55px !important;
  margin: 0 !important;
  color: var(--card-accent) !important;
  font: 900 .62rem "Courier New", monospace !important;
  letter-spacing: .05em !important;
  text-align: center !important;
  text-transform: uppercase !important;
}

.subject-card .card-action {
  position: absolute !important;
  right: 12px !important;
  bottom: 12px !important;
  left: 43px !important;
  min-height: 27px !important;
  padding: 6px 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border: 2px solid var(--card-accent) !important;
  background: rgba(5, 12, 31, .94) !important;
  color: color-mix(in srgb, var(--card-accent) 72%, #dce9ff) !important;
  font: 900 .58rem "Courier New", monospace !important;
  letter-spacing: .045em !important;
  line-height: 1.1 !important;
  opacity: 1 !important;
  transform: none !important;
  text-transform: uppercase !important;
}

.subject-card .card-action::before,
.subject-card .card-action span,
.subject-card .book-selected-count {
  display: none !important;
}

.subject-card.has-selections .card-action {
  background: color-mix(in srgb, var(--card-accent) 18%, #071024) !important;
  box-shadow: 0 0 10px color-mix(in srgb, var(--card-accent) 35%, transparent);
  color: #fff !important;
}
'''
css_path.write_text(css)

Path(__file__).unlink()
print("Vertical book covers applied; helper removed.")
