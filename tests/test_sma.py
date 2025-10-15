import pandas as pd

from core.signals.sma import SMACrossover


def test_sma_crossover_basic():
    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3])
    sig = SMACrossover(2, 4).generate(s)
    assert 1 in sig.values
    assert -1 in sig.values
