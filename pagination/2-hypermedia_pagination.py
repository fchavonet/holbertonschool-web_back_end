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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return hypermedia information about the dataset
        based on pagination parameters.

        Args:
            - page (int): page number (default is 1).
            - page_size (int): number of items per page (default is 10).

        Returns:
            - dict: hypermedia information including page_size, page number,
                    dataset page, next_page, prev_page, and total_pages.
        """
        current_page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_info = {
            "page_size": len(current_page_data),
            "page": page,
            "data": current_page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_info
