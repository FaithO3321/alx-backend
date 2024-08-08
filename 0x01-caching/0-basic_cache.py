#!/usr/bin/python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
