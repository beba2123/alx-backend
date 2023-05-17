#!/usr/bin/env python3
""" Create a class LIFOCache that inherits
    from BaseCaching and is a caching system
"""
from basic_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO-CACHE"""

    def __init__(self):
        super.__init__()
        self.keys = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
            the item value for the key key
        """

        if (key is not None or item is not None):
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        ''' Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None. '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
