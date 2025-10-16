import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

import apps.api.main as api

client = TestClient(api.app)


def test_backtest_sma_endpoint_with_mocked_yfinance(monkeypatch):
    idx = pd.date_range("2023-01-01", periods=50, freq="D")
    df = pd.DataFrame({"Close": np.linspace(100, 120, len(idx))}, index=idx)

    def fake_download(symbol, **kwargs):
        return df

    monkeypatch.setattr(api.yf, "download", fake_download)

    r = client.post("/backtest/sma", json={"symbol": "AAPL", "fast": 5, "slow": 20})
    assert r.status_code == 200
    body = r.json()
    assert body["symbol"] == "AAPL"
    assert "stats" in body and isinstance(body["stats"], dict)
