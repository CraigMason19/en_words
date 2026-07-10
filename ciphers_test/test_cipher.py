import unittest

from ciphers.cipher import Cipher


class BadCipher(Cipher):
    pass


class TestCipher(unittest.TestCase):
    def test_cant_instantiate(self):
        with self.assertRaises(TypeError):
            _ = Cipher()

    def test_cant_instantiate_subclass_without_implementation(self):
        with self.assertRaises(TypeError):
            _ = BadCipher()

    def test_cipher_methods_are_class_methods(self):
        self.assertIsInstance(Cipher.__dict__['encode'], classmethod)
        self.assertIsInstance(Cipher.__dict__['decode'], classmethod)


if __name__ == '__main__': # pragma: no cover
    unittest.main()