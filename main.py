"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

STORY = "He finally forgave her. Too late."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words, got %d" % len(words))
    if not 1 <= len(STORY) <= 60:
        raise ValueError("story must be 1-60 characters, got %d" % len(STORY))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(STORY + "\n")


if __name__ == "__main__":
    main()
