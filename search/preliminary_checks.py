
#preliminary checks to prevent unnecessary DFS of every word
def is_pass_preliminary_check(word,lettercount,combinations_count):
    if word == "QEERISH":
        print("check started")
    if not is_all_letters_inside_board(word,lettercount):
        return False
    if not is_all_3long_formable(word,combinations_count):
        return False
    if word == "QEERISH":
        print("check passed")
    return True

def is_all_letters_inside_board(word,lettercount):
    word_letter_counts = [0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for letter in word:
        letter_value = ord(letter) - ord("A")
        word_letter_counts[letter_value] += 1
    # print(f"the word letter count is {word_letter_counts}")
    # print(f"the baor letter count is {lettercount}")
    for letter in range(26):
        if word_letter_counts[letter] > lettercount[letter]:
            return False
    return True

def is_all_3long_formable(word,combinations_count):
    required_3longs = [[],[]]
    for x in range(len(word)-2):
        i = letter_value(word[x])
        j = letter_value(word[x+1])
        k = letter_value(word[x+2])
        if [i,j,k] in required_3longs[0]:
            position = required_3longs[0].index([i,j,k])
            required_3longs[1][position] += 1
        else:
            required_3longs[0].append([i,j,k])
            required_3longs[1].append(1)
    
    for x in range(len(required_3longs[0])):
        i,j,k = required_3longs[0][x]
        if not combinations_count[i][j][k] >= required_3longs[1][x]:
            return False
    return True


def letter_value(letter): #expects a capital char alphabet
    return ord(letter) - ord("A")

def is_board_contain_q(letter_counts):
    return not letter_counts[16]==0  