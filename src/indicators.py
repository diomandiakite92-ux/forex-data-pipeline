import pandas as pd


def add_sma_strategy(df):
    df = df.copy()

    # Moyennes mobiles
    df["sma_5"] = df["close"].rolling(5).mean()
    df["sma_20"] = df["close"].rolling(20).mean()

    # Régime de marché
    df["signal"] = 0
    df.loc[df["sma_5"] > df["sma_20"], "signal"] = 1
    df.loc[df["sma_5"] < df["sma_20"], "signal"] = -1

    # Croisement haussier : SMA5 passe au-dessus de SMA20
    df["buy"] = (
        (df["sma_5"] > df["sma_20"])
        & (df["sma_5"].shift(1) <= df["sma_20"].shift(1))
    )

    # Croisement baissier : SMA5 passe sous SMA20
    df["sell"] = (
        (df["sma_5"] < df["sma_20"])
        & (df["sma_5"].shift(1) >= df["sma_20"].shift(1))
    )

    return df