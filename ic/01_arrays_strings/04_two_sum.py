# 04
# Easy

# 2 Sum Problem: Given a sorted array of integers, find two numbers in the array that sum
# to a given integer target.

# For example, if a = [1,2,3,5,6,7] and target = 11, the answer will be 5 and 6.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def two_sum(s_arr: list, t: int) -> tuple[int, int]:
    low = 0
    high = len(s_arr)-1
    while low < high:
        v = s_arr[low] + s_arr[high]
        if v == t:
            return s_arr[low], s_arr[high]
        if v < t:
            low += 1
        else:
            high -= 1
    raise Exception('No value found')


# -----------------------------------------------------

import pytest

def test_two_sum():
    s_arr = [1,2,3,5,6,7]
    t = 11
    result = 5, 6
    assert(two_sum(s_arr, t) == result)

pytest.main()
