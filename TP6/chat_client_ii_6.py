import asyncio
import aioconsole
import json

HOST = '127.0.0.1'
PORT = 8888


async def get_input(writer):
    while True:
        msg = await aioconsole.ainput()
        writer.write(json.dumps({'action':'msg','content':msg}).encode())
        await writer.drain()

async def async_receive(reader):
    while True:
        # if the reader is down (connection closed), stop the application
        if reader.at_eof():
            print("Connection closed by the server")
            break
        data = await reader.read(1024)
        print(data.decode())

async def main(pseudo):
    reader, writer = await asyncio.open_connection(HOST, PORT)
    print("Connected to server")
    
    writer.write(json.dumps({'action':'join','pseudo':f'Hello|{pseudo}'}).encode())
    await writer.drain()

    asyncio.create_task(get_input(writer))
    asyncio.create_task(async_receive(reader))

    await asyncio.gather(*asyncio.all_tasks())


if __name__ == "__main__":
    pseudo = input("Entrez votre pseudo : ")
    asyncio.run(main(pseudo))