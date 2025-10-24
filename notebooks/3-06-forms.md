# Forms with FastAPI

xxx WIP xxx

for now this is the raw Flask text, to be updated for FastAPI

xxx WIP xxx

---

A recurring thing in web development is forms:

- Authentication
- Messaging
- User interface
- ...

<br><br>

A need

````{div}
:class: center
Specify the fields (name and nature/type); aggregate data entered by the user; send this data to the backend; process this data and emit a response
````

A ready-made Python module WTForm and its interface for Flask FlaskWTF

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

## Principles

Using Flask-WTF is done by defining your own form by creating a class inheriting from the `FlaskForm` class.

```python
from flask_wtf import FlaskForm
```

For example, a login form could be written as follows:

```python
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
```

---

## Input types

`````{div}
:class: columns
````{div}
:class: fifty
The different predefined types in `WTForm` are as follows:

- `BooleanField`: represents a boolean
- `IntegerField`
- `FloatField`
- `DecimalField`
- `SelectField`: choice from a list of options
- `DateField`: represents a date
- `FileField`: for file selection
- `MultipleFileField`: for multiple selection
- `PasswordField`: field for password (displays stars)
- `TextAreaField`: free text input field
- `SubmitField`: the form submission button
````
  ````{div}
:class: fifty
Possibility to add "validators"

- `DataRequired`: required field
- `Email`: the field is an email address
- `EqualTo`: equality test
- `NumberRange`: numeric value in a range
- `Optional`: optional field

<div style="position: relative; bottom: 10%; right: 5%; transform: rotate(20deg) scale(0.6) translate(50pt, 50pt)">
<iframe src="https://giphy.com/embed/lPF1CyJXXcTZmUrP2J" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>

````
`````
---

## Using with templates

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

The `form.hidden_tag` method will generate a line like:

```html
<input
  id="csrf_token"
  name="csrf_token"
  type="hidden"
  value="ImI0ODg5NjE3NzdiYjM5NWJlZWRiYzE3MDlmZjBhNjFkMDhlMjE4M2Ii.Xq_IiQ.GG9q2vWBhqbZGuGGJue2MwDIQwI"
/>
```

No functional interest. However useful for security 🚨 and to protect against attacks like
<br><br>

```{div}
:class: center
**C**ross **S**ite **R**equest **F**orgery
```

And this requires defining a secret key
 `app.config['SECRET_KEY'] = os.urandom(32))`
````

`````

---

## Form data in the *handlers*

We can directly reuse the `LoginForm` class in our *handler* functions, for example:

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
Notes

- `login.html` must be in a `/templates` directory
- its extension must be `.html`, `.htm`, `.xml`, `.xhtml`, or `.svg`
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

## A little bonus: Cookies 🍪

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

For example, number of times we visit a page!


````{div}
:class: center

xxx no longer working xxx

[http://bit.ly/408GbcF](http://bit.ly/408GbcF)

```{image} media/qrcode/flask_cookie.png
:width: 20%
```
````

---

## A word on the `Session` concept

Very often need the concept of a user session

````{div}
:class: center
Store user-specific information between two requests
````

Possible to do this manually 🖖🏻 using cookies 🍪 ...

````{div}
:class: center
but Flask can do it all for you
````

`````{div}
:class: columns

````{div}
:class: fourty
```python
from Flask import session
```

Need a bit of config though

```python
app.config["SECRET_KEY"] = "a secret"
```
````

````{div}
:class: sixty

```python
@app.route("/une/url/<string:username>")
def handler( username ):
  session["name"] = username
  return "Ok I saved it"

@app.route("/")
def index():
  name = session.get("name")
  if name:
    return f"Hello {name}"
  else:
    return ("Please first make a request"
            " to /une/url/<username>")
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
