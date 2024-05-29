import requests
from concurrent.futures import ThreadPoolExecutor
import time
urls = ['https://ironpython.net/', 'https://www.jython.org/'] * 50

def fetch_url(url):
    response = requests.get(url)
    return response.text

start_time = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_url, urls)

for result in results:
    print(len(result))

end_time = time.time()

print(f"Time taken Multithreading version: {end_time - start_time} seconds")