# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:32:57 2024

@author: deepa
"""

import yfinance as yf

tickers = ["AMZN", "GOOG", "MSFT"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='15m')
    temp.dropna(how="any", inplace = True)
    ohlcv_data[ticker] = temp
    
    
def Bollinger_Band(DF, n = 14):
    df = DF.copy()
    df["MB"] = df["Adj Close"].rolling(n).mean()
    df["UB"] = df["MB"] + 2 * df["Adj Close"].rolling(n).std(ddof = 0)
    df["LB"] = df["MB"] - 2 * df["Adj Close"].rolling(n).std(ddof = 0)
    df["BB_Width"] = df["UB"] - df["LB"]
    return df[["MB", "UB", "LB", "BB_Width"]]

for ticker in tickers:
    ohlcv_data[ticker][["MB", "UB", "LB", "BB_Width"]] = Bollinger_Band(ohlcv_data[ticker])
    