import string
from textwrap import wrap

ENCODING_DELIMITER: str = '/'
UNKNOWN_TOKEN = '_'

def chunk_text(text: str, chunk_size: int = 5) -> str:
    """
    Splits a string into fixed-length chunks separated by spaces.

    Args:
        text (str):
            The input string to be chunked.
        chunk_size (int):
            The number of characters per chunk.

    Returns:
        str:
            The chunked string with chunks separated by spaces.
    """
    return ' '.join(wrap(text, chunk_size))


class CleanInput:
    @classmethod
    def to_alpha(cls, text: str, with_spaces: bool = False) -> str:
        """
        Converts a string to lowercase and removes all characters that are not 
        letters.

        Example:
            >>> CleanInput.alphabetical("My, Number is 19!")
            'mynumberis'

            >>> CleanInput.alphabetical("My, Number is 19!", with_spaces=True)
            'my number is'

        Args:
            text (str):
                The input string to clean.
            with_spaces (bool):
                A flag to determine whether to include spaces or not.

        Returns:
            str:
                A lowercase string containing a-z characters and potentially spaces.
        """
        charset = string.ascii_lowercase
        
        if with_spaces:
            charset += " "

        return ''.join([ch for ch in text.lower() if ch in charset])

    @classmethod
    def to_alphanumeric(cls, text: str, with_spaces: bool = False) -> str:
        """
        Converts a string to lowercase and removes all characters that are not 
        letters or digits.

        Example:
            >>> CleanInput.alphanumeric("My, Number is 19!")
            'mynumberis19'

            >>> CleanInput.alphanumeric("My, Number is 19!", with_spaces=True)
            'my number is 19'

        Args:
            text (str):
                The input string to clean.
            with_spaces (bool):
                A flag to determine whether to include spaces or not.

        Returns:
            str:
                A lowercase string containing only a-z, 0-9 characters and potentially spaces.
        """
        charset = string.ascii_lowercase + "0123456789"
        
        if with_spaces:
            charset += " "

        return ''.join([ch for ch in text.lower() if ch in charset])