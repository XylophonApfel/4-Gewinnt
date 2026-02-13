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
        move_spalte = move(spieler1, board)
        board = move_setzen(move_spalte, board)
        winner = "Nicht gewonnen"
        if check_horizontal(board, "x") == "Gewonnen":
            winner = "Gewonnen"
        elif check_vertical(board, "x") == "Gewonnen":
            winner = "Gewonnen"
        elif check_diagonal(board, "x") == "Gewonnen":
            winner = "Gewonnen"
        board = generate_board(board)
        if winner == "Gewonnen":
            print(f"{spieler1} gewinnt!")
            break

        move_spalte = move(spieler2, board)
        board = move_setzen2(move_spalte, board)
        winner = "Nicht gewonnen"
        if check_horizontal(board, "o") == "Gewonnen":
            winner = "Gewonnen"
        elif check_vertical(board, "o") == "Gewonnen":
            winner = "Gewonnen"
        elif check_diagonal(board, "o") == "Gewonnen":
            winner = "Gewonnen"
        board = generate_board(board)
        if winner == "Gewonnen":
            print(f"{spieler2} gewinnt!")


if __name__ == "__main__":
    main()