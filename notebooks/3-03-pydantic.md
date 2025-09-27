# Typer les données avec Pydantic


FastAPI s’appuie sur **Pydantic** pour gérer la validation et la sérialisation des données.  
C’est l’un des points forts du framework : vous décrivez vos données avec des classes Python annotées, et FastAPI s’occupe du reste.

---

## 1. Définir un modèle de données

Un modèle Pydantic est une classe qui hérite de `BaseModel`.  
Chaque attribut est typé avec les annotations Python standard :

```{code-block} python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # valeur par défaut
```

➡️ Ici, `id` et `name` sont obligatoires, `is_active` est optionnel avec une valeur par défaut.

---

## 2. Utiliser un modèle comme corps de requête

Dans FastAPI, si vous déclarez un paramètre de type `BaseModel`, FastAPI lira automatiquement le **JSON du corps de la requête** et vérifiera que les données correspondent.

```{code-block} python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    return {"message": f"Utilisateur {user.name} créé", "data": user}
```

### Exemple d’appel

```{code-block} bash
http POST :8000/users/ id:=1 name="Alice" email="alice@example.com"
```

✅ FastAPI transforme le JSON en un objet `User`.  
✅ Si une valeur manque ou est du mauvais type, une erreur 422 est renvoyée automatiquement.

---

## 3. Validation et transformation automatiques

Pydantic ne se contente pas de vérifier les types :  
il sait aussi **convertir** des données.

```{code-block} python
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
```

```{code-block} bash
http POST :8000/products/ name="Stylo" price="9.99" in_stock=true
```

➡️ `price="9.99"` est une chaîne, mais Pydantic la convertit en `float`.  
➡️ `in_stock=true` est converti en `bool`.

---

## 4. Validation avancée

Pydantic propose des contraintes simples :

```{code-block} python
from pydantic import BaseModel, Field

class Signup(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=18)  # ge = greater or equal
```

- `...` signifie « obligatoire ».  
- Les contraintes sont automatiquement documentées dans la doc OpenAPI.

### Exemple d’erreur

```{code-block} bash
http POST :8000/signup username="ab" password="123" age:=15
```

Réponse :

```{code-block} json
{
  "detail": [
    {"loc": ["body", "username"], "msg": "String should have at least 3 characters"},
    {"loc": ["body", "password"], "msg": "String should have at least 8 characters"},
    {"loc": ["body", "age"], "msg": "Input should be greater than or equal to 18"}
  ]
}
```

---

## 5. Modèles imbriqués

Un modèle peut contenir d’autres modèles :

```{code-block} python
class Address(BaseModel):
    city: str
    zipcode: str

class Customer(BaseModel):
    name: str
    address: Address
```

FastAPI gère la désérialisation automatiquement :

```{code-block} json
{
  "name": "Bob",
  "address": {
    "city": "Paris",
    "zipcode": "75001"
  }
}
```

---

## 6. Réponses avec Pydantic

Vous pouvez aussi déclarer le **schéma de sortie** avec `response_model` :

```{code-block} python
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return {"id": user_id, "name": "Alice", "email": "alice@example.com", "is_active": True}
```

➡️ FastAPI renverra une réponse **validée** selon `User`.  
➡️ Les champs supplémentaires (non définis) sont automatiquement exclus.  
   Utile par exemple pour ne pas exposer des données sensibles.

---

## 7. Avantages pédagogiques

- ✅ **Validation automatique** des entrées  
- ✅ **Conversion de types** (moins d’erreurs de parsing)  
- ✅ **Documentation gratuite** (Swagger/OpenAPI)  
- ✅ **Réutilisation des modèles** (entrées et sorties)  

---

# 🚀 Conclusion

Avec Pydantic, vous décrivez vos données une seule fois sous forme de classes Python.  
FastAPI se charge de :
- lire le JSON du client,  
- valider et convertir les champs,  
- produire une documentation claire,  
- garantir que vos réponses respectent le contrat.  

👉 C’est une bonne pratique d’utiliser **systématiquement des modèles Pydantic** pour vos endpoints qui consomment ou produisent des données structurées.

