from datetime import date
taches = []
def ajout_tache():
    nom = input("Entrez le nom de la tache : ")
    tache = {"id":max([t["id"] for t in taches], default = 0) + 1, "nom":nom, "date":date.today().isoformat(), "statut":"à faire" }
    taches.append(tache)
    print(f"Tache ajoutée(id: {tache['id']})")

def liste_taches():
    for tache in taches:
        print(f"[{tache['id']}] - {tache['nom']} - {tache['statut']} - {tache['date']}")

def changer_status():
    id_tache = int(input("Entrez l'ID de la tache: "))
    for tache in taches:
        if tache["id"] == id_tache:
            tache['statut'] = 'terminée'
            print(f"Tache {id_tache} marquée comme terminée")

def supprimer_tache():
    id_tache = int(input("Entrez l'ID de la tache: "))
    for tache in taches:
        if tache['id'] == id_tache:
            taches.remove(tache)
    print(f"Tache {id_tache} supprimée")

def sauvegarder():
    with open("taches.json", "w", encoding = "utf-8") as f:
        json.dump(taches, f, indent = 2, ensure_ascii = False) 

def charger():
    global taches
    try:
        with open("taches.json", "r", encoding = "utf-8") as f:
            taches = json.load(f)
    except FileNotFoundError:
        taches = []

def launch():
    charger()
    while True:
        print( "\n== MENU ==")
        print(" Entrez votre choix")
        print("  1. Ajouter une tache")
        print("  2. Lister les taches")
        print("  3. Marquer une tache comme terminé")
        print("  4. Supprimer une tache")
        print("  5. Quitter")
        choix = input()
        if choix == "1":
            ajout_tache()
            sauvegarder()
        elif  choix == "2":
            liste_taches()
        elif choix == "3":
            changer_status()
        elif choix == "4":
            supprimer_tache()
        elif choix == "5":
            sauvegarder()
            print("Au revoir")
            break

launch()