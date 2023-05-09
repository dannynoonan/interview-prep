# 01
# Medium

# Given an array of integers that can be both +ve and -ve, find the contiguous subarray
# with the largest sum.

# For example:  [1,2,-1,2,-3,2,-5]  -> first 4 elements have the largest sum. Return (0,3)

# Actually no: just return the sum (4), contiguous subarray can't be found here  


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def kadanes(arr: list) -> None:
    largest = arr[0]
    current = arr[0] 
    for i in range(1, len(arr)):
        current += max(current, current + arr[i])
        largest = max(largest, current)
    return largest


# -----------------------------------------------------

import pytest

def test_kadanes():
    arr = [1,2,-1,2,-3,2,-5]
    largest = 4
    assert(kadanes(arr) == largest)

pytest.main()
