#!/usr/bin/env python3
'''
pagination module
'''


def index_range(page: int, page_size: int) -> tuple:
    ''' returns the right start and end indexes for a list'''
    start_index: int = (page - 1) * page_size
    end_index: int = ((start_index) + page_size)
    return (start_index, end_index)
