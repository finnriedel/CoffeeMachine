import os
import datetime
import csv
#Price in Euro
#Water in ml
#Milk in ml
#Coffee in g

water_tank = 2000
coffee_grinder = 500
milk_tank = 1000

cash_drawer = {
    "0,10€":{
        "wert": 0.1,
        "muenzen": 5
    },
    "0,20€":{
        "wert": 0.2,
        "muenzen": 5
    },
    "0,50€":{
        "wert": 0.5,
        "muenzen": 5
    },
    "1,00€":{
        "wert": 1.0,
        "muenzen": 5
    },
    "2,00€":{
        "wert": 2.0,
        "muenzen": 5
    }
}


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
    }
}


def write_status_to_csv(filename='status.csv'):
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['coffeedrink', 'price', 'water', 'coffee', 'milk']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        
        for coffeedrink, details in menue.items():
                    row = {'coffeedrink': coffeedrink}
                    row.update(details)
                    writer.writerow(row)

def write_cash_status_to_csv(filename='cash_status.csv'):
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['kleingeld', 'wert', 'muenzen']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        
        for kleingeld, details in cash_drawer.items():
                    row = {'kleingeld': kleingeld}
                    row.update(details)
                    writer.writerow(row)


def read_status_from_csv(filename='status.csv'):
    global menue
    load_menue = {}

    try:
        with open(filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            print("Datei geöffnet")
            
            for row in reader:
                try:
                    coffeedrink = row['coffeedrink']
                    menue[coffeedrink] = {
                        'price': float(row['price']),
                        'water': int(row['water']),
                        'coffee': int(row['coffee']),
                        'milk': int(row['milk'])
                    }
                except (KeyError, ValueError) as e:
                     print("Error")

    except FileNotFoundError:
        print("Keine Datei gefunden. Standardwerte werden gelesen")

def read_cash_status_from_csv(filename='cash_status.csv'):
    global cash_drawer
    load_cash_drawer = {}

    try:
        with open(filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                try:
                    kleingeld = row['kleingeld']
                    cash_drawer[kleingeld] = {
                        'wert': float(row['wert']),
                        'muenzen': int(row['muenzen']),
                    }
                except (KeyError, ValueError) as e:
                     print("Error")

    except FileNotFoundError:
        print("Keine Datei gefunden. Kassenbestand auf Standard gesetzt.")

def read_price_config_csv(filename='price_config.csv'):
    global menue
    
    try:
        with open(filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                try:
                    drink_name = row['coffeedrink']
                    new_price = float(row['price'])
                    
                    if drink_name in menue:
                        menue[drink_name]['price'] = new_price
                    else:
                        print(f"-> Warnung: {drink_name} nicht im Menü gefunden. Ignoriert.")
                        
                except ValueError:
                    print(f"-> Fehler: Ungültiger Preis in Zeile: {row}")

    except FileNotFoundError:
        print("Keine Preis-Config Datei gefunden. Alte Preise bleiben bestehen.")     

def cash_drawer_summieren():
    summe = 0
    for element in cash_drawer:
        summe = summe + (cash_drawer[element]['wert'] * cash_drawer[element]['muenzen'])
    return summe

def cash_drawer_balance():


    for element in cash_drawer:
        print(cash_drawer[element], ":", cash_drawer[element]['muenzen'])

def cash_drawer_balance_string():
    lines = [
        f"{element}: {details['muenzen']} Münzen"
        for element, details in cash_drawer.items()
    ]
    return "\n".join(lines)

def resources_report():
    dateiname = "report.txt"

    try:
        dat_Obj = open(dateiname, "w")
        dat_Obj.write(f"Wasserstand: {water_tank} ml\n")
        dat_Obj.write(f"Kaffebohnen: {coffee_grinder} g\n")
        dat_Obj.write(f"Milchstand: {milk_tank} ml\n")
        dat_Obj.write(f"--- Kassenbestand ---")
        dat_Obj.write(cash_drawer_balance_string() + "\n")


    except (IOError) as e:
        print("Fehler")
        os._exit(1)


    print("Wasserstand:",water_tank,"ml")
    print("Kaffebohnen:",coffee_grinder,"g")
    print("Milchstand:",milk_tank,"ml")
    print("In Report-Datei geschrieben...")
    dat_Obj.close()

def replenish():
    aktuelle_zeit = datetime.datetime.now()
    datumsstempel = aktuelle_zeit.strftime("%Y-%m-%d %H:%M:%S")

    global water_tank
    global coffee_grinder
    global milk_tank

    water_tank = 2000
    coffee_grinder = 500
    milk_tank = 1000

    dateiname = "log.txt"

    try:
        dat_Obj = open(dateiname, "a")
        dat_Obj.write(f"{datumsstempel}: Ressourcen wurden vollständig gefüllt.\n")

    except (IOError) as e:
        print("Fehler")
        os._exit(1)

    print("In Log-Datei geschrieben...")
    dat_Obj.close()


read_status_from_csv()
read_cash_status_from_csv()
read_price_config_csv()

while True:

    for i in menue:
        print(i)

    auswahl = input("Kaffee auswählen: ")

    if auswahl in menue:

        if water_tank-menue[auswahl]['water'] >= 0 and coffee_grinder-menue[auswahl]['coffee'] >= 0 and milk_tank-menue[auswahl]['milk'] >= 0:
            print("Die Kaffemaschine hat genügend ressourcen.")
        else:
            print("Die Kaffemaschine muss erst aufgefüllt werden")
            continue
        

        preis = menue[auswahl]['price']
        print("Der ausgewählte Kaffe kostet:", preis, "€")
        
    elif auswahl == "off":
        print("Kaffemaschine wird ausgeschaltet...")
        write_status_to_csv()
        write_cash_status_to_csv()
        break
    elif auswahl == "balance":
        cash_drawer_balance()
        continue
    elif auswahl == "replenish":
        replenish()
        continue
    elif auswahl == "report":
        resources_report()
        continue
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
                cash_drawer["0,10€"]['muenzen']=cash_drawer["0,10€"]['muenzen']+1
            case 0.2:
                preis=preis-0.2
                cash_drawer["0,20€"]['muenzen']=cash_drawer["0,20€"]['muenzen']+1
            case 0.5:
                preis=preis-0.5
                cash_drawer["0,50€"]['muenzen']=cash_drawer["0,50€"]['muenzen']+1
            case 1:
                preis=preis-1
                cash_drawer["1,00€"]['muenzen']=cash_drawer["1,00€"]['muenzen']+1
            case 2:
                preis=preis-2
                cash_drawer["2,00€"]['muenzen']=cash_drawer["2,00€"]['muenzen']+1
            case _:
                print("Bitte werfen Sie nur gültige Geldstücke ein")
        if(preis > 0):        
            print("Es fehlen noch:", preis,"€")

    #GELD WURDE EINGEWORFEN, RESSOURCEN WERDEN ABGEZOGEN
    water_tank = water_tank-menue[auswahl]['water']
    coffee_grinder = coffee_grinder-menue[auswahl]['coffee']
    milk_tank = milk_tank-menue[auswahl]['milk']

    if(preis < 0 and cash_drawer_summieren() >= abs(preis)):
        print("Sie bekommen", abs(preis), "€ Rückgeld")

        while(preis != 0):
            if(preis <= -2) and cash_drawer["2,00€"]['muenzen'] > 0:
                #if cash_drawer["2,00€"]['muenzen'] > 0:
                    preis=preis+2
                    cash_drawer["2,00€"]['muenzen']=cash_drawer["2,00€"]['muenzen']-1
                    print("2,00€")
            elif(preis <= -1) and cash_drawer["1,00€"]['muenzen'] > 0:
                #if cash_drawer["1,00€"]['muenzen'] > 0:
                    preis=preis+1
                    cash_drawer["1,00€"]['muenzen']=cash_drawer["1,00€"]['muenzen']-1
                    print("1,00€")
            elif(preis <= -0.5) and cash_drawer["0,50€"]['muenzen'] > 0:
                #if cash_drawer["0,50€"]['muenzen'] > 0:
                    preis=preis+0.5
                    cash_drawer["0,50€"]['muenzen']=cash_drawer["0,50€"]['muenzen']-1
                    print("0,50€")
            elif(preis <= -0.2) and cash_drawer["0,20€"]['muenzen'] > 0:
                #if cash_drawer["0,20€"]['muenzen'] > 0:
                    cash_drawer["0,20€"]['muenzen']=cash_drawer["0,20€"]['muenzen']-1
                    preis=preis+0.2
                    print("0,20€")
            elif(preis <= -0.1) and cash_drawer["0,10€"]['muenzen'] > 0:
                #if cash_drawer["0,10€"]['muenzen'] > 0:
                    preis=preis+0.1
                    cash_drawer["0,10€"]['muenzen']=cash_drawer["0,10€"]['muenzen']-1
                    print("0,10€")

    print("Kaffe wird ausgegeben")


# Wenn kein Rückgeld mehr da ist, dann hängt sich die Kaffemaschine auf