# Saving data in a database

In the previous chapter, we saw how to use **Pydantic** to validate and structure incoming and outgoing data.  
But an API is not very useful if the data disappears at each restart…  
👉 It's time to **store the data in a database**.

---

## 1. Tool choice: SQLModel

To work with an SQL database in FastAPI, the most practical option is to use **[SQLModel](https://sqlmodel.tiangolo.com/)**:

- based on **SQLAlchemy** (robust and proven),
- compatible with **Pydantic** (automatic validation and serialization),
- simple and modern syntax (Python + types).

Installation:

```{code-block} bash
pip install sqlmodel sqlite
```

Here we'll use **SQLite**: a lightweight database, perfect for getting started.

---

## 2. Define a table model

A SQLModel model looks a lot like a Pydantic model, with the added capability to describe an SQL table.

```{code-block} python
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    is_active: bool = True
```

➡️ `table=True` indicates that this class corresponds to a table.  
➡️ `id` is an auto-incremented primary key (value provided by the database).

---

## 3. Create the database and the session

Now we need to create the database and prepare a **session** to interact with it.

```{code-block} python
from sqlmodel import create_engine, Session

# local SQLite file
database_url = "sqlite:///./test.db"
engine = create_engine(database_url, echo=True)

# create tables
SQLModel.metadata.create_all(engine)

# utility function to get a session
def get_session():
    with Session(engine) as session:
        yield session
```

---

## 4. Write CRUD endpoints

CRUD = Create, Read, Update, Delete.  
Here's a simple API example to manage `User` entries.

### Create a user

```{code-block} python
from fastapi import Depends, FastAPI

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)  # reload the object with the generated ID
    return user
```

### List users

```{code-block} python
from typing import List

@app.get("/users/", response_model=List[User])
def list_users(session: Session = Depends(get_session)):
    users = session.query(User).all()
    return users
```

---

## 5. Usage example

Create a user:

---

## 5. Exemple d’utilisation

Créer un utilisateur :

```{code-block} bash
http POST :8000/users/ name="Alice" email="alice@example.com"
```

Response:

```{code-block} json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "is_active": true
}
```

List users:

```{code-block} bash
http :8000/users/
```

---

## 6. Educational advantages

- ✅ We manipulate **a single class** for both validation and persistence.  
- ✅ The database retains data between runs.  
- ✅ Easy to illustrate CRUD operations.

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

## Conclusion

With **SQLModel**, FastAPI makes it easy to connect:

- **data validation** (inherited from Pydantic),
- and **database persistence** (via SQLAlchemy).

👉 You can now create real APIs capable of storing and retrieving information in an SQL database.  
Next step: enrich your models with relationships (e.g., `User` ↔ `Address`).
