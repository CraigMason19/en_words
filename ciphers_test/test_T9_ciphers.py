import unittest

from ciphers.T9 import T9Cipher, ReversibleT9Cipher

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