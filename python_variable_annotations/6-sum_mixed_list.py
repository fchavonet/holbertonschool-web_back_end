#!/usr/bin/env python3
"""
Module with a type-annotated function
to sum a list with mixed integer and float elements.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list with mixed integer and float elements.

    Args:
        mxd_lst (List[Union[int, float]]): a list containing integers
                                           and/or floats.

    Returns:
        float: the sum of the input list elements.
    """
    return sum(mxd_lst)
