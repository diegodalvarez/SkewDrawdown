# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:34:21 2023

@author: dalvarez_csk
"""

import pandas as pd
import yfinance as yf
import datetime as dt


def collect():

    tickers = (pd.read_csv(
        filepath_or_buffer = "etfs_list.csv")
        ["Trading Symbol"].
        drop_duplicates().
        dropna().
        to_list())
    
    end_date = dt.date.today()
    start_date = dt.date(year = end_date.year - 50, month = 1, day = 1)
    df_out = (yf.download(
        tickers = tickers,
        start = start_date,
        end = end_date)
        ["Adj Close"].
        reset_index().
        melt(id_vars = "Date").
        dropna())
    
    df_out.to_parquet(
        path = "etf_prices.parquet",
        engine = "pyarrow")
    
if __name__ == "__main__":
    collect()