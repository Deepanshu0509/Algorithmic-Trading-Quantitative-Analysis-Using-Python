# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:11:16 2024

@author: deepa
"""

import yfinance as yf

tickers = ["AMZN", "GOOG", "MSFT"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='15m')
    temp.dropna(how="any", inplace = True)
    ohlcv_data[ticker] = temp
    
    
def ATR(DF, n = 14):
    df = DF.copy()
    df["H - L"] = df["High"] - df["Low"]
    df["H - PC"] = abs(df["High"] - df["Adj Close"].shift(1))
    df["L - PC"] = abs(df["Low"] - df["Adj Close"].shift(1))
    df["TR"] = df[["H - L", "H - PC", "L - PC"]].max(axis = 1, skipna = False)
    df["ATR"] = df["TR"].ewm(com = n, min_periods = n).mean()
    return df["ATR"]

for ticker in ohlcv_data:
    ohlcv_data[ticker]["ATR"] = ATR(ohlcv_data[ticker])
    