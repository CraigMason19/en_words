import unittest

from ciphers import T9Cipher

class TestT9Cipher(unittest.TestCase):
    def test_encode(self):
        word = "craig"
        expected = "27244"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_encode_with_numbers(self):
        word = "123Craig123"
        expected = "12327244123"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

    def test_encode_with_non_letters(self):
        word = "Germ?!n---+y"
        expected = "4376?!6---+9"

        result = T9Cipher.encode(word)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()