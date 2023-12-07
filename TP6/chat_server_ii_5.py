import asyncio
import json


global CLIENTS
CLIENTS = {}

# cette fonction sera appelée à chaque fois qu'on reçoit une connexion d'un client
async def handle_client_msg(reader, writer):
    addr = writer.get_extra_info('peername')

    while True:
        data = await reader.read(1024)

        if data == b'':
            break

        message = json.loads(data.decode())
        if message['action'] == 'join':
            print(f"{message['pseudo'].split("|")[1]} a rejoint la chatroom !")
            CLIENTS[addr] = {}
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["pseudo"] = message['pseudo'].split("|")[1]
            for client_addr, client in CLIENTS.items():
                if client_addr != addr:
                    client["w"].write(f"Annonce : {CLIENTS[addr]['pseudo']} a rejoint la chatroom !".encode())
                    await client["w"].drain()

        if message['action'] == 'msg':
            print(f"Message received from {CLIENTS[addr]['pseudo']} : {message['content']}")
            for client_addr, client in CLIENTS.items():
                if client_addr != addr:
                    client["w"].write(f"{CLIENTS[addr]['pseudo']} a dit : {message['content']}".encode())
                    await client["w"].drain()


async def main():
    server = await asyncio.start_server(handle_client_msg, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    # lancement du main en asynchrone avec asyncio.run()
    asyncio.run(main())
