#!/usr/bin/env python3
"""Build the Jekyll site locally into _site/."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "_site"


def main() -> None:
    subprocess.run(
        ["bundle", "exec", "jekyll", "build", "--source", str(DOCS), "--destination", str(OUT)],
        cwd=DOCS,
        check=True,
    )


if __name__ == "__main__":
    main()
