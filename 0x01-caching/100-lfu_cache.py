#!/usr/bin/env python3
'''
LFUCache Module
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    '''Inherits from BaseCaching'''
    def __init__(self):
        '''Initialize the class'''
        super().__init__()
        # initialize an ordered dict to maitain usage
        self.usage_order = OrderedDict()

        # initialize a dict to keep track of access frequences
        self.frequency = {}

    def put(self, key, item):
        '''Assigns to a dict'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find and remove the least frequently used item
                lfu_key = min(self.frequency, key=self.frequency.get)
                del self.cache_data[lfu_key]
                del self.usage_order[lfu_key]
                del self.frequency[lfu_key]
                print('DISCARD: {}'.format(lfu_key))

            '''Add new item to the cache, update usage order,
            and increase frequency'''
            self.cache_data[key] = item
            self.usage_order[key] = None
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        '''Returns cache_data key'''
        if key and key in self.cache_data:
            self.usage_order.move_to_end(key)
            # Icrease frequency for accessed items
            self.frequency[key] += 1
            return self.cache_data[key]
