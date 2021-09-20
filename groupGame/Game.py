import random

print("Hello and welcome to the animal guessing game")
user_name = input("What is your name? >>> ")
print(f"Good luck {user_name} \n")

animal_bank = ["hyena", "mouse", "dolphin", "cheetah", "elephant", "bat", "human", "squirrel", "whale", "hedgehog",
               "rabbit", "fox", "deer", "seal", "polar bar", "platypus",

               "kiwi", "ostrich", "eagle", "hummingbird", "swan", "toucan",

               "corn snake", "komodo dragon", "crocodile", "gecko", "chameleon", "anaconda", "tortoise"]


animal_bank_mammal = ["hyena", "mouse", "dolphin", "cheetah", "elephant", "bat", "human", "squirrel", "whale",
                      "hedgehog", "rabbit", "fox", "deer", "seal", "polar bar", "platypus"]

animal_bank_bird = ["kiwi", "ostrich", "eagle", "hummingbird", "swan", "toucan"]

animal_bank_reptile = ["corn snake", "komodo dragon", "crocodile", "gecko", "chameleon", "anaconda", "tortoise"]


animal_for_game = "kiwi" #random.choice(animal_bank)
print(animal_for_game)

print("Here are all the animals I know:")
for animal in animal_bank:
    print(animal)

print("\n")
print("I am now thinking of an animal")

user_tries = 4

while user_tries > 0:

    print("choose a question to ask me")
    print("1). is your animal warm-blooded?")
    print("2). does your animal lay hard-shell eggs?")
    print("3). how big is your animal?")
    print("4). is your animal a carnivore?")
    print("5). how many legs does your animal have?")
    print("6). can your animal fly? \n")

    question_choice = input("choose a number from 1-6 >>> ")

    if question_choice == "1" and animal_for_game in animal_bank_mammal:
        print("Yes the animal I am thinking of is warm-blooded")

    else:
        print("Nope my animal is not warm-blooded \n")
        user_tries -= 1

    if user_tries == 0:
        print("uh oh you lose")



