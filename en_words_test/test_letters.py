"""
Test suite for letters.py
"""

import unittest
from unittest.mock import patch
from random import Random

import en_words.letters as letters


class TestLetters(unittest.TestCase):
    #---------------------------------------------------------------------------
    # setUp and tearDown run before every single test.
    #---------------------------------------------------------------------------
    def setUp(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.random = Random(1024) # Set a seed so the random output is deterministic

    def tearDown(self):
        pass

    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------
    def test_is_letter(self):
        result = letters.is_letter('e')        
        self.assertTrue(result)

    def test_is_letter_upper_and_lower(self):
        result = letters.is_letter('e')
        self.assertTrue(result)

        result = letters.is_letter('E')
        self.assertTrue(result)

    def test_is_letter_empty_string(self):
        result = letters.is_letter('')        
        self.assertFalse(result)

    def test_is_letter_only_space(self):
        result = letters.is_letter(' ')        
        self.assertFalse(result)

    def test_is_letter_more_than_one_letter(self):
        result = letters.is_letter('ab')        
        self.assertFalse(result)




    def test_letter_to_index(self):
        self.assertEqual(letters.letter_to_index('a'), 0)
        self.assertEqual(letters.letter_to_index('A'), 0)

        self.assertEqual(letters.letter_to_index('d'), 3)
        self.assertEqual(letters.letter_to_index('D'), 3)

        self.assertEqual(letters.letter_to_index('z'), 25)
        self.assertEqual(letters.letter_to_index('Z'), 25)

        for i, letter in enumerate(self.alphabet):
            self.assertEqual(letters.letter_to_index(letter.lower()), i)
            self.assertEqual(letters.letter_to_index(letter.capitalize()), i)

    def test_index_to_letter(self):
        self.assertEqual(letters.index_to_letter(0), 'a')
        self.assertEqual(letters.index_to_letter(0, False), 'a')
        self.assertEqual(letters.index_to_letter(0, True), 'A')

        self.assertEqual(letters.index_to_letter(25), 'z')
        self.assertEqual(letters.index_to_letter(25, False), 'z')
        self.assertEqual(letters.index_to_letter(25, True), 'Z')

        for i, letter in enumerate(self.alphabet):
            # self.alphabet is in CAPS
            self.assertEqual(letters.index_to_letter(i), letter.lower())
            self.assertEqual(letters.index_to_letter(i, False), letter.lower())

            self.assertEqual(letters.index_to_letter(i, True), letter)
            self.assertEqual(letters.index_to_letter(i).capitalize(), letter)
            self.assertEqual(letters.index_to_letter(i, True), letter)

    def test_next_letter(self):
        self.assertEqual(letters.next_letter('a'), 'b')
        self.assertEqual(letters.next_letter('A'), 'B')

        self.assertEqual(letters.next_letter('z'), 'a')
        self.assertEqual(letters.next_letter('Z'), 'A')

    def test_previous_letter(self):
        self.assertEqual(letters.previous_letter('a'), 'z')
        self.assertEqual(letters.previous_letter('A'), 'Z')

        self.assertEqual(letters.previous_letter('z'), 'y')
        self.assertEqual(letters.previous_letter('Z'), 'Y')

    def test_shift_letter_up(self):
        self.assertEqual(letters.shift_letter_up('z', 0), 'z')
        self.assertEqual(letters.shift_letter_up('Z', 0), 'Z')

        self.assertEqual(letters.shift_letter_up('z', 2), 'b')
        self.assertEqual(letters.shift_letter_up('X', 10), 'H')

        # 1x, 2x & 4x loops
        self.assertEqual(letters.shift_letter_up('A', 26), 'A')
        self.assertEqual(letters.shift_letter_up('A', 52), 'A')
        self.assertEqual(letters.shift_letter_up('A', 104), 'A')

        # 1x, 2x & 4x loops with z->a change
        self.assertEqual(letters.shift_letter_up('V', 26), 'V')
        self.assertEqual(letters.shift_letter_up('V', 52), 'V')
        self.assertEqual(letters.shift_letter_up('V', 104), 'V')

        # ValueError test
        self.assertRaises(ValueError, letters.shift_letter_up, 'B', -5)

    def test_shift_letter_down(self):
        self.assertEqual(letters.shift_letter_down('b', 0), 'b')
        self.assertEqual(letters.shift_letter_down('B', 0), 'B')

        self.assertEqual(letters.shift_letter_down('z', -2), 'x')
        self.assertEqual(letters.shift_letter_down('X', -10), 'N')

        # 1x, 2x & 4x loops
        self.assertEqual(letters.shift_letter_down('A', -26), 'A')
        self.assertEqual(letters.shift_letter_down('A', -52), 'A')
        self.assertEqual(letters.shift_letter_down('A', -104), 'A')

        # 1x, 2x & 4x loops with a<-z change
        self.assertEqual(letters.shift_letter_down('d', -26), 'd')
        self.assertEqual(letters.shift_letter_down('d', -52), 'd')
        self.assertEqual(letters.shift_letter_down('d', -104), 'd')

        # ValueError test
        self.assertRaises(ValueError, letters.shift_letter_down, 'B', 5)

    def test_shift(self):
        self.assertEqual(letters.shift('A', 0), 'A')
        self.assertEqual(letters.shift('A', -1), 'Z')
        self.assertEqual(letters.shift('a', 1), 'b')

        self.assertEqual(letters.shift('a', -13), 'n')
        self.assertEqual(letters.shift('A', -13), 'N')
        self.assertEqual(letters.shift('a', 13), 'n')
        self.assertEqual(letters.shift('A', 13), 'N')

        self.assertEqual(letters.shift('A', -52), 'A')
        self.assertEqual(letters.shift('A', 52), 'A')

    def test_alphabet_generator(self):
        gen = letters.alphabet_generator()
        for _, letter in enumerate(self.alphabet.lower()):
            self.assertEqual(next(gen), letter)

        # Test lowercase
        gen = letters.alphabet_generator("a")
        for _, letter in enumerate(self.alphabet.lower()):
            self.assertEqual(next(gen), letter)

        # Test uppercase
        gen = letters.alphabet_generator("A")
        for _, letter in enumerate(self.alphabet):
            self.assertEqual(next(gen), letter)

        mini_alphabet_loop = "XYZABC"

        # Test start at specific position, lowercase
        gen = letters.alphabet_generator("x")
        for _, letter in enumerate(mini_alphabet_loop.lower()):
            self.assertEqual(next(gen), letter)

        # Test start at specific position, uppercase
        gen = letters.alphabet_generator("X")
        for _, letter in enumerate(mini_alphabet_loop):
            self.assertEqual(next(gen), letter)

    def test_shift_alphabet(self):
        self.assertEqual(letters.shift_alphabet(0, False), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(letters.shift_alphabet(0, True), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        self.assertEqual(letters.shift_alphabet(1, True), "BCDEFGHIJKLMNOPQRSTUVWXYZA")
        self.assertEqual(letters.shift_alphabet(-1, True), "ZABCDEFGHIJKLMNOPQRSTUVWXY")

        self.assertEqual(letters.shift_alphabet(26, False), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(letters.shift_alphabet(-26, False), "abcdefghijklmnopqrstuvwxyz")

    def test_caesar_cipher(self):
        self.assertEqual(letters.caesar_cipher('a'), 'd')
        self.assertEqual(letters.caesar_cipher('A'), 'D')

        self.assertEqual(letters.caesar_cipher('z', 0), 'z')
        self.assertEqual(letters.caesar_cipher('Z', 0), 'Z')

        self.assertEqual(letters.caesar_cipher('A', -1), 'Z')
        self.assertEqual(letters.caesar_cipher('a', -2), 'y')

    @patch('letters.random')            
    def test_random_lower_letter(self, random):
        random.choice._mock_side_effect = self.random.choice

        self.assertEqual(letters.random_lower_letter(), 'z')

    @patch('letters.random') 
    def test_random_upper_letter(self, random):
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(letters.random_upper_letter(), 'Z')

    @patch('letters.random') 
    def test_random_letter(self, random):
        random.choice._mock_side_effect = self.random.choice

        self.assertEqual(letters.random_letter(), 'Z')


class TestLetterFrequencies(unittest.TestCase):
    def test_letters_frequency_is_float(self):
        result = letters.LetterFrequency.percentage("e")
        self.assertIsInstance(result, float)

    def test_letters_frequency_has_unique_letters(self):
        result = len(set(letters.LetterFrequency.frequency_dict))

        self.assertEquals(result, 26)

    def test_letters_frequency_invalid_key_rasises_value_error(self):
        with self.assertRaises(ValueError):
            letters.LetterFrequency.percentage("invalid_key")

    def test_letters_frequency_upper_and_lower_doesnt_rasise_value_error(self):
        try:
            a = letters.LetterFrequency.percentage("e")
            b = letters.LetterFrequency.percentage("E")
        except ValueError:
            self.fail("ValueError was raised unexpectedly")

if __name__ == '__main__':
    unittest.main()