# 03
# Easy

# Given an array, reverse the order of its elements.

# For example, [3,5,2,5,2,3,9] -> [9,3,2,5,2,5,3]


# -----------------------------------------------------

# Time Complexity: O(n) 
# Space Complexity: O(1) 

def reverse_array(arr: list) -> None:
    low = 0
    high = len(arr) - 1
    while low <= high:
        swap(arr, low, high)
        low += 1
        high -= 1

def swap(arr: list, i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# -----------------------------------------------------

import pytest

def test_reverse_array():
    start_arr = [3,5,2,5,2,3,9]
    end_arr = [9,3,2,5,2,5,3]
    reverse_array(start_arr)
    assert(start_arr == end_arr)

pytest.main()
        