"""
Polybius Checkerboard
---------------------

Just something fun I found in the Horrible Histories book "The Groovy Greeks". 

A grid based cipher where the letter is encoded / decoded by its vertical then 
horizontal position.

NOTE: The Grid is 25 instead of 26 letters because I & J were used interchangeably.
This implementation defaults to 'I'.

   1  2  3  4  5
1  A  B  C  D  E
2  F  G  H  I  K
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z

Example:
    Encoding:
        "Hello" -> "23 15 31 31 34"
    Decoding:
        "23 15 31 31 34" -> "HELLO"
"""

import re

from .cipher import Cipher
from .utils import CleanInput


class PolybiusCheckerboard(Cipher):
    """ 
    A class wrapper representing a Polybius Checkerboard. 
    
    25 instead of 26 as I and J were used interchangeably. this uses I currently

    Attributes:
        _GRID:
            The grid representation of the checkerboard.

    Methods:
        is_valid_encoding(cls, text: str) -> bool:
            Determines if a string is a valid Polybius encoded string. 
        cell(cls, column: int, row: int) -> str:
            Returns the letter in the cell specified by the column then row.
        cell_coords(cls, letter: str) -> str:
            Returns the co-ordinates of the letter in the checkerboard.
        encode(cls, message: str) -> str:
            Returns the encoded message as a string of 2-digit numbers.
        decode(cls, message: str) -> str:
            Decodes a string of space separated 2-digit numbers to uppercase letters.
        def pretty_print(cls) -> None:
            Prints out the checkerboard in a formatted grid view.
    """
    _GRID = [
        [' ', 1, 2, 3, 4, 5],
        [1, 'A', 'B', 'C', 'D', 'E'],
        [2, 'F', 'G', 'H', 'I', 'K'],
        [3, 'L', 'M', 'N', 'O', 'P'],
        [4, 'Q', 'R', 'S', 'T', 'U'],
        [5, 'V', 'W', 'X', 'Y', 'Z'],
    ]

    @classmethod
    def is_valid_encoding(cls, text: str) -> bool:
        """
        Determines if a string is a valid Polybius encoded string. 
        
        A valid string is a string of 2-digit numbers each digit between (1-5 inclusive) separated by spaces.

        Example:
            >>> is_valid_encoding('11 55 24')
            True

        Args:
            text (str):
                The string to check.

        Returns:
            bool:
                True if it is a valid encoding, False otherwise
        """ 
        pattern = re.compile(r'^(?:[1-5]{2})(?:\s+[1-5]{2})*$', re.ASCII)
        
        return bool(pattern.match(text))

    @classmethod
    def cell(cls, column: int, row: int) -> str:
        """ 
        Returns the letter in the cell specified by the column then row.

        Example:
            >>> PolybiusCheckerboard.cell(1, 3)
            C        

        Args:
            column (int): 
                A number in the range 1-5. 
            row (int): 
                A number in the range 1-5. 

        Raises:
            IndexError:
                If either the column or row index is less than 0 or greater than 5.

        Returns:
            str: 
                The uppercase letter in the corresponding grid position.
        """
        if column < 1 or column > 5:
            raise IndexError("Column index must be in the 1-5 range.")

        if row < 1 or row > 5:
            raise IndexError("Row index must be in the 1-5 range.")

        return cls._GRID[column][row]

    @classmethod
    def cell_coords(cls, letter: str) -> str:
        """ 
        Returns the co-ordinates of the letter in the checkerboard. Specified by
        the column then row. Case is irrelevant.

        NOTE: I & J are interchangeable and will result in the same value.

        Example:
            >>> PolybiusCheckerboard.cell_coords('C')
            13 
            >>> PolybiusCheckerboard.cell_coords('I')
            24
            >>> PolybiusCheckerboard.cell_coords('J')       
            24

        Args:
            letter (str):
                The letter to find in the checkerboard. 

        Returns:
            int: 
                An integer representing the grid column and row.
        """
        letter = letter.upper()  

        letter = 'I' if (letter == "J") else letter

        for i, row in enumerate(cls._GRID):
            for j, col in enumerate(row):
                if cls._GRID[i][j] == letter:
                    return (str(i) + str(j))

    @classmethod
    def encode(cls, message: str) -> str:
        """
        Returns the encoded message as a string of 2-digit numbers. Only letters
        are encoded. Other symbols are ignored (Space included).

        NOTE: I & J are converted to the same number as they were interchangeable.

        Example:
            >>> PolybiusCheckerboard.encode('Hello')
            "23 15 31 31 34"
        
        Args:
            message (str):
                The message to encode.

        Returns:
            str: 
                A string of 2-digit numbers separated by spaces.
        """
        clean = CleanInput.to_alpha(message).upper()
        clean = clean.replace('J', 'I') # interchangeable

        return ' '.join([cls.cell_coords(c) for c in clean])

    @classmethod
    def decode(cls, message: str) -> str:
        """
        Decodes a string of space separated 2-digit numbers to uppercase letters.
        
        NOTE: Because I & J were interchangeable they will both be converted to 'I'.

        Example:
            >>> PolybiusCheckerboard.decode('23 15 31 31 34 52 34 42 31 14')
            "HELLOWORLD"
        
        Args:
            message (str):
                The message to decode.

        Raises:
            ValueError:
                If the string to decode is not a properly formatted polybius code.

        Returns:
            str: 
                A uppercase string without spaces or punctuation containing the original text.
        """       
        if not cls.is_valid_encoding(message):
            raise ValueError("Couldn't decode non properly formatted encoding string")
    
        decoded = []

        for _ in message.split():
            h, v = int(_[0]), int(_[1])
            decoded.append(cls.cell(h, v))

        return ''.join(decoded)

    @classmethod
    def pretty_print(cls) -> None: # pragma no cover
        """ 
        Prints out the checkerboard in a formatted grid view. 

        Example:
            >>> PolybiusCheckerboard.pretty_print()
                 1    2    3    4    5    
            1    A    B    C    D    E    
            2    F    G    H    I    K    
            3    L    M    N    O    P    
            4    Q    R    S    T    U    
            5    V    W    X    Y    Z
        """  
        for r in cls._GRID:
            print(("{: <5}" * 6).format(*r)) 