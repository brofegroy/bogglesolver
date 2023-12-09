from others.user_input import get_board_input
from others.make_excel import make_excel
from search.DFS_controller import *

def main():
    board = get_board_input()
    if not board:
        raise ValueError("input for board must be in the form <ABCD EFGH IJKL MNOP.py> where the ABC can be any alphabetical letters")
    letter_counts = get_total_letter_counts(board)
    combination_counts = get_all_3_combinations_count(board)

    formable_words = [[] for _ in range(3,17)]

    for x in range(3,17):
        wordlist = []
        with open(f"raw/split_length/noQs/csw22_{x}s.txt") as file:
            wordlist = [word.strip() for word in file.readlines()]

        formable_words[x-3] += get_formable_words(board,wordlist,letter_counts,combination_counts)

    if is_board_contain_q(letter_counts): 
        for x in range(3,17):
            wordlist = []
            with open(f"raw/split_length/Qs/csw22_Q{x}s.txt") as file:
                wordlist = [word.strip() for word in file.readlines()]

            formable_words[x-3] += get_formable_words(board,wordlist,letter_counts,combination_counts)
        for x in range(3,17): #assumes only a single Q
            wordlist = []
            with open(f"raw/split_length/QUs/csw22_QU{x-1}s.txt") as file:
                wordlist = [word.strip() for word in file.readlines()]
            
            formable_words[x-3] += [word.replace("Q","QU") for word in get_formable_words(board,wordlist,letter_counts,combination_counts)]

    totallength = sum(len(sublist) for sublist in formable_words)

    print(f"total length is {totallength}")
    print(formable_words)
    make_excel(board,formable_words)

main()




