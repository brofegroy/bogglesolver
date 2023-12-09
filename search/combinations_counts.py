from itertools import product

my_list = [["A","A","A","A"],["E","F","G","H"],["I","J","K","K"],["M","N","O","P"]]

#returns instances of each 3 long word that can be formed.
#example: AAF can be formed 5 different times in the example given above so combinations_count[0][0][6] = 5
#example: AAE can be formed 3 different times in the example given above so combinations_count[0][0][5] = 3
def get_all_3_combinations_count(board): #expects a 4x4 board
    pos1 = pos2 = pos3 = -1
    combinations_count_list = [[[0] * 26 for _ in range(26)] for _ in range(26)]
    initial_positions = [(i,j) for i,j in product(range(4), repeat = 2)]
    for i,j in initial_positions:
        pos1 = letter_value(board[i][j])
        for i1,j1 in get_neighbours(i,j):
            if i1<0 or j1<0 or i1>3 or j1>3:
                continue
            pos2 = letter_value(board[i1][j1])
            for i2,j2 in get_neighbours(i1,j1):
                if i2<0 or j2<0 or i2>3 or j2>3:
                    continue
                if i2 == i and j2 == j:
                    continue
                pos3 = letter_value(board[i2][j2])
                combinations_count_list[pos1][pos2][pos3] += 1
    combinations_count = tuple(tuple(tuple(inner_list) for inner_list in middle_list) for middle_list in combinations_count_list)
    return combinations_count

#helper functions
def convert_board_to_letter_value(board):
    conversion = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                  'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                  'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 
                  'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
                  'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = conversion[board[i][j]]
    return board

# print(convert_board_to_letter_value(my_list))

def get_neighbours(x,y):
    return [(x-1,y-1),(x,y-1),(x+1,y-1),
            (x-1,y),          (x+1,y),
            (x-1,y+1),(x,y+1),(x+1,y+1)]

def letter_value(letter): #expects a capital char alphabet
    return ord(letter) - ord("A")