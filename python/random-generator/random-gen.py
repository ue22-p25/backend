import random

from fastapi import FastAPI, HTTPException

app = FastAPI()


"""
http :8000/api/integer
http ":8000/api/integer?n=2&min=10&max=15"
"""

@app.get("/api/integer")
def random_integers(n: int = 3, min: int = 0, max: int = 100):
    return random.sample(range(min, max + 1), n)


"""
http :8000/api/float
http ":8000/api/float?max=10"
"""

@app.get("/api/float")
def random_floats(n: int = 3, min: float = 0, max: float = 100):
    return [random.uniform(min, max) for _ in range(n)]
