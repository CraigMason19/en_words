import unittest

from ciphers.cipher import Cipher


class EmptyCipher(Cipher):
    pass


class TestCipher(unittest.TestCase):
    def test_cant_instantiate(self):
        with self.assertRaises(TypeError):
            _ = Cipher()

    def test_cant_instantiate_subclass_without_implementation(self):
        with self.assertRaises(TypeError):
            _ = EmptyCipher()

    def test_cipher_methods_are_static_methods(self):
        self.assertIsInstance(Cipher.__dict__['encode'], staticmethod)
        self.assertIsInstance(Cipher.__dict__['decode'], staticmethod)

    def test_cipher_encode_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            _ = Cipher.encode("foo")

    def test_cipher_decode_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            _ = Cipher.decode("foo")


if __name__ == '__main__': # pragma: no cover
    unittest.main()