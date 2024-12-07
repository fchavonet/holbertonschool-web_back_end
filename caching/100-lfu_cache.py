#!/usr/bin/env python3

"""
LFU Cache module.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class.
    Implements an LFU caching system.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LFU policy.
        If key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.__evict_lfu()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

        self.__update_usage_order(key)

    def get(self, key):
        """
        Get an item by key.
        If key is None or the key is not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.__update_usage_order(key)
        return self.cache_data[key]

    def __evict_lfu(self):
        """
        Evict the least frequently used item.
        Resolve ties using LRU (usage order).
        """
        min_freq = min(self.frequency.values())
        min_freq_keys = [
            key for key in self.frequency if self.frequency[key] == min_freq]

        for key in self.usage_order:
            if key in min_freq_keys:
                lfu_key = key
                break

        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        self.usage_order.remove(lfu_key)
        print(f"DISCARD: {lfu_key}")

    def __update_usage_order(self, key):
        """
        Update the usage order for a key.
        """
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)
