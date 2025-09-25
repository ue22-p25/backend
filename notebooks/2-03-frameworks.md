# Les frameworks

Réponse à un besoin mais lequel ?

````{div}
:class: center
***Cadre de développement simplifié***
````

En gros un guide <strike> spirituel </strike>, permettant de développer simplement des applications spécifiques.

````{div}
:class: center
<iframe src="https://giphy.com/embed/MZW5o8f5RaH0Q" width="480" height="197" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Framework vs Librairie

````{div}
:class: center
Frameworks, Librairies, même chose ? <br>
````

`````{div}
:class: columns

````{div}
:class: fifty center
<b> Librairies </b>

Ensemble de programmes effectuant des opérations spécifiques, que vous allez utiliser de manière ponctuelle au sein de vos programmes en suivant votre propre logique.

Par exemple `NumPy` en Python 🐍 est une librairie

```{image} media/code-with-library.excalidraw.svg
:align: center
```
````

````{div}
:class: vertbar
````

````{div}
:class: fifty center bottom
<b> Framework </b>

Cadre de développement dans lequel le développeur vient s'inscrire, i.e. développer des fonctionnalités/comportements. Là ce n'est plus le développeur qui fixe sa logique mais le framework.  

Un code à trou 🕳️ en quelque sorte

```{image} media/code-with-framework.excalidraw.svg
:align: center
```
````

`````

---

## Frontend, backend

````{div}
:class: center
⚠️ Framework web un terme très, trop, générique ⚠️
````

`````{div}
:class: columns

````{div}
:class: fifty center
Framework frontend

```{image} media/framework_frontend.png
:width: 50%
:align: center
```

Focalisé sur le développement d'application côté client
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
Framework backend

```{image} media/framework_backend.png
:align: center
```

Focalisé sur le développement côté serveur
````

`````

---

## frameworks backend: les grands principes

````{div}
:class: center
```{image} media/framework-routes.excalidraw.svg
:width: 70%
```
````

A cela un framework complet ajoute des fonctionnalités de :

````{div}
:class: center
`Web Template`, `Sécurité`, `Accès à des bases de données`
````

---

## Framework FastAPI

Framework Python 🐍 "lightweight" développé depuis 2018.

```{image} media/logos/logo-fastapi.svg
:align: center
:width: 300px
```

<br><br>
🚧 framework "lightweight" ne veut pas dire "pas utilisable sur des gros projets"  ⚠️
<br>
````{div}
:class: center
Netflix, Microsoft, Uber, ... utilisent FastAPI pour certaines parties de leurs backends
````

noyau très léger et minimaliste, mais super puissant

- utilise les **annotations de type** Python pour la validation automatique des données
- **documentation automatique** des API avec Swagger UI et ReDoc
- **nativement asynchrone**, du coup très performant
- de plus, il peut être enrichi avec des **extensions**.

---

## Le setup de base

(label-fastapi-install)=
### Installation

```bash
pip install fastapi[standard]
```

```{admonition} remarque à propos de bash
:class: dropdown

en toute rigueur il faudrait taper  
`pip install "fastapi[standard]"`  
avec les guillemets, pour éviter que votre shell n'interprète mal les crochets `[]`; savez-vous pourquoi ?  
mais bon en pratique la différence est minime...
```

nous allons aussi installer `httpie` pour tester les API en ligne de commande  
c'est juste un outil de développement très pratique, pas besoin de cette dépendance en production

```bash
# ceci installe la commande http, disponible depuis le terminal
pip install httpie
```

---

### Hello world en FastAPI (run it)

`````{grid} 2 2 2 2
````{div}
créons un fichier `hello.py` avec ceci:


```python
# dans hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

```{div}
:class: clignote
? C'est quoi `@app.get('/')` ?
```
````

````{div}
et pour le lancer tapez ceci
```bash
# dans le terminal

fastapi dev hello.py
```

:::{admonition} un mot sur `uvicorn`
:class: dropdown tip
`uvicorn` est le serveur ASGI recommandé pour FastAPI.  
Il est installé automatiquement avec l'option `[standard]` de FastAPI.  
Et pour info, en réalité `fastapi dev` est un alias pour  
`uvicorn hello:app --reload --debug`
:::
````
`````

---

### Hello world en FastAPI (use it)

après quoi on peut interroger notre API... on a le choix entre:

`````{grid} 2 2 2 2
````{div}
ouvrir un navigateur web à l'adresse  
[http://localhost:8000](http://localhost:8000)  
faites-le, vous devez voir ceci:
```text
{"message":"Hello World"}
```
````

````{div}
utiliser `http(ie)` en ligne de commande
```bash
# en version bavarde
http GET http://localhost:8000

# en version concise
http :8000
```

les deux formes sont équivalentes  
et dans les deux cas observez que `http` nous montre les *Headers* HTTP de la réponse 

````

`````

---

## Les routes

`@app.get` est un décorateur qui permet **d'associer une fonction à une URL** (ici de type GET).  
Évidemment une application web c'est plus que ça, on veut gérer plusieurs URLs, et de plusieurs types.  
Du coup une application FastAPI c'est essentiellement une collection de routes.

Par exemple:

```python
@app.post("/items/")
def create_item(item: Item):
    # le code pour créer un item

@app.get("/items/")
def create_item(item: Item):
    # le code pour lister les items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # le code pour lire un item
```

:::{admonition} `@app.api_route`
:class: dropdown tip
il est aussi possible d'utiliser `@app.api_route` pour "capturer" dans une seule fonction plusieurs types de requêtes
:::

---

## On a fini ...

````{div}
:class: center
<iframe src="https://giphy.com/embed/3ohs7XbAurbpO5jIBy" width="480" height="267" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

... ou pas en fait: on va mettre tout ça en pratique avec un exercice

