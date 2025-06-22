# Framework Flask

Micro-framework Python 🐍 développé depuis 2010.
<br><br>
````{div}
:class: center
```{image} media/logos/logo-flask.svg
:width: 35%
```
````
<br><br>
🚧 Micro-framework ne veut pas dire pas utilisable sur des gros projets ⚠️
<br><br>
````{div}
:class: center
Pinterest, Airbnb, Trivago, ...
````
<br><br>
Micro-framework car noyau très léger et minimaliste mais pouvant être enrichi avec des extensions.

---

## Pourquoi Flask et pas autre chose

1️⃣ Vous savez tous à peu prêt faire du Python 🐍

````{div}
:class: center
donc on élimine tout ce qui n'est pas à base Python
````

2️⃣ On va essayer de vous apprendre des trucs utilisés par ailleurs

````{div}
:class: center

````{figure} media/web_framework_survey.png
:class: smaller
:width: 70%
Source: <a href="https://www.jetbrains.com/lp/devecosystem-2022/python/">https://www.jetbrains.com/lp/devecosystem-2022/python/</a>
````

```{div}
:class: smaller
Notez bien que tout ça est extrêmement difficile à mesurer par ailleurs - par exemple, on parle de quelle unité ?  
Il reste toutefois que la tendance FastAPI semble effectivement être à la hausse.
```

---

## Mais au fait ...

... pourquoi on s'intéresse à ça ?

---

## Graphical User Interface

Faire le pont 🌉 entre :

````{div}
:class: center
un code de calcul/traitement de donnée/...  
et une interface graphique  
du coup très pertinent pour les Projets Informatique
````

Deux approches :

`````{div}
:class: columns

````{div}
:class: fifty center
***Old school***  
Utilisation de librairies graphiques et développement d'un client lourd

```{image} media/old-school.svg
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

```{image} media/new-age.svg
```
````

`````


---

## Une première app

### Installation

Pour commencer on installe `Flask`

```bash
pip install flask
```

Vous pourrez alors travailler en local 💻️. 

```{div}
:class: smaller
Au besoin si vous voulez vous mettre dans une configuration serveur vous pouvez utiliser [@Replit](https://replit.com) il y a un template Flask.
```


```{div}
:class: center
Et rien de plus à faire 😯 <br>
c'est l'avantage de Flask par rapport à Django <br> qui nécessite un setup plus poussé pour démarrer un projet
```

---

## Minimal Working Example

`````{div}
:class: columns

````{div}
:class: fifty
- Step 1️⃣ :

```python
from flask import Flask
```
````

````{div}
:class: fifty
- Step 2️⃣

```python
app = Flask("Appli de ouf")
```
````
`````

Ensuite tout repose sur une syntaxe un peu particulière :

```python
*@app.route("/une/url/cible")
def la_fonction_correspondante():
  // fait des trucs très intelligents
  // et encore plus
  return un_resultat ## pouvant être du html, du json, ....

```

Pour finir :

`````{div}
:class: columns
````{div}
:class: fifty
```python
app.run(debug=True, port=3001)
```
````
````{div}
:class: fifty
`debug=True` permet d'activer du hot reloading
````
`````

---

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
```{image} media/http-get-arguments.svg
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
```{image} media/flask-route-param.svg
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

