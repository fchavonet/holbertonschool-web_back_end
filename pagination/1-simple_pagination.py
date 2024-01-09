#!/usr/bin/env python3
""" Server for paginating a database of popular baby names. """

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset
        based on pagination parameters.

        Args:
            - page (int): page number (default is 1).
            - page_size (int): number of items per page (default is 10).

        Returns:
            - List[List]: the correct list of rows
                          for the specified pagination parameters.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        page_indexes: tuple = index_range(page, page_size)
        dataset: List = self.dataset()

        current_page_data = dataset[page_indexes[0]:page_indexes[1]]
        return current_page_data
