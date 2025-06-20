# Côté Serveur !

## Récap de la dernière fois

````{div}
:class: center
Architecture classique Client <-> Serveur avec des variations peer-to-peer, three-tier, ...
````

`````{div}
:class: columns

````{div}
:class: fifty center
```{image} media/osi-model.svg
```
````

````{div}
:class: fifty center
Un modèle OSI en 7 couches

```{image} media/ip-address.svg
:width: 40%
```
<br>

Un protocole HTTP(S) pour le web
```{image} media/http-request.svg
:class: center
```

`````

---

## Quel est le rôle du serveur ?

````{div}
:class: center
```{image} media/client-server.svg
:width: 60%
```
````

````{div}
:class: center
🥱 Attendre et attendre et attendre ... 🥱
````

Et de temps en temps 🥳 il doit traiter une requête !

---

## Serveur et serveur deux choses différentes

**_Attention_** il y a deux significations à serveur ...

````{div}
:class: center
<iframe src="https://giphy.com/embed/xU9TT471DTGJq" width="480" height="365" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

### Le serveur hardware

````{div}
:class: center
```{image} https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1634&q=80
:width: 50%
```
````

````{div}
:class: center
C'est la machine **physique ou virtuelle** connectée au réseau qui va recevoir des paquets de données mais en aucun cas ne s'occupera du traitement de ces données
````

---

### Le serveur hardware : différents types

````{div}
:class: center
Serveur physique vs serveur virtuel (VPS)
````

`````{div}
:class: columns

````{div}
:class: fifty center
```{image} media/bare-metal.svg
```
````

````{div}
:class: fifty center
```{image} media/vps.svg
```
````
`````

Différentes solutions : On Premise vs Cloud (OVH, Azure, GCP, AWS, ... )

---

## Serveur et serveur deux choses différentes

### Le serveur "software"

````{div}
:class: center
```{image} media/server-app.svg
:width: 65%
```
````

C'est l'application (au sens logiciel) qui va s'occuper de

````{div}
:class: center
**Recevoir**, **Traiter** et **Répondre** aux requètes HTTP (ou autres d'ailleurs)
````

Différentes solutions : Nginx (33%), Apache (27%), LiteSpeed (15%), Node.js(4%), IIS (4%), ...

````{div}
:class: smaller
Source : [https://w3techs.com/technologies/overview/web_server](https://w3techs.com/technologies/overview/web_server)
````

---

## Héberger plusieurs serveurs HTTP(S) sur un même serveur physique ?

````{div}
:class: center
OUI 🎯 il suffit de se partager le port 80 🤝
````

````{div}
:class: center
```{image} media/virtual-host.svg
:width: 80%
```
````

````{div}
:class: center
Il suffit de configurer au niveau du serveur HTTP des **Virtual Host**
````

---

### virtual hosts

Exemple de config nginx avec deux sites différents dans le même serveur physique


`````{div}
:class: columns

````{div}
:class: fifty center
```{image} media/servername-mines.png
:width: 40%
```
````

````{div}
:class: fifty center
```{image} media/servername-cpp.png
:width: 70%
```
````
`````

````{div}
:class: center
le "routage" entre les deux sites se fait sur la base du Header `Host:` de la requête HTTP
````

---

## Un mot sur le serverless

````{div}
:class: center
Un serveur traditionnel passe son temps à attendre ... 🥱
````

````{div}
:class: center
**_Un serverless est un serveur qui n'attend pas_**
````

Le principe est de découper le traitement en petites **tâches indépendantes** (fonctions) qui seront exécutées **à la demande**

`````{div}
:class: columns

````{div}
:class: fifty center

### Avantages

- Pas de gestion de serveur
- Pas de coût fixe
- Évolutif
````

````{div}
:class: fifty center

### Inconvénients/Difficultés

- Temps de démarrage
- Coût à l'usage
- Difficulté de débogage
- Stateless
````

`````

Coût plus faible pour les fournisseurs car ils peuvent optimiser l'utilisation des ressources

---

## Tous les serveurs font la même chose ?

**Deux applications**

````{div}
:class: center
Sites statiques vs dynamiques
````

`````{div}
:class: columns

````{div}
:class: fifty center
<iframe src="https://cpp.bmarchand.fr/controlSection.html" width="100%" height="400px" frameBorder="0"></iframe>
````
````{div}
:class: fifty center
<iframe width="100%" height="400px" src="https://xkcd.com"></iframe>
````
`````

---

### Site statique

````{div}
:class: center
Le serveur http ne fait qu'une seule et unique chose
<br>
**_lire des fichiers_** html, png, jpg, pdf, .... et **_envoyer le contenu au client_**

<br>

```{image} media/site-static.svg
:width: 90%
```

<br>voir par exemple [le site du cours C++](https://cpp.bmarchand.fr)

````

---

### Site dynamique (basique)

````{div}
:class: center
Le serveur http va devoir travailler **avec d'autres services** <br>afin de produire le résultat final pouvant être envoyé au client

```{image} media/dynamic-site1.svg
:width: 90%
```

<br>Par exemple: [un site de e-commerce moyen](https://vraimentbeau.com)
````

---

### Site dynamique (avancé)

````{div}
:class: center

Par contre l'architecture derrière un site dynamique peut être aussi très très complexe

```{image} media/cerebro.png
:width: 90%
```


<br>Par exemple: [une plateforme de développement](https://rep.minesparis.psl.eu)
````

---

## Solutions d'hébergement gratuit

`````{div}
:class: columns

````{div}
:class: fifty

### Sites statiques

- Netlify
- Vercel
- Surge
- GitHub Pages (nous y sommes !)
- readthedocs.io (nous y étions ;)
- GitLab Pages
- ...
````

````{div}
:class: fifty

### Sites dynamiques

- Glitch
- Repl.it
- PythonAnywhere
- Vercel (serverless)
- ~~Heroku~~
- ...

````
`````

````{div}
:class: center
Plein d'offres sur le marché, à vous de choisir celle qui vous convient le mieux

Attention en revanche&nbsp;: **_Gratuit_** ne veut pas dire **_sans limite_**

````

---

## Le serveur web : un besoin de perf 🚀

`````{div}
:class: columns bottom

````{div}
:class: .sixty
```{image} media/performance.svg
:width: 700px
```
````

````{div}
:class: fourty
  Comment faire pour que tout le monde

  ait une réponse en un temps raisonnable ?

````
  ⏳️
`````

---

## Solutions techniques

````{div}
:class: center
```{image} media/concurrency.svg
:width: 70%
```
````

````{div}
:class: center
Utilisation du parallélisme de tâches processus/thread et/ou programmation asynchrone
````

---

## Et au fait il répond quoi le serveur à GET ?

.columns[
.fifty[
````{div}
:class: center
```{image} media/http-request.svg
:width: 100%
```
````
]
.fifty[
````{div}
:class: center
```{image} media/response-format.svg
:width: 100%
```
````
]
]

<br><br>
Possible de voir les requêtes et réponses dans votre navigateur via
`Outils de développement > Network`

--

```{image} media/chrome-request-headers.png
:width: 40%
```

```{image} media/chrome-response-headers.png
:width: 70%
```

---

## Faisons un serveur http de base

```sh
## dans votre terminal:
## on va dans le repo du cours
cd /bla-bla-bla/backend

## pour lancer le serveur
python -m http.server
## ... à ce stade le terminal est bloqué
## pour tuer le serveur tapez "Control-C"
```

puis ouvrez dans votre navigateur `http://localhost:8000/index.html` (*)

--

.columns[

.fourty.small[
  On peut aussi écrire le serveur "à la main" en Python 🐍

  📢 ⚠️ On regarde le fichier `server1_static.py`

  ```bash
  $ cat python/http/server1_static.py
  ```
]

.sixty.small[

  ```python
  from http.server import HTTPServer, SimpleHTTPRequestHandler

  handler = SimpleHTTPRequestHandler

  print("Open this in your browser:\nhttp://localhost:9000/index.html")

  httpd = HTTPServer(('', 9000),  handler)
  httpd.serve_forever()
  ```

]

]

.footnote.small[
  (*) vous pouvez aussi le faire avec votre adresse IP - [on en a parlé ici](slides1.html#my-ip-address)
 ]

<!-- [http://bit.ly/3EeuLLo](http://bit.ly/3EeuLLo)

```{image} media/qrcode/http_server.png
:width: 20%
``` -->

---

## Traitement des requêtes

Le fonctionnement interne d'un serveur HTTP est assez simple

1. **Écouter** sur un port (80 par défaut)
2. **Accepter** une connexion
3. **Lire** la requête
4. **Traiter** la requête
5. **Envoyer** la réponse
6. **Fermer** la connexion

Le point important est la transition entre les étapes 3 et 4 qui est le coeur du serveur HTTP  
car il définit la manière dont le serveur va traiter la requête.

---

## Exemples fait à la main

📢 ⚠️ dans le dossier `python/http`, on regarde les fichiers:

- `server2_static_byhand.py`
  - en gros, mêmes fonctions: sait répondre à GET pour les fichiers statiques
  - mais écrit "à la pogne"
    <br><br>
- `server3_post_stateful.py`
  - le serveur est STATEFUL (il se souvient de l'état) - voir la variable `STATE`  
    (NB: dans la vraie vie bien sûr, l'état sera stocké dans une database SQL - ou autre)
  - le POST: les affectations var=value sont mémorisées
  - le GET: quel que soit le PATH, affiche en html le contenu des variables connues dans `STATE` (et autres détails)
    <br><br>
- `server4_template.py`
  - mêmes fonctionnalités mais avec un template JINJA2

tout cela est un peu fastidieux, c'est pourquoi on utilise des frameworks (-> slides suivants)  
mais c'est bien de comprendre comment ça marche  
à retenir tout de même: cette histoire de templates; on en reparlera

<!-- pour info, était aussi dispo sur replit ici:
[http://bit.ly/3EeuLLo](http://bit.ly/3EeuLLo)
```{image} media/qrcode/http_server.png
:width: 20%
``` -->

---

## of course il existe des frameworks pour ça&nbsp;!

---

## Les frameworks

Réponse à un besoin mais lequel ?

````{div}
:class: center
***Cadre de développement simplifié***
````

En gros un guide <strike> spirituel </strike>, permettant de développer simplement des applications spécifiques.

````{div}
:class: center
<iframe src="https://giphy.com/embed/MZW5o8f5RaH0Q" width="480" height="197" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Framework vs Librairie

````{div}
:class: center
Frameworks, Librairies, même chose ? <br>
````

--

.columns[
.fifty[
````{div}
:class: center
<b> Librairies </b>
````

Ensemble de programmes effectuant des opérations spécifiques, que vous allez utiliser de manière ponctuelle au sein de vos programmes en suivant votre propre logique.

Par exemple `NumPy` en Python 🐍 est une librairie

````{div}
:class: center
```{image} media/code-with-library.svg
```
````

]
.vertbar[]
.fifty[
````{div}
:class: center
<b> Framework </b>
````

Cadre de développement dans lequel le développeur vient s'inscrire, i.e. développer des fonctionnalités/comportements. Là ce n'est plus le développeur qui fixe sa logique mais le framework.
 
Un code à trou 🕳️ en quelque sorte

````{div}
:class: center
```{image} media/code-with-framework.svg
```
````

]
]

---

## Frontend, backend

````{div}
:class: center
⚠️ Framework web un terme très, trop, générique ⚠️
````

.columns[
.fifty[

````{div}
:class: center
Framework frontend
````

````{div}
:class: center
```{image} media/framework_frontend.png
:width: 50%
```
````

Focalisé sur le développement d'application côté client

]
.vertbar[]
.fifty[

````{div}
:class: center
Framework backend
````

````{div}
:class: center
```{image} media/framework_backend.png
:width: 100%
```
````

Focalisé sur le développement côté serveur

]
]

---

## frameworks backend: les grands principes

````{div}
:class: center
```{image} media/framework-routes.svg
:width: 70%
```
````

A cela un framework complet ajoute des fonctionnalités de :
````{div}
:class: center
`Web Template`, `Sécurité`, `Accès à des bases de données`
````

---

## Framework Flask

Micro-framework Python 🐍 développé depuis 2010.
<br><br>
````{div}
:class: center
```{image} media/logos/logo-flask.svg
:width: 30% 
```
````

<br><br>
🚧 Micro-framework ne veut pas dire "pas utilisable sur des gros projets"  ⚠️
<br><br>
````{div}
:class: center
Pinterest, Airbnb, Trivago, ...
````
<br><br>
Micro-framework car noyau très léger et minimaliste, mais pouvant être enrichi avec des extensions.

---

## Le setup de base

### Installation

```bash
pip install flask
```

--

### Minimal working example

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

```{div}
:class: center
Une fois lancé -> [http://localhost:5000](http://localhost:5000)

? C'est quoi .clignote[`@app.route('/')`] ?

```

---

## Les routes

`@app.route` est un décorateur qui permet d'associer une fonction à une URL et un type de requête HTTP.

Dans sa version complète on peut écrire :

```python
@app.route('/hello', methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    ## traitement
  elif request.method == 'GET':
    ## traitement
  else:
    return "Méthode non autorisée", 405
```

---

class: center, middle

## On a fini ...

<br><br>

--

## ... ou pas en fait

````{div}
:class: center
<iframe src="https://giphy.com/embed/3ohs7XbAurbpO5jIBy" width="480" height="267" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Petite pause mise en pratique

**Objectif** : Mettre en place une API permettant d'accéder au contenu de fichier CSV

Vous avez <https://github.com/ue22-p24/backend-apitester-frontend> un frontend tout fait !

Et vous avez <https://github.com/ue22-p24/backend-apitester-skeleton> un backend à compléter

L'api du backend doit **impérativement** respecter les routes documentées dans le README.

.footnote.small[
  **astuce**:  
  pour copier le contenu de ces dépôts sur votre machine, plutôt que d'utiliser `git clone`, vous pouvez utiliser ceci
  ```bash
  # si nécessaire (npx command not found)
  # conda install -c conda-forge nodejs
  # download le repo dans le dossier 'frontend'
  npx degit git@github.com:ue22-p24/backend-apitester-frontend.git frontend
  # pareil pour le backend
  npx degit git@github.com:ue22-p24/backend-apitester-skeleton.git backend
  ```
  qui a l'avantage de ne pas recréer un dépôt git dans le dossier créé; surtout si vous vous placez dans un dépôt déjà existant genre `backend-homework`  
  (mais ne vous empeche pas de `git add` le résultat immédiatement)
]

---

## Quelques trucs utiles (1)

### *auto-reload*

- on peut lancer l'application avec `python app.py`; ça marche...  
-  **MAIS** il faut relancer le tout à chaque modification (très sous-optimal)
-  du coup il vaut mieux activer le mode debug en lançant
  ```bash
  flask [--app mon_fichier] run --debug
  ```
  qui permet d'avoir un serveur de développement qui se relance tout seul à chaque modification du code,
  et présente en outre un avantage supplémentaire: les erreurs s'affichent dans le browser plutôt que dans le terminal  
  (notez que c'est néfaste en production, car ça peut donner des informations sensibles sur le code)

.footnote.small[
  et pareil pour le frontend d'ailleurs; si vous avez l'intention d'y toucher, il est préférable de le lancer avec `vite`, comme ça il se relance tout seul à chaque modification
]

---

## Quelques trucs utiles (2)

### les routes en Flask

- une route peut prendre un paramètre, éventuellement typé
  .columns[
  .fifty[
      ```pythona
  @app.route('/hello/<name>')
      def hello(name):
          return f'Hello, {name}!'
      ```
  ]
  .fifty[
```python
  @app.route('/hello/<int:id>')
      def hello(id):
          return f'Hello, {id**2}!'
```
  ]
  ]

- pour raccourcir le code, une route peut retourner des types variés, qui sont traités comme ceci :

  - `str` : renvoie le texte tel quel, avec un code 200
  - `tuple` : renvoie le premier élément comme texte, le deuxième comme code HTTP
  - `dict` or `list` : renvoie un JSON, avec un code 200
  -  **attention** toutefois avec les **itérateurs** car Flask les traite comme des réponses **en streaming**  
       ce qui nécessite un traitement différent dans le frontend, du coup dans
       cet exo ça ne marchera pas si une de vos routes renvoye un itérateur
  - liste non exhaustive...

---

## Quelques trucs utiles (3)

### *httpie*

- c'est pratique d'avoir un vrai frontend en html/css/js
- MAIS pour développer il peut être utile de tester AUSSI les routes en ligne de commande dans le terminal
- pour cela **on peut utiliser `httpie`** (ou `curl` mais c'est moins lisible)
- qui s'installe avec

  ```bash
  pip install httpie
  ```

- et qui s'utilise comme ceci

  ```bash
  # un GET
  http GET http://localhost:5000/hello
  # ou en abrégé
  http :5000/hello
  # un POST
  http POST http://localhost:5000/hello var=value
  # d'ailleurs avec une affectation de ce type le POST est automatique
  # ce qui fait que la commande suivante est équivalente
  http :5000/hello var=value
  ```

- et comme toujours, voir la doc pour plus de détails...

---

## Quelques trucs utiles (4)

### MacOS & AirPlay

- sur MacOS il y a potentiellement déjà un service qui tourne sur le port 5000
- si vous voyez ceci:

  ```bash
  $ http http://localhost:5000
  HTTP/1.1 403 Forbidden
  Content-Length: 0
  Server: AirTunes/845.5.1
  ...
  ```

  c'est que vous avez un service AirPlay qui tourne sur ce port  
  dans ce cas utilisez un autre port avec

  ```bash
  flask run --port 5001
  ```

---

## Un petit point sécurité 🔒

Quelle différence entre

````{div}
:class: center
HTTP et HTTP**S**  
❓
````

--

````{div}
:class: center
Oui oui c'est le **S** de **S**ecure 😓
````

Grosso modo :

````{div}
:class: center
Enrobage du protocôle HTTP dans une couche de chiffrement <br><br>
pour garantir la sécurité de l'utilisateur
````

````{div}
:class: center
```{image} media/https.jpg
:width: 35%
```
````

---

## HTTP un truc pas safe ?

.columns[
.fifty[
***Alors oui le HTTP de base n'est pas sécurisé***
]
.fifty[
````{div}
:class: center
<iframe src="https://giphy.com/embed/1FMaabePDEfgk" width="200" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````
]
]

--

.columns[
.fifty[
````{div}
:class: center
<iframe src="https://giphy.com/embed/dZA4cLPCvSs1s5aCm7" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````
  ]
  .fifty[
    ***Mais ce n'est pas très grave dans pleins de cas***
]
]

---

## Le risque du HTTP

<br>

.columns[
.fifty[
```{image} media/http-not-safe.svg
:width: 100%
```
]
.fifty[

```{image} media/https-safe.svg
:width: 100%
```

]
]

````{div}
:class: center
Le principe est donc de renfermer la requête HTTP et les informations qu'elle contient <br><br> dans un message crypté
````

---

## Principes de chiffrement

En pratique le chiffrement fonctionne avec un système clé publique/clé privée

````{div}
:class: center
```{image} media/timeline-tls.excalidraw.svg
```
````

---

## Autorité de certification (CA)

````{div}
:class: center
**Tiers de confiance** <br>qui va générer les certificats permettant le chiffrement et l'authentification de l'identité des correspondants
````

<br>
Possible de générer ses propres certificat soi-même mais ils ne sont pas considérés comme valides par les clients standard (sachant que les navigateurs web ont une liste de CA de confiance)

<br>
Les logiciels open-source utilisent majoritairement la librairie ***OpenSSL***
```{image} media/logos/openssl.svg
:width: 20%
```

<br>
Pour générer des certificats gratuitement il existe l'initiative **Let's Encrypt**
```{image} media/logos/lets-encrypt.svg
:width: 30%
```

.footnote.small[
  en pratique, un certificat est valide pour une durée finie, de l'ordre de 1 an, il faut donc le renouveler régulièrement
]
---

class: center, middle

## Et maintenant c'est fini ?

````{div}
:class: center
<iframe src="https://giphy.com/embed/I1nwVpCaB4k36" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Les cookies 🍪

Faisons une pause goûter 🤤

````{div}
:class: center
<iframe src="https://giphy.com/embed/3o6MbitgftpbGFP3B6" width="480" height="362" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

````{div}
:class: center
Ça fait partie de ces petites choses ***cachées*** dans les headers HTTP
````

---

## Concrètement c'est quoi ?

 ````{div}
:class: center
Un 🍪 HTTP c'est une donnée qu’un serveur envoie à un client
````

.columns[
.fifty[
```{image} media/cookie1.svg
:width: 100%
```
]
.fifty[
```{image} media/cookie2.svg
:width: 100%
```
]
]

````{div}
:class: center
stockée sur le client (dans le navigateur) <br> et **renvoyée** au serveur à chaque nouvelle requête
````

````{div}
:class: center
```{image} media/cookie3.svg
:width: 40%
```
````

---

## Quel intérêt ?

Les cookies sont là pour enrichir le HTTP.

***Le problème***

````{div}
:class: center
HTTP = protocole sans état
````

En gros impossible pour un serveur HTTP de savoir si deux requêtes viennent d'un même client ou pas 😵‍💫

````{div}
:class: center
Comment rester authentifié alors ?
````

**_La solution_**

````{div}
:class: center
Les cookies 🍪 parce que ça laisse des miettes
````

Concrètement on va pouvoir stocker :

````{div}
:class: center
Un session ID, des préférences utilisateur (light/dark theme, langue, ...)
````

---

## Mettre des cookies

Rien de plus simple, dans l'en-tête de la réponse serveur il suffit d'ajouter
<br>
````{div}
:class: center
`Set-Cookie: <name>=<value>; <attributs...>`
````

Attributs de Cookie

- `Expires` : durée de vie (date/heure)
- `Max-Age` : durée de vie (seconde)
- `Domain` : noms de domaine pour lesquels le cookie est renvoyé
- `Path` : chemin particulier pour lesquels le cookie est renvoyé
- `Secure` : si défini, on n'envoie le cookie que sur https, et pas http
- `HttpOnly` : si défini, on ne peut pas accéder au cookie via JavaScript
- `SameSite` : définit si on envoie le cookie dans les *cross-site requests*

Par exemple, allez sur <https://www.mat.minesparis.psl.eu> et trouvez le cookie `PHPSESSID`

.columns[

.fourty.small[
  plus de détails ici sur MDN, notamment
  - [en termes de durée de vie, au sujet de `Expires` et `Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#removal_defining_the_lifetime_of_a_cookie)
  - [en termes de *scope* au sujet de `Domain` et `Path`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#define_where_cookies_are_sent)
  - [en termes de sécurité, au sujet de `HttpOnly` et `Secure`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#security)
]

.sixty.small[
  <br>Enfin [`SameSite`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#controlling_third-party_cookies_with_samesite), un sujet assez épineux, celui des [*third-party cookies*](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Third-party_cookies); de quoi s'agit-il ?

  Vous allez sur `https://the-shop.com` qui vous met un cookie
  <br>
  un peu plus tard vous consultez `https://other-site.com` 
  <br>qui fait une requête **indirecte**  (e.g. un `fetch()` ou une `<img>`)
  vers `https://the-shop.com`
  <br>
  doit-on envoyer le premier cookie ?
]
]

---

## Quelques règles à suivre

````{div}
:class: center
```{image} media/logos/cnil.svg
:width: 30%
```
````

````{div}
:class: center
<https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies>
````

- Internautes doivent être informés et donner leur consentement avant le dépôt de certains cookies
  - ❌ Traçage publicitaire / réseaux sociaux
  - ✔️ Cookie pour dire qu'on refuse les cookies [exemple](https://cpp.bmarchand.fr), panier d'achat, authentification, ...
- Recueillir le consentement
  - Bouton refusé aussi visible que celui accepté
  - Possibilité de choisir les cookies
  - Facilité de retrait du consentement

.footnote.small[voir aussi les RGPD:
<https://www.economie.gouv.fr/entreprises/reglement-general-protection-donnees-rgpd>
]

---

## Rajoutons un Cookie dans notre serveur

```{div}
:class: center
le dossier `python/http-cookie` du cours
<br>ou<br>
[http://bit.ly/410qbdD](http://bit.ly/410qbdD)
<br>ou<br>
```{image} media/qrcode/cookie.png
:width: 20%
```
```

.footnote.small[
  faites tourner ce code sur votre ordi et cherchez les cookies dans les headers  
  si vous joignez le serveur sur `localhost`, vous allez peut-être en voir plein..
  comment se fait-il d'après vous ?

  <details><summary>réponse</summary>

  le cookie est - en gros - <b>attaché à un hostname</b>; donc tous les cookies qui auront été mis par un serveur que vous avez déjà joint via <code>localhost</code>, même qui n'ont rien à voir avec celui-ci, seront remis dans la requête par le browser

  </details>

  enfin sur Chrome, vous pouvez aussi inspecter les cookies dans le navigateur via `DevTools > Application > Cookies`
]
---

## HTTP + 🍪 suffisant pour tout faire ?

````{div}
:class: center
<br><br>

<iframe src="https://giphy.com/embed/XymaJlgorUL8vOfF88" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Mais pourquoi ?

.columns[

.twenty[
```{image} media/timeline-http.svg
:width: 100%
```
]

.eighty[

    <br><br>

Fonctionnement de HTTP très rigide: orienté **question/réponse**
<br>
**Impossible** pour le serveur d'être **à l'origine** de l'échange : assez limitant en fait 😮‍💨
<br><br>
oblige Patrick à tout le temps demander s'il y a du nouveau pour lui...

.columns[
.fifty[
```{image} media/limitation1.svg
:width: 100%
```
]
.fifty[
```{image} media/limitation2.svg
:width: 100%
```
]
]

]

]

---

## Websocket

````{div}
:class: center
En 2011, révolution: arrivée de Websocket 🤯
````

.columns[
.sixty[
<br><br>
````{div}
:class: center
connexion **bidirectionnelle** entre un client et le serveur
<br><br>on parle de connexion *full-duplex*
<br><br>permet au serveur de ***pousser*** des informations vers le client sans que ce dernier n'ait rien demandé 😲
````
son petit nom: `ws` (ou `wss` pour le sécurisé)
]
.fourty[
````{div}
:class: center
```{image} media/timeline-ws.svg
:width: 70%
```
````
]
]

---

## Comment ça marche

Très simplement en fait !

````{div}
:class: center
Première étape on établit une connexion vers un serveur WebSocket <br> via <br>
`ws://mon-super-server.com` ou `wss://mon-super-server.com`
````

````{div}
:class: center
Une fois la connexion établie <br><br>On doit simplement se mettre en état d'écoute à des évènements particuliers
````

Quatre types d'évènements

````{div}
:class: center
`onopen` 📖, `onclose` 📕, `onerror` 🚨, `onmessage` 📥
````

Et à chaque évènement on va venir associer une action

---

## Par exemple&nbsp;:

Voyez dans le dossier `python/websockets`:

.columns[
.fifty[

le protocole "ping-pong" (en fait "ping-gnip"):

- `ws-server.py` : un serveur WebSocket en Python
- `ws-client.py` : un client WebSocket en Python
- `ws-client.js` : un client WebSocket en JavaScript

ça marche mais ça n'a pas grand intérêt  
disons que ça a le mérite de montrer comment ça fonctionne
]

.fifty[
le protocole "countdown", même logique:

- `python ws-server2.py` pour le serveur
- `python ws-client2.py 3` va durer 3 secondes
- `node ws-client2.js 3` pareil mais en JS

cette fois c'est plus intéressant, le client **envoie au serveur un nombre de
secondes**, et le serveur répond en décomptant jusqu'à 0 ] ]


.footnote[
⚠️ Vous voyez apparaître le mot clé `await` que vous ne connaissez pas en Python 🐍

C'est lié à la programmation asynchrone. Pour plus de détails je vous encourage à faire un tour sur le Mooc

````{div}
:class: center
*Python : des fondamentaux aux concepts avancés du langage*
````
]

---

## En pratique

### Une messagerie instantanée !

```{div}
:class: center
[http://bit.ly/3xu599H](http://bit.ly/3xu599H)
```

````{div}
:class: center
```{image} media/qrcode/tornado.png
:width: 20%
```
````

---

## In the next episode

.columns[
.fifty[
````{div}
:class: center
<iframe src="https://giphy.com/embed/xTiTnBdvZgewvjTBAs" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````
]
.fifty[
````{div}
:class: center
<iframe src="https://giphy.com/embed/RbSmVaVGptW03Wjw3a" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````
]
]

````{div}
:class: center
Un tour d'horizon du **Framework `Flask`** <br>
qui va vous simplifier la vie pour tous les développements Web
````
