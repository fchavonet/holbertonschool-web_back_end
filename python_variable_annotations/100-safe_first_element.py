#!/usr/bin/env python3
"""
Module with a duck-typed function
to safely retrieve the first element of a sequence.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck-typed function to safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): a sequence of elements.

    Returns:
        Union[Any, None]: the first element of the sequence
                          or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
