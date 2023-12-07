import asyncio

# cette fonction sera appelée à chaque fois qu'on reçoit une connexion d'un client
async def handle_client_msg(reader, writer):
    while True:
        # les objets reader et writer permettent de lire/envoyer des données auux clients

        # on lit les 1024 prochains octets
        # notez le await pour indiquer que cette opération peut produire de l'attente
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        # si le client n'envoie rien, il s'est sûrement déco
        if data == b'':
            break

        # on décode et affiche le msg du client
        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[1]} : {message!r}")

async def main():
    # on crée un objet server avec asyncio.start_server()
    ## on précise une fonction à appeler quand un paquet est reçu
    ## on précise sur quelle IP et quel port écouter
    server = await asyncio.start_server(handle_client_msg, '127.0.0.1', 8888)

    # ptit affichage côté serveur
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    # on lance le serveur
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    # lancement du main en asynchrone avec asyncio.run()
    asyncio.run(main())
