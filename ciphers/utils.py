"""
utils.py
---------------

Various tools for displaying and cleaning ciphers.

Globals:
    ENCODING_DELIMITER (str): 
        The default delimiter used in encoding.
    UNKNOWN_TOKEN (str):
        The default token used when decoding a token fails.

Functions:
    chunk_text: 
        Splits a string into fixed-length chunks separated by spaces.
"""

from textwrap import wrap


ENCODING_DELIMITER: str = '/'
UNKNOWN_TOKEN: str = '_'


def chunk_text(text: str, chunk_size: int = 5) -> str:
    """
    Splits a string into fixed-length chunks separated by spaces. 
    
    Characters are preserved whereas spaces are not. The chunk_size must be 
    positive.

    Args:
        text (str):
            The input string to be chunked.
        chunk_size (int):
            The number of characters per chunk. Must be greater than 0.

    Raises:
        ValueError:
            If the chunk_size is less than 1.

    Returns:
        str:
            The chunked string with chunks separated by spaces.
    """
    if chunk_size < 1:
        raise ValueError("chunk_size cannot be less than 1: {chunk_size}")

    return ' '.join(wrap(text.replace(' ', ''), chunk_size))