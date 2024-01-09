#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return hypermedia information about the dataset
        based on index and pagination parameters.

        Args:
            - index (int): start index of the return page (default is None).
            - page_size (int): number of items per page (default is 10).

        Returns:
            - Dict: hypermedia information including index, next_index,
                    page_size, data, and total_pages.
        """
        dataset = self.indexed_dataset()
        current_page_data = []
        next_index = index

        assert index is None or (type(index) is int
                                 and 0 <= index < len(dataset))
        assert type(page_size) is int and page_size > 0

        while len(current_page_data) < page_size and next_index in dataset:
            item = dataset[next_index]
            current_page_data.append(item)
            next_index += 1

        hyper_info = {
            "index": index,
            "data": current_page_data,
            "page_size": page_size,
            "next_index": next_index,
        }

        return hyper_info
