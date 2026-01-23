import os
os.system("cls")


#eingabe der Spieler Namen
def spieler_eingabe():
    spieler1 = input("Bitte geben Sie den Namen des 1 Spielers ein: ")
    spieler2 = input("Bitte geben Sie den Namen des 2 Spielers ein: ")
        
    if not spieler1.isalpha() or not spieler2.isalpha():
        print("Fehler: Namen dürfen nur aus Buchstaben bestehen.")
        return None

    return spieler1, spieler2

print(spieler_eingabe())
    
   