import sys
import json
from json2html import *
from ping3 import *

#function to check connection to server
def Pinger(ip) -> bool:
    resp = ping(ip)
    if resp == False:
        return False
    else:
        return True

#function that shows menu
def DropMenu() -> int:
    print("Maak een keuze uit de volgende opties")
    print("1: Server toevoegen")
    print("2: Server verwijderen")
    print("3: Server lijst tonen en status van server(s) checken")
    print("4: Exit")
    return int(input())

#function to check if the program runs in management or check mode
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

#create or open the json and html file
jsonResult = {}
try:
    serverJson = open("servers.json", "x")
except FileExistsError:
    serverJson = open("servers.json")

try:
    indexHtml = open("index.html", "x")
    indexHtml = open("index.html", "w")
except FileExistsError:
    indexHtml = open("index.html", "w")

servers = json.load(serverJson)
mode = CheckMode()

#main program start
loop = True
updated = False
while loop:
    #check if sys.argv is being used and the correct value is given
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
        #checks what the user wants to do
        match keuze:
            #add server
            case 1:
                if mode <= 1:
                    server_name = input("Welke server wil je toevoegen? \n")
                    servers[server_name] = {"UP": Pinger(server_name)}
                    updated = False
                else:
                    print("Wrong mode!!!")
            #remove server
            case 2:
                if mode <= 1:
                    server_name = input("Welke server wil je verwijderen? \n")
                    if server_name in servers:
                        del servers[server_name]
                    updated = False
                else:
                    print("Wrong mode!!!")
            #check/show servers
            case 3:
                if mode != 1:
                    for s in servers:
                        print(s)
                        servers[s] = {"UP": Pinger(s)}
                    html = json2html.convert(json = servers)
                    indexHtml.write(html)
                    updated = True
                else:
                    print("Wrong mode!!!")
            #end program
            case 4:
                loop = False
        if not loop:
            if not updated:
                html = json2html.convert(json = servers)
                indexHtml.write(html)
            with open("servers.json", "w") as serverJson:
                json.dump(servers, serverJson, indent=4)
            sys.exit(0)
    except ValueError:
        print("Foute waarde")
