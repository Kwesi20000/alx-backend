#!/usr/bin/env python3
"""
A basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class that represents an object that allows stroing
    and retrieving items from a dictionary
    """
    def put(self, key, item):
        """
        Function adds an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Function retrieves an item by key
        """
        return self.cache_data.get(key, None)
