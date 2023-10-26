# 0x01. Caching:file_folder:

**INTRODUCTION**

The project encompassed various aspects of caching systems, including their fundamental definition and understanding, key caching algorithms like FIFO, LIFO, LRU, MRU, and LFU. It also delved into the purpose of a caching system in optimizing data access and the limitations or constraints that can affect the performance of such systems. In essence, the project offered a comprehensive exploration of caching systems and their significance in data management.

**Parent class** `BaseCaching`
- All classes inherits from `BaseCaching` defined [here](./base_caching.py)


## Tasks:page_with_curl:
**0. Basic dictionary**
- [0-basic_cache.py](./0-basic_cache.py): class thats inherits from `BaseCaching` and is a caching system that:
  - uses `self.cache_data` - dictionary from the parent class `BaseCaching`
  - This caching system doesn’t have limit
  - `def put(self, key, item):`
    - Assigna to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method does nothing.
  - `def get(self, key):`
    - Returns the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, it returns `None`

**1. FIFO caching**
- [1-fifo_cache.py](./1-fifo_cache.py): class that inherits from `BaseCaching` and is a caching system that:
  - uses `self.cache_data` - dictionary from the parent class `BaseCaching`
  - overloads `def __init__(self):` and calls the parent init: `super().__init__()`
  - `def put(self, key, item):`
    - Assigns to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method does nothing.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
      - discards the first item put in cache (FIFO algorithm)
      - prints `DISCARD`: with the `key` discarded and following by a new line
  - `def get(self, key):`
    - returns the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, returns `None`

**2. LIFO Caching**
- [2-lifo_cache.py](./2-lifo_cache.py): class that inherits from `BaseCaching` and is a caching system that:
  - uses `self.cache_data` - dictionary from the parent class `BaseCaching`
  - overloads `def __init__(self):` and calls the parent init: `super().__init__()`
  - `def put(self, key, item):`
    - Assigns to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method does nothing.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
      - discards the last item put in cache (LIFO algorithm)
      - print `DISCARD:` with the `key` discarded and following by a new line
  - `def get(self, key):`
    - returns the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, returns `None`

**3. LRU Caching**
- [3-lru_cache.py](./3-lru_cache.py): class that inherits from `BaseCaching` and is a caching system that:
  - uses `self.cache_data` - dictionary from the parent class `BaseCaching`
  - overloads `def __init__(self):` and calls the parent init: `super().__init__()`
  - `def put(self, key, item):`
    - Assigns to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method does nothing.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
      - discards the least recently used item(LRU algorithm)
      - print `DISCARD:` with the `key` discardeea and following by a new line
  - `def get(self, key):`
    - returns the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, returns `None`

**4. MRU Caching**
- [4-mru_cache.py](./4-mru_cache.py): class that inherits from `BaseCaching` and is a caching system that:
  - uses `self.cache_data` - dictionary from the parent class `BaseCaching`
  - overloads `def __init__(self):` and calls the parent init: `super().__init__()`
  - `def put(self, key, item):`
    - Assigns to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method does nothing.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
      - discards the discard the most recently used item (MRU algorithm)
      - print `DISCARD:` with the `key` discardeea and following by a new line
  - `def get(self, key):`
    - returns the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, returns `None`

**5. LFU Caching**
- [100-lfu_cache.py](./100-lfu_cache.py): class that inherits from `BaseCaching` and is a caching system that:
  - uses `self.cache_data` - dictionary from the parent class `BaseCaching`
  - overloads `def __init__(self):` and calls the parent init: `super().__init__()`
  - `def put(self, key, item):`
    - Assigns to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method does nothing.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
      - discards the discard the least frequency used item (LFU algorithm)
      - if more than 1 item to discard found, it uses the LRU algorithm to discard only the least recently used
      - print `DISCARD:` with the `key` discardeea and following by a new line
  - `def get(self, key):`
    - returns the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, returns `None`
