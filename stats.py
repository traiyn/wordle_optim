import string
import copy
import json
import os

class Letter:
    def __init__(self, _char):
        self.char = _char
        self.first = 0
        self.second = 0
        self.third = 0
        self.fourth = 0
        self.fifth = 0


def char_placement_freq(word_list):

    alphabet = list(string.ascii_lowercase)
    wordle_placements = [0,1,2,3,4]
    wordle_counts = [0] * 5
    wordle_dict = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0
    }
    wordle_list = [copy.deepcopy(wordle_dict) for i in range(26)]
    alphabet_freq = dict(zip(alphabet, wordle_list))
    for word in word_list:
        for pos, letter in enumerate(word):
            alphabet_freq[letter][pos] += 1
            print(alphabet_freq[letter][pos])

    with open('data\\alpha_freq_allowed.json', 'w') as f:
        json.dump(alphabet_freq, f)

    print(alphabet)


def calc_freq_score(word_list):
    filepath = os.path.join("C:\\source\\wordle_optim\\data\\", "alpha_freq_possible.json")
    scores = [0] * len(word_list)
    word_scores = dict(zip(word_list, scores))
    with open(filepath) as alpha_freq_file:
        alpha_freq = json.load(alpha_freq_file)

    for word in word_list:
        freq_score = 0
        for pos, char in enumerate(word):
            score = alpha_freq.get(char).get(str(pos))
            freq_score += score
        
        word_scores[word] = freq_score
    
    with open('data\\freq_score_possible.json', 'w') as f:
        json.dump(word_scores, f)
    
    print(word_scores)