import unittest

from ciphers.caesar import Caesar


class TestCaesar(unittest.TestCase):
    def test_instantiation_causes_error(self):
        with self.assertRaises(TypeError):
            _ = Caesar()


class TestCaesarIsValidShift(unittest.TestCase):
    def test_negative_shift_is_false(self):
        result = Caesar._is_valid_shift(-1)
        
        self.assertFalse(result)

    def test_zero_shift_is_false(self):
        result = Caesar._is_valid_shift(0)
        
        self.assertFalse(result)

    def test_1_shift_is_true(self):
        result = Caesar._is_valid_shift(1)
        
        self.assertTrue(result)

    def test_25_shift_is_true(self):
        result = Caesar._is_valid_shift(25)
        
        self.assertTrue(result)

    def test_26_shift_is_false(self):
        result = Caesar._is_valid_shift(26)
        
        self.assertFalse(result)


class TestCaesarEncode(unittest.TestCase):
    def test_encode_default_shift(self):
        result = Caesar.encode("abc")
        expected = "def"
        
        self.assertEqual(result, expected)

    def test_encode_default_shift_preserves_case(self):
        result = Caesar.encode("ABcd")
        expected = "DEfg"
        
        self.assertEqual(result, expected)

    def test_encode_shift_1(self):
        result = Caesar.encode("abc", 1)
        expected = "bcd"
        
        self.assertEqual(result, expected)

    def test_encode_shift_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Caesar.encode("abc", 0)

    def test_encode_shift_26_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Caesar.encode("abc", 26)

    def test_encode_retains_symbols(self):
        result = Caesar.encode("123_##!!! abc  # 555 - =")
        expected = "123_##!!! def  # 555 - ="
        
        self.assertEqual(result, expected)


# decode
class TestCaesarDecode(unittest.TestCase):
    def test_decode_default_shift(self):
        result = Caesar.decode("def")
        expected = "abc"
        
        self.assertEqual(result, expected)

    def test_decode_default_shift_preserves_case(self):
        result = Caesar.decode("DEfg")
        expected = "ABcd"
        
        self.assertEqual(result, expected)

    def test_decode_shift_1(self):
        result = Caesar.decode("bcd", 1)
        expected = "abc"
        
        self.assertEqual(result, expected)

    def test_decode_shift_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Caesar.decode("abc", 0)

    def test_decode_shift_26_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Caesar.decode("abc", 26)

    def test_decode_retains_symbols(self):
        result = Caesar.decode("123_##!!! def  # 555 - =")
        expected = "123_##!!! abc  # 555 - ="
        
        self.assertEqual(result, expected)


class TestCaesarReversible(unittest.TestCase):      
    def test_encode_decode_reversible(self):
        text = "Hello World"

        encoded = Caesar.encode(text)
        decoded = Caesar.decode(encoded)

        self.assertEqual(decoded, text)

    def test_encode_decode_reversible_shift_17(self):
        text = "Hello World"

        encoded = Caesar.encode(text, 17)
        decoded = Caesar.decode(encoded, 17)

        self.assertEqual(decoded, text)

if __name__ == '__main__': # pragma: no cover
    unittest.main()