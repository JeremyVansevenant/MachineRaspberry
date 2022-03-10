import socket
import os
import subprocess
import sys

#DEFINIR LA TAILLE DU BUFFER
BUFFER_SIZE = 1024 * 128 

#RECUPERER IP DU RASPBERRY
hostname = socket. gethostname()
SERVER_HOST = socket. gethostbyname(hostname)

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
