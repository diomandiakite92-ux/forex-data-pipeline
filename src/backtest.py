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
    equity_curve = [initial_capital]

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
            equity_curve.append(capital)

            trades.append({
                "entry_date": entry_date,
                "exit_date": exit_date,
                "entry_price": entry_price,
                "exit_price": exit_price,
                "return_pct": return_pct,
                "profit": profit
            })

    return trades, capital, equity_curve


def calculate_max_drawdown(equity_curve):
    """
    Calcule le max drawdown à partir de la courbe de capital.
    """
    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        if value > peak:
            peak = value
        drawdown = (value - peak) / peak
        if drawdown < max_dd:
            max_dd = drawdown

    return max_dd * 100  # en pourcentage


def calculate_metrics(trades, initial_capital, final_capital, equity_curve):
    """
    Calcule les métriques avancées du backtest.
    """

    total_trades = len(trades)
    winning_trades = [t for t in trades if t["profit"] > 0]
    losing_trades = [t for t in trades if t["profit"] <= 0]

    win_rate = (len(winning_trades) / total_trades * 100) if total_trades > 0 else 0
    total_return = ((final_capital - initial_capital) / initial_capital) * 100

    # Profits
    average_profit = (sum(t["profit"] for t in trades) / total_trades) if total_trades > 0 else 0
    average_win = (sum(t["profit"] for t in winning_trades) / len(winning_trades)) if winning_trades else 0

    # Perte moyenne en valeur absolue
    average_loss = abs(
        sum(t["profit"] for t in losing_trades) / len(losing_trades)
    ) if losing_trades else 0

    # Profit factor
    total_gains = sum(t["profit"] for t in winning_trades)
    total_losses = abs(sum(t["profit"] for t in losing_trades))
    profit_factor = (total_gains / total_losses) if total_losses > 0 else float("inf")

    # Risk/Reward ratio
    risk_reward_ratio = (
        average_win / average_loss
        if average_loss != 0
        else float("inf")
    )

    # Max drawdown
    max_drawdown = calculate_max_drawdown(equity_curve)

    return {
        "initial_capital": initial_capital,
        "final_capital": final_capital,
        "total_return": total_return,
        "total_trades": total_trades,
        "winning_trades": len(winning_trades),
        "losing_trades": len(losing_trades),
        "win_rate": win_rate,
        "average_profit": average_profit,
        "average_win": average_win,
        "average_loss": average_loss,
        "profit_factor": profit_factor,
        "risk_reward_ratio": risk_reward_ratio,
        "max_drawdown": max_drawdown
    }
