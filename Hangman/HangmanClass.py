class HangmanGame:
    def __init__(self, word=None):
        # Generate/Capture the word to guess
        self.word = word
        self.word_length = len(str(self.word))
        self.minimum_word_length = 5
        self.maximum_word_length = 15
        if word is None:
            self.get_word_input()

        # Variables associated with guessing
        self.correct_char_count = 0
        self.current_guess = ['_'] * self.word_length
        self.incorrect_characters = set(())

        # Lives and drawing
        self.lives = 6
        self.drawing = {
            6: '''
               -----
                   |
                   |
                   |
            =========''',
            5: '''
               -----
               O   |
                   |
                   |
            =========''',
            4: '''
               -----
               O   |
               |   |
                   |
            =========''',
            3: '''
               -----
               O   |
              /|   |
                   |
            =========''',
            2: '''
               -----
               O   |
              /|\  |
                   |
            =========''',
            1: '''
               -----
               O   |
              /|\  |
              /    |
            =========''',
            0: '''
               -----
               O   |
              /|\  |
              / \  |
            ========='''
        }

    def get_word_input(self):
        prompt = """Please enter a word that meets the following criterion:
        1. A single word with no spaces
        2. Only letters accepted
        3. Word should be in lower case only
        4. Minimum length of 5 characters
        5. Maximum length of 15 characters"""
        print(prompt)

        invalid_input = True

        while invalid_input:
            self.word = input("\nPlease enter your hidden word: ")
            self.word_length = len(self.word)

            # 1. Check if word is suitable length
            if self.word_length not in range(self.minimum_word_length, self.maximum_word_length):
                print(f"Word length needs to be between {self.minimum_word_length} and {self.maximum_word_length}")
                continue  # Runs loop again

            # 2. Check of word is letters only
            if not self.word.isalpha():
                print("Word can only contain letters")
                continue

            # 3. All criterion met, set flag to false
            invalid_input = False

        self.word = self.word.lower()   # convert word to lower case
        print('\n' * 400)

    # This may belong to the GameController
    def get_guess_input(self):
        invalid_input = True

        while invalid_input:
            guess = input("\nPlease enter a single letter: ")

            # 1. Check if word is suitable length and is a letter
            if len(guess) != 1 or not guess.isalpha():
                print("Your input was invalid, please enter a single character as a letter.")
                continue  # Runs loop again

            # 2. Check if guess has already been made
            if guess in self.incorrect_characters:
                print(f"You have already incorrectly guessed {guess}.\n"
                      f"These are the other incorrect guesses: {self.incorrect_characters}")

            # 3. Input is valid
            invalid_input = False

            return guess

    def __is_valid_guess(self, guess: str):
        if len(guess) != 1 or not guess.isalpha() or guess in self.incorrect_characters:
            return False

        return True

    def make_guess(self, guess: str):
        # Check should have already been made, this is a double-check
        if not self.__is_valid_guess(guess):
            return f"Your guess ({guess}) is invalid"

        if guess in self.incorrect_characters:
            return f"""You have already incorrectly guessed {guess}.
                            These are the other incorrect guesses: {self.incorrect_characters}"""

        guess_incorrect = True  # Assume the guess is wrong

        for i in range(self.word_length):
            if self.word[i] == guess:
                guess_incorrect = False  # Guess was right, set flag accordingly
                self.correct_char_count += 1
                self.current_guess[i] = guess

        if guess_incorrect:
            self.incorrect_characters.add(guess)
            self.lives -= 1  # Game controller handles lives

    def print_current_guess(self):
        print("Your guess: ", end='')
        for c in self.current_guess:
            print(c,end='')
        print()

    def print_incorrect_guess(self):
        # Print the hangman here

        print("Incorrect guesses: ", end='')
        for c in self.incorrect_characters:
            print(f"{c} | ", end='')
        print()

    def print_game_state(self):
        # 1. First display the hangman and lives remaining
        print(self.drawing[self.lives])
        print(f"Lives remaining: {self.lives}")

        # 2. Then display incorrect guesses
        self.print_incorrect_guess()

        # 3. Display the correct guesses
        self.print_current_guess()

        # 4. Let user know if game is over
        if self.word_length == self.correct_char_count:
            print(f"You have successfully guessed the word: {self.word}")
        elif self.lives <= 0:
            print(f"You have ran out of lives. The correct word was: {self.word}")

    def is_game_over(self):
        if self.word_length == self.correct_char_count or self.lives <= 0:
            return True

        return False

    # TODO Implement
    def reset_game(self):
        self.get_word_input()
        self.correct_char_count = 0
        self.current_guess = ['_'] * self.word_length
        self.incorrect_characters.clear()
        self.lives = 6

