#!/usr/bin/env python3

"""
MRU Cache module.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class.
    Implements an MRU caching system.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """
        Add an item to the cache using MRU policy.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            self.mru_key = key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.mru_key in self.cache_data:
                    del self.cache_data[self.mru_key]
                    print(f"DISCARD: {self.mru_key}")
                    self.mru_key = None

    def get(self, key):
        """
        Get an item by key.
        If key is None or the key is not in the cache, return None.
        """
        if key is not None and key in self.cache_data:
            self.mru_key = key
            return self.cache_data[key]
        return None