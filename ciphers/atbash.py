"""
Atbash Cipher
-------------

A implementation of the Atbash Cipher. A cipher that I discovered via Exercism.

A simple substitution cipher that maps each letter to its reverse position in the
alphabet.

The Atbash cipher is symmetric, meaning the same operation is used for both
encoding and decoding.

For example:
    'A' -> 'Z'
    'Z' -> 'A' 
    'b' -> 'y'
    'y' -> 'b' 

https://exercism.org/tracks/javascript/exercises/atbash-cipher
"""

import string

ATBASH_LOOKUP = {a: b for a, b in zip(string.ascii_letters, string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1])} 

class Atbash: 
    @classmethod
    def encode_letter(cls, letter: str) -> str:
        """
        Encodes or decodes a single character using the Atbash cipher.

        Alphabetical characters are mapped to their reverse position in the
        alphabet (e.g. 'A' → 'Z', 'b' → 'y'). Non-alphabetical characters are
        returned unchanged. Letter case is preserved.

        Example:
            >>> Atbash.encodeLetter("A")
            'Z'
            >>> Atbash.encodeLetter("b")
            'y'
            >>> Atbash.encodeLetter("!")
            '!'

        Args:
            letter (str):
                A single character to encode or decode.

        Returns:
            str:
                The encoded (or decoded) character.
        """
        return ATBASH_LOOKUP.get(letter, letter)
    
    @classmethod
    def encode(cls, text: str) -> str:
        """
        Encodes a string using the Atbash cipher.

        Alphabetical characters are mapped to their reverse position in the
        alphabet (e.g. 'A' → 'Z', 'b' → 'y'). Non-alphabetical characters are
        returned unchanged. Letter case is preserved.

        The Atbash cipher is symmetric, so the method `decode` is an alias of
        this method.

        Example:
            >>> Atbash.encode("Hello, World!")
            'Svool, Dliow!'

        Args:
            text (str):
                The input text to encode.

        Returns:
            str:
                The encoded text.
        """   
        return ''.join([cls.encode_letter(l) for l in text])

    decode = encode # Alias