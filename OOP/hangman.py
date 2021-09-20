import random

name = input("Hello. What is your name? \n")

print(f"Good Luck {name}!")

word_bank = ['bat', 'dog', 'ant',
         'shoe', 'love', 'blue',
         'python']

word_for_game = random.choice(word_bank)

print(word_for_game)

length_viewer = []
for letter in word_for_game:
    length_viewer.append("_")

print(f"Your chosen word has {len(word_for_game)} letters")

print("Guess one of the letters")

user_guesses = ' '
wrong_guesses = []
user_chances = 6

while user_chances > 0:

    wrong_guess = 0

    for letter in word_for_game:

        if letter in user_guesses:
            print(letter)

        else:
            print("_")

            wrong_guess += 1

    if wrong_guess == 0:

        print("Congratulations!!! You have won the game!!!")
        print(f"The word is, {word_for_game}")
        break

    user_answer = input("Guess a letter in the word \n")

    user_guesses += user_answer

    if user_answer not in word_for_game:
        user_chances -= 1
        wrong_guesses.append(user_answer)
        print("That guess is incorrect")
        print(f"You have {user_chances} chances left to guess the word")
        print(f"Previous wrong guesses are {wrong_guesses}")
        if user_chances == 0:
            print("Uh Oh! You lose!")


