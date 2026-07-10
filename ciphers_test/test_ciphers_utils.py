import unittest

from ciphers.utils import CleanInput


class TestCipherUtilsCleanInputAlphabetical(unittest.TestCase):
    def test_alphabetical(self):
        result = CleanInput.to_alpha("craig_ 4!4")
        expected = "craig"

        self.assertEqual(result, expected)

    def test_alphabetical_with_space_false(self):
        result = CleanInput.to_alpha("Hello World", with_spaces=False)
        expected = "helloworld"

        self.assertEqual(result, expected)

    def test_alphabetical_with_space_true(self):
        result = CleanInput.to_alpha("Hello World", with_spaces=True)
        expected = "hello world"

        self.assertEqual(result, expected)


class TestCipherUtilsCleanInputAlphanumeric(unittest.TestCase):
    def test_alphanumeric(self):
        result = CleanInput.to_alphanumeric("craig_ 4!4")
        expected = "craig44"

        self.assertEqual(result, expected)

    def test_alphanumeric_with_space_false(self):
        result = CleanInput.to_alphanumeric("Hello World 123", with_spaces=False)
        expected = "helloworld123"

        self.assertEqual(result, expected)

    def test_alphanumeric_with_space_true(self):
        result = CleanInput.to_alphanumeric("Hello World 123", with_spaces=True)
        expected = "hello world 123"

        self.assertEqual(result, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()