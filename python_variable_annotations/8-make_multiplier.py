#!/usr/bin/env python3
""" Module with a type-annotated function to create a multiplier function. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): the multiplier value.

    Returns:
        Callable[[float], float]: a function that takes a float and multiplies
                                  it by the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the specified multiplier.

        Args:
            x (float): the input float.

        Returns:
            float: the result of multiplying x by the specified multiplier.
        """
        return x * multiplier

    return multiplier_function
