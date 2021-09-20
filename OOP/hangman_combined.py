minimum_word_length = 5
maximum_word_length = 15
def get_word_input():
    prompt = """Please enter a word that meets the following criterion:
    1. A single word with no spaces
    2. Only letters accepted
    3. Minimum length of 5 characters
    4. Maximum length of 15 characters"""
    print(prompt)
    word = ""
    invalid_input = True
    while invalid_input:
        word = input("Please enter your hidden word: ")
        word_length = len(word)
        # 1. Check if word is suitable length
        if word_length < minimum_word_length or word_length > maximum_word_length:
            continue    # Runs loop again
        # 2. Check of word is letters only
        if not word.isalpha():
            continue
        # 3. All criterion met, set flag to false
        invalid_input = False
    print('\n' * 400)
    current_output = '_' * len(word)
    print(current_output)
    return word

def get_user_character_input():
    invalid_input = True
    guess = ""
    while invalid_input:
        guess = input("Please enter a character: ")
        # 1. Check if word is suitable length
        if len(guess) != 1 or not guess.isalpha():
            print("Your input was invalid, please enter a single character as a letter.")
            continue  # Runs loop again
        # 2. Input is valid
        invalid_input = False
        return guess

def check_guess_in_word(guess: str, char_count: int, guess_so_far: str):
    for i in range(len(word)):
        if word[i] == guess:
            char_count += 1
            guess_so_far = guess_so_far[:i] + guess + guess_so_far[i + 1:]
    return [char_count, guess_so_far]

def display_hangman_image(lives):
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
    return hangman_drawing_stages[lives]

# Start game
word = get_word_input()
word_length = len(word)
correct_char_count = 0
guess_output = ['_'] * word_length
lives = 6
# print(display_hangman_image(lives))
incorrect_characters = set(()) # A set disallowing duplicated but allowing addition
while correct_char_count != word_length:
    # 1. Get the users guess
    guess = get_user_character_input()
    guess_incorrect = True
    # 2. Check if guess is inside character
    for i in range(word_length):
        if word[i] == guess:
            guess_incorrect = False
            correct_char_count += 1
            guess_output[i] = guess
    if guess_incorrect:
        incorrect_characters.add(guess)
        lives -= 1
    print(f"Your guess: {guess_output}\nLives Remaining: {lives}\nIncorrect characters: {incorrect_characters}\n")
    print(display_hangman_image(lives))
    if lives <= 0:
        break
if lives <= 0:
    print(f"You ran out of lives, the correct word was {word}")
else:
    print(f"Congratulations, you guessed the word ({word})")