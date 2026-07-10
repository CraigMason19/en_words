import unittest

from ciphers.A1Z26 import A1Z26


class TestA1Z26(unittest.TestCase):
    def test_instantiation_causes_error(self):
        with self.assertRaises(TypeError):
            _ = A1Z26()

class TestA1Z26Encode(unittest.TestCase):      
    def test_encode(self):
        result = A1Z26.encode("Hello")
        expected = "8 5 12 12 15"

        self.assertEqual(result, expected)

    def test_encode_spacing_delimiter(self):
        result = A1Z26.encode("Hello World")
        expected = "8 5 12 12 15 / 23 15 18 12 4"

        self.assertEqual(result, expected)

    def test_encode_no_spacing_delimiter(self):
        result = A1Z26.encode("HelloWorld")
        expected = "8 5 12 12 15 23 15 18 12 4"

        self.assertEqual(result, expected)

    def test_encode_number(self):
        result = A1Z26.encode("5")
        expected = ""

        self.assertEqual(result, expected)

    def test_encode_multiple_spaces(self):
        result = A1Z26.encode("Hello           World")
        expected = "8 5 12 12 15 / 23 15 18 12 4"

        self.assertEqual(result, expected)


class TestA1Z26Decode(unittest.TestCase):      
    def test_decode(self):
        result = A1Z26.decode("8 5 12 12 15")
        expected = "HELLO"

        self.assertEqual(result, expected)

    def test_decode_spacing_delimiter(self):
        result = A1Z26.decode("8 5 12 12 15 / 23 15 18 12 4")
        expected = "HELLO WORLD"

        self.assertEqual(result, expected)

    def test_decode_no_spacing_delimiter(self):
        result = A1Z26.decode("8 5 12 12 15 23 15 18 12 4")
        expected = "HELLOWORLD"

        self.assertEqual(result, expected)


    def test_decode_invalid_token_out_of_upper_range(self):
        result = A1Z26.decode("27")
        expected = "_"

        self.assertEqual(result, expected)    

    def test_decode_invalid_token_out_of_lower_range(self):
        result = A1Z26.decode("0")
        expected = "_"

        self.assertEqual(result, expected)    

    def test_decode_invalid_token_letter(self):
        result = A1Z26.decode("T")
        expected = "_"

        self.assertEqual(result, expected)    

    def test_decode_invalid_token_word(self):
        result = A1Z26.decode("THE")
        expected = "_"

        self.assertEqual(result, expected)    

    def test_decode_space(self):
        result = A1Z26.decode(" ")
        expected = ""

        self.assertEqual(result, expected)   

    def test_decode_deliminator(self):
        result = A1Z26.decode("/")
        expected = " "

        self.assertEqual(result, expected)   


class TestA1Z26Reversable(unittest.TestCase):      
    def test_encode_decode_reversable(self):
        word = "Hello World"

        encoded = A1Z26.encode(word)
        decoded = A1Z26.decode(encoded)
        expected = word.upper()

        self.assertEqual(decoded, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()