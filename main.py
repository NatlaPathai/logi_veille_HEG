from fastapi import FastAPI
from mysql import connector
import uvicorn

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@app.get("/")
def welcome():

    # Retourne le message de bienvenue
    return {"message": "bienvenue"}

# endpoint axe légal
@app.get("/axe_legal")
def get_all_axe_legal():

    # On se connecte à la base de données MySQL
    bdd = connector.connect(
        user='root', 
        password='', 
        host='localhost', 
        database='n8n_AthenaIA'
    )

    # On crée un curseur
    curseur = bdd.cursor()

    # On écrit la requête SQL pour récupérer tous les articles qui n'ont pas encore été sélectionné
    sql = "SELECT id, title, link, pub_date, content, source_name FROM axe_legal WHERE is_selected = 0"

    # On exécute la requête
    curseur.execute(sql)

    # On crée une liste vide pour stocker les articles
    liste = []

    # On parcourt les résultats
    for id, title, link, pub_date, content, source_name in curseur:  

        # On crée un dictionnaire pour chaque article
        articles = {
            "id": id,
            "title": title, 
            "link": link,
            "pub_date": str(pub_date),
            "content": content,
            "source_name": source_name
            }
        
        # On ajoute cet article (dictionnaire) à notre liste d'articles
        liste.append(articles)  
    
    # On ferme la connexion à la base de données
    bdd.close()

    # On retourne le résultat
    return(liste)

# endpoint axe actualité
@app.get("/axe_actualite")
def get_all_axe_actualite():

    # On se connecte à la base de données MySQL
    bdd = connector.connect(
        user='root', 
        password='', 
        host='localhost', 
        database='n8n_AthenaIA'
    )

    # On crée un curseur
    curseur = bdd.cursor()

    # On écrit la requête SQL pour récupérer tous les articles qui n'ont pas encore été sélectionné
    sql = "SELECT id, title, link, pub_date, content, source_name FROM axe_actualite WHERE is_selected = 0"

    # On exécute la requête
    curseur.execute(sql)

    # On crée une liste vide pour stocker les articles
    liste = []

    # On parcourt les résultats
    for id, title, link, pub_date, content, source_name in curseur:  

        # On crée un dictionnaire pour chaque article
        articles = {
            "id": id,
            "title": title, 
            "link": link,
            "pub_date": str(pub_date),
            "content": content,
            "source_name": source_name
            }
        
        # On ajoute cet article (dictionnaire) à notre liste d'articles
        liste.append(articles)  
    
    # On ferme la connexion à la base de données
    bdd.close()

    # On retourne le résultat
    return(liste)

# endpoint axe légal
@app.get("/axe_contexte")
def get_all_axe_contexte():

    # On se connecte à la base de données MySQL
    bdd = connector.connect(
        user='root', 
        password='', 
        host='localhost', 
        database='n8n_AthenaIA'
    )

    # On crée un curseur
    curseur = bdd.cursor()

    # On écrit la requête SQL pour récupérer tous les articles qui n'ont pas encore été sélectionné
    sql = "SELECT id, title, link, pub_date, content, source_name FROM axe_contexte WHERE is_selected = 0"

    # On exécute la requête
    curseur.execute(sql)

    # On crée une liste vide pour stocker les articles
    liste = []

    # On parcourt les résultats
    for id, title, link, pub_date, content, source_name in curseur:  

        # On crée un dictionnaire pour chaque article
        articles = {
            "id": id,
            "title": title, 
            "link": link,
            "pub_date": str(pub_date),
            "content": content,
            "source_name": source_name
            }
        
        # On ajoute cet article (dictionnaire) à notre liste d'articles
        liste.append(articles)  
    
    # On ferme la connexion à la base de données
    bdd.close()

    # On retourne le résultat
    return(liste)

# endpoint axe légal
@app.get("/axe_outils")
def get_all_axe_outils():

    # On se connecte à la base de données MySQL
    bdd = connector.connect(
        user='root', 
        password='', 
        host='localhost', 
        database='n8n_AthenaIA'
    )

    # On crée un curseur
    curseur = bdd.cursor()

    # On écrit la requête SQL pour récupérer tous les articles qui n'ont pas encore été sélectionné
    sql = "SELECT id, title, link, pub_date, content, source_name FROM axe_outils WHERE is_selected = 0"

    # On exécute la requête
    curseur.execute(sql)

    # On crée une liste vide pour stocker les articles
    liste = []

    # On parcourt les résultats
    for id, title, link, pub_date, content, source_name in curseur:  

        # On crée un dictionnaire pour chaque article
        articles = {
            "id": id,
            "title": title, 
            "link": link,
            "pub_date": str(pub_date),
            "content": content,
            "source_name": source_name
            }
        
        # On ajoute cet article (dictionnaire) à notre liste d'articles
        liste.append(articles)  
    
    # On ferme la connexion à la base de données
    bdd.close()

    # On retourne le résultat
    return(liste)

# Démarrage de l'app
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
