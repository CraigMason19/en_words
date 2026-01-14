"""
Morse code
----------

This module provides a lookup table and a `MorseCode` class for converting letters
and digits into Morse code.

Encoding follows the rules
    - Letters and digits are converted to dots and dashes.
    - Spaces are replaced with the '/' delimiter to make word boundaries visible.
    - Other characters are stripped out.

Decoding follows the rules
    - Dots and dashes are decoded to lowercase letters & numbers.
    - Unknown dot and dash tokens are replaced with a '_'
    - '/' delimiter is converted into a space.

Timing Conventions (for reference):
    - 1 dot worth of silence between each dash and dot within a character
    - 1 dash worth of silence between each character
    - 1 dash should be the duration of 3 dots
"""

import re

from .cipher import Cipher
from .utils import CleanInput, ENCODING_DELIMITER, UNKNOWN_TOKEN

MORSE_LOOKUP = {
    ' ': ENCODING_DELIMITER,

    'a': ".-",
    'b': "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': ".---",
    'k': "-.-",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    's': "...",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    'x': "-..-",
    'y': "-.--",
    'z': "--..",

    '0': "-----",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
}

REVERSE_MORSE_LOOKUP = {v: k for k, v in MORSE_LOOKUP.items()}

class MorseCode(Cipher):
    @classmethod
    def is_valid_charset(cls, text: str) -> bool:
        """
        Returns True if the string contains only characters from the following
        charset: 
        
        dot (.), dash (-), space ( ) or the word space delimiter(/).

        Example:
            >>> MorseCode.is_valid_charset(".... . .-.. .-.. ---")
            True
            >>> MorseCode.is_valid_charset(".-.. -.. , --- !!")
            False

        Args:
            text (str):
                The input text to test.

        Returns:
            bool:
                True if the string contains valid characters, False otherwise.
        """
        pattern = re.compile(r'^[/ .-]+$', re.ASCII)
        return bool(pattern.match(text))

    @classmethod
    def encode(cls, text: str) -> str:
        """   
        Encodes a string into Morse code as a single space-separated string.

        Encoding follows the rules
        - Letters and digits are converted to dots and dashes.
        - Unknown dot and dash tokens are replaced with a '_'
        - Spaces are replaced with the '/' delimiter to make word boundaries visible.

        Example:
            >>> MorseCode.encode("Hello, World!")
            .... . .-.. .-.. --- / .-- --- .-. .-.. -..
        
        Args:
            text (str):
                The input text to encode.

        Returns:
            str:
                A space-separated Morse code string.
        """
        tokens = CleanInput.alphanumeric_with_space(text).split()
        clean_str = ' '.join(tokens).lower()

        return ' '.join([MORSE_LOOKUP[ch] for ch in clean_str])
    
    encode_as_str = encode # Alias 

    @classmethod
    def encode_as_list(cls, text: str) -> list[str]:
        """
        Encodes a string into Morse code as a list of symbols.

        Encoding follows the rules
        - Letters and digits are converted to dots and dashes.
        - Spaces are replaced with the '/' delimiter to make word boundaries visible.

        Example:
            >>> MorseCode.encode_as_list("Hello, World!")
            ['....', '.', '.-..', '.-..', '---', '/', '.--', '---', '.-.', '.-..', '-..']
        
        Args:
            text (str):
                The input text to encode.

        Returns:
            list[str]:
                A list of Morse code symbols.
        """
        return [MORSE_LOOKUP[ch] for ch in CleanInput.alphanumeric_with_space(text)]
    
    @classmethod
    def decode(cls, text: str) -> str:
        """
        Decodes a string of dots and dashes to english text.
            
        Decoding follows the rules
        - Dots and dashes are decoded to lowercase letters & numbers.
        - Unknown dot and dash tokens are replaced with a '_'
        - '/' delimiter is converted into a space.

        Examples:
            >>> MorseCode.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
            hello world
            >>> MorseCode.decode(".... . .-.. .-.. --- .-- --- .-. .-.. -..")
            helloworld

        Args:
            text (str):
                The input text to decode.

        Raises:
            ValueError:
                If any character in the string is not in the Morse charset. '.- /'

        Returns:
            str:
                A decoded morse string.
        """       
        if not cls.is_valid_charset(text):
            raise ValueError("Input contains characters outside the Morse charset. '.- /'")

        decoded = []

        for token in text.split():
            decoded.append(REVERSE_MORSE_LOOKUP.get(token, UNKNOWN_TOKEN))

        return "".join(decoded)