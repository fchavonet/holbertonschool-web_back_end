#!/usr/bin/env python3
"""
Module with a type-annotated function
to convert a string and an int OR float to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int OR float to a tuple.

    Args:
        k (str): the input string.
        v (Union[int, float]): the input integer or float.

    Returns:
        Tuple[str, float]: a tuple containing the string k
                           and the square of v as a float.
    """
    return (k, v ** 2)
