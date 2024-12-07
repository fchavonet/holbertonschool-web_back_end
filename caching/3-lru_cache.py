#!/usr/bin/env python3

"""
LRU Cache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class.
    Implements an LRU caching system.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LRU policy.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)

            self.cache_data[key] = item
            self.access_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Get an item by key.
        If key is None or the key is not in the cache, return None.
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
