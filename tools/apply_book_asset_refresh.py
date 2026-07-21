from pathlib import Path

index_path = Path("web/index.html")
index = index_path.read_text()
link = '  <link rel="stylesheet" href="book-shelf.css?v=20260721-1">\n'
anchor = '  <link rel="stylesheet" href="home-launcher.css?v=20260721-1">\n'
if link not in index:
    if anchor not in index:
        raise SystemExit("home launcher stylesheet link not found")
    index = index.replace(anchor, anchor + link, 1)
    index_path.write_text(index)

Path("web/book-shelf.css").write_text(r'''/* Standalone PrepFlow closed-book component.
   Cover typography and emblems remain intentionally separate for later art direction. */

.subjects {
  position: relative !important;
  z-index: 6 !important;
  width: min(920px, calc(100% - 72px)) !important;
  margin: -104px auto 0 !important;
  padding: 0 !important;
  display: grid !important;
  grid-template-columns: repeat(3, 188px) !important;
  justify-content: center !important;
  align-items: end !important;
  gap: clamp(72px, 9vw, 126px) !important;
}

.subject-card {
  --book-depth: color-mix(in srgb, var(--card-accent) 58%, #07112c);
  position: relative !important;
  isolation: isolate;
  width: 188px !important;
  min-width: 188px !important;
  min-height: 252px !important;
  padding: 42px 20px 48px 34px !important;
  overflow: visible !important;
  border: 3px solid var(--card-accent) !important;
  border-radius: 4px 8px 8px 4px !important;
  background:
    linear-gradient(90deg, rgba(255,255,255,.13), transparent 14%, transparent 82%, rgba(0,0,0,.3)),
    repeating-linear-gradient(to bottom, rgba(255,255,255,.025) 0 2px, transparent 2px 4px),
    linear-gradient(180deg, color-mix(in srgb, var(--card-accent) 25%, #17254f), #081024 76%, #050a18) !important;
  box-shadow:
    -10px 0 0 var(--book-depth),
    -13px 0 0 #020614,
    7px 8px 0 #909ba5,
    12px 13px 0 rgba(0,0,0,.48) !important;
  transform: none !important;
  image-rendering: pixelated;
}

/* Fixed spine, built as part of the reusable shell. */
.subject-card::before {
  content: "" !important;
  display: block !important;
  position: absolute !important;
  z-index: 2;
  top: -3px !important;
  bottom: -3px !important;
  left: -3px !important;
  width: 28px !important;
  border: 3px solid var(--card-accent);
  border-right: 2px solid rgba(0,0,0,.48);
  border-radius: 4px 0 0 4px !important;
  background:
    linear-gradient(90deg, rgba(255,255,255,.2), transparent 34%, rgba(0,0,0,.4)),
    color-mix(in srgb, var(--card-accent) 68%, #08122f) !important;
  box-shadow: inset -4px 0 0 rgba(0,0,0,.2);
  pointer-events: none;
}

/* Attached page block. */
.subject-card::after {
  content: "" !important;
  display: block !important;
  position: absolute !important;
  z-index: -1;
  top: 8px !important;
  right: -9px !important;
  bottom: -9px !important;
  left: 22px !important;
  border: 2px solid #909ba5 !important;
  border-left: 0 !important;
  border-radius: 0 7px 7px 0 !important;
  background: repeating-linear-gradient(to bottom, #eef0e9 0 2px, #c4c9cb 2px 3px) !important;
  box-shadow: 4px 4px 0 #030716 !important;
  transform: none !important;
  pointer-events: none;
}

.subject-card:hover,
.subject-card:focus-visible {
  transform: translateY(-7px) !important;
  filter: brightness(1.1);
  outline: none;
  box-shadow:
    -10px 0 0 color-mix(in srgb, var(--card-accent) 70%, #07112c),
    -13px 0 0 #020614,
    9px 11px 0 #909ba5,
    15px 17px 0 rgba(0,0,0,.52),
    0 0 22px color-mix(in srgb, var(--card-accent) 34%, transparent) !important;
}

.subject-card:active {
  transform: translateY(-1px) scale(.985) !important;
}

.subject-card .subject-icon {
  position: relative !important;
  top: auto !important;
  left: auto !important;
  width: 62px !important;
  height: 62px !important;
  margin: 0 auto 18px !important;
}

.subject-copy {
  margin: 0 !important;
  text-align: center !important;
}

.subject-card .card-action {
  right: 14px !important;
  bottom: 14px !important;
  left: 35px !important;
}

@media (max-width: 980px) {
  .subjects {
    width: calc(100% - 32px) !important;
    grid-template-columns: repeat(3, 165px) !important;
    gap: clamp(24px, 5vw, 52px) !important;
  }

  .subject-card {
    width: 165px !important;
    min-width: 165px !important;
  }
}
''')

Path(__file__).unlink()
print("Reusable book shelf applied; helper removed.")
