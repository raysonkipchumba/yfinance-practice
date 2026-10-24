import yfinance as yf
import pandas as pd 
import numpy as np


apple_data_raw = yf.download("AAPL",start = "2025-01-01", end="2026-10-10")

apple_data_csv = apple_data_raw.to_csv("apple_data.csv")


# getting shape of data 
data_shape = apple_data.shape
#Print(data_shape)

# getting column names 

col_heads = apple_data.columns.tolist()
print(col_heads)



