#!/usr/bin/env python3

"""
LIFO Cache module.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class.
    Implements a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache using LIFO policy.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

            self.last_key = key

    def get(self, key):
        """
        Get an item by key.
        If key is None or the key is not in the cache, return None.
        """
        return self.cache_data.get(key, None)
