# FastAPI & DBs

````{div}
:class: center
🚀 Cours en mode express 🚀
````

Plein de choses que l'on ne peut pas voir :

````{div}
:class: center
Authentification, gestion de base de données,<br><br>sécurité des applications web, interface avec services externes, ...
````

**Quelques ressources**

```{div}
:class: center
[https://flask.palletsprojects.com/en/1.1.x/](https://flask.palletsprojects.com/en/1.1.x/)

[https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
```

---

## Juste un mot quand même sur l'aspect Base de Données

Pour faire de la base de données relationnelle simplement

````{div}
:class: center
SQLAlchemy
````

Avec une intégration Flask assez simple via `Flask-SQLAlchemy`

Après dans le cas où vous avez besoin d'une base de données `simple` pour faire de la lecture/écriture minimaliste une solution :

````{div}
:class: center
Passer par un service externe
````

Trucs à la mode : Notion ou Airtable par exemple

---

## Flask SQLAlchemy

```bash
pip install Flask-SQLAlchemy
```

````{div}
:class: center
Gestion de base de données se fait via des **modèles**
<br><br>
Dans le jargon, ça s'appelle un ORM (Object-Relationship-Model)
<br><br>
Mais vous allez voir c'est beaucoup plus simple que ce qu'on vous a dit en prépa 😅
````

````{div}
:class: smaller
il y a plein d'autres ORMs utilisables avec Flask, mais SQLAlchemy est le plus populaire
````

---

## La tables des "User"

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)

```
 
Pour initialiser et remplir la base de données

```python
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(User(username="bob", email="bob.leponge@maison-ananas.com"))
    db.session.add(User(username="patrick", email="patrick.etoile@maison-ananas.com"))

   db.session.commit()
```

---

## Interogation de la base de données

**Liste de tous les utilisateurs**

```python
@app.route("/list")
def list():
    users = User.query.all()
    output = [f"{user.username} ({user.email})" for user in users]
    return "<pre><code>" + "<br>".join(output) + "</pre></code>"
```

**Recherche d'un utilisateur**

```python
@app.route("/get/<string:username>")
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return "<h1>User not found</h1>"
    return f"<h1>{user.username} ({user.email})</h1>"
```

---

## La table des "Post"

Ajout d'une classe Post (au sens message publié, pas de rapport avec le POST de http hein)

On a besoin d'une relation entre les deux tables, puisqu'un Post est lié à un utilisateur

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="posts")
```

Du coup, besoin d'ajouter également une relation dans la classe User

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = relationship("Post", back_populates="user")
```

---

## Utilisation

```python
@app.route("/posts")
def posts():
    posts = Post.query.all()
    output = [f"{post.title} ({post.content}) from {post.user.username}" for post in posts]
    return "<pre><code>" + "<br>".join(output) + "</pre></code>"

@app.route("/post/<string:username>")
def get_posts(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return "<h1>User not found</h1>"
    posts = user.posts
    output = [f"{post.title} ({post.content})" for post in posts]
    return "<pre><code>" + "<br>".join(output) + "</pre></code>"
```

````{div}
:class: center
Ainsi toute la science occulte de la base de données relationnelle
<br><br>est cachée derrière des classes Python 🐍
````

