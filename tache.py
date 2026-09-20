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