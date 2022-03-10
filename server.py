import socket
import os
import subprocess
import sys
import fcntl
import struct

#TEST
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
print(sock.getsockname()[0])

#DEFINIR LA TAILLE DU BUFFER
BUFFER_SIZE = 1024 * 128 

#RECUPERER IP DU RASPBERRY
SERVER_HOST = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
print(SERVER_HOST)

#CREER LE SOCKET
SERVER_PORT = 13000
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))

while True:
    #COMMENCER A ECOUTER
    s.listen(5)

    #AUTORISER LA CONNECTION DE L'API
    client_socket, client_address = s.accept()


    #RECEVOIR LA COMMANDE
    command = client_socket.recv(BUFFER_SIZE).decode()
    
    #EXECUTER LA COMMANDE
    output = subprocess.getoutput(command)

    #ENVOYER LE RESULTAT DE LA COMMANDE
    client_socket.send(output.encode())
