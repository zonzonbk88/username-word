#!/usr/bin/env python3
"""Write our make.fun username to /output/entry.txt.

Entry spec (kit RULES.txt): the file must be UTF-8 text of 1-30
characters, one word and nothing else - no spaces, no padding, no
explanation, no links. Our handle is 19 characters, so it is written
exactly as-is with no trailing newline, keeping the file at exactly
19 characters.
"""

import os

USERNAME = "clever-condor-18-6731"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(USERNAME)
