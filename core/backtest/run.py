from typing import Any, Tuple

import pandas as pd
import vectorbt as vbt

from core.signals.sma import SMACrossover


def to_series(close: pd.Series | pd.DataFrame) -> pd.Series:
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    return pd.to_numeric(close, errors="coerce").dropna()


def run_sma_bt(
    close: pd.Series | pd.DataFrame,
    fast: int = 10,
    slow: int = 30,
) -> Tuple[pd.Series, Any]:
    close = to_series(close)
    sig = SMACrossover(fast, slow).generate(close)
    entries = sig == 1
    exits = sig == -1
    pf = vbt.Portfolio.from_signals(close, entries, exits, fees=0.0005)
    return pf.stats(), pf
