# Mon premier serveur

## Et au fait il répond quoi le serveur à GET&nbsp;?

`````{div}
:class: columns

````{div}
:class: fifty
```{image} media/http-request.excalidraw.svg
:width: 100%
:align: center
```
````

````{div}
:class: fifty
```{image} media/response-format.excalidraw.svg
:align: center
:width: 100%
```
````
`````

```{div}
:class: smaller
En vrai, c'est un mauvais exemple car bien souvent le *Body* d'une réponse HTTP est vide;  
mais bon c'est l'idée générale qu'il faut retenir;
```

---

### dans le navigateur

C'est possible de voir les requêtes et réponses dans votre navigateur  
via `Outils de développement → Network`

`````{div}
:class: columns

````{div}
:class: sixty

```{image} media/chrome-request-headers.png
```
````

````{div}
:class: fourty

```{image} media/chrome-response-headers.png
```
````
`````

---

## Faisons un serveur http de base

`````{div}
:class: columns

````{div}
:class: fifty-five

```sh
## dans votre terminal:
## on va dans le repo du cours
cd /bla-bla-bla/backend

## il y a un dossier html
cd html

## pour lancer le serveur
python -m http.server

## NB: ... 
## à ce stade le terminal est bloqué
## pour tuer le serveur tapez "Control-C"
```
````

````{div}
:class: fourty-five

puis ouvrez dans votre navigateur `http://localhost:8000/index.html` (*)
```{div}
:class: smaller
(*) vous pouvez aussi remplacer `localhost` avec votre adresse IP - [on en a parlé ici](#my-ip-address)
```
````
`````

```{div}
:class: smaller center

c'est vraiment la méthode la plus simple possible pour faire un serveur avec Python 🐍  
mais bon c'est juste un jouet hein
```

---

### Un peu moins de base

```{div}
:class: center
Cette fois-ci on va le faire *à la main* et écrire un peu de code, toujours en Python 🐍  
ça se passe dans le dossier `python/http`  
📢 ⚠️ On regarde le fichier `server1_static.py`
```

```{literalinclude} ../python/http/server1_static.py
:align:center
```

---

## Traitement des requêtes

Le fonctionnement interne d'un serveur HTTP est assez simple

1. **Écouter** sur un port (80 par défaut)
2. **Accepter** une connexion
3. **Lire** la requête
4. **Traiter** la requête
5. **Envoyer** la réponse
6. **Fermer** la connexion

Le point important est la transition entre les étapes 3 et 4 qui est le coeur du serveur HTTP  
car il définit la manière dont le serveur va traiter la requête.

---

## Exemples fait à la main

📢 ⚠️ dans le dossier `python/http`, on regarde les fichiers:

- `server2_static_byhand.py`
  - en gros, mêmes fonctions: sait répondre à GET pour les fichiers statiques
  - mais écrit "à la pogne"
    <br><br>
- `server3_post_stateful.py`
  - le serveur est STATEFUL (il se souvient de l'état) - voir la variable `STATE`  
    (NB: dans la vraie vie bien sûr, l'état sera stocké dans une database SQL - ou autre)
  - le POST: les affectations var=value sont mémorisées
  - le GET: quel que soit le PATH, affiche en html le contenu des variables connues dans `STATE` (et autres détails)
    <br><br>
- `server4_template.py`
  - mêmes fonctionnalités mais avec un template JINJA2

---

## of course il existe des frameworks pour ça&nbsp;!

tout cela est un peu fastidieux, c'est pourquoi on utilise des frameworks (→ slides suivants)  
mais c'est bien de comprendre comment ça marche  
à retenir tout de même: cette histoire de templates; on en reparlera

