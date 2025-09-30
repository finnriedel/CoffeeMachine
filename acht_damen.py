spalte = 8
zeile = 8
schachbrett = [[0 for x in range(spalte)] for y in range(zeile)]

#schachbrett[0][0] = 1

def pruefe(zeile, spalte):
    x = zeile 
    y = spalte

    #Vertikale Prüfung
    while(zeile >=0):  
       if(schachbrett[zeile-1][spalte]==1):    
           return False   
       else:
           zeile-=1
    zeile = x
    #Horizontale Prüfung    
    while(spalte >=0):  
       if(schachbrett[zeile][spalte-1]==1):    
           return False   
       else:
           spalte-=1
    spalte = y    
    #Diagonale Prüfung (Links)
    while(spalte >=0 and zeile >=0):
        if(schachbrett[zeile-1][spalte-1]==1):
            return False
        else:
            zeile-=1
            spalte-=1
    zeile = x
    spalte = y
    #Diagonale Prüfung (Rechts)
    while(spalte <=8 and zeile >=0):
        if(schachbrett[zeile-1][spalte+1]==1):
            return False
        else:
            zeile-=1
            spalte+=1
    zeile = x
    spalte = y
    return True

def setze(zeile, spalte):
    if pruefe(zeile, spalte) != False:
        schachbrett[zeile][spalte] = 1
        print("Dame gesetzt in Zeile:", zeile, "Spalte:", spalte)
        return True
    else:
        print("Dame konnte nicht gesetzt werden in Zeile:", zeile, "Spalte:", spalte)
        return False

def loesen(zeile):
    if zeile >= 8:
        return True
    for spalte in range(8):
      if(pruefe(zeile, spalte) == True):
        schachbrett[zeile] [spalte] = 1
        if loesen(zeile +1):
            return True
        schachbrett[zeile][spalte] = 0
    return False
print(loesen(0))  
    