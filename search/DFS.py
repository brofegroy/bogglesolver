
#checks if word is formable from all starting squares
def is_DFS_formable(board,word):
    starting_squares = get_DFS_starting_squares(board,word)
    for starting_square in starting_squares:
        if is_DFS_formable_from_starting_square(board,word,starting_square):
            return True
    return False

#simply DFS a word 
def is_DFS_formable_from_starting_square(board,word,starting_square,traversed_paths = []): #expects board as captial letters
    remaining_word = word[1:]
    i,j = starting_square
    current_path = traversed_paths.copy()
    current_path.append((i,j))

    for i1,j1 in get_neighbours(i,j):
        if i1<0 or j1<0 or i1>3 or j1>3:
            continue
        if (i1,j1) in current_path:
            continue
        if not remaining_word[0] == board[i1][j1]:
            continue
        if len(remaining_word) == 1:
            return True
        if is_DFS_formable_from_starting_square(board,remaining_word,(i1,j1),current_path):
            return True
    return False

def get_neighbours(x,y):
    return [(x-1,y-1),(x,y-1),(x+1,y-1),
            (x-1,y),          (x+1,y),
            (x-1,y+1),(x,y+1),(x+1,y+1)]

def get_DFS_starting_squares(board,word):
    first_letter = word[0]
    starting_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == first_letter:
                starting_squares.append((i,j))
    return starting_squares

