from abc import ABC, abstractmethod

class Cipher(ABC):
    def __new__(cls, *args, **kwargs): 
        raise TypeError("Cipher types cannot be instantiated")

    @classmethod
    @abstractmethod 
    def encode(cls, text: str) -> str:
        pass
        
    @classmethod
    @abstractmethod
    def decode(cls, text: str) -> str:
        pass