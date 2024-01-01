#!/usr/bin/env python3
""" Module with a type-annotated function to sum a list of floats. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): a list of floats.

    Returns:
        float: the sum of the input list of floats.
    """
    return sum(input_list)
