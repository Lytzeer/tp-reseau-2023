import asyncio
import aiohttp
import aiofiles
import os
from sys import argv

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
    if len(args) != 1:
        print("Usage: python3 web_async.py <url>")
        return
    file_name=args[0].split('.')[1]+".html"
    content = await get_content(args[0])
    await write_content(content, file_name)

if __name__ == "__main__":
    asyncio.run(main())