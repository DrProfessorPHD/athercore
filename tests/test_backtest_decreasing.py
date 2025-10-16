import pandas as pd

from core.backtest.run import run_sma_bt


def test_run_sma_bt_on_decreasing_series():
    # strictly down series → different trade pattern
    s = pd.Series(range(200, 0, -1))
    stats, pf = run_sma_bt(s, fast=5, slow=10)
    assert "Total Return [%]" in stats.index
    assert stats["Total Trades"] >= 0
    assert pf is not None
