import random

class Game:

    # The word to guess
    word_to_guess = ''

    # Number of guesses
    number_of_guesses = 8

    # List to keep track of the letters the user has already inputted
    letters_inputted = []

    # The user's guessed word
    user_guessed_word = ''

    # Set a word to guess randomly
    def set_word(self):
        word_list = ['friends', 'apple', 'money', 'crowded', 'squirrel', 'faucet', 'venomous', 'voyage', 'astonish', 'pancake']
        self.word_to_guess = random.choice(word_list)

    # Build user guessed word
    def build_user_guessed_word(self):
        self.user_guessed_word = [None] * len(self.word_to_guess)
    
    # Decreases the number of guesses by one
    def decrease_number_of_guesses(self):
        self.number_of_guesses -= 1

    # Checks if user input is valid
    def valid_input(self, input):
        if len(input) != 1 or not input.isalpha():
            is_valid_input = False
        else:
            is_valid_input = True
        return is_valid_input
    
    # Update user guesses
    def update_user_guesses(self, input):
        if input in self.letters_inputted:
            self.display_output('You have already inputted ' + input)
        else:
            self.letters_inputted.append(input)
            
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == input:
                    self.user_guessed_word[i] = input
        
        # Decrease number of guesses
        self.decrease_number_of_guesses()
    
    # Checks if the word if matched
    def is_word_guessed(self):
        display_word = ''
        word = ''
        if not any(isinstance(x, type(None)) for x in self.user_guessed_word):
            return self.word_to_guess == word.join(self.user_guessed_word)
        else: 
            for x in self.user_guessed_word:
                if x == None:
                    display_word += ' _ '
                else:
                    display_word += x

            self.display_output('\nYou have ' + str(self.number_of_guesses) + ' guesses remaining\n')
            self.display_output(display_word)

    # Displays output 
    def display_output(self, msg):
        print(msg)

    # Intro
    def intro(self):
        self.display_output('\nWelcome to Guess the Word! The word you have to guess has ' + str(len(self.word_to_guess)) + ' letters')

def main():
    game = Game()
    game.set_word()
    game.build_user_guessed_word()
    game.intro()

    while not game.is_word_guessed() and game.number_of_guesses != 0:
        game.display_output('\nPlease enter a letter:')
        user_input = input()
        
        if game.valid_input(user_input):
            game.update_user_guesses(user_input)
        else:
            game.display_output('\nPlease enter only one alpha letter')
    else:
        if game.is_word_guessed():
            game.display_output('\nWell done! You have guessed the word correctly: ' + game.word_to_guess)
        else:
            game.display_output('\nYou have have used all your guesses.  The word was ' + game.word_to_guess)

if __name__ == "__main__":
  main()