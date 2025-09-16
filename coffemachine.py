auswahl = 0
while auswahl != 4:

    print("---------------------------------------")
    print("Folgende Getränke stehen zur Verfügung:")
    print("1: Latte Macchiato")
    print("2: Espresso")
    print("3: Cappuchino")
    print("4: [AUSSCHALTEN]")
    print("---------------------------------------")

    auswahl = int(input("Bitte Wählen Sie eine Option: "))
    price = 0


    match auswahl:
        case 1 : ##Latte Machiato
            price = 5.00
            print("Der Latte Machiato kostet: ",price,"€")

        case 2 : ##Espresso
            price = 3.00
            print("Der Espresso kostet: ",price,"€")

        case 3 : ##Cappuccino
            price = 4.50
            print("Der Cappuccino kostet: ",price,"€")

    print("Ihr Getränk wird zubereitet.")