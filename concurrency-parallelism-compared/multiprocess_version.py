import requests
from concurrent.futures import ProcessPoolExecutor
import time

urls = ['https://ironpython.net/', 'https://www.jython.org/'] * 50

def fetch_url(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_url, urls)

    for result in results:
        print(len(result))

    end_time = time.time()
    print(f"Time taken Multiprocessing version: {end_time - start_time} seconds")
