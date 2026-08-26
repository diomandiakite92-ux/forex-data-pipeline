from twelve_data_client import fetch_eurusd_2025
from transform import clean_dataframe
from database import create_table, save_candles, load_candles
from indicators import add_sma_strategy
from backtest import backtest_strategy, calculate_metrics
import pandas as pd

def main():
    initial_capital = 10000

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

    # 6. Backtest
    trades, final_capital, equity_curve = backtest_strategy(
        strategy_df,
        initial_capital=initial_capital
    )

    # 7. Métriques
    metrics = calculate_metrics(
        trades,
        initial_capital=initial_capital,
        final_capital=final_capital,
        equity_curve=equity_curve
    )

    # 8. Résultats
    print("\n=== BACKTEST RESULTS ===")
    print(f"Initial capital  : {metrics['initial_capital']:.2f} €")
    print(f"Final capital    : {metrics['final_capital']:.2f} €")
    print(f"Return           : {metrics['total_return']:.2f} %")
    print(f"Trades           : {metrics['total_trades']}")
    print(f"Winning trades   : {metrics['winning_trades']}")
    print(f"Losing trades    : {metrics['losing_trades']}")
    print(f"Win rate         : {metrics['win_rate']:.2f} %")
    print(f"Average profit   : {metrics['average_profit']:.2f} €")
    print(f"Average win      : {metrics['average_win']:.2f} €")
    print(f"Average loss     : {metrics['average_loss']:.2f} €")
    print(f"Profit factor    : {metrics['profit_factor']:.2f}")
    print(f"Risk/Reward      : {metrics['risk_reward_ratio']:.2f}")
    print(f"Max drawdown     : {metrics['max_drawdown']:.2f} %")

if __name__ == "__main__":
    main()
