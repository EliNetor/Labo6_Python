def DropMenu():
    print("Maak een keuze uit de volgende opties")
    print("1: Server toevoegen")
    print("2: Server verwijderen")
    print("3: Server lijst tonen")
    ant = int(input())


while True:
    try:
        DropMenu()
    except ValueError:
        print("Foute waarde")


