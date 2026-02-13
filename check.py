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

liste = [["x", "-", "-", "x", "x", "x", "-"],["-", "x", "-", "-", "x", "-", "-"],["-", "-", "x", "x", "x", "-", "-"],["x", "x", "-", "x", "x", "-", "-"],["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"]]
winner = check_diagonal(liste, "x")
print(winner)