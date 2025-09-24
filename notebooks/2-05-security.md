# Sécurité et Web

## Un petit point sécurité 🔒

Quelle différence entre

````{div}
:class: center
HTTP et HTTP**S** ❓  
Oui oui c'est le **S** de **S**ecure 😓
````

Grosso modo :

````{div}
:class: center
Enrobage du protocôle HTTP dans une couche de chiffrement <br>
pour garantir la sécurité de l'utilisateur
```{image} media/https.jpg
:width: 35%
```
````

---

## HTTP un truc pas safe ?

`````{div}
:class: columns

````{div}
:class: sixty
***Alors oui le HTTP de base n'est pas sécurisé***
````

````{div}
:class: fourty
```{div}
:class: center
<iframe src="https://giphy.com/embed/1FMaabePDEfgk" height="50" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````
`````

`````{div}
:class: columns

````{div}
:class: fifty
```{div}
:class: center
<iframe src="https://giphy.com/embed/dZA4cLPCvSs1s5aCm7" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````

````{div}
:class: fifty
***Ce n'est pas très grave dans pleins de cas***  
Mais les browsers modernes commencent à être très stricts sur le sujet
````

`````

---

## Le risque du HTTP

<br>

`````{div}
:class: columns
````{div}
:class: fifty
```{image} media/http-not-safe.excalidraw.svg
:width: 100%
```
````

````{div}
:class: fifty
```{image} media/https-safe.excalidraw.svg
:width: 100%
```
````
`````

````{div}
:class: center
Le principe est donc de renfermer la requête HTTP et les informations qu'elle contient  
dans un message crypté
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

Possible de générer ses propres certificats soi-même mais ils ne sont pas considérés comme valides par les clients standard (sachant que les navigateurs web ont une liste de CA de confiance)

Les logiciels open-source utilisent majoritairement la librairie ***OpenSSL***

```{image} media/logos/openssl.svg
:width: 20%
```

<br><br>
Pour générer des certificats gratuitement il existe l'initiative **Let's Encrypt**
```{image} media/logos/lets-encrypt.svg
:width: 20%
```

```{div}
:class: smaller
en pratique, un certificat est valide pour une durée finie, de l'ordre de 1 an, il faut donc le renouveler régulièrement
```

---

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

`````{div}
:class: columns

````{div}
:class: fifty
```{image} media/cookie1.excalidraw.svg
:width: 100%
```
````

````{div}
:class: fifty
```{image} media/cookie2.excalidraw.svg
:width: 100%
```
````
`````

````{div}
:class: center
stockée sur le client (dans le navigateur) <br> et **renvoyée** au serveur à chaque nouvelle requête
````

````{div}
:class: center
```{image} media/cookie3.excalidraw.svg
:width: 40%
```
````

---

## Quel intérêt ?

Les cookies sont là pour enrichir le HTTP.

### Le problème

````{div}
:class: center
HTTP = protocole sans état
````

En gros impossible pour un serveur HTTP de savoir si deux requêtes viennent d'un même client ou pas 😵‍💫

````{div}
:class: center
Comment rester authentifié alors ?
````

---

### La solution

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

---

### Les détails scabreux

`````{div}
:class: smaller

````{div}
plus de détails ici sur MDN, notamment
  - [en termes de durée de vie, au sujet de `Expires` et `Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#removal_defining_the_lifetime_of_a_cookie)
  - [en termes de *scope* au sujet de `Domain` et `Path`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#define_where_cookies_are_sent)
  - [en termes de sécurité, au sujet de `HttpOnly` et `Secure`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#security)
````

````{admonition} et les *Third-Party Cookies* ?
:class: warning dropdown smaller

Enfin s'agissant de [`SameSite`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#controlling_third-party_cookies_with_samesite), un sujet assez épineux, celui des [*third-party cookies*](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Third-party_cookies); de quoi s'agit-il ?

  Vous allez sur `https://the-shop.com` qui vous met un cookie
  <br>
  un peu plus tard vous consultez `https://other-site.com` 
  <br>qui fait une requête **indirecte**  (e.g. un `fetch()` ou une `<img>`)
  vers `https://the-shop.com`
  <br>
  doit-on envoyer le premier cookie ?
````

`````

---

## Quelques règles à suivre

````{div}
:class: center
```{image} media/logos/cnil.svg
:width: 30%
```

<https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies>
````

- Internautes doivent être informés et donner leur consentement avant le dépôt de certains cookies
  - ❌ Traçage publicitaire / réseaux sociaux
  - ✔️ Cookie pour dire qu'on refuse les cookies [exemple](https://cpp.bmarchand.fr), panier d'achat, authentification, ...
- Recueillir le consentement
  - Bouton refusé aussi visible que celui accepté
  - Possibilité de choisir les cookies
  - Facilité de retrait du consentement

```{div}
:class: smaller
voir aussi les RGPD:
<https://www.economie.gouv.fr/entreprises/reglement-general-protection-donnees-rgpd>
```

---

## Rajoutons un Cookie dans notre serveur

````{div}
:class: center
allons dans le dossier `python/cookies` du cours
````

````{div}
faites tourner ce code sur votre ordi et cherchez les cookies dans les headers  

```{div}
:class: smaller
notez que sur Chrome, vous pouvez aussi inspecter les cookies dans le navigateur via   
`DevTools > Application > Cookies`
```

```{admonition} Vous en voyez trop ?
:class: dropdown smaller

si vous joignez le serveur sur `localhost`, vous allez peut-être en voir plein..  
enfin, beaucoup plus que ce que le serveur met lui-même  
comment se fait-il d'après vous ?

<details><summary>réponse</summary>

le cookie est - en gros - <b>attaché à un hostname</b>; donc tous les cookies qui auront été mis par un serveur que vous avez déjà joint via <code>localhost</code>, même qui n'ont rien à voir avec celui-ci, seront remis dans la requête par le browser

</details>
```
````

---

## HTTP + 🍪 suffisant pour tout faire ?

````{div}
:class: center
<br><br>

<iframe src="https://giphy.com/embed/XymaJlgorUL8vOfF88" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Mais pourquoi ?

`````{div}
:class: columns
````{div}
:class: twenty
```{image} media/timeline-http.excalidraw.svg
:width: 100%
```
````

````{div}
:class: eighty

Fonctionnement de HTTP très rigide: orienté **question/réponse**
<br>
**Impossible** pour le serveur d'être **à l'origine** de l'échange : assez limitant en fait 😮‍💨
<br><br>
oblige Patrick à tout le temps demander s'il y a du nouveau pour lui...
````
`````

`````{div}
:class: columns

````{div}
:class: fifty
```{image} media/limitation1.excalidraw.svg
:width: 100%
```
````

````{div}
:class: fifty
```{image} media/limitation2.excalidraw.svg
:width: 100%
```
````

`````

---

## Websocket

````{div}
:class: center
En 2011, révolution: arrivée de Websocket 🤯
````

`````{div}
:class: columns

````{div}
:class: sixty
<br><br>
```{div}
:class: center
connexion **bidirectionnelle** entre un client et le serveur
<br>on parle de connexion *full-duplex*
<br>permet au serveur de ***pousser*** des informations vers le client sans que ce dernier n'ait rien demandé 😲
```
son petit nom: `ws` (ou `wss` pour le sécurisé)
````

````{div}
:class: fourty center
```{image} media/timeline-ws.excalidraw.svg
:width: 80%
```
````

`````

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

`````{div}
:class: columns smaller

````{div}
:class: fifty
le protocole "ping-pong" (en fait "ping-gnip"):

- `ws-server.py` : un serveur WebSocket en Python
- `ws-client.py` : un client WebSocket en Python
- `ws-client.js` : un client WebSocket en JavaScript

ça marche mais ça n'a pas grand intérêt  
disons que ça a le mérite de montrer comment ça fonctionne
````

````{div}
:class: fifty
le protocole "countdown", même logique:

- `python ws-server2.py` pour le serveur
- `python ws-client2.py 3` va durer 3 secondes
- `node ws-client2.js 3` pareil mais en JS

cette fois c'est plus intéressant, le client **envoie au serveur un nombre de
secondes**, et le serveur répond en décomptant jusqu'à 0
```` 
`````

````{div}
:class: smaller
⚠️ Vous voyez apparaître le mot clé `await` que vous ne connaissez pas en Python 🐍  
C'est lié à la programmation asynchrone. Pour plus de détails je vous encourage à faire un tour sur le Mooc

```{div}
:class: center
*Python : des fondamentaux aux concepts avancés du langage*
```
````

---

## En pratique

### Une messagerie instantanée !

xxx dead link xxx

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

`````{div}
:class: columns

````{div}
:class: fifty center
<iframe src="https://giphy.com/embed/xTiTnBdvZgewvjTBAs" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

````{div}
:class: fifty
```{div}
:class: center
<iframe src="https://giphy.com/embed/RbSmVaVGptW03Wjw3a" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````
`````

````{div}
:class: center
Un tour d'horizon du **Framework `FastAPI`** <br>
qui va vous simplifier la vie pour tous les développements Web
````
