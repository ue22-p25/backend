# Épilogue

## Un mot sur l'authentification

Pour s'authentifier auprès d'une API REST, il faut à chaque requête fournir la preuve de qui l'on est. Cela passe généralement par l'association à la requète d'un token qui permet à l'application de savoir

.cols[
.fifty[

- Qui l'on est
- Ce que l'on a le droit de faire sur quelles ressources
  ]
  .fifty[

```bash
Authorization: Bearer <token>
```

]
]

L'obtention du token se fait généralement via l'interface Web du service visé.

.center[⚠️ Attention un token ne doit ***jamais*** être partagé 💣️]

Dans la plupart des cas à un token est associé :

- Un ensemble de ressources accessibles
- Les droits sur ces ressources (consultation, modification, création, suppression)
- Une durée de validité (date d'expiration du token)

.center[Une solution pour conserver les tokens d'une application est d'utiliser un fichier `.env`]

---

# Une API utilisable est une API documentée

Donc pour conclure sur les API, il s'agit d'un moyen très simple pour offrir une interface vers des ressources et données distantes. La seule difficulté dans ce domaine c'est la définition et surtout la **documentation des API** 📑. Donc si vous mettez en place un service Web disposant d'une API et que vous souhaitez ouvrir votre service vers l'extérieur merci de prendre le temps de documenter votre API.

On trouve en ligne plein d'API ouverte un lien pour avoir une liste non exhaustive

.cols[

.fifty[
.center[
[https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)<br>
ou <br>
[http://bit.ly/3YHC1qX](http://bit.ly/3YHC1qX) <br>
ou <br>
<img src="media/qrcode/public_api_qr.png" width="40%">
]
]

.fifty[
.center[
notamment un exemple d'API utile<br> <https://adresse.data.gouv.fr/outils/api-doc/adresse>
]
]

]
---

# Illustration

Considérons par exemple le cas d'un serveur générant des listes de nombres aléatoires à la demande. L'api d'un tel serveur pourrait être

- `/api/integer` renvoie un nombre aléatoire entier
- `/api/float` renvoie un nombre aléatoire flottant
- `/api/integer?n=100` renvoie 100 nombres aléatoires entiers
- ...

.center[
le dossier `python/api-random` du cours
<br>ou<br>
[http://bit.ly/3HONIFN](http://bit.ly/3HONIFN)
<br> ou <br>
<img src="media/qrcode/random_number.png" width="20%">
]

---

# Par exemple

.center[Générer quelques statistiques sur Github]

```md
![Basile's GitHub stats](https://github-readme-stats.vercel.app/api?username=basileMarchand&count_private=true&show_icons=true&theme=dark)
![Basile's top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=basileMarchand&hide=jupyter%20notebook&langs_count=10&theme=dark&layout=compact)
```

![Basile's GitHub stats](https://github-readme-stats.vercel.app/api?username=basileMarchand&count_private=true&show_icons=true&theme=dark)
![Basile's top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=basileMarchand&hide=jupyter%20notebook&langs_count=10&theme=dark&layout=compact)

---

# Un mot sur le "No Code"

Depuis quelques années de plus en plus à la mode: **No Code**, **Low Code**

.center[
<img src="media/make.png" width="50%">
]

<br><br>
.center[demande de support par mail qui provoque une nouvelle entrée dans une base de données<br>et une notification par mail si "urgent" dans le sujet du mail 🤯]

---

# Application 1

Je vous ai mis en place un serveur minimaliste offrant une API permettant :

1. Lister l'ensemble des utilisateurs de la base de données
2. Mettre à jour votre status
3. Envoyer un message à un utilisateur
4. Récupérer les messages qui m'ont été envoyés.

.center[ 🚀 https://mines.bmarchand.fr/api/doc 🚀]

--

L'idée est que vous réalisiez les actions suivantes :

1. A l'aide d'un programme Python 🐍 :
   1. faire une requète `GET` permettant de trouver quel est votre ID d'utilisateur
   2. faire une requète `PATCH` pour mettre à jour votre status
   3. faire des requètes `GET`/`POST` pour vous envoyer des messages entre vous
2. Pour les plus joueurs, à l'aide du combo HTML/CSS/JS
   1. Faire le client web de ce serveur 🤗 !

---

# Application 2 : utilisation de l'API Notion

L'objectif ici est de mettre en place un programme Python permettant de modifier le contenu d'une base de données Notion. **[Un squelette est disponible ici](https://github.com/ue22-p24/backend-notion-api-skeleton)**. L'application à terme doit pouvoir :

.small[

.cols[
.sixty[

- Lister l'ensemble des tâches d'une base de données
- Afficher le détail d'une tâche défini par son ID
  ]
  .fifty[
- Changer le status d'une tâche
- Ajouter du texte dans la page de la tâche
  ]
  ]

.cols[
.fifty[
**Step 1️⃣** : créer une base de données dans Notion
.center[vous pouvez dupliquer [celle-ci](https://bmarchand.notion.site/04620d6c67274d8e96211ddc738acf76?v=31bcb2e38fa242cfbc8eb9c51eca6108)]

**Step 2️⃣** : créer une intégration Notion
.center[Se rendre sur le site [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) et créer une intégration]

<img src="media/notion-token.png" width="80%">

]

.fifty[
**Step 3️⃣** : ajouter la base de données à l'intégration créée précédemment
.center[depuis la page de la base de données]

<img src="media/notion-db-to-integ.png" width="37%">

**Step 4️⃣** : récuper l'ID de la base de données

<img src="media/notion-db-id.png" width="80%">

]
]

]
---

class: middle, center

# La semaine prochaine❕

## On passe du côté obscur <br> et on voit comment définir nos API

.center[
<iframe src="https://giphy.com/embed/6x4CLjC8KofaU" width="469" height="380" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]
