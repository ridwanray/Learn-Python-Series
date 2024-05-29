import requests
import time

urls = ['https://ironpython.net/', 'https://www.jython.org/'] * 50

def fetch_url(url):
    response = requests.get(url)
    return response.text

start_time = time.time()
responses = [fetch_url(url) for url in urls]

for response in responses:
    print(len(response))

end_time = time.time()

print(f"Time taken Sync version: {end_time - start_time} seconds")
