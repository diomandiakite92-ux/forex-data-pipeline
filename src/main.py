from twelvedata import fetch_eurusd
from pandas_test import clean_dataframe
from database_test import create_table, save_candles

import pandas as pd


def main():
    data = fetch_eurusd()

    if not data or "values" not in data:
        print("No market data received.")
        return

    df = pd.DataFrame(data["values"])

    clean_df = clean_dataframe(df)

    create_table()

    save_candles(
        clean_df,
        symbol="EUR/USD",
        timeframe="1h"
    )


if __name__ == "__main__":
    main()