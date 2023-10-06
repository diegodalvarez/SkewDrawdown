# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:03:45 2023

@author: Diego
"""

import os
import pandas as pd
import datetime as dt

from blp import blp

# path management
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
data_dir = os.path.join(parent_dir, "data")
csv_path = os.path.join(data_dir, "eurekahedge.csv")
out_path = os.path.join(data_dir, "eurekahedge.parquet")

# get tickers from csv
df_eurekahedge = (pd.read_csv(
    filepath_or_buffer = csv_path, index_col = 0).
    query("Category == 'Index/Stats'"))

eurekahedge_tickers = (df_eurekahedge[
    "Security"].
    drop_duplicates().
    dropna().
    to_list())

# collect data

bquery = blp.BlpQuery(parser=blp.BlpParser(raise_security_errors=False)).start()

start_date = dt.date(year = 2000, month = 1, day = 1)
end_date = dt.date.today()

end_date_input  = end_date.strftime("%Y%m%d")
start_date_input = start_date.strftime("%Y%m%d")

df_tmp = (bquery.bdh(
    securities = eurekahedge_tickers, 
    fields = ["PX_LAST"], 
    start_date = start_date_input,
    end_date = end_date_input))

df_tmp.to_parquet(
    path = out_path, engine = "pyarrow")