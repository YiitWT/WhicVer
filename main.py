import pyfiglet as pf
import sys, requests, time, os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ascii_banner = pf.figlet_format("WhicVer?")
print(bcolors.OKGREEN + ascii_banner)
print(bcolors.OKCYAN + "Made by Yiit#3276 on discord")
try:
    ip = input("Server's ip: ")
    port = input("Server's port(default: 25565):")
    def cls():
            os.system('cls' if os.name=='nt' else 'clear')

    if not port and not ip:
        print("Please enter a valid port and IP address. Project is'll get crash in 3 seconds.")
        time.sleep(3)
        sys.exit(0)

    url = f"https://api.mcsrvstat.us/2/{ip}:{port}"
    response = requests.get(url)
    data = response.json()
    def isPremium(data):
        online = data["online"]
        if online:
            print("[*] Online: True")
        else:
            print("[*] Online: False")


    if response.status_code == 200:
        version = data["version"]
        software = data["software"]
        players = data["players"]["online"]
        p_max = data["players"]["max"]
        motd = data["motd"]["clean"]
        try:
            mods = data["mods"]["names"]
            num_of_mods = len(mods)
        except Exception:
            print("Server has 0 mods")
        print("-" * 18 + "Server is open" + "-" * 18)
        isPremium(data)
        print(f"[*] Version: {version}")
        print(f"[*] Software: {software}")
        print(f"[*] Players: {p_max}/{players}")
        print(f"[*] Mods: {num_of_mods}")
        print("-" * 50)
        y_n = input(str("Do you want to see mods? (y/n)"))
        if(y_n.lower() == "y"):
            cls()
            print(bcolors.OKGREEN + ascii_banner)
            for index, mod_name in enumerate(data["mods"]["names"]):
                print(f"{bcolors.WARNING}[{index+1}]{bcolors().OKGREEN}-{bcolors.WARNING}{mod_name}")
        else:
            print("Okay, see you.")
            sys.exit(0)
    else:
        print("An error occurred: ", response.status_code)
except Exception:
    print(bcolors.FAIL+"An error occurred, there could be several different reasons for this.\n1. Server is down\n2. API is down\n3. API cannot get the information\n4. Server is modded\n5. Server's machine banned the API's IP address\n6. API's machine has banned your IP address\n7. You wrote wrong IP or port.")
except KeyboardInterrupt:
    print("\nKeyboard interrupt has detected, project has been terminated.\n")
    sys.exit(0)
