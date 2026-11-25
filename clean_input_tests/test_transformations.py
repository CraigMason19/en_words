import unittest

import clean_input as ci 


class TestAlpha(unittest.TestCase):
    def test_strips_numbers(self):
        text = "Hello123"
        result = ci.Alpha.transform(text)
        expected = "Hello"

        self.assertEqual(result, expected)

    def test_strips_punctuation(self):
        text = "Hello!!!!###;"
        result = ci.Alpha.transform(text)
        expected = "Hello"

        self.assertEqual(result, expected)

    def test_spaces_are_not_stripped(self):
        text = "Hello ;"
        result = ci.Alpha.transform(text)
        expected = "Hello "

        self.assertEqual(result, expected) 


if __name__ == '__main__': # pragma: no cover
    unittest.main()