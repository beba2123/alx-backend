#!/usr/bin/env python3
"""Discription:> implement a method name get_page that takes two arguments page
            with default value 1 and page size with default value 10.
            use assert to verify both arguments are integer greater than zero
            and also use index_range to find the correct indexes to paginate
            dataset.
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function.py').index_range

# this is for importing index_range function from 0-simple _helper_function.py


class server:
    """server class to paginate a database of popular baby names"""
    DATA_FILE = "popular baby names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Return page of dataset. '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []
        return dataset[start:end]
