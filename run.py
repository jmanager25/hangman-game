import random
import os
from time import sleep
from words import words
import art


def clear_terminal():
    """
    Clears the terminal
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def start_game():
    """
    Welcomes the player to the game, and asks them to
    input their name.
    """
    sleep(5)
    clear_terminal()
    art.hangman_art()
    while True:
        player_name = input("Please enter your name:\n")
        if not player_name.isalpha():
            print("Your name must contain only letters\n")
            continue
        else:
            clear_terminal()
            print(
                f"""
                Hi there {player_name}! Welcome to the classic word guessing
                game, Hangman! You will try to guess a secret word by inputting
                letters or words. Be careful, as you only have 7 wrong attempts
                before the man is hanged.\n
                Are you ready to put your vocabulary and problem solving skills
                to the test? Let's get started!
                Good luck!\n
                """
                )
        return player_name


def get_words():
    """
    Selects a random word from the list of words provided.
    The word is returned in uppercase.
    """
    random_word = random.choice(words)
    return random_word.upper()


def get_player_input(guessed_letters, guessed_words):
    """
    Allows the player to input the letter or word into
    the terminal and also includes a try-except statement to
    raise ValueErrors.
    """
    while True:
        player_guess = input("\nPlease enter a letter:\n").upper()
        try:
            if not player_guess.isalpha():
                raise ValueError(
                    f"\nEnter a valid letter, {player_guess} is not a letter."
                )
            elif len(player_guess) > 1 and player_guess in guessed_words:
                raise ValueError(
                    f"\nYou already guessed {player_guess}."
                )
            elif len(player_guess) == 1 and player_guess in guessed_letters:
                raise ValueError(
                    f"\nYou already guessed {player_guess}."
                )
            return player_guess
        except ValueError as err:
            print(f"{err} Try again")


def play_game(random_word, player_name):
    """
    Executes the main logic of the game. Keeps track of the player's
    attempts, guessed letters and words. Updates the hangman draw
    in case of wrong attempts and uncover the letters in case of
    correct guess. It ultimatly determines if the player wins or
    loses based on their correct guessing of the secret word before
    running out of attempts.
    """
    blank_space = "_" * len(random_word)
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print(hangman_draw(attempts))
    print(f"\n{len(random_word)} letter Word: ")
    print(blank_space)
    while attempts > 0:
        player_guess = get_player_input(guessed_letters, guessed_words)
        if len(player_guess) == 1 and player_guess not in random_word:
            print(f"\n{player_guess} is not in the word")
            attempts -= 1
            guessed_letters.append(player_guess)
        elif len(player_guess) == 1 and player_guess in random_word:
            print(f"\n{player_guess} is in the word")
            guessed_letters.append(player_guess)
            # Replaces the underscores with correctly guessed letters.
            indices = [i for i, letter in enumerate(random_word) if letter ==
                       player_guess]
            blank_space = "".join([random_word[i] if i in indices else x for i,
                                  x in enumerate(blank_space)])
            if "_" not in blank_space:
                print(
                    f"""
                    Congratulations {player_name}, {random_word}
                    is the word, YOU WIN!
                    """
                    )
                art.you_win()
                break
        elif len(player_guess) > 1:
            if player_guess != random_word:
                print(f"\n{player_guess} is not the word")
                attempts -= 1
                guessed_words.append(player_guess)
            else:
                print(
                    f"""
                    Congratulations {player_name}, {player_guess}
                    is the word, YOU WIN!
                    """
                    )
                art.you_win()
                break
        sleep(2)
        clear_terminal()
        print("Guessed letters: ", guessed_letters, "\n")
        print(hangman_draw(attempts), "\n")
        print("Attempts left: ", attempts)
        print(f"\n{len(random_word)} letter Word:\n")
        print(blank_space)
    if attempts == 0:
        print(f"\nSorry {player_name}, {random_word} was the word, YOU LOSE!")
        art.you_lose()


def play_again(random_words, player_name):
    """
    Gives the player the option to play Again. If they chose yes, restarts
    the game if not exit the game.
    """
    while True:
        restart_game = input("\nDo you want to play Again? (y/n)\n").lower()
        if restart_game == "y":
            clear_terminal()
            art.hangman_art()
            random_words = get_words()
            play_game(random_words, player_name)
        elif restart_game == 'n':
            clear_terminal()
            return
        else:
            print("\nPlease enter 'y' for yes or 'n' for no")


def hangman_draw(attempts):
    """
    Draws the hangman graphics to be displayed if the
    player guess wrong the letter or word.
    """
    if attempts == 7:
        print(" ==========       ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 6:
        print(" ==========       ")
        print("||       |        ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 5:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 4:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||       |        ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 3:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|        ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 2:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|\\      ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 1:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|\\      ")
        print("||      /         ")
        print("||                ")
        print("||                ")
    elif attempts == 0:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|\\      ")
        print("||      / \\      ")
        print("||                ")
        print("||                ")


def main():
    """
    Contains all the functions of the game
    """
    art.introduction_art()
    player_name = start_game()
    random_words = get_words()
    play_game(random_words, player_name)
    play_again(random_words, player_name)


main()
