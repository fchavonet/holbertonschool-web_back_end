#!/usr/bin/env python3
"""
Module with a function that takes two integer
and return a tuple of size two containing a start index and an end index.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for pagination.

    Parameters:
      - page: an integer representing the current page (1-indexed)
      - page_size: an integer representing the number of items per page

    Returns:
      - A tuple containing the start index and end index
        for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
