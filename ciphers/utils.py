import string
from textwrap import wrap


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
    def alphabetical(cls, text: str) -> str:
        """
        Converts a string to lowercase and removes all characters that are not 
        letters.

        Example:
            >>> CleanInput.alphabetical("My, Number is 19!")
            'mynumberis'

        Args:
            text (str):
                The input string to clean.

        Returns:
            str:
                A lowercase string containing only a-z characters.
        """
        return ''.join([ch for ch in text.lower() if ch in string.ascii_lowercase])

    @classmethod
    def alphanumeric(cls, text: str) -> str:
        """
        Converts a string to lowercase and removes all characters that are not 
        letters or digits.

        Example:
            >>> CleanInput.alphanumeric("My, Number is 19!")
            'mynumberis19'

        Args:
            text (str):
                The input string to clean.

        Returns:
            str:
                A lowercase string containing only a-z and 0-9 characters.
        """
        return ''.join([ch for ch in text.lower() if ch in string.ascii_lowercase + "0123456789"])

    @classmethod
    def alphanumeric_with_space(cls, text: str) -> str:
        """
        Converts a string to lowercase and removes all characters that are not 
        letters, digits, or spaces.

        Example:
            >>> CleanInput.alphanumeric_with_space("My, Number is 19!")
            'my number is 19'

        Args:
            text (str):
                The input string to clean.

        Returns:
            str:
                A lowercase string containing only a-z, 0-9, and spaces.
        """
        return ''.join([ch for ch in text.lower() if ch in string.ascii_lowercase + "0123456789" + " "])