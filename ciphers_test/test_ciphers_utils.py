import unittest

from ciphers.utils import (
    chunk_text,
)


class TestChunkText(unittest.TestCase):
    def test_chunk_size_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = chunk_text("quintessence", -1)

    def test_chunk_size_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = chunk_text("quintessence", 0)    

    def test_chunk_size_default(self):
        result = chunk_text("quintessence")
        expected = "quint essen ce"

        self.assertEqual(result, expected)

    def test_chunk_size_default_same(self):
        result = chunk_text("hello world")
        expected = "hello world"

        self.assertEqual(result, expected)

    def test_chunk_size_default_with_space(self):
        result = chunk_text("hi craig")
        expected = "hicra ig"

        self.assertEqual(result, expected)

    def test_chunk_text_chunk_size_3(self):
        result = chunk_text("quintessence", 3)
        expected = "qui nte sse nce"

        self.assertEqual(result, expected)

    def test_chunk_text_chunk_size_9(self):
        result = chunk_text("quintessence", 9)
        expected = "quintesse nce"

        self.assertEqual(result, expected)

    def test_chunk_text_chunk_size_4_long_text(self):
        text = "Lorem ipsum dolor sit amet, consectetuer"
        result = chunk_text(text, 4)
        expected = "Lore mips umdo lors itam et,c onse ctet uer"

        self.assertEqual(result, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()