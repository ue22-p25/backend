# Chapitre : Persister les données dans une base avec FastAPI

Dans le chapitre précédent, nous avons vu comment utiliser **Pydantic** pour valider et structurer les données entrantes et sortantes.  
Mais une API n’est pas très utile si les données disparaissent à chaque redémarrage…  
👉 Il est temps de **stocker les données dans une base**.

---

## 1. Choix de l’outil : SQLModel

Pour manipuler une base SQL avec FastAPI, le plus pratique est d’utiliser **[SQLModel](https://sqlmodel.tiangolo.com/)** :
- basé sur **SQLAlchemy** (robuste et éprouvé),
- compatible avec **Pydantic** (validation et sérialisation automatiques),
- syntaxe simple et moderne (Python + types).

Installation :

```{code-block} bash
pip install sqlmodel sqlite
```

Ici nous utiliserons **SQLite** : une base légère, parfaite pour débuter.

---

## 2. Définir un modèle de table

Un modèle SQLModel ressemble beaucoup à un modèle Pydantic, avec en plus la possibilité de décrire une table SQL.

```{code-block} python
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    is_active: bool = True
```

➡️ `table=True` indique que cette classe correspond à une table.  
➡️ `id` est une clé primaire auto-incrémentée (valeur fournie par la base).

---

## 3. Créer la base et la session

Il faut maintenant créer la base et préparer une **session** pour dialoguer avec elle.

```{code-block} python
from sqlmodel import create_engine, Session

# fichier SQLite local
database_url = "sqlite:///./test.db"
engine = create_engine(database_url, echo=True)

# création des tables
SQLModel.metadata.create_all(engine)

# fonction utilitaire pour obtenir une session
def get_session():
    with Session(engine) as session:
        yield session
```

---

## 4. Écrire des endpoints CRUD

CRUD = Create, Read, Update, Delete.  
Voici un exemple d’API simple pour gérer des `User`.

### Créer un utilisateur

```{code-block} python
from fastapi import Depends, FastAPI

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)  # recharge l’objet avec l’ID généré
    return user
```

### Lister les utilisateurs

```{code-block} python
from typing import List

@app.get("/users/", response_model=List[User])
def list_users(session: Session = Depends(get_session)):
    users = session.query(User).all()
    return users
```

---

## 5. Exemple d’utilisation

Créer un utilisateur :

```{code-block} bash
http POST :8000/users/ name="Alice" email="alice@example.com"
```

Réponse :

```{code-block} json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "is_active": true
}
```

Lister les utilisateurs :

```{code-block} bash
http :8000/users/
```

---

## 6. Avantages pédagogiques

- ✅ On manipule **une seule classe** pour la validation *et* la persistance.  
- ✅ La base conserve les données entre deux exécutions.  
- ✅ Facile d’illustrer les opérations CRUD.  

---

# 🚀 Conclusion

Avec **SQLModel**, FastAPI permet de relier facilement :
- la **validation des données** (héritée de Pydantic),
- et la **persistance en base** (via SQLAlchemy).

👉 Vous pouvez maintenant créer de vraies APIs capables de conserver et retrouver les informations dans une base SQL.  
Prochaine étape : enrichir vos modèles avec des relations (ex. `User` ↔ `Address`).
