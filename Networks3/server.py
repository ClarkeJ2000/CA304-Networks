import socket
import os
#allows us to run on either mac windows or linux with no differences.
import select
from threading import Thread
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("webpage.html")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#taken from week 9 notes

sock.bind((IP, PORT))
sock.listen()

socket_list = [sock]
clients = {}

client, client_address = sock.accept()
username = client.recv(1024).decode("utf-8")

print(username + " connected to the server")
       
#watched youtube video along with notes online to create recieve function
def recieve(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8"))
        return {"data": client_socket.recv(message_length)}
    except:
        socket.close()


while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)
    for notification in read_sockets:
        if notification == sock:
            client_socket, client_address = sock.accept()

            user = recieve(client_socket)
            if user is False:
                continue

            socket_list.append(client_socket)
            #user is from dictionary; data
            #current info on the user 
            clients[client_socket] = user
            print("Accepted new connection")
        else:
            message = recieve(notification)
            if message is False:
                print("Connection closed.")
                socket_list.remove(notification)
                continue
        
        user = clients[notification]

        for client_socket in clients:
            if client_socket != notification:
                client_socket.send(user['data'] + message['data']) #send the message to the server 
    
    for notification in exception_sockets:
        socket_list.remove(notification)
        del clients[notification]
