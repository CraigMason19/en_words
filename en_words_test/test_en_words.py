import types
import unittest

from en_words import en_words

class TestWords(unittest.TestCase):
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


class TestUnsortedWords(unittest.TestCase):
    def test_unsorted_words_returns_list(self):
        result = en_words.unsorted_words()

        self.assertIsInstance(result, list)


class TestUnsortedWordsGen(unittest.TestCase):
    def test_unsorted_words_gen_returns_generator(self):
        result = en_words.unsorted_words_gen()

        self.assertIsInstance(result, types.GeneratorType)


class TestSortedWords(unittest.TestCase):
    def test_sorted_words_returns_list(self):
        result = en_words.sorted_words()

        self.assertIsInstance(result, list)


class TestSortedWordsGen(unittest.TestCase):
    def test_sorted_words_gen_returns_generator(self):
        result = en_words.sorted_words_gen()

        self.assertIsInstance(result, types.GeneratorType)


class TestAnagrams(unittest.TestCase):
    def test_anagrams_returns_list(self):
        result = en_words.anagrams("opts")

        self.assertIsInstance(result, list)

    def test_finds_anagrams(self):
        result = en_words.anagrams("opts")
        expected = ['post', 'pots', 'spot', 'stop', 'tops']

        self.assertEqual(result, expected)

    def test_no_anagrams_returns_empty_list(self):
        result = en_words.anagrams("anagram")
        expected = []

        self.assertEqual(result, expected)


class TestAnagramsGen(unittest.TestCase):
    def test_anagrams_gen(self):
        result = list(en_words.anagrams_gen("opts"))
        expected = ['post', 'pots', 'spot', 'stop', 'tops']

        self.assertEqual(result, expected)

    def test_anagrams_gen_returns_generator(self):
        result = en_words.anagrams_gen("opts")

        self.assertIsInstance(result, types.GeneratorType)

    def test_anagrams_gen_returns_only_strings(self):
        for _ in en_words.anagrams_gen("opts"):
            self.assertIsInstance(_, str)


if __name__ == '__main__': # pragma no cover
    unittest.main()