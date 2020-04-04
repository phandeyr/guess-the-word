import random
import numpy

# Boolean to determine if the word has been guessed
word_guessed = False 

# List to keep track of the letters the user has already inputted
letters_inputted = []

# Number of guesses
number_of_guesses = 8

# The word to guess
word_to_guess = ''

# Dictionary to keep track of the index of the letter
letter_dict = {}

# Empty array to be used for building the word guessed
build_word = []

def get_word():
    word_list = ['friends', 'apple', 'money', 'crowded', 'squirrel', 'faucet', 'venomous', 'voyage', 'astonish', 'pancake']
    return random.choice(word_list)

def validate_input(input):
    global number_of_guesses

    # Ensure only one letter has been inputted
    if len(input) != 1:
        print('Please enter one letter')
        return 
    
    # Check if the letter has already been inputted
    if input in letters_inputted:
        print('You have already inputted ' + input)
    else:
        # Check if the letter is in the word to guess (case insensitive)
        for i in range(len(word_to_guess)):
            if word_to_guess[i].casefold() == input.casefold():
                if word_to_guess[i] in letter_dict:
                    value = letter_dict.get(word_to_guess[i])
                    value.append(i)
                else:
                    letter_dict[word_to_guess[i]] = [i]

        letters_inputted.append(input)
    
    # Check if the user has used all their guesses
    number_of_guesses -= 1
    if number_of_guesses > 0:
        print('\nNumber of guesses: ' + str(number_of_guesses))

def word_found(word_to_guess):
    global word_guessed

    # Initialise array to length of the word to guess
    build_word = numpy.empty(len(word_to_guess), dtype=object)

    # Set the position of the letters
    for key, value in letter_dict.items():
        build_word[value] = key

    # String join the values array is populated and check if the words match
    display_word = ''
    word = ''
    if not any(isinstance(x, type(None)) for x in build_word):
        if word.join(build_word) == word_to_guess:
            word_guessed = True
    else:
        for x in build_word:
            if x == None:
                display_word += ' _ '
            else:
                display_word += x
        print('\n' + display_word + '\n')

def main():
    global word_to_guess

    word_to_guess = get_word()
    print('Welcome to Guess the Word')
    
    while not word_guessed and number_of_guesses != 0:
        print('Enter a letter:')
        validate_input(input())
        word_found(word_to_guess)
    else:
        if word_guessed:
            print('Well done! You have guessed the word correctly: ' + word_to_guess)
        else:
            print('You have have used all your guesses.  The word was ' + word_to_guess)

main()