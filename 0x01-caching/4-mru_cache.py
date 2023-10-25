#!/usr/bin/env python3
'''
MRUCache Module
'''
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
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
                mru_key = next(reversed(self.usage_order))
                del self.cache_data[mru_key]
                del self.usage_order[mru_key]
                print('DISCARD: {}'.format(mru_key))

            self.cache_data[key] = item
            self.usage_order[key] = None

    def get(self, key):
        '''Returns cache_data key'''
        if key and key in self.cache_data:
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
