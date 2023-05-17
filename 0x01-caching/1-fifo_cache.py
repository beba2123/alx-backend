#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from BaseCaching
                  and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
            the item value for the key key
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item
            if (key not in self.keys):
                self.keys.append(key)
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Must return the value in self.cache_data
                linked to key
        """
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
