# Typing data with Pydantic

FastAPI relies on **Pydantic** to handle data validation and serialization.  
This is one of the framework's strengths: you describe your data with annotated Python classes, and FastAPI takes care of the rest.

---

## 1. Define a data model

A Pydantic model is a class that inherits from `BaseModel`.  
Each attribute is typed with standard Python annotations:

```{code-block} python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # default value
```

➡️ Here, `id` and `name` are required, `is_active` is optional with a default value.

---

## 2. Use a model as request body

In FastAPI, if you declare a parameter of type `BaseModel`, FastAPI will automatically read the **JSON from the request body** and verify that the data matches.

```{code-block} python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created", "data": user}
```

### Call example

```{code-block} bash
http POST :8000/users/ id:=1 name="Alice" email="alice@example.com"
```

✅ FastAPI transforms the JSON into a `User` object.  
✅ If a value is missing or of the wrong type, a 422 error is returned automatically.

---

## 3. Automatic validation and transformation

Pydantic doesn't just check types:  
it also knows how to **convert** data.

```{code-block} python
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
```

```{code-block} bash
http POST :8000/products/ name="Pen" price="9.99" in_stock=true
```

➡️ `price="9.99"` is a string, but Pydantic converts it to `float`.  
➡️ `in_stock=true` is converted to `bool`.

---

## 4. Advanced validation

Pydantic offers simple constraints:

```{code-block} python
from pydantic import BaseModel, Field

class Signup(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=18)  # ge = greater or equal
```

- `...` means "required".  
- Constraints are automatically documented in the OpenAPI doc.

### Error example

```{code-block} bash
http POST :8000/signup username="ab" password="123" age:=15
```

Response:

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

## 5. Nested models

A model can contain other models:

```{code-block} python
class Address(BaseModel):
    city: str
    zipcode: str

class Customer(BaseModel):
    name: str
    address: Address
```

FastAPI handles deserialization automatically:

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

## 6. Responses with Pydantic

You can also declare the **output schema** with `response_model`:

```{code-block} python
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return {"id": user_id, "name": "Alice", "email": "alice@example.com", "is_active": True}
```

➡️ FastAPI will return a **validated** response according to `User`.  
➡️ Additional fields (not defined) are automatically excluded.  
   Useful for example to avoid exposing sensitive data.

---

## 7. Educational advantages

- ✅ **Automatic validation** of inputs  
- ✅ **Type conversion** (fewer parsing errors)  
- ✅ **Free documentation** (Swagger/OpenAPI)  
- ✅ **Model reuse** (inputs and outputs)

---

## Conclusion

With Pydantic, you describe your data once in the form of Python classes.  
FastAPI takes care of:

- reading the JSON from the client,  
- validating and converting fields,  
- producing clear documentation,  
- ensuring your responses respect the contract.  

👉 It's good practice to **systematically use Pydantic models** for your endpoints that consume or produce structured data.

