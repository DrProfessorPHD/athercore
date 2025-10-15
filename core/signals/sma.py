import pandas as pd


class SMACrossover:
    def __init__(self, fast: int = 10, slow: int = 30):
        assert fast > 0 and slow > 0 and fast < slow
        self.fast, self.slow = fast, slow

    def generate(self, close: pd.Series) -> pd.Series:
        f = close.rolling(self.fast).mean()
        s = close.rolling(self.slow).mean()
        sig = (f > s).astype(int).diff().fillna(0)
        return sig  # 1 buy cross, -1 sell cross, 0 hold
