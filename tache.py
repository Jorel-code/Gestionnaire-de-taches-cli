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
