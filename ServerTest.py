import sys
import json


def DropMenu() -> int:
    print("Maak een keuze uit de volgende opties")
    print("1: Server toevoegen")
    print("2: Server verwijderen")
    print("3: Server lijst tonen")
    print("4: Exit")
    return int(input())

def CheckMode() -> int:
    if len(sys.argv) > 1:
        if sys.argv[1] == "manage":
            return 1
        elif sys.argv[1] == "check":
            return 2 
        else: 
            return 0
    else:
        return -1

loop = True
jsonResult = {}
try:
    serverJson = open("servers.json", "x")
except FileExistsError:
    serverJson = open("servers.json")

servers = json.load(serverJson)
mode = CheckMode()

while loop:
    try:
        if len(sys.argv) >= 2:
            if sys.argv[1] == "add":
                keuze = 1
                loop = False
            elif sys.argv[1] == "remove":
                keuze = 2
                loop = False
            elif sys.argv[1] == "show":
                keuze = 3
                loop = False
            else:
                keuze = DropMenu()
        else:
            keuze = DropMenu()
        match keuze:
            case 1:
                if mode <= 1:
                    server_name = input("Welke server wil je toevoegen? \n")
                    servers[server_name] = {}
                else:
                    print("Wrong mode!!!")
            case 2:
                if mode <= 1:
                    server_name = input("Welke server wil je verwijderen? \n")
                    if server_name in servers:
                        del servers[server_name]
                else:
                    print("Wrong mode!!!")
            case 3:
                if mode != 1:
                    for s in servers:
                        print(s)
                else:
                    print("Wrong mode!!!")
            case 4:
                loop = False
        if not loop:
            with open("servers.json", "w") as serverJson:
                json.dump(servers, serverJson, indent=4)
            sys.exit(0)
    

    except ValueError:
        print("Foute waarde")
