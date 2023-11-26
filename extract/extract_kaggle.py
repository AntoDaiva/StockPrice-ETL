import pandas as pd
import os
# from dotenv import load_dotenv 
# load_dotenv() 
# kaggle_username = os.getenv("KAGGLE_USERNAME")
# kaggle_key = os.getenv("KAGGLE_KEY") 


def get_stock_info():
    stock_info = "csv/robinhood.csv"

    df = pd.read_csv(stock_info)

    columns_to_keep = ["name", "symbol", "type", "description", "ceo", "headquarters_city", "industry"]
    df_t = df[columns_to_keep] 

    columns_to_check = ["ceo", "headquarters_city"]
    df_cleaned = df_t.dropna(subset=columns_to_check) 

    df_fix = df_cleaned[df_cleaned["type"] == 'stock']
    symbols = df_fix["symbol"] 
    
    symbols.to_csv(f"csv/stock_symbols.csv", index=False)
    df_fix.to_csv(f"csv/stock_info.csv", index=False)

if __name__ == "__main__":
    get_stock_info()