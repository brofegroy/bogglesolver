from .DFS import *
from .preliminary_checks import *
from .letter_counts import *
from .combinations_counts import *


mylist = ['ASDF', 'UIOP', 'QWER', 'UIOO']

def is_Q_in_board(board):
    return any(("Q" in line for line in board))

def get_preliminary_values(board,wordlist):
    lettercount = get_total_letter_counts(board)
    combinations_count = get_all_3_combinations_count(board)

def get_formable_words(board,wordlist,letter_counts,combination_counts):

    formable_words = []

    for word in wordlist:
        if is_pass_preliminary_check(word,letter_counts,combination_counts):
            if is_DFS_formable(board,word):
                formable_words.append(word)

    return formable_words

    



