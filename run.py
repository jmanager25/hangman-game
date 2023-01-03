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
    Welcomes the player to the game, and asks them to
    input their name.
    """
    print("WELCOME TO THE HANGMAN GAME!\n")

    player_name = ""

    while True:
        player_name = input("Please enter your name:\n")

        if not player_name.isalpha():
            print("Your name must contain only letters\n")
            continue
        else:
            print(
                f"""\nHi there {player_name}! in this classic word guessing 
game, you will try to guess a secret word by inputing letters 
or word. You have 5 attempts to try to find the correct word.\n
Are you ready to put your vocabulary and problem solving skills
to the test? Let's get started!\n
                """
                )
        
        return player_name


def get_words():
    """
    Selects a ramdom word from the list of words provided.
    The words are returned in uppercase.
    """
    random_word = random.choice(words)
    return random_word.upper()
    

def main():
    """
    Contains all the functions of the game
    """
    start_game()
    get_words()


main()