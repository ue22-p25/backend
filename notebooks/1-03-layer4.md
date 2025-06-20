# La couche transport 🚗

> On sait s'orienter, comment on cause maintenant
>
> ➡️ On a besoin de la 4ème couche du modèle OSI

---

## La couche 4

> spécification de comment on fait pour envoyer des données <br>
> d'un serveur A vers un client B et inversement.

`````{div}
:class: columns

````{div}
:class: thirty
Différents protocoles établis&nbsp;:

- TCP
- UDP
- ...

````
````{div}
:class: seventy
**⚠️ Attention ⚠️**
````{div}
:class: center
La couche transport ne fait que définir la ***manière*** dont deux applications communiquent
<br>
mais ne spécifie en rien le ***contenu*** de ces communications
````
`````

---

## Un serveur == une application ?

Connaitre l'IP du serveur ne vous permet pas encore de communiquer avec l'application qui se trouve sur ce serveur
<br>

````{div}
:class: center
❓ D'ailleurs sur un serveur il ne peut y avoir qu'une application réseau ou peut-on en mettre plusieurs ❓
````

`````{div}
:class: columns

````{div}
:class: seventy-five
On peut avoir plusieurs applications sur un même serveur, et heureusement 🥳

Le choix de l'application avec laquelle on va discuter implique la notion de **_port_**

```{div}
:class: center
port = porte d'entrée du service 🚪
```

```{div}
:class: center
(mais on ne fait pas tourner autant d'applications sur un serveur)
```
````

````{div}
:class: twenty-five
```{image} media/address-ports-bound.excalidraw.svg
```
````

`````

---

## Les ports standard

`````{div}
:class: columns

````{div}
:class: fifty

Sur une machine on a 2<sup>16</sup> = 65,536 ports
````

````{div}
:class: fifty
Quelques port normalisés :

service | port
-|-
SSH | 22
SMTP | 25
DNS | 53
HTTP | 80
HTTPS | 443
... | ...
````
`````

<br>

et voici à quoi ressemble un paquet:

<br>

```{image} media/packet-layers.svg
```

---

## TCP/IP

### Principe

````{div}
:class: center
**T**ransmission **C**ontrol **P**rotocol
````

est **le** protocole historique (Bob Kahn et Vinton Cerf, Septembre 1973), qui doit sa longévité par sa robustesse et sa fiabilité.

````{div}
:class: center
Aujourd'hui lorsque vous naviguez sur le web<br>la plupart des échanges qui ont lieu entre votre navigateur et les sites web sont basés sur du TCP
````

<br>
Le principe du TCP est très simple et se décompose en trois étapes:

- établissement de la connexion
- transfert de données
- fin de la connexion

---

### TCP/IP : open

`````{div}
:class: columns

````{div}
:class: fourty
```{image} media/handshake.svg
```
````

````{div}
:class: sixty
La connexion d'un client à un serveur TCP se décompose en trois étapes

```{div}
:class: center
___three way handshake___
```

de la manière suivante :

- 1️⃣ Client : Hello le serveur tu m'entends&nbsp;?
  <br><br>
- 2️⃣ Serveur : Oui je t'entends et toi ?
  <br><br>
- 3️⃣ Client : Oui c'est bon je t'entends
  <br><br>

````
`````

---

### TCP/IP : close

`````{div}
:class: columns

````{div}
:class: fourty

```{image} media/tcp-close.svg
```
````

````{div}
:class: sixty
Clotûre en 4 étapes
<br><br>

- 1️⃣ Client : j'ai fini
  <br><br>
- 2️⃣ Serveur : Ok c'est noté
  <br><br>
- 3️⃣ Serveur : moi aussi je n'ai plus rien à te dire
  <br><br>
- 4️⃣ Client : Ok à la prochaine
````
`````

---

## Regardons un peu en vrai comment ca marche

```{div}
:class: center
allons voir le dossier `python/tcp` du cours
```

---

## TCP un truc de riche 🤑

Vous pouvez donc voir qu'avec cette approche
````{div}
:class: center
✅ la connexion est extrêmement fiable et il y a peu de chances d'avoir des loupés
````

En revanche cette fiabilité n'est pas gratuite 💰️
````{div}
:class: center
❌ elle s'accompagne d'un coût en terme d'échanges relativement élevé
````

C'est pour cela qu'il existe une alternative au TCP 😯

---

## UDP

Le protocole UDP (User Datagram Protocol) est complémentaire au protocole TCP. Créé par David Reed en 1980.

Cas d'usage :

````{div}
:class: center
Transmission rapide de données et réception de l'intégralité **pas impérative**
````

````{div}
:class: center
TCP = très fiable mais lent

*vs*
<br>

UDP = rapide mais peu fiable
````

Les applications d'UDP sont nombreuses, par exemple :

````{div}
:class: center
```{image} media/udp-applications.svg
```
````
