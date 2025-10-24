# FastAPI & templates

xxx this chapter is a WIP xxx

there are lots of pieces but all in disorder; the plan is to

- explain the difference between static and dynamic pages
- introduce templates and jinja2
- show the usual structure of a repo
- and more vaguely, talk about SSR, CSR, ISR

I lost Basile's demo, I'm not sure I need a concrete case for now

xxx WIP xxx

---

## Serving HTML pages

Now that we know how to return JSON, we'll see how to return HTML  
This is of course necessary to offer a user interface  
And let's not forget that HTML itself may require CSS/JS

And make the distinction between

- **static** files (CSS, JS, images, fonts, ...)
- **templates** (HTML files with placeholders to insert data, calculated by FastAPI code)

```{admonition} static files in production
:class: tip dropdown
For performance reasons, it's better to serve static files via a dedicated web server (typically nginx, apache, ...) - because we don't need Python for that  
That's why we separate them well from the rest
```

---
## Pages statiques vs dynamiques

Deux cas de figures :

---

## Static vs dynamic pages

Two cases:

````{div}
:class: columns

```{div}
:class: center fifty
"Static" responses  
content depending on nothing  
so the simplest actually

<iframe src="https://giphy.com/embed/Rl9Yqavfj2Ula" frameBorder="0" class="giphy-embed"></iframe>
```

```{div}
:class: center fifty
"Dynamic" responses  
content depending on external data

typically:  
product search, user profile  
obviously the most common case
```
````

It's still useful to make the distinction for performance reasons!  
It's really not useful to solicit a Python stack just to serve a CSS file!

C'est tout de même utile de faire la distinction pour des raisons de performance !  
Ce n'est vraiment pas utile de solliciter une stack Python pour juste servir un fichier CSS !

---

### Repo structure

So, this is not imposed by the framework but we usually find a repo structure like this:

`````{div}
:class: columns

````{div}
:class: fifty
```{code} bash
:label: fastapi-repo-structure
:caption: Structure usuelle d'un repo FastAPI
./
├── main.py               # FastAPI entrypoint
├── templates/            # Jinja2 (or other) templates
│   ├── base.html
│   └── users/
│       └── profile.html
├── static/               # CSS, JS, images, fonts
└── config.py             # settings
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

However, all files contained in the `static` folder will be
**automatically accessible** without us having to do anything and that's 🆒!

---

## Dynamic page: CSR vs SSR

For dynamic pages, two approaches exist

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
```{image} media/rendering-csr.excalidraw.svg
:width: 70%
```
````

---

## Approche SSR

````{div}
:class: center
```{image} media/rendering-ssr.excalidraw.svg
:width: 70%
```
````

````{div}
:class: center
Besoin d'un mécanisme de ***génération de page HTML***
````

---

## Template engine

Mechanism for generating HTML pages from a model and data.

````{div}
:class: center
```{image} media/template-engine.excalidraw.svg
:width: 40%
```
````

Several technologies/solutions:

````{div}
:class: center
***Jinja2***, **Pug**, **Mustache**, **Ejs**
````

---

## Jinja 2

Pythonic template engine 🐍

Link with Flask via the `render_template` function

```python
from flask import render_template
```

Which we use in routing functions

```python
@app.route("/")
def index():
  context = {}
  ### do something
  return render_template("templated_html.html", **context)
```

Where `context` is a Python dictionary containing the variables we want to transmit from our Flask application to the template engine.

---

### Variable substitution

To display the content of a variable in HTML, you need to surround it with double braces in HTML code.

```html
<div>Hello {{ name }}</div>
```

---

### Conditional blocks

To choose whether to display a part of the HTML page  
you can use branches of type `{% if %}` `{% else %}` `{% endif %}`  
The syntax is as follows

```html
{% if a_condition %}
<div>some html mess</div>
{% elif another_condition %}
<div>another html jumble</div>
{% else %}
<div>the default html</div>
{% endif %}
```

_Note_ Python's `None` becomes `none` in Jinja2

---

### For loops

The main interest being dynamic table display.  
`{% for %}` loops in Jinja2 allow you to iterate over any iterable Python object  
The syntax is as follows

```html
{% for x in my_list %}
<div>Iteration {{ x }}</div>
{% endfor %}
```

---

### Dictionary access

if `x` is itself a dictionary, we can access its keys/values via e.g. `x.name` or `x['name']`, the first being generally more convenient  

```html
{% for user in users %}
<div>Iteration
  {{ x.name }}
  or also
  {x['age']}
</div>
{% endfor %}
```

see `python/jinja-demo.py` for an executable example

---

### Many other things

We've skimmed over Jinja's basic features but there are lots of _advanced_ super practical things

[https://jinja.palletsprojects.com/en/3.1.x/templates/](https://jinja.palletsprojects.com/en/3.1.x/templates/)

Non-exhaustive list:

- Template composition by inheritance
  - to nest templates within each other
- Filters
  - to format data
- Macro definition
  - a bit like functions in Python

---

## CSR vs SSR summary

Two modes with advantages and disadvantages

Roughly

- CSR is cool for

````{div}
:class: center
Having pages with lots of interaction,<br><br>especially when you're more into web app than website
````

- SSR is good for

````{div}
:class: center
speeding up the initial loading of your site, if you have little user interaction,<br><br>if you want to optimize your natural search engine ranking.
````

And from a very pragmatic point of view
````{div}
:class: center
may also depend on your comfort level programming in Python or Javascript
````

