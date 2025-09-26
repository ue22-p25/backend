# FastAPI - les bases

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

## Graphical User Interface

Mais au fait ... pourquoi on s'intéresse à ça ?  
La GUI c'est ce qui fait le pont 🌉 entre :

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

## FastAPI: on sait déjà un peu !

```{div}
:class: center
on sait déjà vaguement s'en servir, rappelez-vous, on a déjà vu  
[comment installer FastAPI](label-fastapi-install)  
et  
[comment faire un serveur minimal avec FastAPI](label-exo-apitester)

remarquez comme c'est simple de démarrer 😯  
c'est un avantage de Flask/FastAPI par rapport à Django  
qui nécessite un setup plus poussé pour démarrer un projet
```

---

### Rappel rapide

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

Ensuite on attache des fonctions Python aux chemins d'URL  
on appelle ces fonctions des *route handlers* ou des *router functions*

```python
@app.get("/un/chemin/cible")
def la_fonction_correspondante():
  // fait des trucs très intelligents
  return un_resultat    # pouvant être des données ou du html ou ...
```

---
### Et pour lancer le serveur ?


`````{div}
:class: columns

````{div}
:class: fifty
depuis le terminal
```{code} bash
:caption: le serveur en mode développement
fastapi dev mon_app.py
```
```{code} bash
:caption: ou sur un autre port
fastapi dev mon_app.py --port 8080
```
````


````{div}
:class: fifty
ou aussi
```{code} bash
:caption: en mode production
fastapi run mon_app.py
```

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

## Paramètres dans un GET

````{div}
:class: center

On peut écrire des URLs un tout petit peu plus évoluées:  

```{image} media/http-get-arguments.excalidraw.svg
:width: 80%
```

Besoin de **récupérer les arguments** dans la fonction *handler* 🤔
````

<br>


````{div}
:class: center
FastAPI a tout prévu
````

`````{div}
:class: columns

````{div}
:class: fifty
```python
@app.get("/une/route/donnee")
def get_parameters(
        name: str,
        age: int):
    return {'name': name, 'age': age}
````

````{div}
:class: fifty
il suffit de déclarer les paramètres  
avec leur type  
et FastAPI fait le reste  
et même la conversion de type

````
`````

````{div}
:class: center
🚧 Pas de notion de type dans les échanges réseau, tout est chaîne de caractère 🚧
````

---

## URL paramétrique

Possibilité offerte par Flask de définir des paramètres au sein même d'une URL

````{div}
:class: center
```{image} media/fastapi-route-param.excalidraw.svg
```
````

`````{div}
:class: columns

````{div}
:class: fifty-five smaller
Cas particulier des `/`

- par défaut un paramètre ne contient pas de slash `/`
- **mais** dans une route on peut déclarer  
  `"/ma/route/{parametre:path}"`  

  pour autoriser les slashs `\` dans le paramètre
````
````{div}
:class: fourty-five
```python
@app.get("/ma/route/{parameter}")
def url_parameter(parameter: int):
    return {"square": parameter**2}
```
```{div}
:class: tiny
et bien sûr on peut aussi recevoir comme ça plusieurs paramètres
```
````
`````

---

## Un générateur aléatoire (exo)

`````{div}
:class: columns

````{div}
:class: fifty

**dans `python/random-generator.py`**
- lire le code
- lancer le serveur
````

````{div}
:class: fifty

API de génération de nombres aléatoires

- `/api/integer` : génère des entiers
- `/api/float` : génère des flottant

````

`````

````{div}
:class: center

depuis le browser - ou le terminal avec httpie - interrogez le *endpoint* `/api/integer`
````

```{code} bash
# n'hésitez pas à voir aussi ce que ça donne avec l'option -v
# qui va vous montrer AUSSI la requête envoyée
http :8000/api/integer
```

```{exercise}
:label: exo-random-one

- comment faire pour générer 4 nombres flottants entre 10 et 50 ?  
  ici encore pensez à la documentation interactive
```

```{exercise}
:label: exo-random-two

- que se passe-t-il si on passe un max plus petit que le min ?  
  comment pourrait-on gérer ça ?
```
---

## Solutions de l'exercice

````{solution} exo-random-one
:class: dropdown

- dans le browser:  
  `http://localhost:8000/api/float?min=10&max=50&count=4`

- c'est important de **bien comprendre comment fonctionne *`http`***  
  avec httpie, c'est plus simple:
  ```{code} bash
  :linenos:
  :emphasize-lines: 7

  # en version longue - attention aux guillemets !
  # à cause du & qui est un caractère spécial en bash
  http ":8000/api/float?min=10&max=50&count=4"

  # en version courte, pour passer des paramètres avec GET
  # il faut utiliser ==
  http :8000/api/float min==10 max==50 count==4

  # attention le = simple est pour les requêtes POST !
  # si on utilise = ça ne fait pas ce qu'on veut !
  # NE PAS FAIRE COMME ÇA !
  # http GET :8000/api/float min=10 max=50 count=4

  ```
````

````{solution} exo-random-two
:class: dropdown

en l'état, il n'y aucun contrôle sur les paramètres, du coup le serveur appelle la fonction `random.uniform` avec des paramètres invalides et ça génère une erreur 500

pour pallier à cela, plusieurs choix sont possibles:

- soit on ajoute un contrôle dans la fonction `random_floats` pour vérifier que `min < max` et si ce n'est pas le cas on lève une exception HTTP 400 (Bad Request)
- soit on utilise les fonctionnalités de validation de Pydantic; mais ça pour l'instant c'est prématuré puisqu'on n'a pas encore vu Pydantic 😉

du coup pour l'instant on va se contenter de la 1ère solution

```{code} python
:linenos:
:emphasize-lines: 5

from fastapi import HTTPException

def random_floats(min: float, max: float) -> float:
    if min >= max:
        raise HTTPException(status_code=400, detail="Invalid range")
    return random.uniform(min, max)
````

---

## Les verbes HTTP

Petit rappel du 1er épisode, HTTP différentes requêtes possibles

- `GET` : requêtes pour **_obtenir_** du serveur une ressource (fichier html/css/js, image, video, données, ...)
- `POST` : requêtes pour **_envoyer_** des données au serveur en vu d'un traitement (ajout d'un utilisateur dans une base de données, ...)
- `PATCH` : requêtes pour **_modifier partiellement_** une ressource du serveur (mettre à jour l'addresse mail d'un utilisateur dans la base de données)
- `DELETE` : requêtes pour **_supprimer_** une ressource du serveur (supprimer un commentaire sur un article, ... )

Il s'agit là des principaux types de requêtes mais il en existe d'autres, pour la liste complète vous pouvez faire un tour ici: [https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol).

---

## Paramètres dans un POST

```{admonition} vu plus haut: les paramètres GET sont dans l'URL
:class: tip dropdown admonition-smaller

genre `/ma/route?param1=val1&param2=val2`  
et pour info le protocole HTTP ne prévoit pas qu'on puisse mettre des paramètres dans le corps d'une requête GET, si vous le faites quand même le comportement est indéfini
```

par contre pour les requêtes POST, PATCH, DELETE, ...  
les paramètres sont passés dans le **corps** de la requête

Voyons ça sur un exemple

---

### la requête POST

Et pour commencer regardons ce qui est envoyé par `httpie` quand on fait un POST

````{admonition} le corps d'une requête POST
:class: dropdown

Voici

```{code} bash
:linenos:
:emphasize-lines: 2,11-13

❯ http -v :8000/api/seed seed_value:=42
POST /api/seed HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
Host: localhost:8000
User-Agent: HTTPie/3.2.4

{
    "seed_value": 42
}
```
````

Comme on peut le voir, les paramètres sont envoyés **au format JSON**  
dans le *Body* de la requête - i.e. après les *headers*  

**Retenez bien ça, c'est important !**  
C'est ce procédé qu'il va nous falloir utiliser lorsqu'on voudra envoyer des données au serveur (et notamment lorsque c'est le frontend qui envoie la requête via du JS)

---

### côté FastAPI

Voici à présent le code FastAPI qui va bien pour gérer cette requête

```{code} python
:linenos:
:emphasize-lines: 5

from fastapi import Body

@app.post("/api/seed")
# avec Body() on indique que le paramètre vient du body de la requête
def set_seed(seed_value: int=Body(..., embed=True)):
    random.seed(seed_value)
    return {"message": f"Seed set to {seed_value}"}
```

```{admonition} c'est plus simple avec Pydantic
:class: tip dropdown
on verra ça plus tard, mais si on utilise un modèle Pydantic pour définir les paramètres, c'est encore plus simple...
```

---

## La suite

À ce stade vous savez implémenter des *endpoints* FastAPI qui gèrent des
requêtes GET et POST avec des paramètres

On a plein d'autres choses à voir, et notamment:

- comment FastAPI tire parti des annotations de type pour faire de la validation automatique
- comment retourner du HTML plutôt que de simples données
- et quelques autres tips & tricks

On va voir ça dans les épisodes suivants...
