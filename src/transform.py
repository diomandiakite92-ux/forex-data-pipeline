import pandas as pd

def clean_dataframe(df):
    df = df.copy()

    df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

    ohlc_cols = ["open", "high", "low", "close"]
    for col in ohlc_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["datetime"] + ohlc_cols)
    df = df.sort_values("datetime")
    df = df.drop_duplicates(subset="datetime")
    df = df.reset_index(drop=True)

    return df
