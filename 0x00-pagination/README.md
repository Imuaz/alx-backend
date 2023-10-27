# 0x00. Pagination:scroll:

**INTRODUCTION**

The project encompassed various aspects of dataset pagination, including techniques like simple pagination with page and page_size parameters, pagination with hypermedia metadata, and achieving pagination in a deletion-resilient manner. These methods are crucial for efficiently managing and navigating large datasets in software applications.

## Resources:books:
***Read or watch:***
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.m.wikipedia.org/wiki/HATEOAS)

**SETUP**:wrench:
`Popular_Baby_Names.csv`
[this data file](./Popular_Baby_Names.csv) is used fo this project.

## Tasks:page_with_curl:
**0. Simple helper function**
- [0-simple_helper_function.py](./0-simple_helper_function.py): A function that takes two integer arguments `page` and `page_size`.
  - It returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to rturn in a list for those particular pagination parameters.
  - Page numbers are 1-indexed, i.e. the first page is page 1.

**1. Simple pagination**
- [1-simple_pagination.py](./1-simple_pagination.py): A method defined in `Server` class that takes two integer arguments `page` with default value `1` and `page_size` with default value `10`.
  - It uses `assert` to verify that both arguments are integers greater than `0`,
  - `index_range` to find the correct indexes to paginate the dataset correctly and returns the appropriate page of the dataset (i.e. the correct list of rows).
  - If the input arguments are out of range for the dataset, returns an empty list.

**2. Hypermedia pagination**
- [2-hypermedia_pagination.py](./2-hypermedia_pagination.py): A method defined in `Server` class that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
  - `page_size`: the length of the returned dataset page
  - `page`: the current page number
  - `data`: the dataset page (equivalent to return from previous task)
  - `next_page`: number of the next page, None if no next page
  - `prev_page`: number of the previous page, None if no previous page
  - `total_pages`: the total number of pages in the dataset as an integer
- it reuses `get_page` method and the `math` module where necessary.

**3. Deletion-resilient hypermedia pagination**
- [3-hypermedia_del_pagination.py](./3-hypermedia_del_pagination.py): A method in `Server` class that takes two integer arguments: `index` with a `None` default value and `page_size` with default value of `10`.
  - The method returns a dictionary with the following key-value pairs:
    - `index`: the current start index of the return page. That is the index of the first item in the current page. For example if requesting `page` 3 with `page_size` 20, and no data was removed from the dataset, the current index should be 60.
    - `next_index`: the next index to query with. That is the index of the first item after the last item on the current page.
    - `page_size`: the current page size
    - `data`: the actual page of the dataset
  - Requirements/Behavior:
    - Uses `assert` to verify that `index` is in a valid range.
    - If the user queries index 0, `page_size` 10, they will get rows indexed 0 to 9 included.
    - If they request the next index (10) with `page_size` 10, but rows 3, 6 and 7 were deleted, the user still receive rows indexed 10 to 19 included.
