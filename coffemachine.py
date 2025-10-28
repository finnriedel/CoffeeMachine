#Price in Euro
#Water in ml
#Milk in ml
#Coffee in g

water_tank = 2000
coffee_grinder = 50
milk_tank = 1000
cash_drawer = 0

while True:

    menue = {
        "Latte Machiato":{
            "price":5,
            "water":100,
            "coffee":25,
            "milk":250
        }, 
        "Espresso":{
            "price":3,
            "water":50,
            "coffee":20,
            "milk":0
            }, 
        "Cappuccino":{
            "price":4.5,
            "water":250,
            "coffee":25,
            "milk":100
            }}

    for i in menue:
        print(i)

    auswahl = input("Kaffee auswählen: ")

    if auswahl in menue:

        if water_tank-menue[auswahl]['water'] >= 0 and coffee_grinder-menue[auswahl]['coffee'] >= 0 and milk_tank-menue[auswahl]['milk']:
            print("Die Kaffemaschine hat genügend ressourcen.")
        else:
            print("Die Kaffemaschine muss erst aufgefüllt werden")
            continue
        

        preis = menue[auswahl]['price']
        print("Der ausgewählte Kaffe kostet:", preis, "€")
        
    elif auswahl == "off":
        print("Kaffemaschine wird ausgeschaltet...")
        break
    else:
        print("Ungültige Auswahl")
        continue

    
    while(preis > 0):
        muenzeinwurf = float(input("Münzen einwerfen: "))

        match muenzeinwurf:
            case 0:
                break
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

    #GELD WURDE EINGEWORFEN, RESSOURCEN WERDEN ABGEZOGEN
    water_tank = water_tank-menue[auswahl]['water']
    coffee_grinder = coffee_grinder-menue[auswahl]['coffee']
    milk_tank = milk_tank-coffee_grinder-menue[auswahl]['milk']
    cash_drawer = cash_drawer+menue[auswahl]['price']

    if(preis < 0):
        print("Sie bekommen", abs(preis), "€ Rückgeld")
        cash_drawer = cash_drawer - abs(preis)

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
