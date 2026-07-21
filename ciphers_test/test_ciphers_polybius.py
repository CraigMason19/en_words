import unittest

from ciphers.polybius_checkerboard import PolybiusCheckerboard


class TestPolybius(unittest.TestCase):
    def test_instantiation_causes_error(self):
        with self.assertRaises(TypeError):
            _ = PolybiusCheckerboard()

    def test_name_attribute(self):
        result = PolybiusCheckerboard.NAME
        expected = "PolybiusCheckerboard"

        self.assertEqual(result, expected)


class TestPolybiusIsValidEncoding(unittest.TestCase):
    def test_valid(self):
        result = PolybiusCheckerboard.is_valid_encoding("23 15 31 31 34")
        
        self.assertTrue(result)
        
    def test_valid_multiple_spaces(self):
        result = PolybiusCheckerboard.is_valid_encoding("23 15  31   31    34")
        
        self.assertTrue(result)

    def test_invalid_empty(self):
        result = PolybiusCheckerboard.is_valid_encoding("")
        
        self.assertFalse(result)

    def test_invalid_whitespaces(self):
        result = PolybiusCheckerboard.is_valid_encoding("     ")
        
        self.assertFalse(result)

    def test_invalid_too_few_digits(self):
        result = PolybiusCheckerboard.is_valid_encoding("1")
        
        self.assertFalse(result)

    def test_invalid_too_many_digits(self):
        result = PolybiusCheckerboard.is_valid_encoding("111")
        
        self.assertFalse(result)

    # Range
    def test_invalid_first_digit_out_of_lower_range(self):
        result = PolybiusCheckerboard.is_valid_encoding("05")
        
        self.assertFalse(result)

    def test_invalid_first_digit_out_of_upper_range(self):
        result = PolybiusCheckerboard.is_valid_encoding("65")
        
        self.assertFalse(result)


    def test_invalid_second_digit_out_of_lower_range(self):
        result = PolybiusCheckerboard.is_valid_encoding("10")
        
        self.assertFalse(result)

    def test_invalid_second_digit_out_of_upper_range(self):
        result = PolybiusCheckerboard.is_valid_encoding("16")
        
        self.assertFalse(result)

    # Letters & Syntax
    def test_invalid_letters(self):
        result = PolybiusCheckerboard.is_valid_encoding("11 aa")
        
        self.assertFalse(result)

    def test_invalid_syntax(self):
        result = PolybiusCheckerboard.is_valid_encoding("11 ..")
        
        self.assertFalse(result)


class TestPolybiusCell(unittest.TestCase):
    def test_cell(self):
        result = PolybiusCheckerboard.cell(1, 3)
        expected = 'C'

        self.assertEqual(result, expected)

    def test_cell_column_out_of_range_lower(self):
        with self.assertRaises(IndexError):
            result = PolybiusCheckerboard.cell(0, 3)

    def test_cell_column_out_of_range_upper(self):
        with self.assertRaises(IndexError):
            result = PolybiusCheckerboard.cell(6, 2)

    def test_cell_row_out_of_range_lower(self):
        with self.assertRaises(IndexError):
            result = PolybiusCheckerboard.cell(1, 0)

    def test_cell_row_out_of_range_upper(self):
        with self.assertRaises(IndexError):
            result = PolybiusCheckerboard.cell(1, 6)


class TestPolybiusCellCoords(unittest.TestCase):
    def test_cell_coords_lowercase(self):
        result = PolybiusCheckerboard.cell_coords('c')
        expected = '13'

        self.assertEqual(result, expected)

    def test_cell_coords_uppercase(self):
        result = PolybiusCheckerboard.cell_coords('C')
        expected = '13'

        self.assertEqual(result, expected)

    def test_cell_coords_I(self):
        result = PolybiusCheckerboard.cell_coords('I')
        expected = '24'

        self.assertEqual(result, expected)

    def test_cell_coords_J_is_I(self):
        result = PolybiusCheckerboard.cell_coords('J')
        expected = '24'

        self.assertEqual(result, expected)


class TestPolybiusEncode(unittest.TestCase):
    def test_encode_lowercase(self):
        result = PolybiusCheckerboard.encode("foo")
        expected = "21 34 34"

        self.assertEqual(result, expected)

    def test_encode_uppercase(self):
        result = PolybiusCheckerboard.encode("FOO")
        expected = "21 34 34"

        self.assertEqual(result, expected)

    def test_encode_ignores_spaces(self):
        result = PolybiusCheckerboard.encode("fo  o")
        expected = "21 34 34"

        self.assertEqual(result, expected)

    def test_encode_removes_non_letters(self):
        result = PolybiusCheckerboard.encode("123 ./#-+ foo.456")
        expected = "21 34 34"

        self.assertEqual(result, expected)


class TestPolybiusDecode(unittest.TestCase):
    def test_returns_uppercase(self):
        result = PolybiusCheckerboard.decode("21 34 34")
        expected = "FOO"

        self.assertEqual(result, expected)

    def test_cant_decode_improper_string(self):
        with self.assertRaises(ValueError):
            result = PolybiusCheckerboard.decode("21 34 34 10")


class TestPolybiusReversable(unittest.TestCase):
    def test_encode_reversable(self):
        result = PolybiusCheckerboard.decode(PolybiusCheckerboard.encode('foo'))
        expected = 'FOO'

        self.assertEqual(result, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()