---

class: center, middle

# On sait s'orienter, comment on cause maintenant

➡️ On a besoin de la 4ème couche du modèle OSI

---

# La couche transport 🚗

La quatrième couche du modèle

> spécification de comment on fait pour envoyer des données <br>
> d'un serveur A vers un client B et inversement.

Différents protocole établis :

- TCP
- UDP
- ...

<br><br>
**⚠️ Attention ⚠️**
<br><br>
.center[
La couche transport ne fait que définir la ***manière*** dont deux applications communiquent
<br><br>
mais ne spécifie en rien le ***contenu*** de ces communications
]

---

# Un serveur == une application ?

Connaitre l'IP du serveur ne vous permet pas encore de communiquer avec l'application qui se trouve sur ce serveur
<br>

.center[❓ D'ailleurs sur un serveur il ne peut y avoir qu'une application réseau ou peut-on en mettre plusieurs ❓]

--

.cols[

.seventy-five[
On peut avoir plusieurs applications sur un même serveur, et heureusement 🥳

Le choix de l'application avec laquelle on va discuter implique la notion de **_port_**

.center[ port = porte d'entrée du service 🚪]

.center[(mais on ne fait pas tourner autant d'applications sur un serveur)]
]
.twenty-five[
<img src="media/address-ports-bound.excalidraw.svg" width="100%">
]
]

---

# Les ports standard

.cols[

.fifty[

Sur une machine on a 2<sup>16</sup> = 65,536 ports
]

.fifty[
Quelques port normalisés :

service | port
-|-
SSH | 22
SMTP | 25
DNS | 53
HTTP | 80
HTTPS | 443
... | ...
]
]

<br>

et voici à quoi ressemble un paquet:

<br>

<img src="media/packet-layers.svg" width="100%" style="margin-top: -30px">

---

# Bas niveau

## TCP/IP

.center[Transmission Control Protocol]
<br><br>
est **le** protocole historique (Bob Kahn et Vinton Cerf, Septembre 1973), qui doit sa longévité par sa robustesse et sa fiabilité.
<br>

.center[Aujourd'hui lorsque vous naviguez sur le web<br>la plupart des échanges qui ont lieu entre votre navigateur et les sites web sont basés sur du TCP]

<br>
Le principe du TCP est très simple et se décompose en trois étapes:

- établissement de la connexion
- transfert de données
- fin de la connexion

---

# Bas niveau

## TCP/IP : open

.cols[
.fourty[
<img src="media/handshake.svg" style="width: 80%">
]
.fifty[
La connexion d'un client à un serveur TCP se décompose en trois étapes

.center[___three way handshake___]

de la manière suivante :

- 1️⃣ Client : Hello le serveur tu m'entends ?
  <br><br>
- 2️⃣ Serveur : Oui je t'entends et toi ?
  <br><br>
- 3️⃣ Client : Oui c'est bon je t'entends
  <br><br>

  ]
]

---

# Bas niveau

## TCP/IP : close

.cols[
.fourty[

<img src="media/tcp-close.svg" style="width: 75%">

]
.fifty[
Clotûre en 4 étapes
<br><br>

- 1️⃣ Client : j'ai fini
  <br><br>
- 2️⃣ Serveur : Ok c'est noté
  <br><br>
- 3️⃣ Serveur : moi aussi je n'ai plus rien à te dire
  <br><br>
- 4️⃣ Client : Ok à la prochaine
  ]
  ]

---

# Regardons un peu en vrai comment ca marche

.center[
le dossier `python/tcp` du cours
<br>ou<br>
[https://replit.com/@BasileMarchand/TcpExample?v=1](https://replit.com/@BasileMarchand/TcpExample?v=1)
<br>ou<br>
[http://bit.ly/3HHQ49i](http://bit.ly/3HHQ49i)
<br>ou<br>
<img src="media/qrcode/tcp_qrcode.png" width="20%">
]

---

# Bas niveau

## TCP un truc de riche 🤑

Vous pouvez donc voir qu'avec cette approche
<br><br>
.center[
✅ la connexion est extrêmement fiable et il y a peu de chances d'avoir des loupés
]
<br><br>
En revanche cette fiabilité n'est pas gratuite 💰️
<br><br>
.center[
❌ elle s'accompagne d'un coût en terme d'échanges relativement élevé]
<br><br>
C'est pour cela qu'il existe une alternative au TCP 😯

---

# Bas niveau

## UDP

Le protocole UDP (User Datagram Protocol) est complémentaire au protocole TCP. Créé par David Reed en 1980.

Cas d'usage :

.center[Transmission rapide de données et réception de l'intégralité **pas impérative**]

.center[

TCP = très fiable mais lent

*vs*
<br>

UDP = rapide mais peu fiable
]

--

Les applications :

.center[
<img src="media/udp-applications.svg" width=60%>
]
