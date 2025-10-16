import pandas as pd

from core.backtest.run import run_sma_bt


def test_run_sma_bt_on_synthetic_series():
    # monotonic up series; should produce sensible stats
    s = pd.Series(range(1, 201))
    stats, pf = run_sma_bt(s, fast=5, slow=10)
    # key metrics present
    for key in ["Total Return [%]", "Total Trades", "Max Drawdown [%]"]:
        assert key in stats.index
    # basic sanity
    assert stats["Total Trades"] >= 0
    assert pf is not None
