import asyncio
import aiohttp
import aiofiles
import os
from sys import argv
from time import perf_counter

async def get_content(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
async def write_content(content, file):
    if not os.path.exists("./TP6/web_pages"):
        os.makedirs("./TP6/web_pages")
    file = "./TP6/web_pages/"+file
    async with aiofiles.open(file, "w", encoding="utf-8") as out:
        await out.write(content)
        await out.close()

async def main():
    args = argv[1:]
    # read urls from file in async way
    urls = []
    async with aiofiles.open(args[0], "r") as f:
        urls = await f.readlines()
    # remove \n from urls
    urls = [url.strip() for url in urls]
    tasks = []
    for url in urls:
        file_name="web_"+url.split('//')[1]+".html"
        tasks.append(asyncio.create_task(write_content(await get_content(url), file_name)))
    await asyncio.wait(tasks)

if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"Time elapsed: {end-start} seconds")