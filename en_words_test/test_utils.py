import unittest

from en_words.utils import is_sublist


class TestIsSublist(unittest.TestCase):

    # Empty
    def test_both_lists_empty(self):
        result = is_sublist([], [])
        expected = True

        self.assertEqual(result, expected)

    def test_both_list_a_empty(self):
        result = is_sublist([], [5])
        expected = True

        self.assertEqual(result, expected)

    def test_both_list_b_empty(self):
        result = is_sublist([5], [])
        expected = False

        self.assertEqual(result, expected)

    # None
    def test_both_lists_none(self):
        with self.assertRaises(ValueError):
            _ = is_sublist()

    def test_both_list_a_none(self):
        with self.assertRaises(ValueError):
            _ = is_sublist(None, [5])

    def test_both_list_b_none(self):
        with self.assertRaises(ValueError):
            _ = is_sublist([5], None)

    # Mixed sets
    def test_mixed_lists_true(self):
        result = is_sublist([1, "bar"], [1, 2, "foo", "bar"])
        expected = True

        self.assertEqual(result, expected)

    # General
    def test_list_a_under(self):
        result = is_sublist([1, 2], [1, 2, 2])
        expected = True

        self.assertEqual(result, expected)

    def test_list_a_same(self):
        result = is_sublist([1, 2, 2], [1, 2, 2])
        expected = True

        self.assertEqual(result, expected)

    def test_list_a_over(self):
        result = is_sublist([1, 2, 2, 2], [1, 2, 2])
        expected = False

        self.assertEqual(result, expected)

    # Integers
    def test_integers_true(self):
        result = is_sublist([1, 2], [1, 2, 3])
        expected = True

        self.assertEqual(result, expected)

    def test_integers_false(self):
        result = is_sublist([1, 2], [1, 5, 6])
        expected = False

        self.assertEqual(result, expected)

    # Strings
    def test_strings_true(self):
        result = is_sublist(["A", "B"], ["A", "B", "C"])
        expected = True

        self.assertEqual(result, expected)

    def test_strings_false(self):
        result = is_sublist(["A", "B", "B"], ["A", "B", "C"])
        expected = False

        self.assertEqual(result, expected)