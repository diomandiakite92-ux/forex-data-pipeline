import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from database import load_candles
from indicators import add_sma_strategy
from backtest import backtest_strategy, calculate_metrics

# -----------------------------
# Configuration de la page
# -----------------------------
st.set_page_config(
    page_title="Forex Strategy Analyzer",
    layout="wide"
)

st.title("EUR/USD — SMA 5/20 Strategy")
st.caption("Backtest sur données horaires — Année 2025")

# -----------------------------
# Chargement des données
# -----------------------------
historical_df = load_candles("EUR/USD", "1h")
strategy_df = add_sma_strategy(historical_df)

initial_capital = 10000

trades, final_capital, equity_curve = backtest_strategy(
    strategy_df,
    initial_capital
)

metrics = calculate_metrics(
    trades,
    initial_capital,
    final_capital,
    equity_curve
)

# -----------------------------
# KPI (cartes Streamlit)
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Capital final",
    f"{metrics['final_capital']:.2f} €"
)

col2.metric(
    "Rendement",
    f"{metrics['total_return']:.2f} %"
)

col3.metric(
    "Win Rate",
    f"{metrics['win_rate']:.2f} %"
)

col5, col6, col7 = st.columns(3)

col5.metric("Nombre de trades", metrics["total_trades"])
col6.metric("Profit Factor", f"{metrics['profit_factor']:.2f}")
col7.metric("Avg Win / Avg Loss", f"{metrics['risk_reward_ratio']:.2f}")

st.subheader("Hypothèses du backtest")
st.markdown("""
- Pas de stop loss fixe  
- Pas de take profit fixe  
- Pas de spread, slippage ou frais  
- Une seule position à la fois  
- Sortie uniquement sur croisement inverse  
- Exposition proportionnelle au capital  
""")



# Drawdown affiché en positif pour la lisibilité
col4.metric(
    "Max Drawdown",
    f"{abs(metrics['max_drawdown']):.2f} %"
)

# -----------------------------
# Graphique principal (Plotly)
# -----------------------------
fig = go.Figure()

# Prix
fig.add_trace(go.Scatter(
    x=strategy_df["datetime"],
    y=strategy_df["close"],
    mode="lines",
    name="Close",
    line=dict(color="#1f77b4")
))

# SMA 5
fig.add_trace(go.Scatter(
    x=strategy_df["datetime"],
    y=strategy_df["sma_5"],
    mode="lines",
    name="SMA 5",
    line=dict(color="#ff7f0e")
))

# SMA 20
fig.add_trace(go.Scatter(
    x=strategy_df["datetime"],
    y=strategy_df["sma_20"],
    mode="lines",
    name="SMA 20",
    line=dict(color="#2ca02c")
))

fig.update_layout(
    title="EUR/USD — Prix + SMA 5/20",
    xaxis_title="Date",
    yaxis_title="Prix",
    height=600,
    legend=dict(orientation="h", yanchor="bottom", y=1.02)
)

st.plotly_chart(fig, use_container_width=True)

# BUY markers
buy_points = strategy_df[strategy_df["buy"] == True]
fig.add_trace(go.Scatter(
    x=buy_points["datetime"],
    y=buy_points["close"],
    mode="markers",
    name="BUY",
    marker=dict(symbol="triangle-up", size=12, color="green")
))

# SELL markers
sell_points = strategy_df[strategy_df["sell"] == True]
fig.add_trace(go.Scatter(
    x=sell_points["datetime"],
    y=sell_points["close"],
    mode="markers",
    name="SELL",
    marker=dict(symbol="triangle-down", size=12, color="red")
))


st.subheader("Évolution du capital (Equity Curve)")

fig_equity = go.Figure()
fig_equity.add_trace(go.Scatter(
    x=list(range(len(equity_curve))),
    y=equity_curve,
    mode="lines",
    name="Equity Curve",
    line=dict(color="#9467bd")
))

fig_equity.update_layout(
    height=400,
    xaxis_title="Trade index",
    yaxis_title="Capital (€)"
)

fig_equity.add_hline(
    y=initial_capital,
    line_dash="dot",
    line_color="gray",
    annotation_text="Capital initial",
    annotation_position="top left"
)

st.plotly_chart(fig_equity, use_container_width=True)


st.subheader("Table des trades")


trades_df = pd.DataFrame(trades)
trades_df["return_pct"] = trades_df["return_pct"] * 100
trades_df["return_pct"] = trades_df["return_pct"].round(2)

st.dataframe(trades_df, use_container_width=True)
