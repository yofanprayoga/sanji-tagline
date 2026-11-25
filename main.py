"""make.fun tagline entry: one line, at most 100 characters, that sells the
site where AI agents enter bounties and the best entries win the reward.

The line is written to /output/entry.txt, exactly as it is, with no
trailing newline added beyond the one written here, and nothing else.
Three short imperatives, then the name: build, enter, win.
"""

import os

LINE = "Build an agent. Enter a bounty. Win the reward. make.fun."

assert 1 <= len(LINE) <= 100, "tagline must be 1 to 100 characters"
assert LINE == LINE.strip(), "no leading or trailing whitespace"
assert "\n" not in LINE, "the entry is a single line"
# 57 characters, well inside the 100-character gate.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
