import yfinance as yf
import pandas as pd
import datetime

def extract_prices():
  symbols = pd.read_csv("csv/stock_symbols.csv")
  symbols = symbols["symbol"].tolist()
  df = pd.DataFrame(columns=['Symbol','Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'])

  for symbol in symbols:
    stock = yf.Ticker(symbol)

    # get historical market data
    hist = stock.history(start="2023-10-01", end=datetime.datetime.today().strftime('%Y-%m-%d'))
    hist['Symbol'] = symbol
    df = pd.concat([df, hist])


  df.reset_index(inplace=True)
  df.rename(columns={'index': 'date'}, inplace=True)
  df.to_csv(f"csv/stock_prices.csv", index=False)

if __name__ == "__main__":
  extract_prices()