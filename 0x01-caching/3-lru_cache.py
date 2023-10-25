#!/usr/bin/env python3
'''
LRUCache Module
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''Inherits from BaseCaching'''
    def __init__(self):
        '''Initialize the class'''
        super().__init__()
        # initialize an ordered dict to maitain usage
        self.usage_order = OrderedDict()

    def put(self, key, item):
        '''Assigns to a dict'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = next(iter(self.usage_order))
                del self.cache_data[lru_key]
                del self.usage_order[lru_key]
                print('DISCARD: {}'.format(lru_key))

            self.cache_data[key] = item
            self.usage_order[key] = None

    def get(self, key):
        '''Returns cache_data key'''
        if key and key in self.cache_data:
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
