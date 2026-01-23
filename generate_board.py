board = [[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]

def generate_board():
    print("----------------")
    print("  1 2 3 4 5 6 7")
    for a in board:
        for i in range(6):
            print(f"{i+1} " + "|".join(board[i]))
        print("----------------") 
        return generate_board

generate_board()