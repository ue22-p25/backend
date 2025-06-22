# Et les websocket ...


`````{div}
:class: columns

````{div}
:class: fifty
Petit rappel au cas où ...
<br><br>
```{div}
:class: center
connexion **bidirectionnelle** entre un client et le serveur
<br><br>on parle de connexion *full-duplex*
<br><br>Permet au serveur de ***pousser*** des informations vers le client sans que ce dernier n'ait rien demandé 😲
```
````

````{div}
:class: fifty center
```{image} media/timeline-ws.svg
:width: 70%
```
````

`````

---

## Utilisation des Websocket

Un module dédié dans Flask

```bash
pip install flask-socketio
```

L'utilisation de websocket avec Flask se fait de manière très simple. Il suffit tout d'abord de créer notre serveur websocket à l'aide de la classe `SocketIO` que l'on attache à notre application Flask.

```python
from flask_socketio import SocketIO
socketio = SocketIO(app)
```

Ensuite rien de révolutionnaire on enregistre des fonctions pour des `events` donnés

```python
@socketio.on('message')
def handle_message(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)
```

---

## Exemple de Chat Flask + SocketIO

``````{div}
:class: columns

`````{div}
:class: fifty

```python
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on('receive_msg')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('the_response', json)

```

Possibilité d'ajouter par dessus la notion de `room` <br>
pour une gestion plus fine des destinataires
<br>
````{div}
:class: center
📥️ 📤️
<http://bit.ly/3yVAEdt>

```{image} media/qrcode/flask_socketio.png
:width: 150px
```
````
`````


````{div}
:class: fifty 
```js
let socket = io.connect(
    "http://" + document.domain + ":" + location.port);
$("form").on("submit", (e) => {
  e.preventDefault();
  let user_name = $("input.username").val();
  let user_input = $("input.message").val();
  socket.emit("receive_msg", {
    user_name: user_name,
    message: user_input,
  });
  $("input.message").val("").focus();
});
socket.on("the_response", (msg) => {
  if (typeof msg.user_name !== "undefined") {
    $("h3").remove();
    $("div.message_holder").append(
      '<div><b style="color: #000">' +
        msg.user_name +
        "</b> " +
        msg.message +
        "</div>"
    );
  }
});
```
````

``````
