# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:15:05 2024

@author: deepa
"""

import yfinance as yf
import datetime as dt
import pandas as pd


stocks = ["AMZN", "MSFT", "INTC", "GOOG"]

start = dt.datetime.today() - dt.timedelta(360)
end = dt.datetime.today()

cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
    ohlcv_data[ticker] = yf.download(ticker, start, end)
    
