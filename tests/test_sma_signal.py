import pandas as pd

from core.signals.sma import SMACrossover


def test_sma_basic_shapes_and_activity():
    s = pd.Series([1, 2, 3, 4, 5, 4, 3, 2, 1], index=pd.RangeIndex(9))
    sig = SMACrossover(fast=2, slow=3)
    entries, exits = sig.generate(s)
    # shapes match input
    assert entries.shape == s.shape
    assert exits.shape == s.shape
    # at least one signal flips somewhere
    assert bool(entries.any()) or bool(exits.any())
