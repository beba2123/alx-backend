#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from BaseCaching
                      and is a caching system
"""

from base_caching import BaseCaching


class BasiCache(BaseCaching): #inherit BaseCaching from base_Caching..
    """Base Cache"""
    
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """assign to the dictionary self.cache_data 
             the item value for the key key
        """
        if(key is not None and item is not None):
            self.cache__data[key] = item
    
    def get(self, key, item):
        """
        Must return the value in self.cache_data 
           linked to key
        """
        if(key is not None and item is not None):
            return self.cache__data[key]
        
        return None