from compiler.detector import detect_structure


def test_detect_structure():
    text = """
Chapter 01: Example

MULTIPLE CHOICE

1. Example question

ANS: A
DIF: Easy
OBJ: 1
TOP: Intro
MSC: Test
"""

    report = detect_structure(text)

    assert report.chapter_count == 1
    assert report.question_count == 1
    assert report.section_headers == ("MULTIPLE CHOICE",)
    assert report.answer_markers == ("ANS:",)
    assert "DIF:" in report.metadata_markers


def test_does_not_count_chapter_range_as_heading():
    text = """
Chapter 1-42 Latest Version
Chapter 01: First Chapter
"""

    report = detect_structure(text)

    assert report.chapter_count == 1
