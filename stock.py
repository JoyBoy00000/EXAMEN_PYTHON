from datetime import datetime

# -------------------------
# DONNÉES EN MÉMOIRE
# -------------------------
produits = {}          # clé = nom_produit
entrees_stock = []
sorties_stock = []

# -------------------------
# FONCTIONS MÉTIER
# -------------------------
def ajouter_produit():
    try:
        nom = input("Nom du produit : ").strip().lower()
        if nom in produits:
            print(" Produit déjà existant")
            return

        prix = float(input("Prix unitaire : "))
        seuil = int(input("Seuil d'alerte : "))

        produits[nom] = {
            "prix": prix,
            "seuil_alerte": seuil,
            "date_creation": datetime.now()
        }
        print(f" Produit '{nom}' ajouté avec succès")

    except ValueError:
        print(" Valeur invalide")

def entree_stock():
    try:
        nom = input("Nom du produit : ").strip().lower()
        if nom not in produits:
            print("Produit inexistant")
            return

        quantite = int(input("Quantité entrée : "))
        if quantite <= 0:
            print("Quantité invalide")
            return

        fournisseur = input("Fournisseur : ")

        entrees_stock.append({
            "nom_produit": nom,
            "quantite": quantite,
            "fournisseur": fournisseur,
            "date": datetime.now()
        })
        print("Entrée de stock enregistrée")

    except ValueError:
        print("Erreur de saisie")

def sortie_stock():
    try:
        nom = input("Nom du produit : ").strip().lower()
        if nom not in produits:
            print("Produit inexistant")
            return

        quantite = int(input("Quantité sortie : "))
        if quantite <= 0:
            print("Quantité invalide")
            return

        stock = calcul_stock(nom)
        if quantite > stock:
            print("Stock insuffisant")
            return

        motif = input("Motif (vente, perte...) : ")

        sorties_stock.append({
            "nom_produit": nom,
            "quantite": quantite,
            "motif": motif,
            "date": datetime.now()
        })
        print("Sortie de stock enregistrée")

    except ValueError:
        print("Erreur de saisie")

def calcul_stock(nom):
    total_entree = sum(
        e["quantite"] for e in entrees_stock if e["nom_produit"] == nom
    )
    total_sortie = sum(
        s["quantite"] for s in sorties_stock if s["nom_produit"] == nom
    )
    return total_entree - total_sortie

def afficher_stock():
    print("\n ÉTAT DU STOCK")
    if not produits:
        print("Aucun produit enregistré")
        return

    for nom, data in produits.items():
        stock = calcul_stock(nom)
        alerte = "STOCK FAIBLE" if stock <= data["seuil_alerte"] else ""
        print(f"{nom.upper()} | Stock : {stock} {alerte}")

def afficher_historique():
    print("\n HISTORIQUE DES MOUVEMENTS")

    print("\n Entrées :")
    for e in entrees_stock:
        print(e)

    print("\n Sorties :")
    for s in sorties_stock:
        print(s)

# -------------------------
# MENU PRINCIPAL
# -------------------------
def menu():
    while True:
        print("""
========= MENU GESTION DE STOCK =========
1. Ajouter un produit
2. Entrée de stock
3. Sortie de stock
4. Afficher le stock
5. Afficher l'historique
0. Quitter
========================================
""")
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_produit()
        elif choix == "2":
            entree_stock()
        elif choix == "3":
            sortie_stock()
        elif choix == "4":
            afficher_stock()
        elif choix == "5":
            afficher_historique()
        elif choix == "0":
            print("Au revoir")
            break
        else:
            print("Choix invalide")

# -------------------------
# LANCEMENT
# -------------------------
if __name__ == "__main__":
    menu()
