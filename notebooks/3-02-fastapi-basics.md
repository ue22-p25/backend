# FastAPI - the basics

Python micro-framework 🐍 - fairly recent (2018);  
occupies the same space as

- Flask - developed since 2010 - lightweight and extensible
- Django - developed since 2003 - perceived as more complete but also heavier

🚧 Micro-framework doesn't mean not usable on large projects ⚠️  

```{image} media/logos/logo-fastapi.svg
:width: 20%
```

---

## FastAPI

similar on the surface to Flask, but **much more modern**!

- encourages a more structured approach
  - leverages **type information** (type annotations / pydantic)
  - especially for data validation / conversion
  - you can define separate models for creation, reading, updating, etc.  
    useful for example for password hashing (not exposed)
- in particular, automatically generates **interactive documentation**
- has native support for asynchronous programming
- as well as for websockets

---

## Why FastAPI and not something else

1️⃣ You all more or less know how to do Python 🐍

````{div}
:class: center
so we eliminate everything that's not Python-based
````

2️⃣ We'll try to teach you things used elsewhere  
And the FastAPI trend indeed seems to be experiencing spectacular growth!

````{div}
:class: center

```{figure} media/web-framework-survey.png
:class: smaller
:width: 85%
Source: <a href="https://www.jetbrains.com/lp/devecosystem-2023/python/">https://www.jetbrains.com/lp/devecosystem-2023/python/</a>
```

````

---

## Graphical User Interface

But actually... why are we interested in this?  
The GUI is what bridges 🌉 between:

````{div}
:class: center
a calculation/data processing code/...  
and a graphical interface  
so very relevant for the "Computer Science Projects" at the end of S2
````

Two approaches:

`````{div}
:class: columns

````{div}
:class: fifty center
***Old school***  
Using graphical libraries and developing a thick client

```{image} media/old-school.excalidraw.svg
:width: 50%
:align: center
```
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
***New age***

Using the browser

```{image} media/new-age.excalidraw.svg
```
````

`````

---

## FastAPI: we already know a bit

```{div}
:class: center
we already vaguely know how to use it, remember, we've already seen  
[how to install FastAPI](label-fastapi-install)  
and  
[how to make a minimal server with FastAPI](label-exo-apitester)

notice how simple it is to get started 😯  
this is an advantage of Flask/FastAPI compared to Django  
which requires a more advanced setup to start a project
```

---

### Quick recap

`````{div}
:class: columns

````{div}
:class: fifty
- Step 1️⃣:

```python
from fastapi import FastAPI
```
````

````{div}
:class: fifty
- Step 2️⃣

```python
app = FastAPI()
```
````
`````

Then we attach Python functions to URL paths  
we call these functions *route handlers* or *router functions*

```python
@app.get("/a/path/target")
def the_corresponding_function():
  // does very smart things
  return a_result    # which can be data or html or ...
```

---
### And to start the server?


`````{div}
:class: columns

````{div}
:class: fifty
from the terminal
```{code} bash
:caption: the server in development mode
fastapi dev my_app.py
```
```{code} bash
:caption: or on another port
fastapi dev my_app.py --port 8080
```
````


````{div}
:class: fifty
or also
```{code} bash
:caption: in production mode
fastapi run my_app.py
```

````

`````

<!-- ---

### Pour ceux qui auraient la flemme !

`````{div}
:class: columns

````{div}
:class: sixty
```{div}
:class: center
<iframe src="https://giphy.com/embed/4KkSbPnZ5Skec" width="471" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````

````{div}
:class: fourty center

xxx no longer working xxx

[http://bit.ly/3Z5C5k7](http://bit.ly/3Z5C5k7)

```{image} media/qrcode/flask_sandbox.png
:width: 60%
```
````
`````
 -->
---

## Parameters in a GET

````{div}
:class: center

We can write slightly more sophisticated URLs:  

```{image} media/http-get-arguments.excalidraw.svg
:width: 80%
```

Need to **retrieve the arguments** in the *handler* function 🤔
````

<br>


````{div}
:class: center
FastAPI has it all figured out
````

`````{div}
:class: columns

````{div}
:class: fifty
```python
@app.get("/some/route/data")
def get_parameters(
        name: str,
        age: int):
    return {'name': name, 'age': age}
````

````{div}
:class: fifty
you just need to declare the parameters  
with their type  
and FastAPI does the rest  
and even type conversion

````
`````

````{div}
:class: center
🚧 No notion of type in network exchanges, everything is a string 🚧
````

---

## Parametric URL

Possibility offered by Flask to define parameters within a URL itself

````{div}
:class: center
```{image} media/fastapi-route-param.excalidraw.svg
```
````

`````{div}
:class: columns

````{div}
:class: fifty-five smaller
Special case for `/`

- by default a parameter does not contain a slash `/`
- **but** in a route you can declare  
  `"/my/route/{parameter:path}"`  

  to allow slashes `\` in the parameter
````
````{div}
:class: fourty-five
```python
@app.get("/my/route/{parameter}")
def url_parameter(parameter: int):
    return {"square": parameter**2}
```
```{div}
:class: tiny
and of course you can also receive multiple parameters this way
```
````
`````

---

## A random generator (exercise)

`````{div}
:class: columns

````{div}
:class: fifty

**in `python/random-generator.py`**
- read the code
- start the server
````

````{div}
:class: fifty

Random number generation API

- `/api/integer`: generates integers
- `/api/float`: generates floats

````

`````

````{div}
:class: center

from the browser - or the terminal with httpie - query the *endpoint* `/api/integer`
````

```{code} bash
# don't hesitate to also see what it gives with the -v option
# which will ALSO show you the request sent
http :8000/api/integer
```

```{exercise}
:label: exo-random-one

- how to generate 4 floating point numbers between 10 and 50?  
  here again think about the interactive documentation
```

```{exercise}
:label: exo-random-two

- what happens if we pass a max smaller than the min?  
  how could we handle that?
```
---

## Exercise solutions

````{solution} exo-random-one
:class: dropdown

- in the browser:  
  `http://localhost:8000/api/float?min=10&max=50&count=4`

- it's important to **understand how *`http`* works well**  
  with httpie, it's simpler:
  ```{code} bash
  :linenos:
  :emphasize-lines: 7

  # long version - watch out for quotes!
  # because of the & which is a special character in bash
  http ":8000/api/float?min=10&max=50&count=4"

  # short version, to pass parameters with GET
  # you must use ==
  http :8000/api/float min==10 max==50 count==4

  # warning the simple = is for POST requests!
  # if we use = it doesn't do what we want!
  # DON'T DO IT LIKE THIS!
  # http GET :8000/api/float min=10 max=50 count=4

  ```
````

````{solution} exo-random-two
:class: dropdown

as it stands, there is no control on the parameters, so the server calls the `random.uniform` function with invalid parameters and that generates a 500 error

to address this, several choices are possible:

- either we add a check in the `random_floats` function to verify that `min < max` and if not we raise an HTTP 400 (Bad Request) exception
- or we use Pydantic's validation features; but for now that's premature since we haven't seen Pydantic yet 😉

so for now we'll settle for the 1st solution

```{code} python
:linenos:
:emphasize-lines: 5

from fastapi import HTTPException

def random_floats(min: float, max: float) -> float:
    if min >= max:
        raise HTTPException(status_code=400, detail="Invalid range")
    return random.uniform(min, max)
````

---

## HTTP verbs

Quick reminder from the 1st episode, HTTP different possible requests

- `GET`: requests to **obtain** a resource from the server (html/css/js file, image, video, data, ...)
- `POST`: requests to **send** data to the server for processing (adding a user to a database, ...)
- `PATCH`: requests to **partially modify** a server resource (updating a user's email address in the database)
- `DELETE`: requests to **delete** a server resource (deleting a comment on an article, ... )

These are the main types of requests but there are others, for the complete list you can check here: [https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol).

---

## Parameters in a POST

```{admonition} seen above: GET parameters are in the URL
:class: tip dropdown admonition-smaller

like `/my/route?param1=val1&param2=val2`  
and for info the HTTP protocol doesn't provide for putting parameters in the body of a GET request, if you do it anyway the behavior is undefined
```

however for POST, PATCH, DELETE requests, ...  
the parameters are passed in the **body** of the request

Let's look at an example

---

### the POST request

And to start let's look at what is sent by `httpie` when we do a POST

````{admonition} the body of a POST request
:class: dropdown

Here it is

```{code} bash
:linenos:
:emphasize-lines: 2,11-13

❯ http -v :8000/api/seed seed_value:=42
POST /api/seed HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
Host: localhost:8000
User-Agent: HTTPie/3.2.4

{
    "seed_value": 42
}
```
````

As we can see, the parameters are sent **in JSON format**  
in the *Body* of the request - i.e. after the *headers*  

**Remember this well, it's important!**  
This is the process we'll need to use when we want to send data to the server (and especially when it's the frontend sending the request via JS)

---

### on the FastAPI side

Here now is the FastAPI code that works well to handle this request

```{code} python
:linenos:
:emphasize-lines: 5

from fastapi import Body

@app.post("/api/seed")
# with Body() we indicate that the parameter comes from the request body
def set_seed(seed_value: int=Body(..., embed=True)):
    random.seed(seed_value)
    return {"message": f"Seed set to {seed_value}"}
```

```{admonition} it's simpler with Pydantic
:class: tip dropdown
we'll see this later, but if we use a Pydantic model to define the parameters, it's even simpler...
```

---

## What's next

At this point you know how to implement FastAPI *endpoints* that handle
GET and POST requests with parameters

We have many other things to see, including:

- how FastAPI leverages type annotations to do automatic validation
- how to return HTML rather than simple data
- and a few other tips & tricks

We'll see that in the following episodes...
