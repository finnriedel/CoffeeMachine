while True: 
    menue = {
        "Latte Machiato":{
            "price":5,
            "water":"100ml",
            "Coffee":"25g"
        }, 
        "Espresso":{
            "price":3,
            "water":"50ml",
            "coffe":"25g",
            "milk":"100ml Oatmilk"
            }, 
        "Cappuccino":{
            "price":4.5,
            "water":"250ml",
            "coffee":"25g",
            "milk":"250ml Oatmilk"
            }}

    for i in menue:
        print(i)

    auswahl = input("Kaffee auswählen: ")

    if auswahl in menue:
        preis = menue[auswahl]['price']
        print("Der ausgewählte Kaffe kostet:", preis, "€")
    elif auswahl == "off":
        print("Kaffemaschine wird ausgeschaltet...")
        break
    else:
        print("Ungültige Auswahl")

    while(preis > 0):
        muenzeinwurf = float(input("Münzen einwerfen: "))

        match muenzeinwurf:
            case 0.1:
                preis=preis-0.1
            case 0.2:
                preis=preis-0.2
            case 0.5:
                preis=preis-0.5
            case 1:
                preis=preis-1
            case 2:
                preis=preis-2
            case _:
                print("Bitte werfen Sie nur gültige Geldstücke ein")
        if(preis > 0):        
            print("Es fehlen noch:", preis,"€")

    if(preis < 0):
        print("Sie bekommen", abs(preis), "€ Rückgeld")

    print("Kaffe wird ausgegeben")
