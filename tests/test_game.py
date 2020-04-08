import unittest
from scripts.game import Game

class TestGame(unittest.TestCase):

    # Create local instance of the class
    def setUp(self):
        self.func = Game()

    # Test case to ensure a word is set
    def test_set_word(self):
        self.func.set_word()
        self.assertTrue(len(self.func.word_to_guess) > 0)

    # Test case to ensure number of guesses decreases
    def test_number_of_guesses(self):
        self.func.decrease_number_of_guesses()
        self.assertEqual(self.func.number_of_guesses, 7)
    
    # Test case to validate user input 
    def test_valid_input(self):
        self.assertTrue(self.func.valid_input('a'))
        self.assertFalse(self.func.valid_input('hello'))
        self.assertFalse(self.func.valid_input('@'))

    # Test case to check if the word has been guessed correctly 
    def test_is_word_guessed(self):
        self.func.word_to_guess = 'apple'
        self.func.user_guessed_word = ['a', 'p', 'p', 'l', 'e']
        self.assertTrue(self.func.is_word_guessed())

        self.func.user_guessed_word = ['a', None, None, None, 'e']
        self.assertFalse(self.func.is_word_guessed())
    
    # Test case to update user guesses 
    def test_update_user_guesses(self):
        self.func.word_to_guess = 'apple'
        self.func.build_user_guessed_word()
        self.func.update_user_guesses('p')
        self.assertEqual(self.func.user_guessed_word, [None, 'p', 'p', None, None])
        self.assertTrue('p' in self.func.letters_inputted)