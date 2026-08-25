import pandas as pd
from twelvedata import fetch_eurusd


def load_raw_data():
    """
    Récupère les données brutes depuis Twelve Data.
    Retourne un DataFrame brut (types = str).
    """
    data = fetch_eurusd()

    if not data:
        print("No data received.")
        return None

    values = data.get("values")
    if not values:
        print("No values found.")
        return None

    df = pd.DataFrame(values)

    print("\n=== Raw DataFrame ===")
    print(df)
    print("\n=== Raw dtypes ===")
    print(df.dtypes)

    return df


def clean_dataframe(df):
    """
    Transforme le DataFrame brut en DataFrame exploitable :
    - copie pour éviter de modifier raw_df
    - conversion datetime
    - conversion str → float
    - tri chronologique
    - suppression des doublons
    - réindexation propre
    - contrôle qualité
    """

    # 🔒 0. Copie pour éviter de modifier raw_df
    df = df.copy()

    # 1. Conversion datetime
    df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

    # 2. Conversion OHLC en float
    ohlc_cols = ["open", "high", "low", "close"]
    for col in ohlc_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 3. Suppression des lignes invalides
    df = df.dropna(subset=["datetime"] + ohlc_cols)

    # 4. Tri chronologique
    df = df.sort_values("datetime")

    # 5. Suppression des doublons temporels
    df = df.drop_duplicates(subset="datetime")

    # 6. Réindexation propre
    df = df.reset_index(drop=True)

    print("\n=== Cleaned DataFrame ===")
    print(df)
    print("\n=== Cleaned dtypes ===")
    print(df.dtypes)

    # 7. Contrôle qualité
    print("\n=== Null values per column ===")
    print(df.isnull().sum())

    print("\n=== Duplicate datetimes ===")
    print(df.duplicated(subset=["datetime"]).sum())

    return df


def main():
    raw_df = load_raw_data()
    if raw_df is None:
        return

    clean_df = clean_dataframe(raw_df)


if __name__ == "__main__":
    main()
