import sys
import socket
import os

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 8000

username = input("Username: ")
#Using Sock Stream for TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # taken from your notes on sockets, week 9


host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
print("Your IP address is: ", ip)

client_socket.connect((IP, PORT))
client_socket.setblocking(False) # tells recv method not to block 

#next line taken from online resource
new_username = username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + new_username)

print("Successfully connected to {} : {}".format(IP, PORT))
print("Please Type a message ")


while True:
    message = input(  ' > ') #allows user to send message
    if message: #if message is not empty 
        message = message.encode('utf-8') #changes message to bytes 
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message) #sends the message to the server 

    #infinite loop that will keep checking to see if message has been sent.
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection lost")
                sys.exit()

            #next two lines grab the username 
            username_length = int(username_header.decode("utf-8")) #changes bytes back to a string 
            username = client_socket.recv(username_length).decode("utf-8")

            #next 3 lines grab the message sent
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8"))
            message = client_socket.recv(message_length).decode("utf-8")

            print(username, message)
    
    
    except OSError:
        break
