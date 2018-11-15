'''

@author: Arnav Garg
@Date: 10/27/2018

Check README.txt for instructions on how to run.
'''

import requests
import re
from collections import defaultdict
import sys
import json
import argparse

class Status:
    ALIVE = 'ALIVE'
    DEAD = 'DEAD'
    FREE = 'FREE'


def read_wordlist_file(filename):
    '''
        A function to read all the words in the
        worddict that I got online and return the list. 

        Return -> List
    '''
    global_word_list = []
    with open(filename, 'r') as f:
        for line in f:
            global_word_list.append(line)
    return global_word_list


def send_guess(guess, token):
    '''
        A function to send the guessed word and the token to the 
        API

        Return -> None
    '''
    post_url = 'http://gallows.hulu.com/play?code=arnavgarg@cs.ucla.edu&token={}&guess={}'.format(token, guess)
    res = requests.post(post_url)
    return json.loads(res.text)


def word_database_search(word, global_word_list, char_freq):
    '''
        This is the most important function. This is responsible
        for finding all the words that are a potential match for 
        the current state and based on that updating the char freq
        mapping. 

        Return -> None
    '''
    regex  = '^' + word.replace('_', '[a-z]') + '$'
    # Going over each word in my dictionary and checking 
    # if that could be a potential word or not. 
    for list_word in global_word_list:
        if len(list_word) == len(word)+1:
            result = re.search(regex, list_word, re.IGNORECASE)
            if result:
                # if found a woed, then we add it to the freq mapping. 
                for i, char in enumerate(word):
                    if word[i] == '_':
                        char_at_i = result.group(0)[i].lower()
                        char_freq[char_at_i] += 1


def guess_letter(state, guessed_words, global_word_list):
    '''
        Takes in the current state, list of already guessed words, and a 
        global word list, and predicts which is the most probable
        word we should choose next. 

        Return: Char -> most probable next word. 
    '''
    # getting all the individual words. 
    wordList = state.split(' ')
    # char to freq mapping.
    char_freq = defaultdict(int)
    for word in wordList:
        if '_' in word:
            # calling function to fill the freq mapping.
            word_database_search(word, global_word_list, char_freq)
    # getting the most freq char that hasn't been guessed before.
    char_freq_list = sorted(char_freq.items(), key=lambda x: -x[1])
    i = 0
    # this is the fail safe if my word list falls short
    if not char_freq_list:
        for char in string.ascii_lowercase:
            if char not in guessed_words:
                return char
    max_char_freq = char_freq_list[i][0]
    while max_char_freq in guessed_words:
        i += 1
        max_char_freq = char_freq_list[i][0]
    return max_char_freq


def main():
    '''
        The main function. Responsible for knitting everything together

        Return: None
    '''
    parser = argparse.ArgumentParser(description='Hangman Game for Hulu')
    parser.add_argument("-v", "--verbose", dest='verbose', action="count", default=0,
                        help="-vv for more verbose")

    args = parser.parse_args()

    URL = 'http://gallows.hulu.com/play?code=arnavgarg@cs.ucla.edu'
    filename = 'wordlist.txt'
    global_word_list = read_wordlist_file(filename)
    tries = 0
    wins, loses = 0, 0
    while True:
        # Getting the json from the url provided. 
        req = requests.get(url=URL)
        data = req.json()
        # set of words already guesses by my program.
        guessed_words = set()
        # Keep going till the status changes.
        while data['status'] == Status.ALIVE:
            state = data['state']
            # function to help guess what the next best possible word would be. 
            guess = guess_letter(state, guessed_words, global_word_list)
            # adding it to the list of words that I have already guessed. 
            guessed_words.add(guess)
            # Send the guess. 
            data = send_guess(guess, data['token'])
            if args.verbose == 2:
                print('State: {} || Guessed: \"{}\" || Remaining Guesses: {}'.format(data['state'], guess, data['remaining_guesses']))
        
        result = ''

        if data['status'] == Status.FREE:
            wins += 1
            result = 'WON'
        else:
            loses += 1
            result = 'LOST'

        print()
        if args.verbose  > 0:
            print('Result: {} || Token: {} || State: {}'.format(result, data['token'], data['state']))
        else:
            print('Result: {} || Token: {}'.format(result, data['token']))
        tries += 1 
        print()

    print('Win percent: ', wins/500)


if __name__ == '__main__':
    main()
