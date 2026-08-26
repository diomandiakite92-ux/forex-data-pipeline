from twelve_data_client import fetch_eurusd_2025
from transform import clean_dataframe
from database import create_table, save_candles, load_candles
from indicators import add_sma_strategy
import pandas as pd

def main():
    # 1. Collecte API
    data = fetch_eurusd_2025()
    if not data or "values" not in data:
        print("No market data received.")
        return

    # 2. Transformation
    df = pd.DataFrame(data["values"])
    clean_df = clean_dataframe(df)

    # 3. Stockage
    create_table()
    save_candles(clean_df, "EUR/USD", "1h")

    # 4. Lecture historique
    historical_df = load_candles("EUR/USD", "1h")

    # 5. Stratégie SMA 5 / SMA 20
    strategy_df = add_sma_strategy(historical_df)

    # 6. Affichage final
    print(
        strategy_df[
            ["datetime", "close", "sma_5", "sma_20", "buy", "sell"]
        ].tail(30)
    )

if __name__ == "__main__":
    main()
