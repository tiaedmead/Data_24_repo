import random

def get_word():
    word_bank = ['bat', 'dog', 'ant',
                 'shoe', 'love', 'blue',
                 'python']

    word_for_game = random.choice(word_bank)
    return word_for_game.upper()

def play(word_for_game):
    word_completion = "_" * len(word_for_game)
    word_guessed = False
    guessed_letters = []
    guessed_words = []
    tries_left = 6
    print("Let's play hangman!")
    print(display_hangman_image(tries_left))
    print(word_completion)
    print("\n")
    while not word_guessed and tries_left > 0:
        user_guess = input("Please guess a letter or word: ").upper()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print(f"You already guessed the letter {user_guess}")
            elif user_guess not in word_for_game:
                print(f"{user_guess}, is not in the word")
                tries_left -= 1
                guessed_letters.append(user_guess)
            else:
                print(f"Good guess, {user_guess} is in the word")
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word_for_game) if letter == user_guess]
                for index in indices:
                    word_as_list[index] = user_guess
                word_completion = " ".join(word_as_list)
                if "_" not in word_completion:
                    word_guessed = True

        elif len(user_guess) == len(word_for_game) and user_guess.isalpha():
            if user_guess in guessed_words:
                print(f"You already guessed th word {user_guess}")
            elif user_guess != word_for_game:
                print(f"{user_guess}, is not the word")
                tries_left -= 1
                guessed_words.append(user_guess)
            else:
                word_guessed = True
                word_completion = word_for_game

        else:
            print("Not a valid guess")

        print(display_hangman_image(tries_left))
        print(word_completion)
        print("\n")

    if word_guessed:
        print("Congrats! You guessed the word. You Win!")
    else:
        print(f"You ran out of tries :( \n The word was {word_for_game}. Maybe next time!")

def display_hangman_image(tries_left):
    hangman_drawing_stages = ['''
       -----
       O   |
      /|\  |
      / \  |
    =========''', '''
       -----
       O   |
      /|\  |
      /    |
    =========''', '''
       -----
       O   |
      /|\  |
           |
    =========''', '''
       -----
       O   |
      /|   |
           |
    =========''', '''
       -----
       O   |
       |   |
           |
    =========''', '''
       -----
       O   |
           |
           |
    =========''']
    return hangman_drawing_stages[tries_left]

def main():
    word_for_game = get_word()
    play(word_for_game)
    while input("Play Again? (Y/N)").upper() == "Y":
        word_for_game = get_word()
        play(word_for_game)

main()