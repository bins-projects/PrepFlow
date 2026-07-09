from pathlib import Path

RAW_PATH = Path("scratch/pharm_raw.txt")
CLEAN_PATH = Path("scratch/pharm_clean.txt")

JUNK_PREFIXES = (
    "Stuvia.com",
    "Downloaded by:",
    "Distribution of this document is illegal",
    "Want to earn",
    "extra per year",
)

JUNK_EXACT = {
    "Med C",
    "Test bank",
    "===PAGE===",
}

def is_junk_line(line: str) -> bool:
    stripped = line.strip()

    if not stripped:
        return False

    if stripped in JUNK_EXACT:
        return True

    return any(prefix in stripped for prefix in JUNK_PREFIXES)

def normalize_choice_lines(lines: list[str]) -> list[str]:
    normalized = []
    i = 0

    while i < len(lines):
        current = lines[i].strip()

        # Pattern:
        # b
        # .
        # Choice text
        if current in {"a", "b", "c", "d", "e", "f"}:
            if i + 2 < len(lines) and lines[i + 1].strip() == ".":
                choice_text = lines[i + 2].strip()
                normalized.append(f"{current}. {choice_text}")
                i += 3
                continue

        # Pattern:
        # b Choice text
        # Safer: only treat as a choice when the text looks like an answer option,
        # not when it is a sentence continuation like "a specific manufacturer."
        if len(current) > 2 and current[0] in {"a", "b", "c", "d", "e", "f"} and current[1] == " ":
            choice_text = current[2:].strip()
            if choice_text and (choice_text[0].isupper() or choice_text[0] in {"“", "\""}):
                normalized.append(f"{current[0]}. {choice_text}")
                i += 1
                continue

        normalized.append(lines[i])
        i += 1

    return normalized


def clean_text(text: str) -> str:
    cleaned_lines = []

    for line in text.splitlines():
        for junk in JUNK_PREFIXES:
            if junk in line:
                line = line.split(junk)[0]

        if is_junk_line(line):
            continue

        cleaned_lines.append(line.rstrip())

    cleaned_lines = normalize_choice_lines(cleaned_lines)

    return "\n".join(cleaned_lines)

def main() -> None:
    raw = RAW_PATH.read_text(encoding="utf-8")
    clean = clean_text(raw)
    CLEAN_PATH.write_text(clean, encoding="utf-8")
    print(f"Created {CLEAN_PATH}")

if __name__ == "__main__":
    main()
