# And websockets ...


xxx WIP xxx

for now this is the raw Flask text, to be updated for FastAPI

xxx WIP xxx

---

`````{div}
:class: columns

````{div}
:class: fifty
A quick reminder just in case ...
<br><br>

```{div}
:class: center
**bidirectional** connection between a client and the server
<br><br>we talk about *full-duplex* connection
<br><br>Allows the server to **push** information to the client without the client having asked for anything 😲
```
````

````{div}
:class: fifty center
```{image} media/timeline-ws-excalidraw.svg
:width: 70%
```
````

`````

---

## Using Websockets

A dedicated module in Flask

```bash
pip install flask-socketio
```

Using websockets with Flask is very simple. First, you need to create our websocket server using the `SocketIO` class that we attach to our Flask application.

```python
from flask_socketio import SocketIO
socketio = SocketIO(app)
```

Then nothing revolutionary, we register functions for given `events`

```python
@socketio.on('message')
def handle_message(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)
```

---

## Chat Example with Flask + SocketIO

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

Possibility to add on top the concept of `room` <br>
for finer-grained management of recipients
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
