# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:58:01 2023

@author: Diego
"""

#import pdblp
import pandas as pd
import datetime as dt

end_date = dt.date(year = 2023, month = 5, day = 2)
start_date = dt.date(year = 2000, month = 1, day = 1)

end_date_input  = end_date.strftime("%Y%m%d")
start_date_input = start_date.strftime("%Y%m%d")

tickers = (pd.read_csv(
    filepath_or_buffer = "hf_tickers.csv").
    assign(Ticker = lambda x: x.Ticker.str.strip()).
    dropna().
    Ticker.
    drop_duplicates().
    to_list())

con = pdblp.BCon(debug = False, port = 8194, timeout = 5_000)
con.start()

df_tmp = (con.bdh(
    tickers = tickers,
    flds = ["PX_LAST"],
    start_date = start_date_input,
    end_date = end_date_input).
    reset_index().
    melt(id_vars = "date"))

(df_tmp.to_parquet(
    path = "hf_indices.parquet",
    engine = "pyarrow"))