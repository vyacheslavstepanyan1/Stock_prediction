import yfinance as yf
from datetime import date


data = yf.download("AAPL", start="2024-01-01", end="2024-02-20")
df = data