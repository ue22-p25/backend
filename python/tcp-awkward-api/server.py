"""
here we implement a very rustic "api" to manage contacts
the client can send requests to the server to list, or add contacts

it does work, but it's awkward because it is not a standard way to do things
"""

import os
import socketserver
import json

global contact
contacts = {"Jean Dupond": "jean.dupond@fake.com", "John Doe": "john.doe@fake.com"}


class ContactRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data_json = self.request.recv(1024).decode()

        data = json.loads(data_json)
        cmd = data["cmd"]
        print(f"Receive : {data}")
        ret = {"status": False, "msg": "", "data": {}}
        if cmd == "help":
            ret["status"] = True
            ret["msg"] = "Available commands help, list, add"
        elif cmd == "list":
            ret["status"] = True
            ret["msg"] = "The list of all registered contacts"
            ret["data"] = contacts
        elif cmd == "add":
            name = data["args"]["name"]
            mail = data["args"]["mail"]
            contacts[name] = mail

            ret["status"] = True
            ret["msg"] = f"{name} added to contacts"
        else:
            ret["status"] = False
            ret["msg"] = f"command {cmd} unknown"

        to_send = json.dumps(ret).encode()

        print(f"Send : {to_send}")

        self.request.send(to_send)
        print("message sent")
        self.request.close()
        print("request close")
        return


if __name__ == "__main__":
    import socket

    address = ("localhost", 3001)
    server = socketserver.TCPServer(address, ContactRequestHandler)
    print(f"Server listen at {address}")
    server.serve_forever()
