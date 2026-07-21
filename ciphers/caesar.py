"""
Caesar Cipher
-------------

A simple substitution cipher that shifts each alphabetical character forward
by a fixed number of positions. Case is preserved and non‑alphabetic symbols
are left unchanged. Shifts must be between 1 and 25 inclusive; a shift of 0 
or 26 would return the original text unchanged.

Examples:
    'A' shifted by 3 → 'D'
    'x' shifted by 4 → 'b'
"""

from ciphers.cipher import Cipher

from en_words.letters import shift_letter_up, shift_letter_down


class Caesar(Cipher): 
    """
    Implements the classic Caesar shift cipher.

    The cipher moves each alphabetical character forward (encode) or backward
    (decode) by a fixed number of positions. Case is preserved and any
    non‑alphabetic characters are returned unchanged. Valid shifts are integers
    from 1 to 25 inclusive.

    Methods:
        _is_valid_shift(shift: int=3):
            Checks if the shift amount is greater than 0 and less than 26.
        encode(cls, message: str, shift=3) -> str:
            Encode a string using the Caesar cipher.
        decode(cls, message: str, shift=3) -> str:
            Decodes a string using the Caesar cipher.
    """

    def _is_valid_shift(shift: int=3):
        """
        Checks if the shift amount is greater than 0 and less than 26.

        A valid shift is any integer from 1 to 25 inclusive. A shift of 0 or 26
        would leave the text unchanged. Negative shifts are not permitted.

        Returns True if the shift is valid, otherwise False.

        Args:
            shift (int):
                The amount to shift a letter by in the encoding.

        Returns:
            bool:
                True if the shift is valid, False otherwise.
        """
        if 0 < shift < 26:
            return True
        
        return False
        
    @classmethod
    def encode(cls, text: str, shift: int=3) -> str:
        """
        Encode a string using the Caesar cipher.

        Each alphabetical character is shifted forward by the given amount.
        Case is preserved and non‑alphabetic characters are returned unchanged.
        The shift must be between 1 and 25 inclusive.

        Example:
            >>> Caesar.encode("abc", 1)
            'bcd'

        Args:
            text (str):
                The input text to encode.
            shift (int):
                The number of positions to shift (default 3).

        Raises:
            ValueError:
                If the shift amount is not greater than 0 and less than 26.

        Returns:
            str:
                The encoded text.
        """   
        if not cls._is_valid_shift(shift):
            raise ValueError("Caesar cipher shift must be greater than 0 and less than 26.")

        encoded_tokens = []

        for token in text:
            encoded_token = shift_letter_up(token, shift) if token.isalpha() else token
            encoded_tokens.append(encoded_token)

        return ''.join(encoded_tokens)

    @classmethod
    def decode(cls, text: str, shift=3) -> str:
        """
        Decodes a string using the Caesar cipher.

        Each alphabetical character is shifted forward by the given amount.
        Case is preserved and non‑alphabetic characters are returned unchanged.
        The shift must be between 1 and 25 inclusive.

        Example:
            >>> Caesar.decode("def", 2)
            'bcd'

        Args:
            text (str):
                The input text to encode.
            shift (int):
                The number of positions to shift (default 3).

        Raises:
            ValueError:
                If the shift amount is not greater than 0 and less than 26.

        Returns:
            str:
                The encoded text.
        """   
        if not cls._is_valid_shift(shift):
            raise ValueError("Caesar cipher shift must be greater than 0 and less than 26.")

        decoded_tokens = []

        for token in text:
            decoded_token = shift_letter_down(token, -shift) if token.isalpha() else token
            decoded_tokens.append(decoded_token)

        return ''.join(decoded_tokens)