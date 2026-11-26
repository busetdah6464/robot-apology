#!/usr/bin/env python3
"""Write the robot's two-line apology to /output/entry.txt.

Deterministic, standard library only, no network.
"""
import os

ENTRY = (
    "I'm sorry I sorted your books by height and buried the cookbook you "
    "reach for every morning under the encyclopedias.\n"
    "I learned the tidiest shelf isn't the one you live with, so from "
    "now on I'll shelve by how often you touch a thing, not by how tall "
    "it stands.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
