import os 
os.system("cls")

def check_horizontal(board, player):
    zaehler = 0
    winner = "leer"
    for zeile in board:
        if winner == "Gewonnen": 
            break
        for feld in zeile:
            if feld == "x":
                zaehler += 1
                if zaehler == 4:
                    winner = "Gewonnen"
                    break
            else:
                zaehler = 0
                winner = "Nicht gewonnen"
                
    
    return winner

def check_vertical(board, player):
    zaehler = 0
    zaehler2 = 0
    winner = "leer"
    for zeile in board:
        for zeile2 in board:

            if winner == "Gewonnen": 
                break
            if zeile2[zaehler2] == "x":
                zaehler += 1
                if zaehler == 4:
                    winner = "Gewonnen"
                    break
            else:
                zaehler = 0
                winner = "Nicht gewonnen"
        if winner != "Gewonnen":
            zaehler2 += 1
    
    return winner

def check_diagonal(board, player):
    rows, cols = len(board), len(board[0])
    # \-Diagonale (links oben -> rechts unten)
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return "Gewonnen"
    # /-Diagonale (links unten -> rechts oben)
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return "Gewonnen"
    return "Nicht gewonnen"

    
#eingabe der Spieler Namen
def spieler_eingabe():
    spieler1 = input("Bitte geben Sie den Namen des 1 Spielers ein: ")
    spieler2 = input("Bitte geben Sie den Namen des 2 Spielers ein: ")
        
    if not spieler1.isalpha() or not spieler2.isalpha():
        print("Fehler: Namen dürfen nur aus Buchstaben bestehen.")
        return None

    return spieler1, spieler2

print(spieler_eingabe())


def move():
    while True:
        try:
            move_Zeile = int(input("Bitte gebe die Zeile ein (1-6):\n "))
            if move_Zeile >= 1 and move_Zeile <= 6:
                break
            else:
                print("Zahl muss zwischen 1 und 6 liegen.")
                continue
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

        move_Spalte= int(input("Bitte die Spalte eingeben (1-7): \n"))
    while True:
        try:
            move_Spalte= int(input("Bitte die Spalte eingeben (1-7): \n"))
            if move_Spalte >= 1 and move_Spalte <= 6:
                break
            else:
                print("Zahl muss zwischen 1 und 6 liegen.")
                continue
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
    return move_Spalte, move_Zeile
