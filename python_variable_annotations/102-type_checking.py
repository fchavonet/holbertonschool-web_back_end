#!/usr/bin/env python3
""" Module with a type-annotated function for zooming in on an array. """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on an array by repeating each element.

    Args:
        lst (Tuple): the input tuple.
        factor (int, optional): the zoom factor. Defaults to 2.

    Returns:
        List: the zoomed-in array with each element
              repeated according to the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
