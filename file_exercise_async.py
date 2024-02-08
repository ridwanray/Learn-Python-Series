import asyncio
import aiohttp

FILE_PATH = "ip_addresses.txt"

async def get_location(ip_address, session):
    url = f"https://ipinfo.io/{ip_address}/city"
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.text()
        else:
            data = "Not found"
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        with open(FILE_PATH, 'r') as file:
            ip_addresses = [line.strip() for line in file]

        tasks = [get_location(ip_address, session) for ip_address in ip_addresses]
        locations = await asyncio.gather(*tasks)
        print(locations)

        with open(FILE_PATH, 'w') as file:
            for ip_address, location in zip(ip_addresses, locations):
                file.write(f"{ip_address} {location}")

asyncio.run(main())