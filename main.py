from tui import *
from management import *
import os

os.system("cls")

def main():
    board = [[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]
    spieler1, spieler2 = spieler_eingabe()

    os.system("cls")
    board = generate_board(board)
    while True: # Spieler 1
        move_spalte, move_zeile = move(spieler1)
        board = move_setzen(move_spalte, move_zeile, board)
        winner = check_horizontal(board, spieler1)
        winner = check_diagonal(board, spieler1)
        winner = check_vertical(board, spieler1)
        board = generate_board(board)
        if winner == "Gewonnen":
            print(f"{spieler1} gewinnt!")
            break

        move_spalte, move_zeile = move(spieler2)        
        board = move_setzen2(move_spalte, move_zeile, board)
        winner = check_horizontal(board, spieler2)
        winner = check_diagonal(board, spieler2)
        winner = check_vertical(board, spieler2)
        board = generate_board(board)
        if winner == "Gewonnen":
            print(f"{spieler2} gewinnt!")


if __name__ == "__main__":
    main()