import pandas as pd

from core.signals.sma import SMACrossover


def test_sma_crossover_basic():
    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3])
    entries, exits = SMACrossover(2, 4).generate(s)

    # Both are Series of booleans aligned to s
    assert isinstance(entries, pd.Series)
    assert isinstance(exits, pd.Series)
    assert entries.shape == s.shape
    assert exits.shape == s.shape

    # Should trigger at least one crossover somewhere
    assert bool(entries.any()) or bool(exits.any())
