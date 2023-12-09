

my_list = ["ABCD","EFGH","IJKK","MNOP"]

def get_total_letter_counts(board):
    letter_counts = [0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for line in board:
        for letter in line:
            letter_value = ord(letter) - ord("A")
            letter_counts[letter_value] += 1
    return letter_counts
            
# print(get_total_letter_counts(my_list))