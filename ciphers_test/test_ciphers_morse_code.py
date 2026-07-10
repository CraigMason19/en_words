import unittest

from ciphers.morse_code import MorseCode


class TestMorseCode(unittest.TestCase):
    def test_instantiation_causes_error(self):
        with self.assertRaises(TypeError):
            _ = MorseCode()


class TestMorseCodeIsValidCharset(unittest.TestCase):      
    def test_valid(self):
        result = MorseCode.is_valid_charset(".... . .-.. .-.. ---")
        self.assertTrue(result)

    def test_invalid(self):
        result = MorseCode.is_valid_charset(".... . .-.. | .-.. ---")
        self.assertFalse(result)


class TestMorseCodeEncode(unittest.TestCase):      
    def test_encode(self):
        result = MorseCode.encode("Hello")
        expected = ".... . .-.. .-.. ---"

        self.assertEqual(result, expected)

    def test_encode_alias(self):
        result = MorseCode.encode_as_str("Hello")
        expected = ".... . .-.. .-.. ---"

        self.assertEqual(result, expected)

    def test_encode_as_list(self):
        result = MorseCode.encode_as_list("Hello")
        expected = [
            "....",
            ".",
            ".-..",
            ".-..",
            "---",
        ]

        self.assertEqual(result, expected)

    def test_encode_as_list_returns_list_of_str(self):
        result = MorseCode.encode_as_list("Hello")

        self.assertIsInstance(result, list) 

        for item in result: 
            self.assertIsInstance(item, str)

    def test_encode_word_spacing_delimiter(self):
        result = MorseCode.encode("Hello world")
        expected = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
 
        self.assertEqual(result, expected)   

    def test_encode_word_multiple_spaces(self):
        result = MorseCode.encode("Hello      world")
        expected = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
 
        self.assertEqual(result, expected)   


class TestMorseCodeDecode(unittest.TestCase):      
    def test_decode(self):
        result = MorseCode.decode(".-- --- .-. .-.. -..")
        expected = "world"

        self.assertEqual(result, expected)

    def test_decode_invalid_token(self):
        result = MorseCode.decode(".-.-.-.-")
        expected = "_"

        self.assertEqual(result, expected)    

    def test_decode_contains_invalid_tokens(self):
        result = MorseCode.decode(".-- .-.-.-.- .-. .-.-.-.- -..")
        expected = "w_r_d"

        self.assertEqual(result, expected)    

    def test_decode_word_spacing_delimiter(self):
        result = MorseCode.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        expected = "hello world"

        self.assertEqual(result, expected)   

    def test_decode_input_outside_charset(self):
        with self.assertRaises(ValueError):
            _ = MorseCode.decode("hello, world!")


class TestMorseCodeReversable(unittest.TestCase):      
    def test_encode_decode_reversable(self):
        encoded = MorseCode.encode("Hello World")
        decoded = MorseCode.decode(encoded)
        expected = "hello world"

        self.assertEqual(decoded, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()