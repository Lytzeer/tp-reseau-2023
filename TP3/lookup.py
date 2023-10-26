import socket
from sys import argv

def lookup(domain):
    print(socket.gethostbyname(domain))