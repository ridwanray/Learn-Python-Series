import aiohttp
import asyncio
import time


urls = ['https://ironpython.net/', 'https://www.jython.org/'] * 10

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            print(len(response))
    
    end_time = time.time()
    print(f"Time taken Async version: {end_time - start_time} seconds")

asyncio.run(main())
