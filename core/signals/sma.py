from __future__ import annotations

import pandas as pd


class SMACrossover:
    """Simple moving average crossover signal generator (long-only)."""

    def __init__(self, fast: int, slow: int) -> None:
        self.fast = int(fast)
        self.slow = int(slow)

    def generate(self, close: pd.Series) -> tuple[pd.Series, pd.Series]:
        """Return (entries, exits) for a simple long-only SMA crossover.

        entries → fast crosses above slow
        exits   → fast crosses below slow
        """
        fast_ma = close.rolling(self.fast).mean()
        slow_ma = close.rolling(self.slow).mean()

        crossed_up = (fast_ma > slow_ma) & (fast_ma.shift(1) <= slow_ma.shift(1))
        crossed_dn = (fast_ma < slow_ma) & (fast_ma.shift(1) >= slow_ma.shift(1))

        entries = crossed_up.reindex(close.index, fill_value=False).astype(bool)
        exits = crossed_dn.reindex(close.index, fill_value=False).astype(bool)
        return entries, exits
