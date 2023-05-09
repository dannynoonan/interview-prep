# 02
# Easy

# Given a sorted array that can contain duplicates, find the first occurrence of the
# target element. 

# For example: [1,3,4,6,6,6,7] and Target = 6, return index 3


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def find_first_occurrence(s_arr: list, t: int) -> int:
    low = 0
    high = len(s_arr)-1
    while low <= high:
        mid = round(low + (high-low)/2)
        if s_arr[mid] == t and (mid == 0 or s_arr[mid-1] < t):
            return mid
        elif s_arr[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    raise Exception(f"Target {t} not found")


# -----------------------------------------------------

import pytest

def test_find_first_occurrence():
    s_arr = [1,3,4,6,6,6,7]
    t1 = 6
    index_of_t1 = 3
    assert(find_first_occurrence(s_arr, t1) == index_of_t1)

    t2 = 4
    index_of_t2 = 2
    assert(find_first_occurrence(s_arr, t2) == index_of_t2)

    t3 = 5
    with pytest.raises(Exception):
        find_first_occurrence(s_arr, t3)

pytest.main()
