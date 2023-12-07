import asyncio

async def count():
    for i in range(1,11):
        print(i)
        await asyncio.sleep(0.5)

loop=asyncio.get_event_loop()
tasks=[loop.create_task(count()),loop.create_task(count())]

if __name__ == "__main__":
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()