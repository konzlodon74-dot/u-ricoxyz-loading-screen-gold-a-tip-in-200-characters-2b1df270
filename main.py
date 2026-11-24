#!/usr/bin/env python3
"""Loading Screen Gold: one sharp, funny tip for stressed devs and AI agents.

Writes the single tip line to /output/entry.txt with no trailing newline.
Standard library only.
"""

import os

TIP = "If it worked yesterday, blame the cache, not yourself — clear it, breathe, read the error twice, then fix the typo you swore wasn't there."


def main() -> None:
    line = TIP
    assert 1 <= len(line) <= 200, f"tip length {len(line)} outside 1-200"
    assert line.strip(), "tip must not be blank"
    assert "\n" not in line and "\r" not in line, "tip must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Self-check: what landed on disk must be exactly the tip, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the tip exactly"
    print(f"Wrote {len(line)}-char tip to /output/entry.txt")


if __name__ == "__main__":
    main()
