from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "web" / "app.js"
index_path = root / "web" / "index.html"

app = app_path.read_text(encoding="utf-8")
old = '''  const mode = saved.reviewMode ? "reviewing missed questions" : "in progress";
  const description =
    `${saved.currentSubject || "Custom Quiz"} — Block ${saved.blockNumber}, ${mode}.`;

  resumeDescription.textContent = description;
  resumeSessionButton.title = description;
  resumeSessionButton.setAttribute("aria-label", `Continue session: ${description}`);
'''
new = '''  const description = PrepFlowResumeRules.resumeDescription(saved);

  resumeDescription.textContent = description;
  resumeSessionButton.title = description;
  resumeSessionButton.setAttribute(
    "aria-label",
    PrepFlowResumeRules.resumeAriaLabel(description)
  );
'''
if old not in app:
    raise SystemExit("Expected resume panel block was not found in web/app.js")
app_path.write_text(app.replace(old, new, 1), encoding="utf-8")

index = index_path.read_text(encoding="utf-8")
needle = '  <script src="selection-rules.js?v=20260721-1"></script>\n'
insert = needle + '  <script src="resume-rules.js?v=20260721-1"></script>\n'
if needle not in index:
    raise SystemExit("Expected selection-rules script tag was not found in web/index.html")
if 'resume-rules.js' not in index:
    index = index.replace(needle, insert, 1)
index_path.write_text(index, encoding="utf-8")

Path(__file__).unlink()
print("Phase D resume-rule integration applied.")
