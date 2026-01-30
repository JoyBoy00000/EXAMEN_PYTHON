# 📦 Projet Python – Scraping Web & Gestion de Stock

Ce dépôt contient **deux programmes Python indépendants** réalisés dans le cadre d’un exercice / examen :
1. Un script de **scraping web** avec `requests` et `BeautifulSoup`
2. Une application **console de gestion de stock**

---

## 🧩 1. Script de Scraping Web

### 🎯 Objectif
Récupérer automatiquement des informations depuis une page web locale :
- images
- titres
- paragraphes
- champs de formulaire
- liens de navigation

---

### 🛠️ Technologies utilisées
- Python 3
- `requests`
- `beautifulsoup4`

---

### 📁 Fichier concerné
- `scriping.py`

---

### 🌐 Prérequis
- Avoir un fichier `index.html`
- Lancer un serveur local (ex: **Live Server sur VS Code**)
- URL utilisée :
http://127.0.0.1:5500/index.html


---

### ⚙️ Fonctionnalités
- Connexion à une page HTML locale
- Extraction des balises `<img>`
- Extraction des titres `<h3>` dans les sections `.card-service`
- Extraction des paragraphes `<p>`
- Récupération des champs de formulaire (`input`, `textarea`)
- Récupération des liens de navigation

---

### ▶️ Exécution
python scriping.py

 # 📊 Application de Gestion de Stock en Python

Cette application est un programme **console** développé en Python permettant de gérer un stock de produits.  
Elle permet d’enregistrer les produits, les entrées et sorties de stock, et de consulter l’état du stock en temps réel.

---

## 🎯 Objectifs du programme
- Gérer des produits avec un prix et un seuil d’alerte
- Suivre les entrées et sorties de stock
- Calculer automatiquement le stock disponible
- Alerter en cas de stock faible
- Consulter l’historique des mouvements

---

## 🛠️ Technologies utilisées
- Python 3
- Module standard `datetime`

---

## 📁 Fichier principal
- `gestion_stock.py` *(nom à adapter selon ton fichier)*

---

## ⚙️ Fonctionnalités

### ➕ Ajouter un produit
- Nom du produit
- Prix unitaire
- Seuil d’alerte

### 📥 Entrée de stock
- Nom du produit
- Quantité entrée
- Fournisseur
- Date automatique

### 📤 Sortie de stock
- Nom du produit
- Quantité sortie
- Motif (vente, perte, etc.)
- Vérification du stock disponible

### 📦 Affichage du stock
- Stock calculé dynamiquement
- Alerte si le stock est inférieur ou égal au seuil

### 📜 Historique
- Liste des entrées de stock
- Liste des sorties de stock
- Dates enregistrées automatiquement

---
## 📋 Structure des données

Toutes les données sont conservées **en mémoire** sous forme de dictionnaires et de listes.

```python
# Dictionnaire des produits
produits = {
    "nom_produit": {          # clé = nom du produit (str)
        "prix": float,        # prix unitaire
        "seuil_alerte": int,  # seuil pour alerte de stock faible
        "date_creation": datetime  # date d'ajout du produit
    }
}

# Liste des entrées de stock
entrees_stock = [
    {
        "nom_produit": str,    # nom du produit
        "quantite": int,       # quantité entrée
        "fournisseur": str,    # fournisseur
        "date": datetime       # date d'entrée
    }
]

# Liste des sorties de stock
sorties_stock = [
    {
        "nom_produit": str,    # nom du produit
        "quantite": int,       # quantité sortie
        "motif": str,          # motif (vente, perte, etc.)
        "date": datetime       # date de sortie
    }
]


