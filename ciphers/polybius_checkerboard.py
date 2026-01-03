""" 
Just something fun I found in the Horrible Histories book 'The Groovy Greeks'. 
"""

class PolybiusCheckerboard:
    """ 
    25 instead of 26 as I and J were used interchangably 
    """
    _grid = [
        [' ', 1, 2, 3, 4, 5],
        [1, 'A', 'B', 'C', 'D', 'E'],
        [2, 'F', 'G', 'H', 'I', 'K'],
        [3, 'L', 'M', 'N', 'O', 'P'],
        [4, 'Q', 'R', 'S', 'T', 'U'],
        [5, 'V', 'W', 'X', 'Y', 'Z'],
    ]

    @classmethod
    def cell(cls, hor, vert):
        """ A horizontal and then vertical lookup table """
        if hor < 1 or hor > 5:
            raise IndexError("Horizontal index must be in 1-5 range.")

        if vert < 1 or vert > 5:
            raise IndexError("Vertical index must be in 1-5 range.")

        return cls._grid[hor][vert]

    @classmethod
    def grid_position(cls, letter: str) -> int:
        letter = letter.upper()  

        for i, row in enumerate(cls._grid):
            for j, col in enumerate(row):
                if cls._grid[i][j] == letter:
                    return (str(i) + str(j))

    @classmethod
    def encode(cls, message: str) -> str:
        message = message.replace(' ', '').upper()
        message = message.replace('J', 'I') # interchangeable

        return ' '.join([cls.grid_position(c) for c in message])

    @classmethod
    def decode(cls, message: str) -> str:
        tmp = message.split(' ')
        decrypted = []

        for _ in tmp:
            h, v = int(_[0]), int(_[1]) # raise if cant convert, raise if not an int
            decrypted.append(cls.cell(h, v))

        return ''.join(decrypted)

    @classmethod
    def pretty_print(cls):
        for r in cls._grid:
            print(("{: <5}" * 6).format(*r)) 