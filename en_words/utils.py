from collections import Counter
from typing import Any


def is_sublist(a: list[Any]=None, b: list[Any]=None) -> bool:
    """
    Return True if `a`` can be formed from `b`, including duplicates.

    Both lists default to None but must be given, otherwise a ValueError is 
    raised.

    Args:
        a (list[Any]):
            The collection to test for containment.
        b (list[b]):
            The collection to test against.

    Raises:
        ValueError:
            If either `a` or `b` are None or not given. 

    Returns:
        bool:
            True if `a` is a sublist of `b`, otherwise False.
    """
    if a is None or b is None:
        raise ValueError("Both lists must be given")

    return Counter(a) <= Counter(b)