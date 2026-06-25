# logi_veille_HEG
Logiciel de veille Open Source. Réalisé dans le cadre d'un mandat de veille pour le compte de M. Sievering.

# Crédits
Ali Kaley Muna ; Glassey Léa ; Grosso Luca ; Frey Morgane ; Thai Nathan

# Guide d'utilisation
## n8n
Vous trouverez dans le dossier n8n cinq fichiers JSON correspondant chacun à un workflow n8n. Pour les importer, créez un nouveau workflow dans votre environnement n8n. Faites dérouler les options en haut à droite et sélectionnez « Import from file… ». Répétez cette action pour chaque workflow.

## index.html
Le fichier index.html correspond à l’interface web du logiciel. Pour la rendre disponible sur le serveur local, vous pouvez utiliser la commande suivante dans le terminal à l’emplacement du fichier index.html :
py -m http.server 8005 / 
8005 correspond au port de votre serveur. Vous pouvez le modifier vers un autre port libre de votre serveur.

## main.py
Le fichier main.py correspond à l’API de la base de données. Pour la rendre disponible sur le serveur local, vous pouvez simplement exécuter le fichier. Cela ouvrira un terminal qui instanciera l’API sur le port 8001 du serveur local. Si vous souhaitez modifier ce port, vous pouvez le modifier directement dans le fichier main.py, ligne 206. Assurez-vous de modifier le fichier HTML également à l’endroit approprié, ligne 35.

## requete_sql.txt
Le fichier requete_sql.txt contient quatre requêtes SQL à lancer dans la base de données afin de créer les tables de la base de données. Il est recommandé de nommer la base de données comme suit afin d’éviter d’avoir à modifier certains nœuds n8n : 
n8n_AthenaIA

## test_time.py
Ce fichier est un fichier test pour l'amélioration du logiciel. Vous pouvez l'ignorer.
