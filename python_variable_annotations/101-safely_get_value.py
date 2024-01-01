#!/usr/bin/env python3
"""
Module with a type-annotated function
to safely retrieving a value from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): the input dictionary.
        key (Any): the key to search for in the dictionary.
        default (Union[T, None], optional): the default value to return
                                            if the key is not found.
                                            Defaults to None.

    Returns:
        Union[Any, T]: the value associated with the key if it exists,
                       otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
