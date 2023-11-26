import pandas as pd

# Read the CSV file into a DataFrame
stock_df = pd.read_csv('csv/stock_prices.csv')
print(len(stock_df))
stock_df.head()

#select attributes
clean_df = stock_df[['date', 'Symbol', 'Open','High','Low','Close','Volume','Dividends']]

# convert datetime and uniforms to utc
clean_df['date'] = pd.to_datetime(clean_df['date'], utc=True)

# Assure columns to desired data types
clean_df['Symbol'] = clean_df['Symbol'].astype('object')
clean_df['Open'] = clean_df['Open'].astype('float64')
clean_df['High'] = clean_df['High'].astype('float64')
clean_df['Low'] = clean_df['Low'].astype('float64')
clean_df['Close'] = clean_df['Close'].astype('float64')
clean_df['Volume'] = clean_df['Volume'].astype('int64')
clean_df['Dividends'] = clean_df['Dividends'].astype('float64')

# Lowercase all column names
clean_df.columns = clean_df.columns.str.lower()

#drop null values
clean_df.dropna(inplace=True)

#save to csv
clean_df.to_csv(f"csv/stock_prices_clean.csv", index=False)