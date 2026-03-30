---
short_title: "code snippets index"
---
# Summary of code snippets

## 1-02-networking

- [`python/ip-address/` — `my-public-ip.py` and `my-local-ip.py` (literalinclude)](networking#my-ip-address)  
  - scripts to discover one's public and local IP addresses

## 1-03-layer4

- [`python/tcp/` (mentioned)](layer4#id-lets-see-how-it-really-works)  
  - a hands-on demo of raw TCP client/server communication

## 1-04-marshaling

- [`python/tcp-awkward-api/` (mentioned)](marshaling#id-a-concrete-example)  
  - illustrates the need for data encoding on top of raw TCP

## 1-05-http

- [`python/httpbin-client/` (mentioned)](http#id-lets-experiment)  
  - uses the `requests` library against httpbin.org to experiment with HTTP

## 1-06-epilogue

- [`python/api-random/` (mentioned)](epilogue#id-illustration)  
  - a simple API server that generates random numbers on demand

## 2-02-my-first-server

- [`python/http-servers/server1_static.py` (literalinclude)](my-first-server#id-a-bit-less-basic)  
  - a minimal static-file HTTP server written with the stdlib
- [`python/http-servers/` — other files (mentioned)](my-first-server#id-examples-made-by-hand)  
  - hand-written variants: static server from scratch, stateful POST server

## 2-05-security

- [`python/cookies/` (mentioned)](security#id-lets-add-a-cookie-to-our-server)  
  - a server that sets and reads cookies, to inspect in browser DevTools
- [`python/raw-websockets/` (mentioned)](security#id-for-example)  
  - a raw "ping-pong" WebSocket demo (server + client in Python and JS)  

## 3-02-fastapi-basics

- [`python/random-generator/` (mentioned)](fastapi-basics#id-a-random-generator-exercise)  
  - exercise: a FastAPI app with GET/POST endpoints for random numbers
- [`python/random-generator/generator.py` (mentioned)](fastapi-basics#id-on-the-fastapi-side)  
  - alternative seed endpoint using a Pydantic model

## 3-04-databases-1

- [`python/db-single-table/` (mentioned)](databases-1#id-previously)  
  - complete CRUD example with a single `User` table using SQLModel

## 3-04-databases-2

- [`python/db-relationships/user_posts.py` (mentioned)](databases-2#id-one-to-many-relationships)  
  - one-to-many example: one User has many Posts
- [`python/db-relationships/students_courses.py` (mentioned)](databases-2#id-many-to-many-relationships)  
  - many-to-many example with an association table for students/courses

## 3-05-templates-html

- [`python/jinja-demo.py` (mentioned)](templates-html#id-dictionary-access)  
  - runnable example of Jinja2 template rendering with dictionary data

## 3-06-forms

- [`python/db-single-table/users.py` (literalinclude)](forms#id-the-backend)  
  - the SQLModel `User` class used as the backend data model
- [`python/fastapi-forms/register.html` (literalinclude)](forms#id-the-form-html-element-frontend)  
  - an HTML form to register a user (name, email, active checkbox)  
- [`python/fastapi-forms/hijack-forms.js` (literalinclude)](forms#id-converting-form-data-to-json)  
  - JS snippet that intercepts form submission and sends JSON via fetch
- [`python/db-single-table`, `python/fastapi-forms` (mentioned)](forms#id-cors-breaks-the-naive-way)  
  - running backend and frontend on separate ports triggers CORS errors
- [`python/fastapi-forms/` (mentioned)](forms#id-a-workaround-vite-as-a-proxy)  
  - vite.config.js that proxies API requests to bypass CORS in dev

## 3-07-websockets

- [`python/fastapi-websockets/` (mentioned)](websockets#id-a-simple-example)  
  - shared on/off toggle demo: all connected clients see state changes in real-time
- [`python/fastapi-websockets/app.py` (literalinclude)](websockets#id-builtin-in-fastapi)  
  - the FastAPI WebSocket endpoint definition
- [`python/fastapi-websockets/index.html` (literalinclude)](websockets#id-and-builtin-in-js)  
  - the JS client that connects to the WebSocket and updates the UI
