from dataclasses import dataclass
import re


@dataclass(frozen=True)
class DetectionReport:
    chapter_count: int
    section_headers: tuple[str, ...]
    answer_markers: tuple[str, ...]
    metadata_markers: tuple[str, ...]
    question_count: int


SECTION_PATTERNS = (
    "MULTIPLE CHOICE",
    "MULTIPLE RESPONSE",
    "COMPLETION",
    "ORDERING",
)

METADATA_PATTERNS = (
    "DIF:",
    "OBJ:",
    "TOP:",
    "MSC:",
    "KEY:",
    "NCLEX:",
)


def detect_structure(text: str) -> DetectionReport:
    chapter_count = len(
        re.findall(r"(?mi)^Chapter\s+\d+(?!\s*-\s*\d)\s*[:.-]", text)
    )

    question_count = len(
        re.findall(r"(?m)^\s*\d+\.\s+\S", text)
    )

    sections = tuple(
        section
        for section in SECTION_PATTERNS
        if re.search(
            rf"(?mi)^{re.escape(section)}$",
            text,
        )
    )

    answer_markers = tuple(
        marker
        for marker in ("ANS:",)
        if marker in text
    )

    metadata = tuple(
        marker
        for marker in METADATA_PATTERNS
        if marker in text
    )

    return DetectionReport(
        chapter_count=chapter_count,
        section_headers=sections,
        answer_markers=answer_markers,
        metadata_markers=metadata,
        question_count=question_count,
    )
