Forex Strategy Analyzer — SMA 5/20 Backtest (Année 2025)

1. Contexte et objectif
   Ce projet a été réalisé dans le cadre d’un mémoire universitaire.
   L’objectif est de construire un pipeline complet permettant :

la collecte automatisée de données Forex (EUR/USD, timeframe 1h)

leur nettoyage et stockage

le calcul d’indicateurs techniques

la détection de signaux de trading

l’exécution d’un backtest complet

l’analyse quantitative des résultats

la visualisation via un dashboard interactif Streamlit

Ce projet illustre la mise en place d’une chaîne Data Engineering appliquée à l’analyse de stratégies de trading.

2. Problématique
   Dans quelle mesure un pipeline automatisé de données financières permet-il d’évaluer de manière fiable une stratégie de trading basée sur le croisement de moyennes mobiles ?

Cette problématique permet d’aborder :

la qualité des données

la reproductibilité des analyses

la rigueur du backtest

les limites d’un prototype expérimental

l’interprétation quantitative d’une stratégie simple

3. Architecture
   Code
   Twelve Data API
   │
   ▼
   twelve_data_client.py
   │
   ▼
   transform.py
   pandas / Data Quality
   │
   ▼
   database.py
   SQLite
   │
   ▼
   indicators.py
   SMA5 / SMA20
   │
   ▼
   backtest.py
   │
   ▼
   dashboard.py
   Streamlit / Plotly
4. Pipeline de données
   ✔ Collecte
   Récupération des données EUR/USD (H1) via Twelve Data, découpées en deux fenêtres pour couvrir toute l’année 2025.

✔ Transformation
Nettoyage, typage, tri, conversion des colonnes.

✔ Stockage
Insertion dans SQLite avec contrainte d’unicité pour éviter les doublons.

✔ Lecture
Extraction de l’historique complet pour analyse.

✔ Indicateurs
Calcul de SMA 5 et SMA 20.

✔ Signaux
Détection des croisements haussiers (BUY) et baissiers (SELL).

✔ Backtest
Simulation des trades sur l’année 2025.

✔ Dashboard
Visualisation interactive via Streamlit + Plotly.

5. Stratégie SMA 5/20
   La stratégie testée est volontairement simple :

BUY : SMA 5 croise SMA 20 à la hausse

SELL : SMA 5 croise SMA 20 à la baisse

Une seule position à la fois

Pas de short selling

Sortie uniquement sur croisement inverse

Cette stratégie est un classique des systèmes de suivi de tendance.

6. Méthodologie du backtest
   ✔ Hypothèses du modèle
   Pas de spread

Pas de slippage

Pas de frais

Pas de stop loss fixe

Pas de take profit fixe

Exposition proportionnelle au capital

Une seule position à la fois

Sortie uniquement sur croisement inverse

Données : EUR/USD, timeframe 1h

Période : année 2025

✔ Calculs effectués
Pour chaque trade :

entry_date / exit_date

entry_price / exit_price

return_pct

profit

Métriques :

capital final

rendement

nombre de trades

win rate

gain moyen

perte moyenne (valeur absolue)

profit factor

ratio gain/perte (Avg Win / Avg Loss)

max drawdown

equity curve

7. Résultats (Année 2025)
   Indicateur Résultat
   Capital initial 10 000 €
   Capital final 10 417,57 €
   Rendement +4,18 %
   Trades 203
   Trades gagnants 69
   Trades perdants 134
   Win rate 33,99 %
   Gain moyen 45,71 €
   Perte moyenne 20,42 €
   Ratio gain/perte 2,24
   Profit Factor 1,15
   Max Drawdown -3,88 %

Analyse
Le backtest met en évidence une légère profitabilité de la stratégie sur l’échantillon étudié.
Cependant :

un win rate faible (33,99 %)

compensé par un ratio gain/perte élevé (2,24)

mais un Profit Factor modeste (1,15)

indiquent que les gains sont moins fréquents mais plus importants que les pertes.

La marge reste limitée :
l’intégration des coûts de transaction pourrait réduire, voire annuler cette performance.

8. Dashboard
   Le dashboard Streamlit permet :

✔ KPI principaux
Capital final

Rendement

Win Rate

Max Drawdown

✔ KPI avancés
Nombre de trades

Profit Factor

Avg Win / Avg Loss

✔ Graphique principal
Prix EUR/USD

SMA 5

SMA 20

BUY ▲

SELL ▼

✔ Equity Curve
Courbe du capital

Ligne du capital initial

✔ Table des trades
return_pct en %

profits / pertes

✔ Lancement
Code
python -m streamlit run src/dashboard.py 9. Limites
Ce prototype :

ne prend pas en compte spread, slippage et frais

n’utilise pas de stop loss / take profit

ne teste qu’une seule paire (EUR/USD)

ne teste qu’une seule année (2025)

ne démontre aucune performance future

repose sur une stratégie simple

ne modélise pas les conditions de marché réelles

Ces limites sont assumées :
le projet vise à démontrer une méthodologie, pas une stratégie exploitable en production.

10. Installation
    Code
    pip install -r requirements.txt
    ou :

Code
pip install streamlit plotly pandas requests 11. Lancement
Pipeline complet
Code
python src/main.py
Dashboard
Code
python -m streamlit run src/dashboard.py 12. Technologies
Python

Pandas

SQLite

Twelve Data API

Streamlit

Plotly

VS Code
