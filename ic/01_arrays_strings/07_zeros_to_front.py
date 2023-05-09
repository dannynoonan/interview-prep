# 07
# Easy

# You are given an array of integers. Rearrange the array so that all zeroes are at
# the beginning of the array.

# For example, [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def zeros_to_front(arr: list) -> None:
    zero_i = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            swap(arr, zero_i, i)
            zero_i += 1

def swap(arr: list, i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# -----------------------------------------------------

import pytest

def test_zeros_to_front():
    arr = [4,2,0,1,0,3,0]
    end_arr = [0,0,0,1,2,3,4]
    zeros_to_front(arr)
    assert(arr == end_arr)

pytest.main()
