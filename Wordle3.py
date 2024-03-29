# File: Wordle3.py

"""
Check whether the letters entered by the user form a word
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
)


def wordle():
    def enter_action(s):
        nonlocal current_row
        nonlocal game_over

        # Check if the game is over
        if game_over:
            return

        cleaned_input = str(s).strip().upper()

        # Check if the entered word has exactly 5 letters
        if len(cleaned_input) == 5 and cleaned_input.isalpha():
            if cleaned_input in [word.upper() for word in FIVE_LETTER_WORDS]:
                # Set the letters in the current row
                for col, letter in enumerate(cleaned_input):
                    gw.set_square_letter(current_row, col, letter)

                # Initialize square colors
                square_colors = [MISSING_COLOR] * 5
                word_copy = list(word)

                # First Pass: Check for correct positions
                for col, guess_letter in enumerate(cleaned_input):
                    if guess_letter == word[col]:
                        square_colors[col] = CORRECT_COLOR
                        word_copy[col] = None

                    # Second Pass: Check for presence in wrong positions
                    for col, guess_letter in enumerate(cleaned_input):
                        if square_colors[col] == MISSING_COLOR and guess_letter in remaining_word:
                            square_colors[col] = PRESENT_COLOR
                            remaining_word[remaining_word.index(guess_letter)] = None  # Remove one occurrence

                # Apply colors to the squares
                for col in range(len(cleaned_input)):
                    gw.set_square_color(current_row, col, square_colors[col])

                

                    # Move to the next row
                    current_row += 1
                    if current_row < N_ROWS:
                        gw.set_current_row(current_row)

                else:

                    # the word does not found in the dictionary, it shows "Not in the word list"
                    gw.show_message("Invalid Word. Press DELETE to try again.")

                    
            else:
                gw.show_message("Invalid Word. Press DELETE to try again.")
        else:
            gw.show_message("Please enter a 5-letter word.")

    # Set the current row = 0 and initialize game_over to False
    current_row = 0
    game_over = False
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Choose a random word from 5 letter words for the answer
    #word = random.choice(FIVE_LETTER_WORDS).upper()
    word = "GLASS"
    print(word)

    # Check of the character is match with the random word
    

if __name__ == "__main__":
    wordle()
