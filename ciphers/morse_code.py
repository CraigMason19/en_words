"""
Morse code encoding utilities
-----------------------------

This module provides a lookup table for converting letters and digits into
Morse code, along with helper methods for producing either a space-separated
string or a list of Morse symbols.

Timing Conventions (for reference):
    - 1 dot worth of silence between each dash and dot within a character
    - 1 dash worth of silence between each character
    - 1 dash should be the duration of 3 dots
"""

import re

from .cipher import Cipher
from .utils import CleanInput

ENCODING_DELIMITER: str = "|"

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

class MorseCode(Cipher):
    @classmethod
    def is_valid_charset(cls, text: str) -> bool:
        """
        Return True if the string contains only characters from the Morse code
        character set: dot (.), dash (-), and space.

        Example:
            >>> MorseCode.is_valid_charset(".... . .-.. .-.. ---")
            True
            >>> MorseCode.is_valid_charset(".-.. -.. / --- !!")
            False
                    
        Args:
            text (str):
                The input text to test.

        Returns:
            bool:
                True if the string contains valid characters, False otherwise.
        """
        pattern = re.compile(r'^[ .-]+$', re.ASCII)
        return bool(pattern.match(text))

    @classmethod
    def encode(cls, text: str) -> str:
        """   
        Encodes a string into Morse code as a single space-separated string.

        Letters and digits are converted to dots and dashes. Spaces are replaced
        with the '|' delimiter to make word boundaries visible. All other
        characters are removed before encoding.

        Example:
            >>> MorseCode.encode("Hello, World!")
            .... . .-.. .-.. --- | .-- --- .-. .-.. -..
        
        Args:
            text (str):
                The input text to encode.

        Returns:
            str:
                A space-separated Morse code string.
        """
        return ' '.join([MORSE_LOOKUP[ch] for ch in CleanInput.alphanumeric_with_space(text)])
    
    encode_as_str = encode # Alias 

    @classmethod
    def encode_as_list(cls, text: str) -> list[str]:
        """
        Encodes a string into Morse code as a list of symbols.

        Letters and digits are converted to dots and dashes. Spaces are replaced
        with the '|' delimiter to make word boundaries visible. All other
        characters are removed before encoding.

        Example:
            >>> MorseCode.encode_as_list("Hello, World!")
            ['....', '.', '.-..', '.-..', '---', '|', '.--', '---', '.-.', '.-..', '-..']
        
        Args:
            text (str):
                The input text to encode.

        Returns:
            list[str]:
                A list of Morse code symbols.
        """
        return [MORSE_LOOKUP[ch] for ch in CleanInput.alphanumeric_with_space(text)]