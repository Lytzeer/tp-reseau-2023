import socket
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", action="store", type=int)

args = parser.parse_args()

# On choisit une IP et un port où on va écouter
host = '10.1.4.2' # string vide signifie, dans ce conetxte, toutes les IPs de la machine

if args.port is None:
    port = 13337 # port choisi arbitrairement
elif args.port<0 or args.port>65535:
    print("ERROR Le port specifie n'est pas un port possible (de 0 à 65535.)")
    exit(1)
elif args.port<1024:
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)
else:
    port = args.port


# On crée un objet socket
# SOCK_STREAM c'est pour créer un socket TCP (pas UDP donc)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# On demande à notre programme de se bind sur notre port
s.bind((host, port))  

# Place le programme en mode écoute derrière le port auquel il s'est bind
s.listen(1)
# On définit l'action à faire quand quelqu'un se connecte : on accepte
conn, addr = s.accept()
conn.sendall(b"Hi mate !")
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse
print(f"Un client vient de se co et son IP c'est {addr[0]}.")

# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)

        # Si on a rien reçu, on continue
        if not data: break

        # On affiche dans le terminal les données reçues du client
        print(f"Données reçues du client : {data}")
        if str(data).__contains__("meo"):
            anwser=("Meo a toi confrere.")
        elif str(data).__contains__("waf"):
            anwser=("ptdr t ki")
        elif not str(data).__contains__("waf") and not str(data).__contains__("meo"):
            anwser=("Mes respects humble humain.")
        # On répond au client un truc
        conn.sendall(anwser.encode())

    except socket.error:
        print ("Error Occured.")
        break

# On ferme proprement la connexion TCP
conn.close()
