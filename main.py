import pyfiglet as pf
import sys
import requests
import time

ascii_banner = pf.figlet_format("WhicVer?")
print(ascii_banner)
print("Made by Yiit#3276 on discord")

ip = input("Server's ip: ")
port = input("Server's port(default: 25565):")

if not port and not ip:
    print("Please enter a valid port and IP address. Project is'll get crash in 3 seconds.")
    time.sleep(3)
    sys.exit(0)

url = f"https://api.mcsrvstat.us/2/{ip}:{port}"
response = requests.get(url)

def isPremium(data):
    online = data["online"]
    if online:
        print("[*] Online mod: Yes")
    else:
        print("[*] Online mod: No")

try:
    if response.status_code == 200:
        data = response.json()
        version = data["version"]
        software = data["software"]
        print("-" * 18 + "Server is open" + "-" * 18)
        isPremium(data)
        print(f"[*] Version: {version}")
        print(f"[*] Software: {software}")
        print("-" * 50)
    else:
        print("An error occurred: ", response.status_code)
except Exception:
    print("An error occurred, there could be several different reasons for this.\n1. Server is down\n2. API is down\n3. API cannot get the information\n4. Server is modded\n5. Server's machine banned the API's IP address\n6. API's machine has banned your IP address\n7. You wrote wrong IP or port.")
