#!/usr/bin/env python3
"""
File: 3-lru_cache.py
 Create a class LIFOCache that inherits from BaseCaching
                  and is a caching system.
Author: Anteneh Alem
Date Created: May 17, 2023
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU(List Recently Used) Caching"""
    lst = []

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Stores a new item to the cache"""
        if key is not None and item is not None:
            if key in LRUCache.lst:
                LRUCache.lst.remove(key)
                LRUCache.lst.append(key)
                return
            self.cache_data[key] = item
            LRUCache.lst.append(key)

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            key_to_be_removed = LRUCache.lst[0]
            if (key_to_be_removed in self.cache_data.keys()):
                self.cache_data.pop(key_to_be_removed)
                print('DISCARD: {}'.format(LRUCache.lst.pop(0)))

    def get(self, key):
        """Returns an item based on the key"""
        if (key is None or key not in self.cache_data.keys()):
            return None
        if key in LRUCache.lst:
            LRUCache.lst.remove(key)
            LRUCache.lst.append(key)

        return self.cache_data[key]
