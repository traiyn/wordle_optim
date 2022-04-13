from operator import concat
from re import L
from colorama import Fore
from colorama import Style
import os
import random
import stats

# SOLUTION = 'THORN'
WORD_LIST_PATH = 'C:\\source\\wordle_optim\\data\\'
WORD_LIST_DICT = {
    'POSSIBLE': 'words_possible.txt',
    'ALLOWED': 'words_allowed.txt',
    'ALPHA_FREQ_POSSIBLE': 'alpha_freq_allowed.json',
    'ALPHA_FREQ_ALLOWED': 'alpha_freq_possible.json'
}
# WORD_LIST_FILENAME = 'word_list_500.txt'
FONT_COLORS = {
    0 : Fore.WHITE,
    1 : Fore.YELLOW,
    2 : Fore.GREEN
}

def get_word_list(WORD_LIST_FILENAME):
    filepath = os.path.join(WORD_LIST_PATH, WORD_LIST_FILENAME)
    word_list_file = open(filepath, "r")
    word_list = word_list_file.read().split('\n')
    return word_list

def check_guess(_guess, _solution):
    _result = [0,0,0,0,0]
    for idx_guess, char_guess in enumerate(_guess):
        for idx_sol, char_sol in enumerate(_solution):
            if char_guess == char_sol:
                if idx_guess == idx_sol:
                    _result[idx_guess] = 2
                else:
                    if _result[idx_guess] < 2:
                        _result[idx_guess] = 1

    return _result

def apply_color(_guess, _result):
    j=0
    _result_color = ''
    while(j < len(_result)):
        colored = FONT_COLORS[_result[j]] + _guess[j] + Style.RESET_ALL
        _result_color += colored
        j+=1
    return _result_color

def print_guesses(_guesses):
    print('')
    print('-----')
    for _guess in _guesses:
        print(_guess)
    print('-----')
    print('')

def play_wordle(_allowed, _solution):
    guesses = []
    solved = False
    i=0
    result = []
    while(i <= 7 and not solved):
        guess = str.upper(input('Please enter your next guess:   '))
        if len(guess) != 5 or guess.lower() not in _allowed:
            print('Please use a valid 5 letter word.')
            continue
        if guess == _solution:
            solved = True
            print('You got it!')
        result = check_guess(guess, _solution)
        result_color = apply_color(guess, result)
        guesses.append(result_color)
        print_guesses(guesses)
        i += 1

def main():

    words_possible = get_word_list(WORD_LIST_DICT['POSSIBLE'])
    words_allowed = get_word_list(WORD_LIST_DICT['ALLOWED'])
    # stats.char_placement_freq(words) # already pulled for possible and allowed
    solution = random.choice(words_possible).upper()
    # stats.calc_freq_score(words_possible)
    play = True
    while play:
        play_wordle(words_allowed, solution)
        answer = input('Play again? Y/N: ')
        if answer == 'N':
            continue
    

if __name__ == '__main__':
    main()