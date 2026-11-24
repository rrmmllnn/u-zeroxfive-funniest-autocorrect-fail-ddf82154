#!/usr/bin/env python3
# One-line autocorrect disaster, saved to the entry file.
#
# The joke is one ordinary message to a partner where a single
# wrong word turns a routine school pickup into something far
# darker: no setup and no punchline tag, just the swap doing
# all the work on its own.

from pathlib import Path
import os
import sys

MESSAGE = "Honey, can you pick up the kids from prison?"
LIMIT = 199


def _validate(text):
    if text != text.strip() or not text:
        return "entry must be non-blank with no surrounding whitespace"
    if len(text) > LIMIT:
        return "entry runs past the %d-character cap" % LIMIT
    if "\n" in text or "\r" in text:
        return "entry must fit on one line"
    return None


def _run():
    issue = _validate(MESSAGE)
    if issue is not None:
        print("refusing to write entry: " + issue, file=sys.stderr)
        return 1
    target = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(MESSAGE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(_run())
