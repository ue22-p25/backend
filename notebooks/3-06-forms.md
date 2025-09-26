# Formulaires avec FastAPI

Un truc récurrent dans le web c'est les formulaires :

- Authentification
- Messagerie
- Interface utilisateur
- ...

<br><br>
Un besoin

````{div}
:class: center
Spécifier les champs (nom et nature/type) ; agréger les données saisies par l'utilisateur ; envoyer ces données au backend ; traiter ces données et émettre une réponse
````

Un module tout fait en Python WTForm et son interface pour Flask FlaskWTF

```bash
pip install flask-wtf
```

<div style="position: absolute; top: 22%; left: 25%">
<iframe src="https://giphy.com/embed/26FPJGjhefSJuaRhu" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>
<div style="position: absolute; top: 13%; right: 8%">
<iframe src="https://giphy.com/embed/xT5LMUv1JAxBiCft4I" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>

---

## Principes

L'utilisation de Flask-WTF se fait en définissant son propre formulaire en créant une classe héritant de la class `FlaskForm`.

```python
from flask_wtf import FlaskForm
```

Par exemple un formulaire de login pourrait s'écrire de la manière suivante :

```python
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
```

---

## Les types input

`````{div}
:class: columns
````{div}
:class: fifty
Les différents types prédéfinis dans `WTForm` sont les suivants :

- `BooleanField` : représente un booléen
- `IntegerField`
- `FloatField`
- `DecimalField`
- `SelectField` : choix parmi une liste d'option
- `DateField` : représente une date
- `FileField` : pour la sélection de fichier
- `MultipleFileField` : pour la sélection multiple
- `PasswordField` : champ pour le mot de passe (affiche des étoiles)
- `TextAreaField` : champ de saisie de texte libre
- `SubmitField` : le bouton de soumission du formulaire
````
  ````{div}
:class: fifty
Possibilité d'ajouter des "validateurs"

- `DataRequired` : champs obligatoire
- `Email` : le champs est une adresse email
- `EqualTo` : test d'égalité
- `NumberRange` : valeur numérique dans un intervalle
- `Optional` : champs optionnel

<div style="position: relative; bottom: 10%; right: 5%; transform: rotate(20deg) scale(0.6) translate(50pt, 50pt)">
<iframe src="https://giphy.com/embed/lPF1CyJXXcTZmUrP2J" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>

````
`````
---

## Utilisation en lien avec les templates

`````{div}
:class: columns smaller

````{div}
:class: fifty
```html
<html>
  <head>
    <title>Flask WTF</title>
  </head>
  <body>
    <hr />
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
      {{ form.hidden_tag() }}
      <p>
        {{ form.username.label }}<br />
        {{ form.username(size=32) }}
      </p>
      <p>
        {{ form.password.label }}<br />
        {{ form.password(size=32) }}
      </p>
      <p>{{ form.submit() }}</p>
    </form>
  </body>
</html>
```
````

````{div}
:class: fifty

La méthode `form.hidden_tag` va générer une ligne du genre :

```html
<input
  id="csrf_token"
  name="csrf_token"
  type="hidden"
  value="ImI0ODg5NjE3NzdiYjM5NWJlZWRiYzE3MDlmZjBhNjFkMDhlMjE4M2Ii.Xq_IiQ.GG9q2vWBhqbZGuGGJue2MwDIQwI"
/>
```

Aucun intérêt fonctionnel. En revanche utile pour la sécurité 🚨 et se prémunir des attaques type
<br><br>
```{div}
:class: center
**C**ross **S**ite **R**equest **F**orgery
```

Et ça demande de définir une clé secrete
 `app.config['SECRET_KEY'] = os.urandom(32))`
````

`````

---

## Données du formulaire dans les *handlers*

On peut directement réutiliser la classe `LoginForm` dans nos fonctions *handler* par exemple :

```python
@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Log in requested for {form.username.data} with password {form.password.data}")
        ## Add function here to check password

        return redirect("/home")
    return render_template("login.html", form=form)
```

`````{div}
:class: columns

````{div}
:class: sixty
Remarques
- `login.html` doit être dans un répertoire `/templates`
- son extension doit être `.html`, `.htm`, `.xml`, `.xhtml`, ou `.svg`
````

````{div}
:class: fourty center

xxx no longer working xxx

[http://bit.ly/3JyTBb2](http://bit.ly/3JyTBb2)

```{image} media/qrcode/flask_form.png
:width: 20%
```
````
`````

---

## Un petit bonus : les Cookies 🍪

`````{div}
:class: columns

````{div}
:class: fifty
```python
@app.route('/route/install/cookie')
def handler():

  resp = make_response(render_template('mapage.html'))
  resp.set_cookie('cookie', "eat me")

  return resp
```
````

````{div}
:class: fifty
```python
@app.route('/route/read/cookie')
def handler():
   name = request.cookies.get('cookieName')
   # ...
```
````
`````

Par exemple, nombre de fois qu'on visite une page !


````{div}
:class: center

xxx no longer working xxx

[http://bit.ly/408GbcF](http://bit.ly/408GbcF)

```{image} media/qrcode/flask_cookie.png
:width: 20%
```
````

---

## Un mot sur la notion de `Session`

Très souvent besoin de la notion de session utilisateur

````{div}
:class: center
Stocker des infos spécifiques à un utilisateur entre deux requêtes
````

Possible de faire ça à la main 🖖🏻 à l'aide de cookies 🍪 ...

````{div}
:class: center
mais Flask peut tout faire à votre place
````

`````{div}
:class: columns

````{div}
:class: fourty
```python
from Flask import session
```

Besoin d'un peu de config par contre

```python
app.config["SECRET_KEY"] = "un secret"
```
````

````{div}
:class: sixty

```python
@app.route("/une/url/<string:username>")
def handler( username ):
  session["name"] = username
  return "Ok j'ai enregistré"

@app.route("/")
def index():
  name = session.get("name")
  if name:
    return f"Hello {name}"
  else:
    return ("Merci de faire d'abord une requête"
            " vers /une/url/<username>")
```
````

`````

<!-- 
xxx no longer working xxx
<div class="center" style="position: absolute; top: 10%; right: 5%">

<a href="http://bit.ly/3JYyboX">http://bit.ly/3JYyboX</a>
<br>
```{image} media/qrcode/flask_session_demo.png
:width: 200px
```
</div> -->
