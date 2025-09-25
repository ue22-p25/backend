# Framework FastAPI

Micro-framework Python 🐍 - plutôt récent (2018);  
occupe le même espace que

- Flask - développé depuis 2010 - léger et extensible
- Django - développé depuis 2003 - perçu comme plus complet mais plus lourd aussi

🚧 Micro-framework ne veut pas dire pas utilisable sur des gros projets ⚠️  

```{image} media/logos/logo-fastapi.svg
:width: 20%
```

---

## FastAPI

similaire en surface à Flask, mais **beaucoup plus moderne** !

- favorise une approche plus structurée
  - tire parti des **informations de type** (annotations de type / pydantic)
  - notamment pour la validation / conversion des données
  - on peut définir des modèles séparés pour la création, la lecture, la mise à jour, etc.  
    utile par exemple pour le hachage de mots de passe (non exposé)
- en particulier, génère automatiquement une **documentation interactive**
- a un support natif pour la programmation asynchrone
- ainsi que pour les websockets

---

## Pourquoi FastAPI et pas autre chose

1️⃣ Vous savez tous à peu près faire du Python 🐍

````{div}
:class: center
donc on élimine tout ce qui n'est pas à base Python
````

2️⃣ On va essayer de vous apprendre des trucs utilisés par ailleurs  
Et la tendance FastAPI semble effectivement être à une hausse spectaculaire !

````{div}
:class: center

```{figure} media/web-framework-survey.png
:class: smaller
:width: 85%
Source: <a href="https://www.jetbrains.com/lp/devecosystem-2023/python/">https://www.jetbrains.com/lp/devecosystem-2023/python/</a>
```

````

---

## Mais au fait ...

... pourquoi on s'intéresse à ça ?

---

## Graphical User Interface

Faire le pont 🌉 entre :

````{div}
:class: center
un code de calcul/traitement de données/...  
et une interface graphique  
du coup très pertinent pour les "Projets Informatique" de la fin du S2
````

Deux approches :

`````{div}
:class: columns

````{div}
:class: fifty center
***Old school***  
Utilisation de librairies graphiques et développement d'un client lourd

```{image} media/old-school.excalidraw.svg
:width: 50%
:align: center
```
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
***New age***

Utilisation du navigateur

```{image} media/new-age.excalidraw.svg
```
````

`````

---

## On sait déjà vaguement s'en servir

```{div}
:class: center
rappelez-vous, on a déjà vu  
[comment installer FastAPI](label-fastapi-install)  
et  
[comment faire un serveur minimal avec FastAPI](label-exo-apitester)

remarquez comme c'est simple de démarrer 😯  
c'est un avantage de Flask/FastAPI par rapport à Django  
qui nécessite un setup plus poussé pour démarrer un projet
```

---

## Rappel rapide

`````{div}
:class: columns

````{div}
:class: fifty
- Step 1️⃣ :

```python
from fastapi import FastAPI
```
````

````{div}
:class: fifty
- Step 2️⃣

```python
app = FastAPI()
```
````
`````

Ensuite tout repose sur une syntaxe un peu particulière :

```python
*@app.get("/un/chemin/cible")
def la_fonction_correspondante():
  // fait des trucs très intelligents
  // et encore plus
  return un_resultat ## pouvant être du html, du json, ....
```

Pour le lancer en mode développement depuis le terminal

`````{div}
:class: columns

````{div}
:class: fifty
```bash
fastapi dev mon_fichier.py
```
````


````{div}
:class: fifty
ou en mode prod avec  
`fastapi run mon_fichier.py`
````
`````

<!-- ---

### Pour ceux qui auraient la flemme !

`````{div}
:class: columns

````{div}
:class: sixty
```{div}
:class: center
<iframe src="https://giphy.com/embed/4KkSbPnZ5Skec" width="471" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````

````{div}
:class: fourty center

xxx no longer working xxx

[http://bit.ly/3Z5C5k7](http://bit.ly/3Z5C5k7)

```{image} media/qrcode/flask_sandbox.png
:width: 60%
```
````
`````
 -->
---

## Envoyer autre chose qu'une chaine !

Si on veut pour une url donnée renvoyer, non pas une chaîne, mais un fichier HTML qui lui même peut nécessiter des CSS/JS, il va falloir une organisation un peu particulière

`````{div}
:class: columns

````{div}
:class: fifty
```bash
.
├── app.py
├── static
│   ├── css
│   │   └── wheel.css
│   └── js
│       └── wheel.js
└── templates
    └── wheel.html
```
````

````{div}
:class: fifty
```python
from flask import render_template
```

```python
@app.route("/")
def index():
  return render_template("wheel.html")
```
````
`````

En revanche tous les fichiers contenus dans le dossier `static` seront
**automatiquement accessibles** sans que l'on ait rien à faire et ça c'est 🆒 !

---

## Un truc un tout petit peu plus évolué

### Passage de paramètres aux URLs

````{div}
:class: center
```{image} media/http-get-arguments.excalidraw.svg
:width: 80%
```
````

Besoin de récupérer dans la fonction `handler` la requête et donc ses arguments 🤔

````{div}
:class: center
Flask a tout prévu
````

`````{div}
:class: columns

````{div}
:class: sixty
```python
from flask import request

@app.route("/une/route/donnee")
def handler():
  name = request.args.get("name")
  age = request.args.get("age")
  return f"<h1> Hello {name} ! Tu as vraiment {age} ans ? </h1>"
```
````

````{div}
:class: fourty
⚠️ Si l'argument n'existe pas la fonction `get` retourne `None`
````
`````

````{div}
:class: center
🚧 Pas de notion de type dans les arguments, tout est chaîne de caractère 🚧
````

---

## URL paramétrique

Possibilité offerte par Flask de définir des paramètres au sein même d'une URL

````{div}
:class: center
```{image} media/flask-route-param.excalidraw.svg
```
````

`````{div}
:class: columns
````{div}
:class: fifty
Possibilité de typer les paramètres :

- `string` : pour tout texte sans slash
- `int` : valeur entière positive
- `float` : valeur flottante positive
- `path` : un string qui peut contenir un slash `/`
````
````{div}
:class: fifty
```python
@app.route("/home/<int:user_id>")
def home_uid(user_id):
    ## do something according to user_id value
    return f"we were passed {user_id}"
```
````
`````

```{div}
:class: smaller
bien sûr on peut aussi recevoir comme ça plusieurs paramètres
```

---

## Un exemple : générateur de nombre aléatoire

API de génération de nombres aléatoires

- `/api/integer` : génère des entiers
- `/api/float` : génère des flottant

Possibilité pour les deux d'ajouter un paramètre `n` par exemple `?n=10` pour générer 10 valeurs alétoires.

````{div}
:class: center

xxx no longer working xxx

```{div}
[http://bit.ly/3nb0yaG](http://bit.ly/3nb0yaG)

```{image} media/qrcode/flask_random_api.png
:align: center
:width: 20%
```
````

---

## Une API complète

Petit rappel du 1er épisode, HTTP différentes requêtes possibles

- `GET` : requêtes pour **_obtenir_** du serveur une ressource (fichier html/css/js, image, video, données, ...)
- `POST` : requêtes pour **_envoyer_** des données au serveur en vu d'un traitement (ajout d'un utilisateur dans une base de données, ...)
- `PATCH` : requêtes pour **_modifier partiellement_** une ressource du serveur (mettre à jour l'addresse mail d'un utilisateur dans la base de données)
- `DELETE` : requêtes pour **_supprimer_** une ressource du serveur (supprimer un commentaire sur un article, ... )

Il s'agit là des principaux types de requêtes mais il en existe d'autres, pour la liste complète vous pouvez faire un tour [https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol).

---

## Spécification des requêtes

Une même fonction pour un chemin, mais pour différents types de requête (e.g. GET et POST)

```python
from flask import request

@app.route("/chemin", methods=['GET', 'POST'])
def the_function():
  if request.method == "POST":
    ## do something for post
    return post_response
  elif request.method == "GET":
    ## do other thing
    return get_response
```

Mais on peut aussi faire: une fonction par chemin et par type de requête

```python
@app.get("/chemin")
def get_for_chemin():
  return

@app.post("/chemin")
def post_for_chemin():
  return
```

---

## Récupérer les données reçues

````{div}
:class: center
Encore une fois tout se passe dans `request`
````

Plusieurs méthodes à disposition :

- `request.is_json()` pour vérifier qu'il y a bien du json dans la requête
- `request.get_json()` qui retourne le contenu de la requête

````{div}
:class: center
⚠️ Lorsque vous traitez une requête `POST` il faut impérativement que votre fonction renvoie quelque chose ⚠️
````

````{div}
:class: center

xxx no longer working xxx

[http://bit.ly/40ly786](http://bit.ly/40ly786)

```{image} media/qrcode/flask_post.png
:width: 20%
```
````

