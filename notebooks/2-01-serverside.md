# C'est quoi un serveur&nbsp;?

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
