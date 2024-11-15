#!/usr/bin/env python3

"""
FIFO Cache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class.
    Implements a FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO policy.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)

            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Get an item by key.
        If key is None or the key is not in the cache, return None.
        """
        return self.cache_data.get(key, None)
