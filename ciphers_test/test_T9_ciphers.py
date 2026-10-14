import unittest

from ciphers.T9 import (
    presses_for_letter,
    letter_from_presses,
    T9Cipher, 
    ReversibleT9Cipher,
)


class PressesForLetter(unittest.TestCase):
    def test_1_press(self):
        result = presses_for_letter('p')
        expected = 1

        self.assertEqual(result, expected)

    def test_4_presses(self):
        result = presses_for_letter('z')
        expected = 4

        self.assertEqual(result, expected)

    def test_empty_letter_raises_value_error(self):
        with self.assertRaises(ValueError):
            presses_for_letter('')

    def test_multiple_letters_raises_value_error(self):
        with self.assertRaises(ValueError):
            presses_for_letter('pq')

    def test_word_raises_value_error(self):
        with self.assertRaises(ValueError):
            presses_for_letter('pq')


class LetterFromPresses(unittest.TestCase):
    def test_number_out_of_min_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_from_presses(1, 1)

    def test_number_out_of_max_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_from_presses(10, 1)

    def test_number_2_presses_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_from_presses(2, 0)

    # Digit 2
    def test_number_2_presses_1(self):
        result = letter_from_presses(2, 1)
        expected = "a"

        self.assertEqual(result, expected)

    def test_number_2_presses_3(self):
        result = letter_from_presses(2, 3)
        expected = "c"

        self.assertEqual(result, expected)

    def test_number_2_presses_4(self):
        with self.assertRaises(ValueError):
            letter_from_presses(2, 4)

    # Digit 9
    def test_number_9_presses_1(self):
        result = letter_from_presses(9, 1)
        expected = "w"

        self.assertEqual(result, expected)

    def test_number_9_presses_4(self):
        result = letter_from_presses(9, 4)
        expected = "z"

        self.assertEqual(result, expected)

    def test_number_9_presses_5(self):
        with self.assertRaises(ValueError):
            letter_from_presses(9, 5)


class TestT9Cipher(unittest.TestCase):
    def test_name_attribute(self):
        result = T9Cipher.NAME
        expected = "T9Cipher"

        self.assertEqual(result, expected)

    def test_encode(self):
        word = "craig"
        expected = "27244"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_encode_with_numbers(self):
        word = "123Craig123"
        expected = "27244"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_encode_with_spaces(self):
        word = "Craig Mason"
        expected = "2724462766"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_encode_with_non_letters(self):
        word = "Germ?!n---+y"
        expected = "437669"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_decode_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            T9Cipher.decode("test")


class TestReversibleT9Cipher(unittest.TestCase):
    def test_name_attribute(self):
        result = ReversibleT9Cipher.NAME
        expected = "ReversibleT9Cipher"

        self.assertEqual(result, expected)

    def test_encode_with_punctuation(self):
        word = "Hello!!!"
        expected = "44-33-555-555-666"

        result = ReversibleT9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_encode_with_spaces(self):
        word = "Craig  Mason"
        expected = "222-777-2-444-4-6-2-7777-666-66"

        result = ReversibleT9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_decode(self):
        input = "44-33-555-555-666"
        expected = "hello"

        result = ReversibleT9Cipher.decode(input)
        self.assertEqual(result, expected)

    def test_decode_invalid_input(self):
        invalid_inputs = [
            "",              # empty string
            "-7----9",       # empty chunks
            "abc-def-ghi",   # no digits at all
            "222--777",      # empty chunk between delimiters
            "222-7x7-2",     # chunk with non-digit character
            "no-digits-here" # all letters and hyphens
        ]

        for invalid in invalid_inputs:
            with self.assertRaises(ValueError, msg=f"Input: {invalid}"):
                ReversibleT9Cipher.decode(invalid)

    def test_encode_and_decode_match(self):
        word = "Craig Mason"
        encoded = ReversibleT9Cipher.encode(word)
        decoded = ReversibleT9Cipher.decode(encoded)

        expected = "craigmason"
        self.assertEqual(decoded, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()