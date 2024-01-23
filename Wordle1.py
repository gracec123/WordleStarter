# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
    #Choose a random word from 5 letter words
    word =  random.choice(FIVE_LETTER_WORDS)

    #Print the word on terminal
    print(word)

    # Display the solution word in the first row of boxes
    for col in range(N_COLS):
        gw.set_square_letter(0, col, word[col].upper())
    
if __name__ == "__main__":
    wordle()


