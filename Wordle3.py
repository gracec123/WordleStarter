# File: Wordle3.py

"""
Check whether the letters entered by the user form a word

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

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

                    # Set the letters in the current row
                    for col, letter in enumerate(cleaned_input.upper()):
                        gw.set_square_letter(current_row, col, letter)

  
                
                    # ...
                    # After the first pass for correct positions
                    # Create a copy of the word to keep track of matched letters
                    remaining_word = list(word)

                    # Create a list to store the color for each square
                    square_colors = [MISSING_COLOR] * len(cleaned_input)

                    for col, guess_letter in enumerate(cleaned_input):
                        word_letter = word[col]

                        # First Pass: Check for correct positions
                        if guess_letter == word_letter:
                            square_colors[col] = CORRECT_COLOR
                            remaining_word[col] = None  # Remove this letter from remaining_word

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

                    # If there are more rows, update the current row in the graphics window
                    if current_row < N_ROWS:
                        gw.set_current_row(current_row)

                else:

                    # the word does not found in the dictionary, it shows "Not in the word list"
                    gw.show_message("Invalid Word. Press DELETE to try again.")

                    
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
    #word = random.choice(FIVE_LETTER_WORDS).upper()
    word = "GLASS"
    print(word)

    # Check of the character is match with the random word
    

# Startup code
if __name__ == "__main__":
    wordle()
