import random

# Words to guess
words = [
    "abruptly", "absurd", "lengths", "luxury", "avenue", "transcript",
    "transplant",
    "nightclub", "nowadays", "unknown", "nowadays", "oxygen", "pneumonia", 
    "gossip",
    "jackpot", "buffalo", "espionage", "strength", "scratch", "jigsaw", 
    "zombie",
    "duplex", "duplex"
]


def start_game():
    """
    Welcomes the player to the game, asks their name and gives them the 
    choice to play the game or read the rules
    """
    print(
        """
        Welcome to the Hangman Game! In this classic word guessing 
        game, you will try to guess a secret word by inputing letters 
        or word. You have 5 attempts to try to find the correct word.\n
        Are you ready to put your vocabulary and problem solving skills
        to the test? Let's get started!\n
        """)

    player_name = ""

    while True:
        player_name = input("Please enter your name:\n")

        if not player_name.isalpha():
            print("Your name must contain only letters\n")
            continue
        else:
            break
    

start_game()
