# File: Wordle4.py

"""
Check whether the letters entered by the user form a word
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from Adjusted_Modified_WordleGraphics import (
    WordleGWindow,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
    toggle_colors,
)
import Adjusted_Modified_WordleGraphics


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
                square_colors = [Adjusted_Modified_WordleGraphics.MISSING_COLOR] * 5
                word_copy = list(word)

                # First Pass: Check for correct positions
                for col, guess_letter in enumerate(cleaned_input):
                    if guess_letter == word[col]:
                        square_colors[
                            col
                        ] = Adjusted_Modified_WordleGraphics.CORRECT_COLOR
                        word_copy[col] = None

                # Second Pass: Check for presence in wrong positions
                for col, guess_letter in enumerate(cleaned_input):
                    if (
                        square_colors[col]
                        == Adjusted_Modified_WordleGraphics.MISSING_COLOR
                        and guess_letter in word_copy
                    ):
                        square_colors[
                            col
                        ] = Adjusted_Modified_WordleGraphics.PRESENT_COLOR
                        word_copy[word_copy.index(guess_letter)] = None

                # Apply colors to the squares and update keyboard keys
                for col in range(len(cleaned_input)):
                    gw.set_square_color(current_row, col, square_colors[col])
                    key_color = gw.get_key_color(cleaned_input[col])
                    if (
                        square_colors[col]
                        == Adjusted_Modified_WordleGraphics.CORRECT_COLOR
                    ):
                        gw.set_key_color(
                            cleaned_input[col],
                            Adjusted_Modified_WordleGraphics.CORRECT_COLOR,
                        )
                    elif (
                        square_colors[col]
                        == Adjusted_Modified_WordleGraphics.PRESENT_COLOR
                        and key_color != Adjusted_Modified_WordleGraphics.CORRECT_COLOR
                    ):
                        gw.set_key_color(
                            cleaned_input[col],
                            Adjusted_Modified_WordleGraphics.PRESENT_COLOR,
                        )

                # Check for win condition
                if all(
                    color == Adjusted_Modified_WordleGraphics.CORRECT_COLOR
                    for color in square_colors
                ):
                    gw.show_message(f"Congrats! You've guessed the word {word}!")
                    gw.set_game_over(True)
                else:
                    current_row += 1
                    if current_row < N_ROWS:
                        gw.set_current_row(current_row)
                    elif current_row == N_ROWS:
                        gw.show_message(f"Game Over! The word was {word}.")
                        gw.set_game_over(True)
            else:
                gw.show_message("Invalid Word. Press DELETE to try again.")
        else:
            gw.show_message("Please enter a 5-letter word.")

    # Set the current row = 0 and initialize game_over to False
    current_row = 0
    game_over = False
    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)

    # Choose a specific word or a random word from 5-letter words for the answer, in upper case
    word = random.choice(FIVE_LETTER_WORDS).upper()
    # word = "GLASS"
    print(word)


if __name__ == "__main__":
    wordle()
