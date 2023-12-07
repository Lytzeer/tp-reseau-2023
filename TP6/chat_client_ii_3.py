import asyncio
import aioconsole

HOST = '127.0.0.1'
PORT = 8888


async def input(writer):
    while True:
        msg = await aioconsole.ainput()
        writer.write(msg.encode())
        await writer.drain()

async def async_receive(reader):
    while True:
        data = await reader.read(1024)
        print(data.decode())

async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    print("Connected to server")

    asyncio.create_task(input(writer))
    asyncio.create_task(async_receive(reader))

    await asyncio.gather(*asyncio.all_tasks())

if __name__ == "__main__":
    asyncio.run(main())