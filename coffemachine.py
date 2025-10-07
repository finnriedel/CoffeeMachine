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

    while True:
        if auswahl in menue:
            preis = menue[auswahl]['price']
            print("Der ausgewählte Kaffe kostet:", preis, "€")
            
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
                while(preis != 0):
                    if(preis <= -2):
                        preis=preis+2
                        print("2,00€")
                    elif(preis <= -1):
                        preis=preis+1
                        print("1,00€")
                    elif(preis <= -0.5):
                        preis=preis+0.5
                        print("0,50€")
                    elif(preis <= -0.2):
                        preis=preis+0.2
                        print("0,20€")
                    elif(preis <= -0.1):
                        preis=preis+0.1
                        print("0,10€")

            print("Kaffe wird ausgegeben")

        elif auswahl == "off":
            print("Kaffemaschine wird ausgeschaltet...")
        else:
            print("Ungültige Auswahl")

    
