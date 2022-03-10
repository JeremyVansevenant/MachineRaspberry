import socket
import os
import subprocess
import sys

#TEST
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print(get_ip_address("eth0"))
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
