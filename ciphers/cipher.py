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

    Methods:
        __new__(cls, *args, **kwargs): 
            Prevent instantiation of cipher classes.
        encode(cls, text: str) -> str:
            Encode the given text using the cipher.
    """

    def __new__(cls, *args, **kwargs): 
        """
        Prevent instantiation of cipher classes.

        Cipher implementations are intended to be used via their
        class methods (`encode` and `decode`) rather than as objects.
        """
        raise TypeError("Cipher types cannot be instantiated")

    @classmethod
    @abstractmethod 
    def encode(cls, text: str) -> str:
        """
        Encodes the given text using the cipher.

        Args:
            text (str):
                The plain-text string to encode.

        Returns:
            str:
                The encoded cipher-text string.
        """
        pass # pragma: no cover
        
    @classmethod
    @abstractmethod
    def decode(cls, text: str) -> str:
        """
        Decodes the given text using the cipher.

        Args:
            text (str):
                The cipher-text string to decode.

        Returns:
            str:
                The decoded plain-text string.
        """
        pass # pragma: no cover