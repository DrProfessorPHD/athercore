import numpy as np
import pandas as pd

from core.backtest.run import run_sma_bt


def test_run_sma_bt_on_random_series():
    rng = np.random.default_rng(42)
    s = pd.Series(100 + rng.standard_normal(300).cumsum())
    stats, pf = run_sma_bt(s, fast=5, slow=15)
    # sanity: key metrics exist and trades count is non-negative
    for k in ["Total Return [%]", "Total Trades", "Max Drawdown [%]"]:
        assert k in stats.index
    assert stats["Total Trades"] >= 0
