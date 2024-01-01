#!/usr/bin/env python3
"""
Module with a type-annotated function
to process element lengths in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the parameters and return values with the appropriate types.

    Args:
        lst (Iterable[Sequence]): an iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: a list of tuples where each tuple contains
                                    a sequence from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
