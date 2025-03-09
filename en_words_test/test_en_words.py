#-------------------------------------------------------------------------------
# Name:        test_en_words.py
#
# Notes:       A collections of tests for en_words.py
#
# Links:       
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

from en_words import en_words

class TestWords(unittest.TestCase):
    #---------------------------------------------------------------------------
    # setUpClass and tearDownClass run before and after all tests, called once
    # NOTE - the camelCase syntax. Important that they are named this way.
    #---------------------------------------------------------------------------
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #---------------------------------------------------------------------------
    # setUp and tearDown run before every single test.
    #---------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------
    def test_dict_length(self):
        result = en_words.word_count()
        expected = 194433
        self.assertEqual(result, expected)

    def test_longest_word(self):
        result = en_words.find_largest_word()
        expected = 'dichlorodiphenyltrichloroethane'
        self.assertEqual(result, expected)

    def test_words_of_length(self):
        result = len(en_words.words_of_length(4))
        expected = 5368
        self.assertEqual(result, expected)

    def test_potential_words(self):
        word = '_?tt-e'
        result = len(en_words.potential_words(word))
        expected = 38
        self.assertEqual(result, expected)
 
    def test_words_from_letters(self):
        letters = "beetles"
        result = len(en_words.words_from_letters(letters, min_len=3, max_len=5))
        expected = 107
        self.assertEqual(result, expected)

    def test_is_potential_match_01(self):
        result = en_words.is_potential_match("??ttl-", "battle", 'x', 'b')
        expected = True
        self.assertEqual(result, expected)

    def test_is_potential_match_02(self):
        result = en_words.is_potential_match("??ttl-", "battle", 'xe', 'b')
        expected = False
        self.assertEqual(result, expected)

    def test_letters_in_word_remove_doubles(self):
        result = en_words.letters_in_word('adls', 'salad', True)
        expected = False
        self.assertEqual(result, expected)

    def test_letters_in_word_allow_doubles(self):
        result = en_words.letters_in_word('adls', 'salad')
        expected = True
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()