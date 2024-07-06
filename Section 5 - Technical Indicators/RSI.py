# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:47:24 2024

@author: deepa
"""

import yfinance as yf
import numpy as np

tickers = ["AMZN", "GOOG", "MSFT"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how="any", inplace = True)
    ohlcv_data[ticker] = temp
    
    
def RSI(DF, n = 14):
    df = DF.copy()
    df["change"] = df["Adj Close"] - df["Adj Close"].shift(1)
    df["gain"] = np.where(df["change"] >= 0, df["change"], 0)
    df["loss"] = np.where(df["change"] < 0, -1 * df["change"], 0)
    df["avg gain"] = df["gain"].ewm(alpha = 1 / n, min_periods = n).mean()
    df["avg loss"] = df["loss"].ewm(alpha = 1 / n, min_periods = n).mean()
    df["rs"] = df["avg gain"]/df["avg loss"]
    df["rsi"] = 100 - (100 / (1 + df["rs"]))
    return df["rsi"]


for ticker in tickers:
    ohlcv_data[ticker]["RSI"] = RSI(ohlcv_data[ticker])

