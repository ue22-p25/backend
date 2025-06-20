# Ma première API

## Petite pause mise en pratique

**Objectif** : Mettre en place une API permettant d'accéder au contenu de fichier CSV

Vous avez <https://github.com/ue22-p24/backend-apitester-frontend> un frontend tout fait !

Et vous avez <https://github.com/ue22-p24/backend-apitester-skeleton> un backend à compléter

L'api du backend doit **impérativement** respecter les routes documentées dans le README.

````{div}
:class: smaller

**astuce**:  
pour copier le contenu de ces dépôts sur votre machine, plutôt que d'utiliser `git clone`, vous pouvez utiliser ceci
```bash
# si nécessaire (npx command not found)
# conda install -c conda-forge nodejs
# download le repo dans le dossier 'frontend'
npx degit git@github.com:ue22-p24/backend-apitester-frontend.git frontend
# pareil pour le backend
npx degit git@github.com:ue22-p24/backend-apitester-skeleton.git backend
```

qui a l'avantage de ne pas recréer un dépôt git dans le dossier créé; surtout si vous vous placez dans un dépôt déjà existant genre `backend-homework`  
(mais ne vous empeche pas de `git add` le résultat immédiatement)
````

---

## Quelques trucs utiles (1)

### *auto-reload*

- on peut lancer l'application avec `python app.py`; ça marche...  
-  **MAIS** il faut relancer le tout à chaque modification (très sous-optimal)
-  du coup il vaut mieux activer le mode debug en lançant
  ```bash
  flask [--app mon_fichier] run --debug
  ```
  qui permet d'avoir un serveur de développement qui se relance tout seul à chaque modification du code,
  et présente en outre un avantage supplémentaire: les erreurs s'affichent dans le browser plutôt que dans le terminal  
  (notez que c'est néfaste en production, car ça peut donner des informations sensibles sur le code)

````{div}
:class: smaller
et pareil pour le frontend d'ailleurs; si vous avez l'intention d'y toucher, il est préférable de le lancer avec `vite`, comme ça il se relance tout seul à chaque modification
````

---

## Quelques trucs utiles (2)

### les routes en Flask

- une route peut prendre un paramètre, éventuellement typé

`````{div}
:class: columns
````{div}
:class: fifty
```python
  @app.route('/hello/<name>')
      def hello(name):
          return f'Hello, {name}!'
```
````

````{div}
:class: fifty
```python
  @app.route('/hello/<int:id>')
      def hello(id):
          return f'Hello, {id**2}!'
```
````
`````

- pour raccourcir le code, une route peut retourner des types variés, qui sont traités comme ceci :

  - `str` : renvoie le texte tel quel, avec un code 200
  - `tuple` : renvoie le premier élément comme texte, le deuxième comme code HTTP
  - `dict` or `list` : renvoie un JSON, avec un code 200
  -  **attention** toutefois avec les **itérateurs** car Flask les traite comme des réponses **en streaming**  
       ce qui nécessite un traitement différent dans le frontend, du coup dans
       cet exo ça ne marchera pas si une de vos routes renvoye un itérateur
  - liste non exhaustive...

---

## Quelques trucs utiles (3)

### *httpie*

- c'est pratique d'avoir un vrai frontend en html/css/js
- MAIS pour développer il peut être utile de tester AUSSI les routes en ligne de commande dans le terminal
- pour cela **on peut utiliser `httpie`** (ou `curl` mais c'est moins lisible)
- qui s'installe avec

  ```bash
  pip install httpie
  ```

- et qui s'utilise comme ceci

  ```bash
  # un GET
  http GET http://localhost:5000/hello
  # ou en abrégé
  http :5000/hello
  # un POST
  http POST http://localhost:5000/hello var=value
  # d'ailleurs avec une affectation de ce type le POST est automatique
  # ce qui fait que la commande suivante est équivalente
  http :5000/hello var=value
  ```

- et comme toujours, voir la doc pour plus de détails...

---

## Quelques trucs utiles (4)

### MacOS & AirPlay

- sur MacOS il y a potentiellement déjà un service qui tourne sur le port 5000
- si vous voyez ceci:

  ```bash
  $ http http://localhost:5000
  HTTP/1.1 403 Forbidden
  Content-Length: 0
  Server: AirTunes/845.5.1
  ...
  ```

  c'est que vous avez un service AirPlay qui tourne sur ce port  
  dans ce cas utilisez un autre port avec

  ```bash
  flask run --port 5001
  ```
