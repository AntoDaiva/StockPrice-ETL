import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

def load_price(csv_file, table_name):
    load_dotenv()
    db_host = os.environ.get("DB_HOST")
    db_name = os.environ.get("DB_NAME")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")

    df = pd.read_csv(f"csv/{csv_file}.csv")

    # PostgreSQL connection parameters
    db_params = {
        'user': db_user,
        'password': db_password,
        'host': db_host,
        'port': 5432,
        'database': db_name
    }

    # Create a SQLAlchemy engine
    engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

    # Insert the DataFrame into the PostgreSQL database, avoiding duplicates
    df.to_sql(table_name, engine, index=False, if_exists='append', index_label=['date', 'symbol'], method='multi', chunksize=1000)

if __name__ == "__main__":
    load_price('stock_prices_clean', 'price')