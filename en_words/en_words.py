#-------------------------------------------------------------------------------
# Name:        en_words.py
#
# Notes:       A collection of methods for reading and interacting with a text 
#              file containing words in a dictionary. Also contains methods for
#              working with words. 
#
#              Makes use of a sorted dictionary (sorted by length as well as 
#              alphabetically) for faster lookups, a helper function
#              called create_sorted_dict will create one from a normal 
#              alphabetized dictionary.
#
# Links:        
#
# TODO:        
#
#-------------------------------------------------------------------------------

import os

from en_words.letters import VOWELS, CONSONANTS

# region Globals

_PATH = os.path.dirname(__file__)
_NAME = 'en_words'

_FILENAME = _PATH + "\\" + _NAME + ".txt"
_FILENAME_SORTED = _PATH + "\\" + _NAME + "_sorted.txt"

# Guess characters e.g. s?a_d -> salad
MISSING_CHARACTERS = '?-_.' 

#endregion

#region Dictionary Functions

def create_sorted_dict(filename=_FILENAME, filename_sorted=_FILENAME_SORTED):
    """ Reads a dictionary in alphabetical order and then creates a file that is 
        sorted by length and then alphabetically.

    Args:
        filename:
            The name of the file containing the dictionary.
        filename_sorted:
            The name of the file to create containing the sorted dictionary.

    Returns:
        None.
    """
    lines = None

    with open(filename) as f:
        lines = f.readlines()
        lines.sort(key=lambda item: (len(item), item)) # length then alphabetical
    
    with open(filename_sorted, 'w+') as f:
        for line in lines:
            f.write(line.lower())

def unsorted_words(filename: str=_FILENAME) -> list[str]:
    """ 
    Returns a list of words from a dictionary (not sorted by length) and in 
    lowercase.

    Args:
        filename (str):
            The name of the file containing the dictionary.

    Returns:
        list[str]:
            A list of lowercase words.
    """
    with open(filename) as f:
        return f.read().lower().splitlines()

def unsorted_words_gen(filename: str=_FILENAME):
    """ 
    A generator that returns a list of words from a dictionary (not sorted by 
    length) and in lowercase.

    Args:
        filename (str):
            The name of the file containing the dictionary.

    Returns:
        Generator
    """
    with open(filename) as f:
        for line in f:
            yield line.lower().strip()

def sorted_words(filename_sorted=_FILENAME_SORTED) -> list[str]:
    """ 
    Returns a list of words from a dictionary sorted by length as well as 
    alphabetically in lowercase.

    Args:
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        list[str]:
            A list of lowercase words.
    """
    with open(filename_sorted) as f:
        return f.read().lower().splitlines()

def sorted_words_gen(filename_sorted: str=_FILENAME_SORTED):
    """ 
    A generator that returns a word from a dictionary sorted by length and 
    alphabetically in lowercase.

    Args:
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        Generator
    """
    with open(filename_sorted) as f:
        for line in f:
            yield line.lower().strip()

def word_count(filename=_FILENAME):
    """ Returns the number of words in the dictionary.

    Args:
        filename:
            The name of the file containing the dictionary.

    Returns:
        A int.
    """
    counter = 0

    for word in sorted_words_gen(filename):
        counter += 1

    return counter

def find_largest_word(filename=_FILENAME):
    """ Returns the largest word in the dictionary. If there is no largest word, 
        the first word of largest length is returned.

    Args:
        filename:
            The name of the file containing the dictionary.

    Returns:
        A string.
    """
    max_word = ""

    for word in unsorted_words_gen(filename):
        if len(word) > len(max_word):
            max_word = word

    return max_word.lower()

# endregion

#region Word Finder functions 

def words_of_length(length: int=3, filename_sorted: str=_FILENAME_SORTED) -> list[str]:
    """ 
    Returns a list of all words of a certain length.

    Args:
        length (int):
            The minimum number of letters to find.
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        list[str]
    """
    if length < 0:
        return []
 
    words = []

    for word in sorted_words_gen(filename_sorted):
        letter_count = len(word)

        if letter_count > length:
            break

        elif letter_count == length:
            words.append(word.lower())

    return words

def words_of_length_gen(length: int=3, filename_sorted: str=_FILENAME_SORTED):
    """ 
    Returns a generator for finding all words of a certain length.

    Args:
        length (int):
            The minimum number of letters to find.
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        Generator
    """    
    if length < 0:
        return []

    for word in sorted_words_gen(filename_sorted):
        letter_count = len(word)

        if letter_count > length:
            break

        elif letter_count == length:
            yield word.lower()
 
def is_potential_match(partial_word, potential_word, ignore_letters='', required_letters=''):
    """ Compares two words to check if the words are a potential match. Returns 
        True if they are and False otherwise.

        E.g. is_potential_match("??ttl-", "battle", 'x', 'b') == True
             is_potential_match("??ttl-", "battle", 'xe', 'b') == False

    Args:
        partial_word:
            A word with letters missing (represented by MISSING_CHARACTERS global variable).
        potential_word:
            A word to compare.
        ignore_letters:
            A string of letters not needed.
        required_letters:
            A string of letters that are required.

    Returns:
        A bool.
    """ 
    partial_word, potential_word = partial_word.lower(), potential_word.lower()
    ignore_letters, required_letters = ignore_letters.lower(), required_letters.lower()

    # Check that the potential word has the required letters 
    for rl in required_letters:
        if rl not in potential_word:
            return False

    # If it does, compare each letter one at a time
    for letter_a, letter_b in zip(partial_word, potential_word):
        # Letter in second word is not allowed
        if letter_b in ignore_letters:
            return False

        # Unknown letter, go to the next
        elif letter_a in MISSING_CHARACTERS:
            continue

        # Not a match
        elif letter_a != letter_b:
            return False

    return True

def potential_words(partial_word, ignore_letters='', required_letters='', filename_sorted=_FILENAME_SORTED):
    """ Compares a partial word against the words inside the sorted dictionary. Returns a list
        of all potential matches. 

    Args:
        partial_word:
            A word with letters missing (represented by MISSING_CHARACTERS global variable).
        ignore_letters:
            A string of letters not needed.
        required_letters:
            A string of letters that are required.
        filename_sorted:
            The name of the file containing the sorted dictionary.

    Returns:
        A list of words.
    """ 
    partial_word = partial_word.lower()
    ignore_letters, required_letters = ignore_letters.lower(), required_letters.lower()
    
    words = []

    for potential_word in words_of_length_gen(len(partial_word), filename_sorted):
        if is_potential_match(partial_word, potential_word, ignore_letters, required_letters):
            words.append(potential_word.lower())

    return words

def letters_in_word(letters, word, remove_doubles=False):
    """ Checks that letters are in a word.

    Args:
        letters:
            A string of letters that are in a word.
        word:
            The word to check.
        remove_doubles:
            A bool to allow for / against double letters.

    Returns:
        A bool.
    """ 

    # Words with unique characters
    if remove_doubles:
        if len(set(word)) != len(word):
            return False

    for letter in word:
        if letter not in letters:
            return False
        
    return True

def words_from_letters(letters: str, 
        min_len: int=3,
        max_len: int=6,
        remove_doubles: bool=False,
        filename_sorted: str=_FILENAME_SORTED) -> list[str]:
    """ 
    Return all words that can be formed using the supplied letters.

    Unlike an anagram search, each letter may be used any number of times.
    A word is considered valid if it contains only characters from `letters` and 
    its length is between `min_len` and `max_len` (inclusive).

    Remove doubles can be set so that only words with unique letters are returned.

    Args:
        letters (str):
            A string of letters used in a word.
        min_len (int):
            The minimum word length.
        max_len (int):
            The maximum word length.
        remove_doubles (bool):
            Allow for or against double letters.
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        list[str]:
            A list containing all the matching words.
    """ 
    if min_len <= 0:
        raise ValueError(f"min_len cannot be less than 1: {min_len}")

    if max_len <= 0:
        raise ValueError(f"max_len cannot be less than 1: {max_len}")

    if min_len > max_len:
        raise ValueError(f"max_len cannot be bigger than min_len: {max_len} > {min_len}")


    letters = letters.lower()    
    words = []

    for word in sorted_words_gen(filename_sorted):
        if len(word) < min_len:
            continue

        else:
            if len(word) > max_len:
                break

        if letters_in_word(letters, word, remove_doubles):
            words.append(word.lower())

    return(words)

def vowel_count(word: str) -> int:
    """
    Counts the number of vowels in a string.

    Args:
        word (str):
            The input string to count.
    
    Returns:
        int:
            The number of vowels in a string.
    """
    return sum(letter in VOWELS for letter in word)

def consonant_count(word: str) -> int:
    """
    Counts the number of consonants in a string.

    Args:
        word (str):
            The input string to count.
    
    Returns:
        int:
            The number of consonants in a string.
    """
    return sum(letter in CONSONANTS for letter in word)

def anagrams(word: str, filename_sorted: str = _FILENAME_SORTED) -> list[str]:
    """ 
    Finds a list of words that are anagrams of a word.

    Args:
        word (str):
            A string of letters to find anagrams for.
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        list[str]:
            A list of all the anagrams found.
    """ 
    return [_ for _ in anagrams_gen(word, filename_sorted)]


def anagrams_gen(word: str, filename_sorted: str = _FILENAME_SORTED):
    """ 
    Finds a list of words that are anagrams of a word and returns a generator.

    Args:
        word (str):
            A string of letters to find anagrams for.
        filename_sorted (str):
            The name of the file containing the sorted dictionary.

    Returns:
        Generator:
    """ 
    word = word.lower()

    for _ in words_of_length_gen(len(word), filename_sorted):
        if ''.join(sorted(_)) == ''.join(sorted(word)) and _ != word:
            yield _

# endregion