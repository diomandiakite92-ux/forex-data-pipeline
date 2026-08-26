import pandas as pd

def backtest_strategy(df, initial_capital=10000):
    """
    Exécute un backtest simple basé sur les signaux BUY/SELL.
    Une seule position à la fois, pas de short.
    """

    df = df.copy()

    capital = initial_capital
    position_open = False
    entry_price = None
    entry_date = None

    trades = []

    for _, row in df.iterrows():
        price = row["close"]
        date = row["datetime"]

        # BUY signal
        if row["buy"] and not position_open:
            position_open = True
            entry_price = price
            entry_date = date

        # SELL signal
        elif row["sell"] and position_open:
            position_open = False
            exit_price = price
            exit_date = date

            # Calcul du rendement du trade
            return_pct = (exit_price - entry_price) / entry_price
            profit = capital * return_pct

            capital += profit

            trades.append({
                "entry_date": entry_date,
                "exit_date": exit_date,
                "entry_price": entry_price,
                "exit_price": exit_price,
                "return_pct": return_pct,
                "profit": profit
            })

    return trades, capital


def calculate_metrics(trades, initial_capital, final_capital):
    """
    Calcule les métriques du backtest.
    """

    total_trades = len(trades)
    winning_trades = sum(1 for t in trades if t["profit"] > 0)
    losing_trades = sum(1 for t in trades if t["profit"] <= 0)

    win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0
    total_return = ((final_capital - initial_capital) / initial_capital) * 100

    return {
        "initial_capital": initial_capital,
        "final_capital": final_capital,
        "total_return": total_return,
        "total_trades": total_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "win_rate": win_rate
    }
