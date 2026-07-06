"""Execute generated notebooks to verify that the Python course examples run."""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import nbformat
from nbclient import NotebookClient


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = REPO_ROOT / "notebooks"


def main() -> None:
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    notebooks = sorted(NOTEBOOK_DIR.glob("lesson-*.ipynb"))
    if len(notebooks) != 18:
        raise SystemExit(f"Expected 18 notebooks, found {len(notebooks)}")

    with TemporaryDirectory() as tmp:
        os.environ["COURSE_OUTPUT_DIR"] = tmp
        for path in notebooks:
            print(f"executing {path.relative_to(REPO_ROOT)}")
            nb = nbformat.read(path, as_version=4)
            client = NotebookClient(
                nb,
                timeout=120,
                kernel_name="python3",
                resources={"metadata": {"path": str(REPO_ROOT)}},
            )
            client.execute()

    print("all notebooks executed successfully")


if __name__ == "__main__":
    main()
