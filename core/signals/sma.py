import pandas as pd


class SMACrossover:
    """Simple moving-average crossover (long-only) that returns (entries, exits)."""

    def __init__(self, fast: int = 10, slow: int = 30):
        assert fast > 0 and slow > 0 and fast < slow, "Require 0 < fast < slow"
        self.fast, self.slow = int(fast), int(slow)

    def generate(self, close: pd.Series) -> tuple[pd.Series, pd.Series]:
        f = close.rolling(self.fast).mean()
        s = close.rolling(self.slow).mean()
        crossed_up = (f > s) & (f.shift(1) <= s.shift(1))
        crossed_dn = (f < s) & (f.shift(1) >= s.shift(1))
        entries = crossed_up.reindex(close.index, fill_value=False).astype(bool)
        exits = crossed_dn.reindex(close.index, fill_value=False).astype(bool)
        return entries, exits
