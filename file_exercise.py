import requests

def get_location(ip_address):
    url = f"https://ipinfo.io/{ip_address}/city"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
    else:
        data = "Not found"
    return data

FILE_PATH = "ip_addresses.txt"

with open(FILE_PATH, "r") as file_object:
    ip_addresses = [line.strip() for line in file_object]
    print("ips", ip_addresses)

locations = [get_location(ip) for ip in ip_addresses]
print(locations)
with open(FILE_PATH, "w") as write_file_object:
    for ip_address, location in zip(ip_addresses, locations):
        write_file_object.write(f"{ip_address}  {location}")


