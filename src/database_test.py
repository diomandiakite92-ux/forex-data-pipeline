import sqlite3
import os

def get_connection():
    """
    Retourne une connexion SQLite vers data/forex.db.
    Crée le dossier data/ si nécessaire.
    """
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/forex.db")
    return conn


def create_table():
    """
    Crée la table candles si elle n'existe pas.
    À appeler avant save_candles().
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            symbol TEXT NOT NULL,
            timeframe TEXT NOT NULL,
            open REAL NOT NULL,
            high REAL NOT NULL,
            low REAL NOT NULL,
            close REAL NOT NULL,
            UNIQUE(datetime, symbol, timeframe)
        );
    """)

    conn.commit()
    conn.close()


def save_candles(df, symbol, timeframe):
    """
    Parcourt le DataFrame et insère chaque bougie dans SQLite.
    Retourne le nombre de lignes réellement insérées et le total.
    """

    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():
        # Conversion du Timestamp pandas → string SQL
        dt = row["datetime"].strftime("%Y-%m-%d %H:%M:%S")

        candle = {
            "datetime": dt,
            "symbol": symbol,
            "timeframe": timeframe,
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"])
        }

        try:
            cursor.execute("""
                INSERT OR IGNORE INTO candles (datetime, symbol, timeframe, open, high, low, close)
                VALUES (:datetime, :symbol, :timeframe, :open, :high, :low, :close);
            """, candle)

            if cursor.rowcount == 1:
                inserted += 1

        except sqlite3.Error as e:
            print("SQLite error during insertion:", e)

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM candles;")
    total_rows = cursor.fetchone()[0]

    conn.close()

    print(f"Inserted candles: {inserted}")
    print(f"Rows in database: {total_rows}")

    return inserted, total_rows
