# 01
# Easy

# Given a sorted array, search for a target item.


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def find_index_of_target(s_arr: list, t: int) -> int:
    low = 0
    high = len(s_arr)-1
    while low <= high:
        mid = round(low + (high-low)/2)
        if t == s_arr[mid]:
            return mid
        if t > s_arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    raise Exception(f"Target {t} not found")


# -----------------------------------------------------

import pytest

def test_find_index_of_target():
    s_arr = [1,4,7,12,13,15,18,22,25]
    t1 = 22
    index_of_t1 = 7
    assert(find_index_of_target(s_arr, t1) == index_of_t1)

    t2 = 7
    index_of_t2 = 2
    assert(find_index_of_target(s_arr, t2) == index_of_t2)

    t3 = 14
    with pytest.raises(Exception):
        find_index_of_target(s_arr, t3)

pytest.main()
         