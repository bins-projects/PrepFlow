from pathlib import Path
import subprocess
import sys
from extract_text import extract_text

def extract_stage() -> None:
    print("[1/4] Extract text (not implemented)")


def clean_text() -> None:
    print("[2/4] Clean & normalize")
    subprocess.run(
        [sys.executable, "tools/clean_pharm_text.py"],
        check=True,
    )

def parse_questions() -> None:
    print("[3/4] Parse questions")
    subprocess.run(
        [sys.executable, "tools/parse_pharm_module.py"],
        check=True,
    )


def write_source_module() -> None:
    print("[4/4] Write source module")


def main() -> None:
    print("PrepFlow Source Module Builder")
    print(f"Working directory: {Path.cwd()}")
    print()

    extract_stage()
    clean_text()
    parse_questions()
    write_source_module()


if __name__ == "__main__":
    main()