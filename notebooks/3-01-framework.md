# Le framework Flask !

## Récap des épisodes précédents

````{div}
:class: center
Architecture classique Client <-> Serveur avec des variations peer-to-peer, three-tier, ...
````

``````{div}
:class: columns

````{div}
:class: fourty center
```{image} media/osi-model.svg
:width: 70%
```
````

`````{div}
:class: fifty

````{div}
:class: columns

```{image} media/ip-address.svg
:width: 40%
```

```{image} media/http-request.svg
:width: 40%
```
````

```{image} media/server-app.svg
:width: 400px
```
`````

````{div}
:class: twenty
```{image} media/logos/lets-encrypt.svg
:width: 150px
```
<p style="font-size: 4rem"> 🍪 </p>
````

``````

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

`````{div}
:class: columns

````{div}
:class: fifty center
<b> Librairies </b>

Ensemble de programmes effectuant des opérations spécifiques, que vous allez utiliser de manière ponctuelle au sein de vos programmes en suivant votre propre logique.

<br>

Par exemple `NumPy` en Python 🐍 est une librairie

```{image} media/code-with-library.svg
:align: center
```
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
<b> Framework </b>

Cadre de développement dans lequel le développeur vient s'inscrire, i.e. développer des fonctionnalités/comportements. Là ce n'est plus le développeur qui fixe sa logique mais le framework.

<br>

Un code à trou 🕳️ en quelque sorte - comme `arcade`

```{image} media/code-with-framework.svg
:align: center
```
````

`````

---

## Frontend, backend

````{div}
:class: center
⚠️ Framework web un terme très, trop, générique ⚠️
````

`````{div}
:class: columns

````{div}
:class: fifty center
Framework frontend

```{image} media/framework_frontend.png
:width: 60%
:align: center
```

Focalisé sur le développement d'application côté client.
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
Framework backend

```{image} media/framework_backend.png
:width: 100%
```

<br>
Focalisé sur le développement côté serveur
````
`````

Dans le cadre de ce cours on ne se focalisera que sur le côté `backend`

---

## Les grands principes des frameworks backend

````{div}
:class: center
```{image} media/framework-routes.svg
:width: 75%
```
````

À cela un framework complet ajoute des fonctionnalités de :

````{div}
:class: center
`Web Template`, `Sécurité`, `Accès à des bases de données`
````

