"""
This module defines the `Cipher` abstract base class.

Cipher subclasses cannot be instantiated; instead, they expose class-level 
`encode` and `decode` methods.
"""

from abc import ABC, abstractmethod

class Cipher(ABC):
    """
    Abstract base class for cipher implementations.

    Subclasses must implement `encode` and `decode` as class methods.
    Cipher classes are stateless and must not be instantiated.

    Attributes:
        NAME (str):
            A class attribute helper to get the ciphers name easily.

    Methods:
        __new__(cls, *args, **kwargs): 
            Prevent instantiation of cipher classes.
        encode(text: str) -> str:
            Encode the given text using the cipher.
        decode(text: str) -> str:
            Decodes the given text using the cipher.
    """
    NAME: str

    def __init_subclass__(cls):
        """
        """
        super().__init_subclass__()
        cls.NAME = cls.__name__
    
    def __new__(cls, *args, **kwargs): 
        """
        Prevent instantiation of cipher classes.

        Cipher implementations are intended to be used via their
        class methods (`encode` and `decode`) rather than as objects.
        """
        raise TypeError("Cipher types cannot be instantiated")

    @staticmethod
    @abstractmethod 
    def encode(text: str) -> str:
        """
        Encodes the given text using the cipher.

        Args:
            text (str):
                The plain-text string to encode.

        Returns:
            str:
                The encoded cipher-text string.
        """
        raise NotImplementedError
        
    @staticmethod
    @abstractmethod
    def decode(text: str) -> str:
        """
        Decodes the given text using the cipher.

        Args:
            text (str):
                The cipher-text string to decode.

        Returns:
            str:
                The decoded plain-text string.
        """
        raise NotImplementedError