# Le réseau : principe

## Infrastructure

Tout d'abord un réseau c'est quoi ?

````{div}
:class: center
Et bien c'est une **infrastructure** que l'on utilise pour faire transiter des données.
````

Dans sa version la plus élémentaire qui soit, un réseau est composé de deux appareils reliés entre eux, par un câble réseau par exemple.

Le point important là-dedans c'est qu’un appareil connecté au réseau doit posséder une **interface réseau**, un composant capable de communiquer c'est-à-dire d'envoyer et recevoir un signal.

Par exemple votre ordinateur portable possède deux interfaces réseau : la prise RJ45 et la carte wifi. Le signal qui transite par l'interface réseau est un signal binaire.

````{div}
:class: center
**⚠️ L'appareil en lui-même n'a pas besoin de connaître la signification de ce signal, 
<br> car c'est un programme tournant derrière l'interface réseau qui se chargera de traiter le signal en question ⚠️**
````

---

## Petite parenthèse

### Supercalculateur : un modèle peer-to-peer

`````{div}
:class: columns

````{div}
:class: thirty
```{image} media/cluster1.jpg
```
````

````{div}
:class: thirty
```{image} media/cluster2.jpg
```
````

````{div}
:class: rows thirty

```{iframe} https://www.youtube.com/embed/4r6frld1UNE?autoplay=1&mute=1&loop=1&controls=0&playlist=4r6frld1UNE
```

```{iframe} https://www.youtube.com/embed/90-kA3wYuoM?autoplay=1&mute=1&loop=1&controls=0&playlist=90-kA3wYuoM
```
````

`````

---

## High Performance Computing

````{div}
:class: center
Diviser pour mieux régner
````

`````{div}
:class: columns

````{div}
:class: thirty
```{figure} media/aube_dd.png
décomposition en sous-domaines
```
````

````{div}
:class: thirty
```{figure} media/dd.png
Chaque sous-domaine "envoyé" <br> sur une machine de calcul
```
````

````{div}
:class: thirty
```{figure} media/dd_zoom.png
Chaque sous-domaine "éclaté" par paquet d'éléments <br>pour l'intégration de la loi de comportement
```
````

`````

Au niveau de chaque sous-domaine :

- Opérations algébriques distribuées
- Résolution de problèmes locaux (solveurs DD)

mais refermons la parenthèse, on n'est pas là pour parler de HPC mais de réseau !

---

## Différentes qualités du réseau

La qualité du réseau, un petit truc qui a son importance suivant l'application 🚀

<!-- <button onclick="plot_network()"> xxx no longer working - click me 📈 </button> 

````{div}
:class: center
<div id="plot_network"></div>
````
-->

Généralement on parle de trois qualités :

- **Bande passante** : la quantité de données qui peut être transmise par unité de temps (en bits par seconde, bps)
- **Latence** : le temps nécessaire pour qu'un paquet de données atteigne sa destination
- **Fiabilité** : la probabilité que les données soient transmises sans erreur

````{div}
:class: center
⏳️ Sur des grosses simulations le temps des échanges peut représenter 20% du temps de calcul 💣
````

---

## Modèle OSI

``````{div}
:class: columns

`````{div}
:class: fifty
````{div}
:class: center
```{image} media/osi-model.svg
```
````
`````

````{div}
:class: fifty
<br><br>
**O**pen **S**ystem **I**nterconnexion
<br><br><br>

**Norme** mise en place <br>par le commité ISO en 1984
<br><br>

**Objectifs** :
<br><br>

```{div}
:class: center
standardiser les communications<br> entre appareils sur un réseau
```

````

``````

---

## Adressage

````{div}
:class: center
Associer à chaque interface de chaque machine sur un réseau une adresse unique
````

<br>

Cette addresse peut être _temporaire_ ou bien _fixe_.

<br>

C'est ce qu'on appelle l'adresse IP, pour _Internet Protocol_. 
L'adresse IP d'une interface réseau s'écrit comme une combinaison de quatre nombres compris entre 0 et 255.
<br>
````{div}
:class: center
```{image} media/ip-address.svg
:width: 30%
```
````

`````{div}
:class: smaller

il y a donc deux parties : l'adresse du réseau (souvent sur 24 bits) et l'adresse de l'hôte (souvent sur 8 bits)  
lorsqu'on a besoin d'écrire l'adresse d'un réseau on écrit alors comme ceci le nombre de bits de l'adresse réseau
````{div}
:class: center
```{image} media/ip-address-subnet.svg
:width: 20%
```
````
`````

---

### Adresses IPv6

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

## Interconnexion

### Réseau local

````{div}
:class: center
```{image} media/connection-local.svg
:width: 60%
```
````

---

### Réseau distant

````{div}
:class: center
```{image} media/connection-remote.svg
:width: 60%
````

---

## Pour résumer :

````{div}
:class: center
interconnexion qui constitue en fait **la troisième couche** du modèle OSI
````

gère trois éléments :
<br>

- Routage
  ````{div}
  :class: center
  chemin entre deux machines dans des réseaux différents, <br>chemin passant par les passerelles (routeurs)<br>ces fameuses machines ayant des interfaces dans deux réseaux distincts.
  ````

- Relayage
  ````{div}
  :class: center
  s'occupe, une fois la route déterminée, <br>de faire transiter l'information de la machine A à la machine B
  ````

- Contrôle de flux
  ````{div}
  :class: center
  une fonctionnalité optionnelle mais néanmoins essentielle <br> qui permet de décongestionner l'ensemble du réseau (au sens large). <br>Un peu le Waze du transit de données
  ````

---
(my-ip-address)=

## Au passage: c'est quoi mon IP ?

`````{div}
:class: columns

````{div}
:class: fourty
Comment je fais <br>pour connaitre mon IP ?
````

````{div}
:class: sixty
pour commencer je clone le cours (si ce n'est déjà fait)  
sur github: `ue22-p25/backend`  
et je me rends dans le dossier `python/ip-address`
````

`````

`````{div}
:class: columns
````{div}
:class: fitfy

un petit code pour demander à un site extérieur

```{literalinclude} ../python/ip-address/my-public-ip.py
```

````

````{div}
:class: fitfy
ou pour demander à mon OS(*)

```{literalinclude} ../python/ip-address/my-local-ip.py
```


````

`````

`````{div}
:class: columns

````{div}
:class: fifty

et j'obtiens (essayez !)
```{code}
:linenos:
:emphasize-lines: 2
$ python my-public-ip.py
Public IP: 138.96.202.10
```
````

````{div}
:class: fifty
.. et ça peut être différent ! quel est ce mystère ?
```{code}
:linenos:
:emphasize-lines: 2
$ python my-local-ip.py
Outgoing IP: 10.1.1.15
```
````

`````

(*) depuis le terminal, utiliser: `ipconfig` sur Windows, `ifconfig` sur MacOS, `ip address show` sur Linux

---

### le NAT (Network Address Translation)

`````{div}
:class: columns

````{div}
:class: sixty-five
et mon petit doigt me dit que:

- vous allez tous avoir **la même adresse publique**
- mais pour la deuxième vous avez chacun une **adresse locale différente**

en fait il y a deux types d'adresses IP :

- publiques: celles qui sont visibles sur le réseau, et qui sont uniques
- privées: celles qui sont utilisées **uniquement** dans un réseau local

````

````{div}
:class: thirty-five
<br><br>
les adresses privées réservées:

- `192.168.0.0/16` <br> 2<sup>16</sup> = 65,536 adresses

- `172.16.0.0/12` <br> 2<sup>20</sup> = 1,048,576 adresses

- `10.0.0.0/8` <br> 2<sup>24</sup> = 16,777,216 adresses
````
`````

````{div}
:class: center
```{image} media/nat-routing.svg
:width: 125%
```
````

---

## Les noms de domaines là-dedans !

Retenir les adresses IP c'est quand même pas super 🤯 !

````{div}
:class: center
Par exemple imaginez que vous deviez retenir `91.134.82.158` (*)
<br/>pour savoir les salles de cours .... <strike>on ne vous verrait pas souvent !</strike>
````

(*) c'est l'adresse IP du serveur qui héberge OASIS

--

Pour cela dans l'infrastructure d'Internet il y a un truc magique, le :

````{div}
:class: center
**DNS** = **D**omain **N**ame **S**ystem
````

En gros c'est le service qui fait l'association entre un nom de domaine et un adresse IP.

---

### Le DNS depuis le terminal

`````{div}
:class: columns

````{div}
:class: fifty

```bash
# plusieurs utilitaires pour faire des requêtes DNS

$ nslookup oasis.minesparis.psl.eu
Server:		192.168.0.1
Address:	192.168.0.1#53

Non-authoritative answer:
Name:	oasis.minesparis.psl.eu
*Address: 91.134.82.158
```

````

````{div}
:class: fifty
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
````

`````
