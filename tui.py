
def generate_board(board):
    print("----------------")
    print("  1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(f"{i+1} " + "|".join(row))
    print("----------------")
    return board
    