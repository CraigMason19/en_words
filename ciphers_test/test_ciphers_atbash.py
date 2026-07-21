import unittest

from ciphers.atbash import Atbash

class TestAtbashEncode(unittest.TestCase):
    def test_encode_lowercase(self):
        result = Atbash.encode("yes")
        expected = "bvh"

        self.assertEqual(result, expected)

    def test_encode_uppercase(self):
        result = Atbash.encode("YES")
        expected = "BVH"

        self.assertEqual(result, expected)

    def test_name_attribute(self):
        result = Atbash.NAME
        expected = "Atbash"

        self.assertEqual(result, expected)


class TestAtbashDecode(unittest.TestCase):
    def test_decode_lowercase(self):
        result = Atbash.encode("bvh")
        expected = "yes"

        self.assertEqual(result, expected)

    def test_decode_uppercase(self):
        result = Atbash.encode("BVH")
        expected = "YES"

        self.assertEqual(result, expected)


class TestAtbashOnlyLetters(unittest.TestCase):
    def test_leave_extra_charecters(self):
        result = Atbash.encode("Hello, World!")
        expected = "Svool, Dliow!"

        self.assertEqual(result, expected)

    def test_leave_numbers(self):
        result = Atbash.encode("1 2 3 45 50")
        expected = "1 2 3 45 50"

        self.assertEqual(result, expected)


class TestAtbashPhrase(unittest.TestCase):
    def test_encode_phrase(self):
        result = Atbash.encode('The quick brown fox jumps over the lazy dog.')
        expected = 'Gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt.'

        self.assertEqual(result, expected)


class TestAtbashReversable(unittest.TestCase):
    def test_encode_reversable(self):
        result = Atbash.encode(Atbash.encode('yes'))
        expected = 'yes'

        self.assertEqual(result, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()