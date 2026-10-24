import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

"""Hypothesis: The Volume-Confirmed RSI Mean Reversion Alpha
The Premise: When large-cap liquid tech stocks (like AAPL, MSFT, or GOOGL) 
experience heavy selling volume
 combined with a drop into "oversold" territory,
 panic selling often overshoots the true value,
 creating a short-term pricing inefficiency that
 rebounds over the next few trading days.
"""


data = yf.download("AAPL MSFT GOOGL", start="2025-01-01", end="2026-10-10")


close_prices = data["Close"]
open_prices = data["Open"]
highs = data["High"]
lows = data["Low"]
trade_volume = data["Volume"]

aapl_close = close_prices["AAPL"]
aapl_open = open_prices["AAPL"]



#further analysis
aapl_np_close = aapl_close.to_numpy()
aapl_np_open = aapl_open.to_numpy()

aapl_close_avg = np.mean(aapl_np_close)
aapl_open_avg = np.mean(aapl_np_open)


print(f"close average : {aapl_close_avg:.5f} \n open average : {aapl_open_avg:.5f}")

plt.figure(figsize=(12, 6))
aapl_close.plot(kind="bar", color="royalblue")


plt.title("Apple (AAPL) Daily Close Prices", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Close Price (USD)", fontsize=12)


ax = plt.gca()
for index, label in enumerate(ax.get_xticklabels()):
  if index % 20 != 0:
    label.set_visible(False)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



