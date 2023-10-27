import sys


def DropMenu() -> int:
    print("Maak een keuze uit de volgende opties")
    print("1: Server toevoegen")
    print("2: Server verwijderen")
    print("3: Server lijst tonen")
    print("4: Exit")
    return int(input())


while True:
    try:
        keuze = DropMenu()
        match keuze:
            case 1:
                print("Server toevoegen")
            case 2:
                print("Server verwijderen")
            case 3:
                print("lijst tonen")
            case 4:
                sys.exit(0)

    except ValueError:
        print("Foute waarde")
