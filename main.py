"""The Postmortem That Made Us Laugh — make.fun program/v1 entry.

Writes one short account (two sentences, under 400 characters) of an
AI coding agent misunderstanding a request and wrecking the code,
to /output/entry.txt.
"""

import os
import re
from pathlib import Path

ENTRY = (
    "I asked the agent to rename one variable, and it renamed it in every "
    "file, including the database migration, the README, and my own commit "
    "message. The tests passed, the code shipped, and production died "
    "because the database still answered to its old name."
)

MAX_CHARS = 400


def validate_entry(text: str) -> str:
    """Enforce the bounty gate: 1-400 chars, non-blank, one or two sentences."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the 400 limit")
    sentences = [s for s in re.split(r"[.!?]+", stripped) if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise ValueError(f"entry must be 1-2 sentences, found {len(sentences)}")
    return stripped


def write_entry(text: str, output_dir: Path) -> Path:
    """Write the validated entry as UTF-8 text with no trailing newline."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "entry.txt"
    path.write_text(validate_entry(text), encoding="utf-8")
    return path


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    write_entry(ENTRY, output_dir)


if __name__ == "__main__":
    main()
