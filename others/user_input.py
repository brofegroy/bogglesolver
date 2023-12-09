

#function for board input form user

def get_board_input():
    board = []
    with open("board.txt", 'r') as file:
        board = file.readline().strip().split()
    cond1 = all(line.isalpha() for line in board)
    cond2 = all(len(line)==4 for line in board) 
    cond3 = len(board)==4
    if  cond1 and cond2 and cond3:
        print("valid board")
        board = [line.upper() for line in board]
        return board
    else: print("invalid board")
    return []
