#!/usr/bin/env python3
"""API Design: Pagination module"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns a tuple containing the start index
    and end index corresponding to the range of indexes to return
    in a pagination system.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
