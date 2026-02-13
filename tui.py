
def generate_board(board):
    print("  1 2 3 4 5 6 7")
    print(" +-------------+")
    for row in board:
        print(" |" + "|".join(row) + "|")
    print(" +-------------+")
    return board
    