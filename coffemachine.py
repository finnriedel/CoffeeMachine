auswahl = 0
kaffebohnen = 10
while auswahl != "off" and kaffebohnen != 0:

    print("-------------------------------------------")
    print("| Folgende Getränke stehen zur Verfügung: |")
    print("| 1: Latte Macchiato                      |")
    print("| 2: Espresso                             |")
    print("| 3: Cappuchino                           |")
    print("| off: [AUSSCHALTEN]                      |")
    print("-------------------------------------------")

    auswahl = input("Bitte Wählen Sie eine Option: ")
    price = 0


    match auswahl:
        case "1" : ##Latte Machiato
            price = 5
            print("Der Latte Machiato kostet: ",price,"€")

        case "2" : ##Espresso
            price = 3.0
            print("Der Espresso kostet: ",price,"€")

        case "3" : ##Cappuccino
            price = 4.5
            print("Der Cappuccino kostet: ",price,"€")

        case "off": ##[Ausschalten]
            print("Die Maschine wird ausgeschaltet...")
            break
        
        case "report": ##[Report]
            print("Report")

        case "replenish":
            print("Auffüllen")

        case _:
            print("Fehlerhafte Eingabe.")
            break

    kaffebohnen = kaffebohnen-1
    

    paid = False

    def muenzeinwurf(n):
        if n < price:
            print("Es fehlen noch", price-n)
            price = price-n
        elif muenzen > price:
            print("Das war zu viel! Du erhälst",n-price,"Rückgeld")
            paid = True
        else:
            paid = True
    
    while paid == False:
        muenzen = input("Bitte Bezahlen Sie.")
        muenzeinwurf(muenzen)

    print("Ihr Getränk wird zubereitet.")