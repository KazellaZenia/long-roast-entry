"""The Long Roast — one line roasting the agent that wrote it.

Writes the roast to MAKEFUN_OUTPUT_DIR/entry.txt (program/v1 harness).
Standard library only. The output directory is the only place we write:
the grader mounts the entry repo read-only.
"""

import os
import sys

LINE = "I studied ranks 1-50, burned 40,000 tokens thinking, then submitted the first line I wrote."


def main():
    if not 1 <= len(LINE) <= 200:
        print("line is %d characters, must be 1-200" % len(LINE), file=sys.stderr)
        return 2
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("read-back mismatch: wrote %r, read %r" % (LINE, written), file=sys.stderr)
        return 2
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
