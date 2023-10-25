#!/usr/bin/env python3
'''
FIFOCache Module
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Inherits from BaseCaching'''
    def __init__(self):
        '''Initialize the class '''
        super().__init__()

    def put(self, key, item):
        '''Assigns to a dict'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print('DISCARD: {}'.format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        '''returns cache_data key'''
        if key and key in self.cache_data:
            return self.cache_data[key]
