"""
letters.py
----------

Provides useful helper functions for working with letters and alphabets.

English Letter Frequency:
	Taken from Cornell University, a study of 40,000 words.
 
	https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
"""

import string
import random

ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase

def is_letter(letter: str) -> bool:
    """
    Simple helper function to make sure a string is a single letter (upper 
    or lower).
    
    Args:
		letter (str):
			The string to check.
            
    Returns:
		bool:
			True if the string is a single letter. False otherwise.
    """
    if not letter.isalpha() or len(letter) != 1:
        return False

    return True

def letter_to_index(letter):
    """Returns a letter's index position in the alphabet. E.g. a->0, Z->25.

    Args:
      letter:
        The letter whoose index we want to find.

    Returns:
      An integer index of the relevant letter.
    """
    # Doesn't matter if we search the lower or uppercase alphabet, just choose one
    return ALPHABET_UPPER.index(letter.capitalize())

def index_to_letter(index, upper=False):
    """Returns a letter from an index position in the alphabet. E.g. 0->a, 25->Z.

    Args:
      index:
        The index of the letter we want to find.
      upper:
        A flag to determine wheter we return a upper or lower case letter.

    Returns:
      A letter either in upper or lowercase.
    """
    if(upper):
        return ALPHABET_UPPER[index]
    else:
        return ALPHABET_LOWER[index]

def next_letter(letter):
    """Returns the letter after a given letter. E.g. A->B, Z->A.

    Args:
      letter:
        The base letter. 

    Returns:
      A letter either in upper or lowercase depending on the case the letter 
      passed in.
    """
    index, alphabet = letter_to_index(letter), ALPHABET_LOWER

    if letter.isupper():
        alphabet = ALPHABET_UPPER

    if index == 25:
        index = 0
    else:
        index += 1
    
    return alphabet[index]

def previous_letter(letter):
    """Returns the letter before a given letter. E.g. B->A, A->Z.

    Args:
      letter:
        The base letter. 

    Returns:
      A letter either in upper or lowercase depending on the case the letter 
      passed in.
    """
    index, alphabet = letter_to_index(letter), ALPHABET_LOWER

    if letter.isupper():
        alphabet = ALPHABET_UPPER

    if index == 0:
        index = 25
    else:
        index -= 1
    
    return alphabet[index]

def shift_letter_up(letter, offset):
    """Returns a letter that is x letters higher.

    Args:
      letter:
        The base letter 
      offset:
        An integer representing how many places to shift.

    Returns:
      A letter either in upper or lowercase depending on the case of the letter 
      passed in.

    Raises:
      ValueError: A offset value < 0.
    """
    if offset < 0:
        raise ValueError("Shift up offset must not be less than 0")
    elif offset == 0:
        return letter

    index, alphabet = letter_to_index(letter) + offset, ALPHABET_LOWER

    if letter.isupper():
        alphabet = ALPHABET_UPPER

    while index > 25:
        index = index % 26

    return alphabet[index]

def shift_letter_down(letter, offset):
    """Returns a letter that is x letters lower.

    Args:
      letter:
        The base letter 
      offset:
        An integer representing how many places to shift.

    Returns:
      A letter either in upper or lowercase depending on the case of the letter 
      passed in.

    Raises:
      ValueError: A offset value > 0.
    """
    if offset > 0:
        raise ValueError("Shift down offset must not be higher than 0")
    elif offset == 0:
        return letter

    alphabet = ALPHABET_LOWER

    if letter.isupper():
        alphabet = ALPHABET_UPPER

    index, letter_index = -offset, letter_to_index(letter)

    while index > 25:
        index = index % 26

    # For example, (b, -3) = Y
    # letters_after = cdefghijklmnopqrstuvwxyz
    # letters_upto = ab
    # inverted_alphabet = ba + zyxwvutsrqponmlkjihgfedc = bazyxwvutsrqponmlkjihgfedc
    # Now we just got up from 'b' 3 spaces to 'y'
    letters_after = alphabet[letter_index+1:]
    letters_upto = alphabet[:letter_index+1]
    inverted_alphabet = (letters_after + letters_upto)[::-1]

    return inverted_alphabet[index]

def shift(letter, offset):
    """Returns a letter that is x letters higher or lower.

    Args:
      letter:
        The base letter 
      offset:
        An integer representing how many places to shift, negative or positive.

    Returns:
      A letter either in upper or lowercase depending on the case of the letter 
      passed in.
    """
    if offset == 0:
        return letter
    elif offset < 0:
        return shift_letter_down(letter, offset)
    elif offset > 0:
        return shift_letter_up(letter, offset)

def alphabet_generator(start_letter='a'):
    """A generator that will constantly loop over the alphabet, can be set to 
       start at a specific letter.

    Args:
      start_letter:
        The letter to start generating a sequence from. Default is 'a'. 

    Returns:
      A letter either in upper or lowercase depending on the case of the letter 
      passed in.
    """
    index, alphabet = letter_to_index(start_letter), ALPHABET_LOWER

    if start_letter.isupper():
        alphabet = ALPHABET_UPPER

    # To begin, slice the alphabet where the first letter is
    for letter in alphabet[index:]:
        yield letter

    # Now we just keep going 
    while True:
        for letter in alphabet:
            yield letter 

def shift_alphabet(offset, upper):
    """Returns a alphabet sequence that is x letters higher or lower.

    Args:
      offset:
        An integer representing how many places to shift, negative or positive.
      upper:
        A bool determining whether a upper or lower case alphabet sequence is 
        returned.

    Returns:
      A alphabet sequence shifted by an offset amount and in either upper or 
      lowercase depending on the bool passed in.
    """
    if not upper:
        return caesar_cipher(ALPHABET_LOWER, offset)    
    else:
        return caesar_cipher(ALPHABET_UPPER, offset)    

def caesar_cipher(message, offset=3):
    """A classic cipher used commonly by Caesar. Shifts every letter up by a 
       certain offset. 
       Historically by 3. e.g. a->d.

    Args:
      message:
        The message you want to encrypt. 
      offset:
        An integer representing how many places to shift.

    Returns:
      A encrypted message as a string.
    """
    s = [shift(letter, offset) for letter in message]
    return ''.join(s)

def random_lower_letter():
    """Returns a random lowercase letter

    Args:
      None

    Returns:
      A single lowercase letter.
    """  
    return random.choice(ALPHABET_LOWER)   

def random_upper_letter():
    """Returns a random uppercase letter

    Args:
      None

    Returns:
      A single uppercase letter.
    """  
    return random.choice(ALPHABET_UPPER)   

def random_letter():
    """Returns a random lowercase or uppercase letter

    Returns:
      A single lowercase or uppercase letter.
    """    
    return random.choice(ALPHABET_LOWER + ALPHABET_UPPER) 


class LetterFrequency:
    frequency_dict: dict[str, float] = {
		'E'	: 12.02,
		'T'	: 9.10,
		'A'	: 8.12,
		'O'	: 7.68,
		'I'	: 7.31,
		'N'	: 6.95,
		'S'	: 6.28,
		'R'	: 6.02,
		'H'	: 5.92,
		'D' : 4.32,
		'L' : 3.98,
		'U' : 2.88,
		'C' : 2.71,
		'M' : 2.61,
		'F' : 2.30,
		'Y' : 2.11,
		'W' : 2.09,
		'G' : 2.03,
		'P' : 1.82,
		'B' : 1.49,
		'V' : 1.11,
		'K' : 0.69,
		'X' : 0.17,
		'Q' : 0.11,
		'J' : 0.10,
		'Z' : 0.07,
	}
    
    @classmethod
    def percentage(cls, letter: str) -> float:
        """
		Returns the frequency percentage for a specific letter. 

		Args:
			letter (str):
				The letter whoose frequency you want to check.
        
        Rasies:
			ValueError:
				If the letter parameter isn't a single lower or uppercase 
                letter.
				
		Returns:
			float:
				The perctange as a float describing how common the letter is.
		"""               
        if not is_letter(letter):
            raise ValueError(f'Letter parameter "{letter:}" is not a letter.')
        
        return cls.frequency_dict[letter.upper()]