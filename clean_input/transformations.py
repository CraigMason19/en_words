import string

from abc import ABC, abstractmethod


SPACE = " "
NUMBERS = "0123456789"


# region Transformations

class Transformation(ABC):
    """
    Abstract base class for input transformations.

    Subclasses must implement `transform()`, accepting a string
    and returning its transformed representation.
    """
    @abstractmethod
    def transform(self, text: str) -> str:
        """
        Transform the supplied text.

        Args:
            text (str):
                The input string to transform.

        Returns:
            str:
                A transformed string.
        """
        ...


class Alpha(Transformation):
    """
    Retains ASCII characters and spaces, removing all other characters.

    Character case is preserved.

    Examples:
        >>> Alpha.transform("Hello, World!")
        'Hello World'
        >>> Alpha.transform("ABC 123 xyz")
        'ABC  xyz'
    """
    @staticmethod
    def transform(text: str) -> str:
        charset = string.ascii_lowercase + SPACE

        return ''.join([ch for ch in text if ch.lower() in charset])

    
class Alphanumeric(Transformation):
    """
    Retains ASCII characters, numbers and spaces, removing all other characters.

    Character case is preserved.

    Examples:
        >>> Alphanumeric.transform("Hello, World #19!")
        'Hello World 19'
        >>> Alphanumeric.transform("ABC 123 xyz")
        'ABC 123 xyz'
    """
    @staticmethod
    def transform(text: str) -> str:
        charset = string.ascii_lowercase + NUMBERS + SPACE

        return ''.join([ch for ch in text if ch.lower() in charset])
    

class Lowercase(Transformation):
    @staticmethod
    def transform(text: str) -> str:
        return text.lower()


class NormalizeWhitespace(Transformation):
    @staticmethod
    def transform(text: str) -> str:
        return " ".join(text.split())
    

class RemovePunctuation(Transformation):
    @staticmethod
    def transform(text: str) -> str:
        return text.translate(str.maketrans("", "", string.punctuation))
    

class RemoveWhitespace(Transformation):
    @staticmethod
    def transform(text: str) -> str:
        return "".join(text.split())


class Uppercase(Transformation):
    @staticmethod
    def transform(text: str) -> str:
        return text.upper()
    
#endregion


#region Pipeline

class TransformationPipeline:
    def __init__(self, 
        transformations: list[Transformation] | None=None,
        ignore_spaces: bool=True) -> None:

        self.transformations = list(transformations) if transformations is not None else []
        self.ignore_spaces = ignore_spaces

        for t in self.transformations:
            if not isinstance(t, Transformation):
                raise TypeError(f"Every pipeline stage must be a Transformation. '{repr(t)}'")
        

    def transform(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Pipeline input must be a string.")

        for t in self.transformations:
            text = t.transform(text)

        return text


    def transform_all(self, texts: list[str]) -> list[str]:
        """


        Examples:
            >>> import clean_input as ci
            >>> ts = [ci.Uppercase()]
            >>> p = ci.TransformationPipeline(ts)
            >>> ws = ["hello", "world"]
            >>> p.transform_all(ws)
            ['HELLO', 'WORLD']

        Args:
            texts (list[str]):
                A list of strings to transform at once.

        Raises:
            TypeError:
                If the `texts` input is not a list.

        Returns:
            list[str]:
        """
        if not isinstance(texts, list):
            raise TypeError("Pipeline input must be a list of strings.")

        return [self.transform(text) for text in texts]


#endregion