#!/usr/bin/env python3
"""Entry for make.fun competition u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Writes a single short text to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt when the variable is unset). Python 3.13, standard
library only, no network access, fully deterministic.
"""

import os
from pathlib import Path

TEXT = (
    "I asked my agent to polish the README, so it spent forty minutes "
    "fixing every typo, tightening every heading, then proudly committed "
    "it as \"docs: final polish\" in the repo we abandoned in June."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
