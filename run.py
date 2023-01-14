import random

# Words to guess
"""
words = [
    "abruptly", "absurd", "lengths", "luxury", "avenue", "transcript",
    "transplant",
    "nightclub", "nowadays", "unknown", "nowadays", "oxygen", "pneumonia", 
    "gossip",
    "jackpot", "buffalo", "espionage", "strength", "scratch", "jigsaw", 
    "zombie",
    "duplex", "duplex"
]
"""
words = ["Hello"]

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
or word. You have 6 attempts to try to find the correct word.\n
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


def get_player_input(guessed_letters, guessed_words):
    """
    Allows the player to input the letter or word into
    the terminal and also includes a try-except statement to
    raise ValueErrors.
    """
    while True:
        player_guess = input("Please enter a letter:\n").upper()
        try:
            if not player_guess.isalpha():
                raise ValueError(
                    f"""Enter a valid letter, {player_guess} is not a letter"""
                )
            elif len(player_guess) > 1 and player_guess in guessed_words:
                raise ValueError(
                    f"You already guessed {player_guess}"
                )                
            elif len(player_guess) == 1 and player_guess in guessed_letters:
                raise ValueError(
                    f"You already guessed {player_guess}"
                )
            return player_guess
        except ValueError as e:
            print(f"{e} Try again")
    

def play_game(random_word, player_Name):
    """
    Executes the main logic of the game. checks if the player's
    input is in the secret word or not.
    """
    blank_space = "_" * len(random_word)
    guessed_letters = []
    guessed_words = []
    attempts = 7 
    game_over = False
    print(hangman_draw(attempts))
    print("Word: ", blank_space)
    while attempts > 0:
        player_guess = get_player_input(guessed_letters, guessed_words)
        if player_guess not in random_word:
            print(f"{player_guess} is not in the word")
            attempts -= 1
            guessed_letters.append(player_guess)
        elif player_guess in random_word:
            print(f"{player_guess} is in the word")
            guessed_letters.append(player_guess)

            """
            The variable 'indices' is used to store the list of indices
            where the letter is found. Then, the list comprehension iterates
            through the blank_space and check if the index is in the indices 
            list and if it is it will replace it with the letter itself. 
            finally, it joins the list to form a string.
            """
            indices = [i for i, letter in enumerate(random_word) if letter ==
            player_guess]
            blank_space = "".join([random_word[i] if i in indices else x for i, 
            x in enumerate(blank_space)])
            if "_" not in blank_space:
                game_over = True
                print(f"Congratulations {player_Name}, YOU WIN!")
                break
        print(hangman_draw(attempts))
        print(blank_space)
    if attempts == 0:
        print(f"Sorry {player_Name}, YOU LOSE!")

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
        print(" =========        ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|\       ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 1:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|\       ")
        print("||      /         ")
        print("||                ")
        print("||                ")
    elif attempts == 0:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||      /|\       ")
        print("||      / \       ")
        print("||                ")
        print("||                ")



def main():
    """
    Contains all the functions of the game
    """  
    player_name = start_game()
    ramdom_words = get_words()
    play_game(ramdom_words, player_name)


main()