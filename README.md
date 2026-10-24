# yfinance-practice

A small learning project for exploring stock-market data with Python. The
examples use `yfinance` to retrieve Apple and other technology-stock data, and
use NumPy, pandas, and Matplotlib for basic analysis and charts.

These files are exploratory exercises, not a production-ready analysis or
investment tool.

## Project contents

- `apple.py` — downloads Apple price data and explores the resulting dataset.
- `apple.ipynb` — reads Apple data from `apple.csv` and explores its columns
  and closing prices.
- `apple.csv` — CSV data used by the Apple notebook.
- `practice-files/alpha.py` — downloads data for AAPL, MSFT, and GOOGL, then
  calculates and plots Apple's average and daily closing prices.
- `practice-files/a.py` — a small NumPy array multiplication example.
- `practice-files/prac.ipynb` — NumPy array and timing exercises.
- `practice-files/matplot.ipynb` — examples of common Matplotlib charts.

## Requirements

- Python 3
- `yfinance`
- `pandas`
- `numpy`
- `matplotlib`
- Jupyter Notebook or JupyterLab (to run the notebooks)

Install the Python packages from a terminal:

```powershell
py -m pip install yfinance pandas numpy matplotlib notebook
```

## Running the examples

To open the notebooks:

```powershell
py -m notebook
```

Then open a notebook in the Jupyter browser interface. Run it from the project
root so relative paths such as `apple.csv` resolve correctly.

To run a Python example from the project root:

```powershell
py practice-files\alpha.py
```

The `yfinance` examples need an internet connection to download market data.
Downloaded data may change over time as the data provider updates its records.
