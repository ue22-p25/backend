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

```{image} media/code-with-library.svg
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

```{image} media/code-with-framework.svg
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
```{image} media/framework-routes.svg
:width: 70%
```
````

A cela un framework complet ajoute des fonctionnalités de :

````{div}
:class: center
`Web Template`, `Sécurité`, `Accès à des bases de données`
````

---

## Framework Flask

xxx todo : on va utiliser FastAPI xxx

Micro-framework Python 🐍 développé depuis 2010.
<br><br>
````{div}
:class: center
```{image} media/logos/logo-flask.svg
:width: 30% 
```
````

<br><br>
🚧 Micro-framework ne veut pas dire "pas utilisable sur des gros projets"  ⚠️
<br><br>
````{div}
:class: center
Pinterest, Airbnb, Trivago, ...
````
<br><br>
Micro-framework car noyau très léger et minimaliste, mais pouvant être enrichi avec des extensions.

---

## Le setup de base

### Installation

```bash
pip install flask
```

### Minimal working example

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

````{div}
:class: center
Une fois lancé -> [http://localhost:5000](http://localhost:5000)

```{div}
:class: clignote
? C'est quoi `@app.route('/')` ?
```
````

---

## Les routes

`@app.route` est un décorateur qui permet d'associer une fonction à une URL et un type de requête HTTP.

Dans sa version complète on peut écrire :

```python
@app.route('/hello', methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    ## traitement
  elif request.method == 'GET':
    ## traitement
  else:
    return "Méthode non autorisée", 405
```

---

## On a fini ...

````{div}
:class: center
<iframe src="https://giphy.com/embed/3ohs7XbAurbpO5jIBy" width="480" height="267" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

... ou pas en fait: on va mettre tout ça en pratique avec un exercice

