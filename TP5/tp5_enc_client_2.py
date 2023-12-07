import socket

host = '127.0.0.1'
port = 9999

def checkUserInput(userInput) -> bool:
    if (not userInput.__contains__('+')) and (not userInput.__contains__('-')) and (not userInput.__contains__('*')):
        return False

    splitUserInput = userInput.split(' ')
    if (len(splitUserInput) < 3):
        return False
    try:
        int(splitUserInput[0])
        int(splitUserInput[2])
    except ValueError:
        return False

    if (int(splitUserInput[0]) > 4294967295):
        return False
    if (int(splitUserInput[2]) > 4294967295):
        return False

def checkLength(userInput) -> int:
    splitUserInput = userInput.split(' ')
    return len(splitUserInput)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except:
    print(f"\033[31;1mERROR Impossible de se connecter au serveur {host} sur le port {port}\033[0m")
    exit(1)


while True:
    try:
        print("Entrez votre calcul :")
        data = input(">>> ")

        if checkUserInput(data) == False:
            print("\033[31;1mERROR Mauvais format de calcul. Veuillez respecter le format suivant : <nombre> <opérateur> <nombre>\033[0m")
            continue

        # encoded_msg = data.encode('utf-8')
        element = data.split(' ')
        element[0]=int(element[0]).to_bytes(1, byteorder='big')
        element[2]=int(element[2]).to_bytes(1, byteorder='big')
        match (element[1]):
            case "+":
                element[1]=1
            case "-":
                element[1]=10
            case "*":
                element[1]=11
        element[1]=element[1].to_bytes(1, byteorder='big')
        # on calcule sa taille, en nombre d'octets
        msg_len = 3

        header = msg_len.to_bytes(4, byteorder='big')

        payload = header + element[0] + element[1] + element[2]

        s.sendall(payload)

        data = s.recv(1024)

        print(f"Le serveur a répondu : {int(data.decode('utf-8'))}")

        if not data: break

    except KeyboardInterrupt:
        print("\n\033[31;1mERROR Interruption par l'utilisateur.\033[0m")
        s.close()
        exit(1)

s.close()

exit(0)