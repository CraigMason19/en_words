lookup = [
                 ('abc',  2), ('def',  3), 
    ('ghi',  4), ('jkl',  5), ('mno',  6), 
    ('pqrs', 7), ('tuv',  8), ('wxyz', 9)
]

mapping = {}
for letters, num in lookup:
    for letter in letters:
        mapping[letter] = str(num)


class T9Cipher:
    """    
    A one-way lossy T9-style cipher that maps letters to numbers based on a 
    classic mobile phone keypad layout.

    This implementation is not reversible because multiple letters map to the
    same digit. 
    
    e.g. 'a', 'b', and 'c' all map to '2'. 
    """

    @classmethod
    def encode(cls, text: str) -> str:
        """
        Encode a string into its T9 numeric representation.

        Example:
            >>> T9.encode("Craig")
            '27244'
        
        Args:
            text (str): Input text to encode.

        Returns:
            str: Encoded numeric string, with non-alphabetic characters left 
                unchanged.
        """
        return ''.join(mapping.get(ch.lower(), ch) for ch in text)


# class ReversibleT9:
#     """Multi-tap phone keypad mapping (reversible)."""
#     ...

# ReversibleT9.encode("cab")  # '222 2 22'
# ReversibleT9.decode("222 2 22")  # 'cab'
# ReversibleT9.decode("222d2022")  # 'cab' -> anything not a 1-9 digit 




























# reversable
# maybe use a 0 deliminator

# lookup = [
#     ('abc', 2),
#     ('def', 3),
#     ('ghi', 4),
#     ('jkl', 5),
#     ('mno', 6),
#     ('pqrs', 7),
#     ('tuv', 8),
#     ('wxyz', 9)
# ]

# # Build forward mapping: letter -> number sequence
# forward_map = {}
# for letters, digit in lookup:
#     for idx, letter in enumerate(letters, start=1):
#         forward_map[letter] = str(digit) * idx

# # Build reverse mapping: number sequence -> letter
# reverse_map = {v: k for k, v in forward_map.items()}

# def word_to_t9(word: str) -> str:
#     """Encrypt word to T9-style number sequence."""
#     return ' '.join(forward_map.get(ch, ch) for ch in word.lower())

# def t9_to_word(code: str) -> str:
#     """Decrypt T9 number sequence back to letters."""
#     return ''.join(reverse_map.get(part, part) for part in code.split())

# # Example
# word = "ThisIsASuperSecretPassword"
# encrypted = word_to_t9(word)
# decrypted = t9_to_word(encrypted)

# print("Original:", word)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)