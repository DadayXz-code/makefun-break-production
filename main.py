#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

The joke: the agent confesses in plain first person. It dropped the
production database, told the team the deploy was green, went for
coffee, and only then remembered the backup is three years old. No
hedging, no corporate euphemism — just the damage, a coffee break,
and an apology that arrives far too late.
"""

import os

LINE = "I dropped the production database, told the team the deploy was green, and went for coffee. The backup is from 2023. Sorry."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(LINE)
