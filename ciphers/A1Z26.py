"""
A1Z26
-----

A simple cipher that converts letters into their corresponding alphabetical 
position. (e.g. A=1, B=2, …, Z=26)

Encoding follows the rules
    - Upper and lowercase letters are converted to the same value.
    - Spaces are replaced with the '/' delimiter to make word boundaries visible.
    - Encoded numbers are space separated.
    - Other characters are stripped out.

Decoding follows the rules
    - Numbers are converted to Uppercase letters.
    - '/' delimiter is converted into a space.
    - Incorrect tokens (not 1-26) are replaced with a '_'

Example:
    The quick brown fox jumps over the lazy dog.
    20 8 5 / 17 21 9 3 11 / 2 18 15 23 14 / 6 15 24 / 10 21 13 16 19 / 15 22 5 18 / 20 8 5 / 12 1 26 25 / 4 15 7
    THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
"""

import string

from .cipher import Cipher
from .utils import CleanInput, ENCODING_DELIMITER, UNKNOWN_TOKEN


A1Z26_LOOKUP = { k: str(v) for v, k in enumerate(string.ascii_uppercase, 1) } | {' ': ENCODING_DELIMITER }
REVERSE_A1Z26_LOOKUP = {v: k for k, v in A1Z26_LOOKUP.items()}


class A1Z26(Cipher):
    @staticmethod
    def encode(text: str) -> str:
        tokens = CleanInput.to_alpha(text, with_spaces=True).split()
        clean_str = ' '.join(tokens).upper()

        return ' '.join(A1Z26_LOOKUP[ch] for ch in clean_str)

    @staticmethod
    def decode(text: str) -> str:
        
        decoded = []

        for token in text.split():

            decoded.append(REVERSE_A1Z26_LOOKUP.get(token, UNKNOWN_TOKEN))

        return "".join(decoded)