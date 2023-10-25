#!/usr/bin/env python3
'''
BasicChache Module
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Inherits from BaseCaching'''
    def put(self, key, item):
        '''Assigns to a dictionary'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Returns the value linked to cache_data dict'''
        if key and key in self.cache_data:
            return self.cache_data[key]
