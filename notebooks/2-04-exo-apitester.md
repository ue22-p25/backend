# exo: apitester

## Petite pause mise en pratique

**Objectif** : Mettre en place une API permettant d'accéder au contenu de fichier CSV

Vous avez <https://github.com/ue22-p25/backend-apitester-frontend> un frontend tout fait !  
Et vous avez <https://github.com/ue22-p25/backend-apitester-skeleton> un backend à compléter

L'API du backend doit **impérativement** respecter les routes documentées dans le README.

```{admonition} doc automatique avec FastAPI !
:class: smaller
Une fois que votre code fonctionne, allez visiter la route `/docs/` pour voir la doc interactive de votre API.
```

````{admonition} astuce pour copier les dépôts
:class: smaller tip dropdown

pour copier le contenu de ces dépôts sur votre machine, plutôt que d'utiliser `git clone`, vous pouvez utiliser ceci
```bash
# si nécessaire (npx command not found)
# conda install conda-forge::nodejs

# download le repo dans le dossier 'frontend'
npx degit git@github.com:ue22-p25/backend-apitester-frontend.git frontend
# pareil pour le backend
npx degit git@github.com:ue22-p25/backend-apitester-skeleton.git backend
```

qui a l'avantage de ne pas recréer un dépôt git dans le dossier créé; surtout si vous vous placez dans un dépôt déjà existant genre `backend-homework`  
(mais ne vous empeche pas de `git add` le résultat immédiatement)
````

---

## Tip #1: *auto-reload*

- vous remarquez que les applis FastAPI ne contiennent pas de code à exécuter directement  
  (juste des définitions de routes)
- du coup si vous lancez le fichier python avec `python mon_fichier.py`, ça ne fait rien !
- c'est pourquoi il est **indispensable** de lancer l'appli avec `fastapi dev apitester.py`
- aussi et surtout, le serveur **se relance tout seul** à chaque modification du code  

````{div}
:class: smaller
et pareil pour le frontend d'ailleurs; si vous avez l'intention d'y toucher, il est préférable de le lancer avec `vite`, comme ça il se relance tout seul à chaque modification
````

---

## Tip #2: paramètres typés

- une route peut prendre un paramètre, éventuellement typé

`````{div}
:class: columns
````{div}
:class: fifty
```python
# paramètre pas typé

@app.route('/hello/<name>')
  def hello(name):
    # ici name est une simple str
    # c'est à vous 
    # de vérifier son contenu
    return f'Hello, {name}!'
```
````

````{div}
:class: fifty
```python
# ici le paramètre est typé

@app.route('/hello/<int:id>')
  def hello(id):
    # du coup fastapi fait le
    # controle et la conversion
    # automatiquement
    return f'Hello, {id**2}!'
```
````
`````

---

## Tip #3: types de retour

pour raccourcir le code, le type de retour d'une route implique un traitement automatique  
on n'a quasiment pas besoin de convertir les objets en dict/json  
notamment si on utilise des modèles Pydantic (on en reparlera...)

| Retour de la route                   | réponse HTTP                                                                      |
|--------------------------------------|-----------------------------------------------------------------------------------|
| `dict` ou `list` ou `int` ou `float` | Encodé automatiquement en JSON.                                                   |
| `str`                                | Envoyé comme texte brut (`text/plain`)                                            |
| Pydantic `BaseModel`                 | JSON automatiquement.                                                             |
|                                      | Exemple : `return Item(name="Apple", price=1.5)` <br> → `{"name":"Apple","price":1.5}` |

---

## Tip #4: `httpie`

- c'est pratique d'avoir un vrai frontend en HTML/CSS/JS
- MAIS pour développer il est utile de tester ***aussi*** les routes en ligne de commande dans le terminal
- pour cela **on peut utiliser `httpie`** (ou `curl` mais c'est moins lisible)
- qui s'installe avec

  ```bash
  pip install httpie
  ```

- et qui s'utilise comme ceci

  ```bash
  # un GET
  http GET http://localhost:8000/hello
  # ou en abrégé
  http :8000/hello

  # un POST
  http POST http://localhost:8000/hello var=value
  # d'ailleurs avec une affectation de ce type le POST est automatique
  # ce qui fait que la commande suivante est équivalente
  http :8000/hello var=value
  ```

- et comme toujours, faire `http --help` ou voir la doc pour plus de détails...

---
