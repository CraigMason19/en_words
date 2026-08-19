import random

from collections import Counter
from typing import Self

from en_words.en_words import words_from_letters, potential_words, vowel_count
from en_words.utils import is_sublist

def spelling_bee(inner_letter, outer_letters):
    ''' https://spellingbeegame.org '''
    def contains_central_letter(word):
        # return word.find(inner_letter.lower()) == 1
        return (inner_letter.lower() in word)

    letters = outer_letters.lower() + inner_letter.lower()
    
    sb = words_from_letters(letters, min_len=4, max_len=None, remove_doubles=False)
    sb = [word for word in sb if contains_central_letter(word)]

    print(f'Spelling Bee: ({inner_letter.lower()}, {outer_letters.lower()}), count: {len(sb)}')
    print(f"\t{sb}")
    print("")


def wordle(word, ignore, include):
    ''' https://www.nytimes.com/games/wordle/index.html '''
    words = potential_words(word, ignore, include)
    print(f'Wordle: {word}, count: {len(words)}')
    print(f"\t{words}")
    print()


def polygon(inner_letter, outer_letters):
    ''' Game from The Times newspaper'''

    def contains_central_letter(word):
        return (inner_letter.lower() in word)

    letters = outer_letters.lower() + inner_letter.lower()
    
    p = words_from_letters(letters, min_len=4, max_len=9, remove_doubles=False)
    p = [word for word in p if contains_central_letter(word)]

    print(f'Polygon: ({inner_letter.lower()}, {outer_letters.lower()})')
    print(f"\t{p}")
    print("")


def cash_square(word_list):
    ''' From take a break magazine '''

    # E.g.
    #
    # Given words
    # a v e r
    # f l a p
    # g e n t
    # l i m e
    # n e w t
    #
    # Answer
    # f l a p
    # l i m e
    # a v e r
    # g e n t

    rows = [w.lower() for w in word_list]
    cols = [''.join(zipped) for zipped in zip(*rows)]

    # Precompute words that might be a soultion to a column
    potentials_col_1 = words_from_letters(cols[0], 4, 4)
    potentials_col_2 = words_from_letters(cols[1], 4, 4)
    potentials_col_3 = words_from_letters(cols[2], 4, 4)
    potentials_col_4 = words_from_letters(cols[3], 4, 4)

    for a in potentials_col_1:
        for b in potentials_col_2:
            for c in potentials_col_3:
                for d in potentials_col_4:
                    # recreate the rows
                    row_1 = ''.join([a[0], b[0], c[0], d[0]])
                    row_2 = ''.join([a[1], b[1], c[1], d[1]])
                    row_3 = ''.join([a[2], b[2], c[2], d[2]])
                    row_4 = ''.join([a[3], b[3], c[3], d[3]])

                    grid_set = set([row_1, row_2, row_3, row_4])

                    if grid_set.issubset(word_list):
                        answer = set(word_list).difference(grid_set)

                        print(f'Cash Grid: ({rows})')
                        
                        for r in [row_1, row_2, row_3, row_4]:
                            print(f'\t{" ".join(r).upper()}')

                        print(f'{answer.pop()}')
    
    print("")


#region Countdown

class Countdown:
    ''' 
    A solver for the UK TV show Countdown.
        
    Countdown uses nine letters. The selection must contain at least three vowels
    and at least four consonants, so the only valid combinations are:
        - 3 vowels, 6 consonants
        - 4 vowels, 5 consonants
        - 5 vowels, 4 consonants

    Vowels and consonants are drawn from a pool to maintain distribution.

    Valid words must be 3 letters or more.
    
    Attributes:
        VOWEL_POOL (list[str]):
            A class attribute of all available vowels.
        CONSONANT_POOL (list[str]):
            A class attribute of all available consonants.
        MIN_WORD_LEN (int):
            The minimum allowed word length. Default is 3
        MIN_VOWEL_COUNT (int):
            The minimum allowed number of vowels. Default is 3
        MAX_VOWEL_COUNT (int):
            The maximum allowed number of consonants. Default is 5

    Methods:
        __init__(self, letters: str):
            Constructs a Countdown object from a string of letters.

        is_valid_selection(letters: str) -> bool:
            A static method that checks if the letters given are a valid selection 
            in Countdown.

        from_vowel_count(cls, vowel_count: int) -> Self:
            A class method that creates a new Countdown object from a vowel count.

        def solve(self) -> dict[int, list[str]]:
            Finds all words that can be formed from the selected letters, groups 
            them by word count and returns the results as a dictionary. 
    
        solve_and_display(self) -> None:
            Finds all words that can be formed from the selected letters, groups 
            them by word count and then prints to the terminal.

        find_9_letter_game(cls) -> Self:
            A class method to find a Countdown game that has one or more 9 letter
            solutions. 

        __repr__(self) -> str:
            Returns a string representing the Countdown letters game. 
    '''

    VOWEL_POOL: list[str] = (
        ["A"] * 15
        + ["E"] * 13
        + ["I"] * 9
        + ["O"] * 8
        + ["U"] * 5
    )

    CONSONANT_POOL: list[str] = (
        ["B"] * 4
        + ["C"] * 5
        + ["D"] * 6
        + ["F"] * 8
        + ["G"] * 3
        + ["H"] * 5
        + ["J"] * 2
        + ["K"]
        + ["L"] * 5
        + ["M"] * 4
        + ["N"] * 8
        + ["P"] * 4
        + ["Q"]
        + ["R"] * 9
        + ["S"] * 9
        + ["T"] * 9
        + ["V"] * 2
        + ["W"] * 3
        + ["X"]
        + ["Y"] * 3
        + ["Z"] * 2
    )

    MIN_WORD_LEN = 3
    MIN_VOWEL_COUNT = 3
    MAX_VOWEL_COUNT = 5

    def __init__(self, letters: str):
        """
        Constructs a Countdown object from a string of letters.

        Args:
            letters (str):
                A valid string representing a countdown game. Any case.

        Raises:
            ValueError:
                If the string is not a valid game of countdown.
        """
        if not self.is_valid_selection(letters):
            raise ValueError(
                f"Invalid Countdown letter selection. '{letters}' " \
                f"Must be 9 letters long, contain between {Countdown.MIN_VOWEL_COUNT} & {Countdown.MAX_VOWEL_COUNT} vowels (inclusive) with the rest as consonants. " \
                "Must be pulled from the valid countdown letter distribution")

        self.letters = letters.upper()

    @staticmethod
    def is_valid_selection(letters: str) -> bool:
        """
        Checks if the letters given are a valid selection in Countdown.

        A selection is valid if the following criteria is met.
            - Must be 9 letters
            - Must have between 3 & 5 vowels (inclusive)
            - Must be of a valid distribution, matching the `VOWEL_POOL` + 
              `CONSONANT_POOL` distribution.
            - Case is ignored
 
        Args:
            letters (str):
                The letters selection.

        Returns:
            bool:
                True if the the selection is valid.
        """
        if not letters.isalpha():
            return False

        if len(letters) != 9:
            return False

        if not Countdown.MIN_VOWEL_COUNT <= vowel_count(letters) <= Countdown.MAX_VOWEL_COUNT:
            return False
        
        if not is_sublist(list(letters.upper()), Countdown.VOWEL_POOL + Countdown.CONSONANT_POOL):
            return False
                
        return True    

    @classmethod
    def from_vowel_count(cls, vowel_count: int) -> Self:
        """
        Creates a new Countdown object from how many vowels you want to select.

        Letters are chosen randomly and are then jumbled up to reflect a real game.

        Args:
            vowel_count (int):
                A integer between `MIN_VOWEL_COUNT` & `Countdown.MAX_VOWEL_COUNT` inclusive.

        Raises:
            ValueError:
                If the `vowel_count` is invalid

        Returns:
            Self:
                A new Countdown object.
        """
        if not Countdown.MIN_VOWEL_COUNT <= vowel_count <= Countdown.MAX_VOWEL_COUNT:
            raise ValueError(f"'vowel_count' must be between {Countdown.MIN_VOWEL_COUNT} & {Countdown.MAX_VOWEL_COUNT} (inclusive): {vowel_count}")

        letters = []
        consonant_count = 9 - vowel_count

        vowel_pool = Countdown.VOWEL_POOL.copy()
        consonant_pool = Countdown.CONSONANT_POOL.copy()

        for _ in range(vowel_count):
            letter = vowel_pool.pop(random.randrange(len(vowel_pool)))
            letters.append(letter)

        for _ in range(consonant_count):
            letter = consonant_pool.pop(random.randrange(len(consonant_pool)))
            letters.append(letter)

        random.shuffle(letters)

        return Countdown("".join(letters))

    def solve(self) -> dict[int, list[str]]:
        """
        Finds all words that can be formed from the selected letters and groups
        them by word length. The results are returned in a dictionary of the form:

            {word_length: [word, word, ...]}

        Returns:
            dict[int, list[str]]:
        """
        d = { i:[] for i in range(3, 9+1) }

        letters_counter = Counter(self.letters.lower())
        words = words_from_letters(self.letters, self.MIN_WORD_LEN, 9, False)

        for word in words:
            if Counter(word) <= letters_counter:
                d[len(word)].append(word)

        return d

    def solve_and_display(self) -> None:
        """
        Finds all words that can be formed from the selected letters and groups
        them by word length. The results are stored in a dictionary of the form:

            {word_length: [word, word, ...]}

        where the key is the length of the word and the value is a list of words
        of that length.

        The results are then printed to the terminal in increasing order of word
        length.

        Example:
            >>> Countdown('HDGRAEION').solve()

            Countdown: HDGRAEION
                3 letters (122):
                    ['ado', 'age', ...]
        """
        d = self.solve()

        print(f"Countdown: {self.letters}")

        for k, v in d.items():
            print(f"{k} letters ({len(v)}):")
            print(f"\t{v}")
            print("")
            
        print("")  

    @classmethod
    def find_9_letter_game(cls) -> Self:
        """
        A class method to find a Countdown game that has one or more 9 letter
        solutions. 

        Returns:
            Self:
                A new Countdown object.
        """       
        while True:
            vowel_count = random.choice([i for i in range(Countdown.MIN_VOWEL_COUNT, Countdown.MAX_VOWEL_COUNT + 1)])
            c = Countdown.from_vowel_count(vowel_count)
            d = c.solve()

            if len(d[9]) > 0:
                return c
            
    def __repr__(self) -> str:
        """ 
        Returns a string representing the Countdown letters game. 

        Example:
            >>> repr(Countdown("hdgraeion"))
            Countdown("HDGRAEION")

        Returns:
            str:
        """
        return f'Countdown("{self.letters}")'

#endregion