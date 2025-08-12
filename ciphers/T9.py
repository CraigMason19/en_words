import string

ENCODING_DELIMITER: str = "-"

lookup = [
                 ('abc',  2), ('def',  3), 
    ('ghi',  4), ('jkl',  5), ('mno',  6), 
    ('pqrs', 7), ('tuv',  8), ('wxyz', 9)
]

digit_map = {}
for letters, num in lookup:
    for ch in letters:
        digit_map[ch] = str(num)

presses_map = {}
for letters, _ in lookup:
    for i, letter in enumerate(letters, start=1):
        presses_map[letter] = i

def presses_for_letter(ch: str) -> int:
    """
    Return the number of key presses required for a given letter on a classic 
    T9 phone keypad.

    Args:
        ch (str): A letter (any case).

    Returns:
        int: The number of presses needed to type the letter (1-4).

    Raises:
        ValueError
            If `ch` is not a letter present in the T9 lookup.
    """
    ch = ch.lower()

    try:
        return presses_map[ch]
    except KeyError:          
        raise ValueError(f"Parameter passed was not a letter in the T9 lookup: {ch}")

def letter_from_presses(number: int, count: int) -> str:
    """
    Return the letter corresponding to a digit pressed 'count' times on a classic T9 keypad.

    Args:
        number (int): The digit key (2-9).
        count (int): Number of times the key is pressed (1 to number of letters on key).

    Returns:
        str: The decoded letter.

    Raises:
        ValueError: If the digit is not valid or count is out of range.
    """
    for letters, digit in lookup:
        if number == digit:
            if 1 <= count <= len(letters):
                return letters[count - 1]
            else:
                raise ValueError(f"Count {count} out of range for digit {number} (max {len(letters)})")
            
    raise ValueError(f"Digit {number} is not valid in T9 lookup")


def _cleanInput(text: str) -> str:
    return ''.join([ch for ch in text.lower() if ch in string.ascii_lowercase])


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
            str: Encoded numeric string, with non-alphabetic characters removed
        """
        return ''.join(digit_map.get(ch.lower(), '') for ch in _cleanInput(text))


class ReversibleT9Cipher:
    """
    A reversible T9-style cipher for encoding and decoding text using the 
    classic mobile phone keypad layout.

    This class converts letters to their corresponding T9 numeric sequences 
    (e.g., 'c' -> '222') and can reverse the process back to text, ignores 
    spaces and non-alphabetic characters.

    The encoded characters are joined using the delimiter defined by the
    `ENCODING_DELIMITER` ("-").

    NOTE: Case is not preserved and output will always be lowercase.
    """
    @classmethod
    def encode(cls, text: str) -> str:
        """
        Encode a string into a reversible T9 numeric representation.

        The encoded characters are joined using the delimiter defined by the
        `ENCODING_DELIMITER` ("-").

        NOTE: Case is not preserved and output will always be lowercase.

        Example:
            >>> T9.encode("Hello!!!")
            "44-33-555-555-666"
        
        Args:
            text (str): Input text to encode.

        Returns:
            str: Encoded numeric string joined by `ENCODING_DELIMITER`, removes 
                non-alphabetic characters.
        """
        letters = []

        for ch in _cleanInput(text):
            if(ch in digit_map):
                letters.append(digit_map[ch] * presses_map[ch])
                continue

            letters.append(ch)
            
        return ENCODING_DELIMITER.join(letters)

    @classmethod
    def decode(cls, encoded_text: str) -> str:
        """
        Decodes a ReversibleT9Cipher string into its original representation.

        The encoded characters are joined using the delimiter defined by the
        `ENCODING_DELIMITER` ("-").

        NOTE: Case is not preserved and output will always be lowercase.

        Example:
            >>> ReversibleT9Cipher.Decode("44-33-555-555-666")
            "hello"
        
        Args:
            encoded_text (str): ReversibleT9Cipher encoded string.

        Returns:
            str: Decoded lowercase string with letters only.

        Raises
            ValueError: If the encoded string does not contain any digits or the
                encoding delimiter, or if any part between delimiters is empty.
        """
        if not encoded_text or not all(c.isdigit() or c == '-' for c in encoded_text):
            raise ValueError(f"Encoded text must contain digits and use '{ENCODING_DELIMITER}' as the delimiter.")
        
        parts = encoded_text.split(ENCODING_DELIMITER)

        if any(part == '' for part in parts):
            raise ValueError("Encoded text contains empty chunks due to consecutive delimiters.")
    
        letters = []
        
        for part in parts:
            digit, press_count = int(part[0]), len(part)
            letters.append(letter_from_presses(digit, press_count))

        return ''.join(letters)