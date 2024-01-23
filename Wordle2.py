# File: Wordle2.py

"""
Check whether the letters entered by the user form a word

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    # Run Function when player type in and enter the word
    def enter_action(s):
        nonlocal current_row

        # Check if there are available rows
        if current_row < N_ROWS:

            cleaned_input = str(s)
            cleaned_input = cleaned_input.strip() 
             # Check if the entered word has exactly 5 letters
            if cleaned_input.isalpha() and len(cleaned_input) == 5:

                print("Length of entered word:", len(cleaned_input))
                print("Entered word:",  cleaned_input)

                # Check If the word is in the WordleDictionary
                if  cleaned_input.lower() in FIVE_LETTER_WORDS:

                    # the word is in the dictionary, it shows "legitimate word"
                    gw.show_message("It's a legitimate word.")
                else:

                    # the word does not found in the dictionary, it shows "Not in the word list"
                    gw.show_message("Not in word list. Try again.")
            
                # Set the letters in the current row
                for col, letter in enumerate(cleaned_input.upper()):
                    gw.set_square_letter(current_row, col, letter)

                # Move to the next row
                current_row += 1

                # If there are more rows, update the current row in the graphics window
                if current_row < N_ROWS:
                    gw.set_current_row(current_row)


                    
            else:
                # Display an error message if the entered word doesn't have exactly 5 letters
                gw.show_message("Please enter a 5-letter word.")
                print("Length of entered word:", len(cleaned_input))
                print("Entered word:", s)
        else:
            gw.show_message("You've used all rows!")

    # Set the current row = 0
    current_row = 0
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Choose a random word from 5 letter words for the answer
    word = random.choice(FIVE_LETTER_WORDS)
    print(word)

# Startup code
if __name__ == "__main__":
    wordle()
