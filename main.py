#!/usr/bin/env python3
"""Write the competition entry file deterministically (stdlib only)."""

import os

ENTRY_PATH = "/output/entry.txt"

ENTRY = """\
entry: pump-fun-paper-sprint
name: momentum-ladder
runtime: node22 / main.ts
mode: paper-only

strategy:
  Trade the 6-hour forward window on pump.fun bonding curves using a simple,
  fully deterministic momentum ladder. No network, no secrets, no real funds.

signals:
  1. new-token gate: skip anything younger than 90s or older than 45m.
  2. volume acceleration: buy only if 1-minute buy volume exceeds the trailing
     5-minute average by 1.5x and net buyers > net sellers.
  3. curve position: enter while price is still under 40% of the curve cap,
     so the remaining upside to the 85 SOL graduation line is intact.

execution:
  - size: fixed 0.25 SOL paper entries, max 4 open, max 1 entry per token.
  - ladder out: sell 1/3 at +35%, 1/3 at +80%, ride the rest until flow
     reverses (two consecutive 1m closes with seller majority) or +250%.
  - hard stops: -20% from entry, or any 1m close below the entry 1m low.
  - flat overnight: every position is closed at window end; no carries.

risk:
  - daily paper loss cap of 3 SOL halts new entries for the window.
  - no averaging down, no shorts, no leverage, no cross-token hedging.

why:
  Simple rules, hard caps, and early-curve entries keep the replay honest and
  the PnL driven by momentum rather than by luck or by data the entry does
  not ship. Everything runs from the submitted repository at the submitted
  commit: paper trading only, market data only, deterministic logic.
"""


def main() -> None:
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
