📈 Forex Data Pipeline
Pipeline pédagogique visant à construire progressivement une architecture de récupération, d’analyse et de stockage de données Forex.
Le projet est structuré en phases, chacune introduisant un composant essentiel du pipeline.

🧩 Phase 1 — Core Structure
Objectif : établir les fondations du projet et manipuler les premières structures Python.

✔️ Étape 1 — Initial Output
Création du fichier principal main.py

Affichage d’un message simple pour valider l’environnement

✔️ Étape 2 — Configuration Variables
Définition des paramètres de base : pair, timeframe, candles

Affichage formaté des valeurs

✔️ Étape 3 — Forex Instruments List
Création d’une liste de paires Forex

Parcours de la liste via une boucle for

✔️ Étape 4 — Core Functions
Introduction de fonctions dédiées :

display_configuration()

validate_configuration()

✔️ Étape 5 — Configuration Object
Regroupement des paramètres dans un dictionnaire config

Passage du dictionnaire aux fonctions

Structuration du code via main()

🌐 Phase 2 — API Integration Layer (Twelve Data)
Objectif : apprendre à interagir avec une API réelle, analyser les réponses, gérer les erreurs, sécuriser l’authentification et structurer la logique réseau.

✔️ Étape 6 — HTTP Request Handling
Passage de Dukascopy → Twelve Data (API stable et professionnelle)

Requête GET vers https://api.twelvedata.com/time_series

Ajout d’un timeout=10 pour sécuriser les appels réseau

✔️ Étape 7 — Secure Authentication
Suppression de la clé API en dur dans le code

Utilisation d’une variable d’environnement :
TWELVE_DATA_API_KEY

Authentification via header HTTP :
Authorization: apikey <clé>

✔️ Étape 8 — JSON Parsing
Conversion de la réponse en dictionnaire Python via response.json()

Inspection des clés : meta, values, status

Extraction d’une bougie OHLC (open, high, low, close)

✔️ Étape 9 — Response Validation
Vérification du code HTTP :

200 → Request successful

autre → Request failed

Gestion propre des erreurs réseau via try / except

✔️ Étape 10 — Forex Data Retrieval
Récupération de données Forex réelles (EUR/USD, intervalle H1)

Extraction des 10 dernières bougies OHLC

Base du pipeline de données validée
