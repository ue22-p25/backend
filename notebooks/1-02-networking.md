# Le réseau : principe

## Infrastructure

Tout d'abord un réseau c'est quoi ?

.center[Et bien c'est une **infrastructure** que l'on utilise pour faire transiter des données. ]

Dans sa version la plus élémentaire qui soit un réseau est composé de deux appareils reliés entre eux, par un câble réseau par exemple.

Le point important là-dedans c'est qu’un appareil connecté au réseau doit posséder une **interface réseau**, un composant capable de communiquer c'est-à-dire d'envoyer et recevoir un signal.

Par exemple votre ordinateur portable possède deux interfaces réseau : la prise RJ45 et la carte wifi. Le signal qui transite par l'interface réseau est un signal binaire.

.center[
**⚠️ L'appareil en lui-même n'a pas besoin de connaître la signification de ce signal, <br> car c'est un programme tournant derrière l'interface réseau qui se chargera de traiter le signal en question ⚠️**
]

---

# Petite parenthèse

## Supercalculateur : un modèle peer-to-peer

<!-- <div style="position: absolute; left: 10%; top: 25%;"> -->
<img src="media/cluster1.jpg" width="300px">
<!-- </div> -->

<!-- <div style="position: absolute; left: 35%; top: 35%;"> -->
<img src="media/cluster2.jpg" width="300px">
<!-- </div> -->

<!-- <div style="position: absolute; left: 55%; top: 55%;"> -->
<iframe width="400px" height="280" src="https://www.youtube.com/embed/4r6frld1UNE?autoplay=1&mute=1&loop=1&controls=0&playlist=4r6frld1UNE">
</iframe>
<!-- </div> -->

<!-- <div style="position: absolute; left: 65%; top: 25%;"> -->
<iframe width="320px" height="215" src="https://www.youtube.com/embed/90-kA3wYuoM?autoplay=1&mute=1&loop=1&controls=0&playlist=90-kA3wYuoM">
</iframe>
<!-- </div> -->

---

# High Performance Computing

.center[Diviser pour mieux régner]

<div>
<p style="font-size: small;"> Décomposition en sous-domaines </p>
  <img width="250px" src="media/aube_dd.png">
</div>

--

<!-- <div style="position: absolute; left: 40%; top: 25%"> -->
  <p style="font-size: small;"> Chaque sous-domaine "envoyé" <br> sur une machine de calcul </p>
    <img width="250px" src="media/dd.png"> 
<!-- </div> -->

--

<!-- <div style="position: absolute; left: 75%; top: 25%"> -->
  <p style="font-size: small;"> Chaque sous-domaine "éclaté" par paquet d'éléments <br>pour l'intégration de la loi de comportement
    <img width="250px" src="media/dd_zoom.png"> 
<!-- </div> -->

--

<!-- <div style="position: absolute; left: 30%; top: 65%"> -->
  <p> Au niveau de chaque sous-domaine : </p>
  <ul>
    <li>Opérations algébriques distribuées </li>
    <li>Résolution de problèmes locaux (solveurs DD)</li>
  </ul>
<!-- </div> -->

---

# Réseau

## Différentes qualités

La qualité du réseau, un petit truc qui a son importance suivant l'application 🚀 <button onclick="plot_network()"> click me 📈 </button>

.center[

<div id="plot_network"></div>
]

.center[
⏳️ Sur des grosses simulations le temps des échanges peut représenter 20% du temps de calcul 💣
]

---

class: middle, center

# Un réseau et c'est tout ?

---

# Modèle OSI

.cols[
.fifty[

.center[<img src="media/osi-model.svg" style="width: 72%;">]

]
.fifty[
<br><br><br>
**O**pen **S**ystem **I**nterconnexion
<br><br><br>

**norme** mise en place par le commité ISO en 1984
<br><br><br>

Objectifs :
<br><br><br>

.center[standardiser les communications<br> entre appareils sur un réseau]

]
]

---

# Adressage

.center[Associer à chaque interface de chaque machine sur un réseau une adresse unique]
<br><br>
Cette addresse peut être _temporaire_ ou bien _fixe_.
<br><br>
C'est ce qu'on appelle l'adresse IP, pour _Internet Protocol_. L'adresse IP d'une interface réseau s'écrit comme une combinaison de quatre nombres compris entre 0 et 255.
<br><br>
.center[<img src="media/ip-address.svg" style="width: 30%;">]

.footnote.smaller[
il y a donc deux parties : l'adresse du réseau (souvent sur 24 bits) et l'adresse de l'hôte (souvent sur 8 bits)  
lorsqu'on a besoin d'écrire l'adresse d'un réseau on écrit alors comme ceci le nombre de bits de l'adresse réseau
.center[<img src="media/ip-address-subnet.svg" style="width: 30%;">]
]

---

## Adresses IPv6

**en 2011** on prévoit **l'épuisement 💣 des adresses IP** disponibles !...

2<sup>32</sup> = 4,294,967,296 c'est-à-dire environ 1/2 adresse par personne sur terre  
(bien sûr certaines personnes en ont plus que d'autres 😅)

Il a donc été mis en place le protocol **IP v6** (l'ancien protocole était le **v4**)

Le principe est simple: passer d'une adresse sur **32 bits** à une adresse sur **128 bits**  
par exemple (en hexa) `2001:0db8:0000:85a3:0000:0000:ac1f:8001`  
En fait on a tellement d'adresses que l'on peut donner une adresse IP à chaque grain de sable sur terre 🏖  ️

<br>
Actuellement déployé **mais en partie** - principalement, mais pas que, dans le coeur de réseau chez les opérateurs

Et pourquoi pas partout, me direz-vous ?  
eh bien notamment, le besoin de IPv6 est moins important que prévu grâce notamment au NAT  
on en reparlera...

---

# Interconnexion

## Réseau local

.center[
<img src="media/connection-local.svg" style="width: 60%">

]

---

# Interconnexion

## Réseau distant

.center[
<img src="media/connection-remote.svg" style="width: 60%">
]

---

# Interconnexion

Pour résumer :
.center[interconnexion qui constitue en fait la troisième couche du modèle OSI ]

gère trois éléments :
<br>

- Routage
  .center[
  chemin entre deux machines dans des réseaux différents, <br>chemin passant par les passerelles (routeurs)<br>ces fameuses machines ayant des interfaces dans deux réseaux distincts.
  ]
- Relayage
  .center[s'occupe, une fois la route déterminée, <br>de faire transiter l'information de la machine A à la machine B]

- Contrôle de flux
  .center[une fonctionnalité optionnelle mais néanmoins essentielle <br> qui permet de décongestionner l'ensemble du réseau (au sens large). <br>Un peu le Waze du transit de données]

---
name: my-ip-address

## (Au passage c'est quoi mon IP ?)

.cols[

.fifty[
Comment je fais pour connaitre mon IP ?
]
.fifty[
pour commencer je clone le cours (si ce n'est déjà fait)  
sur github: `ue22-p24/web`  
et je me rends dans le dossier `python/ip-address`
]
]

.cols[
.fitfy[
je demande à un site extérieur

```sh
$ cat my-public-ip.py
import requests

response = requests.get("https://api64.ipify.org?format=json")
public_ip = response.json()["ip"]

print("Public IP:", public_ip)
```
]
.sixty[
je demande à mon OS (*)

```sh
$ cat my-local-ip.py
import socket

def get_outgoing_ip():
    with socket.create_connection(("8.8.8.8", 53)) as s:
        return s.getsockname()[0]

print("Outgoing IP:", get_outgoing_ip())
```
]
]

.cols[
  .fifty[
  et j'obtiens (essayez !)
```sh
$ python my-public-ip.py
*Public IP: 138.96.202.10
```

  ]
  .fifty[
  .. et ça peut être différent ! quel est ce mystère ?
```sh
$ python my-local-ip.py
*Outgoing IP: 10.1.1.15
```
  ]
]

.footnote.small[(*): depuis le terminal, utiliser: `ipconfig` sur Windows, `ifconfig` sur MacOS, `ip address show` sur Linux]

---

## le NAT (Network Address Translation)

.cols[

.sixty-five[
et mon petit doigt me dit que:

- vous allez tous avoir **la même adresse publique**
- mais pour la deuxième vous avez chacun une **adresse locale différente**

en fait il y a deux types d'adresses IP :

- publiques: celles qui sont visibles sur le réseau, et qui sont uniques
- privées: celles qui sont utilisées **uniquement** dans un réseau local

<img src="media/nat-routing.svg" width="125%">
]

.thirty-five[
<br><br>
les adresses privées réservées:

- `192.168.0.0/16` <br> 2<sup>16</sup> = 65,536 adresses

- `172.16.0.0/12` <br> 2<sup>20</sup> = 1,048,576 adresses

- `10.0.0.0/8` <br> 2<sup>24</sup> = 16,777,216 adresses
]
]

---

# Les noms de domaines là-dedans !

Retenir les adresses IP c'est quand même pas super 🤯 !

.center[
Par exemple imaginez que vous deviez retenir `91.134.82.158` <br/>pour savoir les salles de cours .... <strike>on ne vous verrait pas souvent !</strike>
]

.footnote[`*` c'est l'adresse IP du serveur qui héberge OASIS]

--

Un truc magique le :

.center[ **DNS** = **D**omain **N**ame **S**ystem]

En gros c'est le service qui fait l'association entre un nom de domaine et un adresse IP.

--

.cols[

.fifty[
```bash
# plusieurs utilitaires pour faire des requêtes DNS

$ nslookup oasis.minesparis.psl.eu
Server:		192.168.0.1
Address:	192.168.0.1#53

Non-authoritative answer:
Name:	oasis.minesparis.psl.eu
*Address: 91.134.82.158
```
]

.fifty[

```bash
$ host oasis.minesparis.psl.eu
*oasis.minesparis.psl.eu has address 91.134.82.158
```

```bash
$ dig @8.8.8.8 oasis.minesparis.psl.eu A +noall +answer

; <<>> DiG 9.10.6 <<>> @8.8.8.8 oasis.minesparis.psl.eu A +noall +answer
; (1 server found)
;; global options: +cmd
*oasis.minesparis.psl.eu. 161	IN	A	91.134.82.158
```

]
]

