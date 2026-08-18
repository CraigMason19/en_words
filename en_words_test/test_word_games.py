import unittest

from en_words.word_games import Countdown


#region Countdown Tests

class TestCountdownCreation(unittest.TestCase):
    def test_construction_lowercase(self):
        result = Countdown("hdgraeion")

        self.assertIsInstance(result, Countdown)

    def test_construction_uppercase(self):
        result = Countdown("PTEORSEDO")

        self.assertIsInstance(result, Countdown)

    def test_valid_construction(self):
        games = [
            "PTEORSEDO",
            "CAITDEHON",
        ]

        for game in games:
            try:
                _ = Countdown(game)
            except Exception as e: # pragma: no cover
                self.fail(f"Raised an exception: {e}")


    def test_invalid_construction(self):
        with self.assertRaises(ValueError):
            _ = Countdown("foo")


class TestCountdownIsValidSelection(unittest.TestCase):
    def test_invalid_less_than_9_letters(self):
        with self.assertRaises(ValueError):
            _ = Countdown("abcdefgh")

    def test_invalid_more_than_9_letters(self):
        with self.assertRaises(ValueError):
            _ = Countdown("abcdefghijk")

    def test_invalid_spaces(self):
        with self.assertRaises(ValueError):
            _ = Countdown("PTEO RSED")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            _ = Countdown("PTEO5RSED")    

    def test_valid_min_vowel_count(self):
        result = Countdown.is_valid_selection('AAA' + 'BBCCDD')
        expected = True

        self.assertEqual(result, expected)

    def test_valid_max_vowel_count(self):
        result = Countdown.is_valid_selection('AAAEE' + 'BBDD')
        expected = True

        self.assertEqual(result, expected)
        
    def test_valid_max_vowel_count_exceeded(self):
        result = Countdown.is_valid_selection('AAAEEE' + 'BDD')
        expected = False

        self.assertEqual(result, expected)

    def test_invalid_selection_incorrect_distribution(self):
        result = Countdown.is_valid_selection('KK' + 'AEO' + 'JKLM')
        expected = False

        self.assertEqual(result, expected)


class TestCountdownFromVowelCount(unittest.TestCase):
    def test_vowel_count_negative(self):
        with self.assertRaises(ValueError):
            _ = Countdown.from_vowel_count(-1)

    def test_vowel_count_zero(self):
        with self.assertRaises(ValueError):
            _ = Countdown.from_vowel_count(0)

    def test_from_below_min_vowel_count(self):
        with self.assertRaises(ValueError):
            _ = Countdown.from_vowel_count(Countdown.MIN_VOWEL_COUNT - 1)

    def test_from_min_vowel_count(self):
        try:
            _ = Countdown.from_vowel_count(Countdown.MIN_VOWEL_COUNT)
        except Exception as e: # pragma: no cover
            self.fail(f"Raised an exception: {e}")

    def test_from_max_vowel_count(self):
        try:
            _ = Countdown.from_vowel_count(Countdown.MAX_VOWEL_COUNT)
        except Exception as e: # pragma: no cover
            self.fail(f"Raised an exception: {e}")

    def test_from_above_max_vowel_count(self):
        with self.assertRaises(ValueError):
            _ = Countdown.from_vowel_count(Countdown.MAX_VOWEL_COUNT + 1)

    def test_from_vowel_count_valid(self):
        """ 
        .from_vowel_count uses random, so each time this test is run it has
        a new game 
        """
        for i in range(Countdown.MIN_VOWEL_COUNT, Countdown.MAX_VOWEL_COUNT+1):
            c = Countdown.from_vowel_count(i)
            expected = True

            self.assertEqual(Countdown.is_valid_selection(c.letters), expected)


class TestCountdownStringRepresentation(unittest.TestCase):
    def test_repr(self):
        result = repr(Countdown("hdgraeion"))
        expected = 'Countdown("HDGRAEION")'

        self.assertEqual(result, expected)


#endregion