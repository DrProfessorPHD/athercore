from typing import Any, Dict

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from core.backtest.run import run_sma_bt

app = FastAPI(title="Athercore API")


class BacktestReq(BaseModel):
    symbol: str
    fast: int = 10
    slow: int = 30


@app.get("/")
def root() -> Dict[str, bool]:
    return {"ok": True}


@app.post("/backtest/sma")
def bt(
    req: BacktestReq,
) -> Dict[str, Any]:  # FastAPI decorator can be untyped; return a simple dict
    import yfinance as yf

    df = yf.download(req.symbol, period="5y", auto_adjust=True, progress=False)
    close = df["Close"] if "Close" in df.columns else df.get("Adj Close", df.squeeze())
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close = pd.to_numeric(close, errors="coerce").dropna()
    stats, _ = run_sma_bt(close, req.fast, req.slow)
    return {"symbol": req.symbol, "stats": stats.to_dict()}
