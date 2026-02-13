import os 
os.system("cls")

def check_horizontal(board, player):
    for zeile in board:
        zaehler = 0
        for feld in zeile:
            if feld == player:
                zaehler += 1
                if zaehler == 4:
                    return "Gewonnen"
            else:
                zaehler = 0

    return "Nicht gewonnen"

def check_vertical(board, player):
    rows = len(board)
    cols = len(board[0])
    for col in range(cols):
        zaehler = 0
        for row in range(rows):
            if board[row][col] == player:
                zaehler += 1
                if zaehler == 4:
                    return "Gewonnen"
            else:
                zaehler = 0

    return "Nicht gewonnen"

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
    spieler1 = str(input("Bitte geben Sie den Namen des 1 Spielers ein: "))
    spieler2 = str(input("Bitte geben Sie den Namen des 2 Spielers ein: "))
        
    if not spieler1.isalpha() or not spieler2.isalpha():
        print("Fehler: Namen dürfen nur aus Buchstaben bestehen.")
        return None

    return spieler1, spieler2



def move(spieler, board):
    while True:
        try:
            move_Spalte = int(input(f"{spieler} bitte die Spalte eingeben (1-7): \n"))
            if move_Spalte < 1 or move_Spalte > 7:
                print("Zahl muss zwischen 1 und 7 liegen.")
                continue
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
            continue

        col_index = move_Spalte - 1
        if board[0][col_index] != " ":
            print("Spalte ist voll!")
            continue

        return move_Spalte

def move_setzen(move_spalte, board):
    col_index = int(move_spalte) - 1
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = "x"
            break

    return board

def move_setzen2(move_spalte, board):
    col_index = int(move_spalte) - 1
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = "o"
            break

    return board
