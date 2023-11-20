import socket
import argparse
import logging
import time
import threading

logging.basicConfig(filename='/var/log/bs_server/bs_server.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%d-%m-%Y %H:%M:%S")

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
logging.info(f"Le serveur tourne sur {host}:{port}")
print("\033[255m"+"INFO"+"\033[0m","Le serveur tourne sur " +host+":"+str(port))

last_connection_time = time.time()

def check_connections():
    global last_connection_time
    while True:
        time.sleep(60)  # Attendre une minute
        if time.time() - last_connection_time > 60:
            logging.warning("Aucun client depuis plus de une minute.")
            print("\033[93m" + "WARN" + "\033[0m", "Aucun client depuis plus de une minute.")

# Démarrer le thread de vérification des connexions
threading.Thread(target=check_connections, daemon=True).start()

# Place le programme en mode écoute derrière le port auquel il s'est bind
s.listen(1)
# On définit l'action à faire quand quelqu'un se connecte : on accepte
conn, addr = s.accept()
conn.sendall(b"Hi mate !")
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse
logging.info(f"Un client {addr[0]} s'est connecté.")
print("\033[255m"+"INFO"+"\033[0m","Un client {addr[0]} s'est connecté.")

# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)

        # Si on a rien reçu, on continue
        if not data: break
        logging.info(f"Le client {addr} a envoyé {str(data)}")
        # On affiche dans le terminal les données reçues du client
        print(f"Données reçues du client : {str(data[2:-1])}")
        if str(data).__contains__("meo"):
            anwser=("Meo a toi confrere.")
        elif str(data).__contains__("waf"):
            anwser=("ptdr t ki")
        elif not str(data).__contains__("waf") and not str(data).__contains__("meo"):
            anwser=("Mes respects humble humain.")
        # On répond au client un truc
        conn.sendall(anwser.encode())
        logging.info(f"Réponse envoyée au client {addr} : {anwser}")
        print("\033[255m"+"INFO"+"\033[0m","Réponse envoyée au client {addr} : {anwser}.")

    except socket.error:
        print ("Error Occured.")
        break

# On ferme proprement la connexion TCP
conn.close()