import sys
import json


def DropMenu() -> int:
    print("Maak een keuze uit de volgende opties")
    print("1: Server toevoegen")
    print("2: Server verwijderen")
    print("3: Server lijst tonen")
    print("4: Exit")
    return int(input())


loop = True
servers = []
try:
    serverJson = open("servers.json", "x")
except FileExistsError:
    serverJson = open("servers.json")
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
        match keuze:
            case 1:
                servers.append(
                    {"Server: " + input("Welke server wil je toevoegen? \n")}
                )
            case 2:
                servers.remove(
                    {"Server: " + input("Welke server wil je verwijderen? \n")}
                )
            case 3:
                for s in servers:
                    print(s)
            case 4:
                serverJson.write(json.dumps(servers))
                sys.exit(0)

    except ValueError:
        print("Foute waarde")
