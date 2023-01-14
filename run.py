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


def get_player_input(random_word, guessed_letters):
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
                    f"""please enter a valid letter, you have
                    entered {player_guess}"""
                )
            elif len(player_guess) > 1:
                if player_guess != random_word:
                    raise ValueError(
                        f"""Wrong word, {player_guess} is not the word"""
                    )
                else: 
                    print(f"You Win! {player_guess} is the word")
                    return
            elif player_guess in guessed_letters:
                raise ValueError(
                    f"You already guessed {player_guess}"
                )
            break
        except ValueError as e:
            print(e)
    return player_guess
    

def play_game(random_word):
    """
    Executes the main logic of the game. checks if the player's
    input is in the secret word or not.
    """
    blank_space = "_" * len(random_word)
    guessed_letters = []
    attempts = 6 
    if attempts > 0:
        print(hangman_draw(attempts))
        print("Word: ", blank_space)
    player_guess = get_player_input(random_word, guessed_letters)
    if player_guess in random_word:
        new_blank_space = ""
        for i in range(len(random_word)):
            if random_word[i] == player_guess:
                new_blank_space += blank_space
            else:
                new_blank_space += blank_space[i]
        blank_space = new_blank_space
        if "_" not in blank_space:
            print("Congratulations, YOU WIN!")
    else:
        attempts -= 1
        hangman_draw(attempts)
    return attempts


def hangman_draw(attempts):
    """
    Draws the hangman graphics to be displayed if the
    player guess wrong the letter or word.
    """
    if attempts == 6:
        print(" ==========       ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 5:
        print(" ==========       ")
        print("||       |        ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
        print("||                ")
    elif attempts == 4:
        print(" ==========       ")
        print("||       |        ")
        print("||       0        ")
        print("||                ")
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
    start_game()
    get_words()
    game_logic = play_game(get_words())


main()