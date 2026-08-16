# 📈 Forex Data Pipeline

Pipeline pédagogique visant à construire progressivement une architecture de récupération et de traitement de données Forex.  
Le projet est structuré en **phases**, chacune introduisant des composants essentiels du pipeline.

---

# 🧩 Phase 1 — Core Structure

Objectif : établir les fondations du projet et manipuler les premières structures Python.

### ✔️ Étape 1 — Initial Output

- Création du fichier principal `main.py`
- Affichage d’un message simple pour valider l’environnement

### ✔️ Étape 2 — Configuration Variables

- Définition des paramètres de base : pair, timeframe, candles
- Affichage formaté des valeurs

### ✔️ Étape 3 — Forex Instruments List

- Création d’une liste de paires Forex
- Parcours de la liste via une boucle `for`

### ✔️ Étape 4 — Core Functions

- Introduction de fonctions dédiées :
  - `display_configuration()`
  - `validate_configuration()`

### ✔️ Étape 5 — Configuration Object

- Regroupement des paramètres dans un dictionnaire `config`
- Passage du dictionnaire aux fonctions
- Structuration du code via `main()`

---

# 🌐 Phase 2 — API Integration Layer

Objectif : apprendre à interagir avec une API, analyser les réponses, gérer les erreurs et structurer la logique réseau.

### ✔️ Étape 6 — HTTP Request Handling

- Requête GET vers `https://api.github.com`
- Affichage du code HTTP de la réponse

### ✔️ Étape 7 — JSON Parsing

- Conversion de la réponse en dictionnaire Python via `response.json()`
- Extraction d’une clé du JSON

### ✔️ Étape 8 — Response Validation

- Vérification du code HTTP :
  - `200` → **Request successful**
  - autre → **Request failed**

### ✔️ Étape 9 — Error Management

- Ajout d’un bloc `try / except`
- Gestion propre des erreurs réseau ou API

### ✔️ Étape 10 — Data Retrieval Function

- Création de la fonction `get_data(url)`
- Retourne les données JSON ou `None`
- Structure réutilisable pour les futures API Forex

---

# 📂 Structure du projet
