# Servir des pages HTML

Deux cas de figures :

- Réponses "statiques" -> contenu ne dépendant de rien donc le plus simple en fait

````{div}
:class: center fifty
<iframe src="https://giphy.com/embed/Rl9Yqavfj2Ula" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

- Réponses "dynamiques" -> contenu dépendant de données externes  
  (base de données typiquement, paramètres utilisateur... )

````{div}
:class: center
Page profil utilisateur, recherche de produits selon critères, ...
````

---

## Page dynamique : CSR vs SSR

Pour le cas de pages dynamiques deux approches existent

````{div}
:class: center
**C**lient **S**ide **R**endering
<br><br> vs <br><br>
**S**erver **S**ide **R**endering
````

````{div}
:class: center fifty
<iframe src="https://giphy.com/embed/QYMBnZjnxko0eCzBuF" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Une démo

````{div}
:class: center

xxx no longer working xxx

[http://bit.ly/3Tx8wqL](http://bit.ly/3Tx8wqL)

```{image} media/qrcode/flask_ssr_vs_csr.png
:width: 30%
```
````

Il faut être curieux et ouvrir l'onglet "Network" des outils de développement du navigateur !

---

## Approche CSR

````{div}
:class: center
```{image} media/csr.svg
:width: 70%
```
````

---

## Approche SSR

````{div}
:class: center
```{image} media/ssr.svg
:width: 70%
```
````

````{div}
:class: center
Besoin d'un mécanisme de ***génération de page HTML***
````

---

## Moteur de template

Mécanisme de génération de page HTML à partir d'un modèle et de données.

````{div}
:class: center
```{image} media/template-engine.svg
:width: 40%
```
````

Plusieurs techno/solutions :

````{div}
:class: center
***Jinja2***, **Pug**, **Mustache**, **Ejs**
````

---

## Jinja 2

Moteur de template Pythonique 🐍

Lien avec Flask via la fonction `render_template`

```python
from flask import render_template
```

Que l'on utilise dans les fonctions de routage

```python
@app.route("/")
def index():
  context = {}
  ### do something
  return render_template("templated_html.html", **context)
```

Où `context` est un dictionnaire Python contenant les variables que l'on souhaite transmettre de notre application Flask au moteur de template.

---

### subbstitution de variables

Pour afficher dans le HTML le contenu d'une variable il faut entourer cette dernière par des doubles accolades dans du code HTML.

```html
<div>Bonjour {{ name }}</div>
```

---

### Blocs conditionnels

Pour choisir d'afficher ou nom une partie de la page HTML  
vous pouvez utiliser des branchements de type `{% if %}` `{% else %}` `{% endif %}`  
La syntaxe est la suivante

```html
{% if une_condition %}
<div>du html en pagaille</div>
{% elif une_autre_condition %}
<div>un autre fouillis de html</div>
{% else %}
<div>le html par défaut</div>
{% endif %}
```

_Remarque_ le `None` de Python se transforme en `none` dans Jinja2

---

### Boucles for

L'intérêt majeur étant l'affichage dynamique de tableau.  
Les boucles `{% for %}` dans Jinja2 vous permettent d'itérer sur tout objet Python itérable  
 La syntaxe est la suivante

```html
{% for x in ma_liste %}
<div>Iteration {{ x }}</div>
{% endfor %}
```

---

### accès dans un dictionnaire

si `x` est lui même un dictionnaire, on peut accéder à ses clés/valeurs via e.g. `x.name` ou `x['name']`, le premier étant généralement plus pratique  

```html
{% for user in users %}
<div>Iteration
  {{ x.name }}
  ou encore
  {x['age']}
</div>
{% endfor %}
```

voyez `python/jinja-demo.py` pour un exemple exécutable

---

### plein d'autres choses

On a survolé les fonctionnalités de base de Jinja mais il y a plein de trucs *advance* super pratiques

[https://jinja.palletsprojects.com/en/3.1.x/templates/](https://jinja.palletsprojects.com/en/3.1.x/templates/)

Liste non exhaustive :

- Composition de template par héritage 
  - pour emboiter les templates les uns dans les autres
- Filtres 
  - pour formater les données
- Définition de macros
  - un peu comme des fonctions en Python

---

## Synthèse CSR vs SSR

Deux modes avec des avantages et inconvénients

Grosso modo

- CSR c'est cool pour

````{div}
:class: center
Avoir des pages avec beaucoup d'interaction,<br><br>notamment lorsque l'on est plus sur de l'appli web que du site web
````

- SSR c'est bien pour

````{div}
:class: center
accélérer le chargement initial de votre site, si vous avez peu d'interaction avec l'utilisateur,<br><br>si vous souhaitez optimiser votre référencement naturel dans les moteurs de recherches.
````

Et d'un point de vue très pragmatique
````{div}
:class: center
peut dépendre également du confort que vous avez à programmer en Python ou Javascript
````

