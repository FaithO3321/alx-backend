#!/usr/bin/python3
"""
    Create a class FIFOCache that inherits
    from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the first item added
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
