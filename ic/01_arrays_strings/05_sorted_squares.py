# 05
# Easy

# Given a sorted array in non-decreasing order, return an array of squares of each number, 
# also in non-decreasing order. 

# For example, [-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]

# How can you do it in O(n) time?


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n)

def sorted_squares(arr: list) -> list:
    squarr = [None] * len(arr)
    low = 0
    high = len(arr)-1
    squarr_i = len(arr)-1
    while low <= high:
        low_sq = arr[low] ** 2
        high_sq = arr[high] ** 2
        if low_sq >= high_sq:
            squarr[squarr_i] = low_sq
            low += 1
        else:
            squarr[squarr_i] = high_sq
            high -= 1
        squarr_i -= 1
    return squarr 


# -----------------------------------------------------

import pytest

def test_sorted_squares():
    arr = [-4,-2,-1,0,3,5]
    squarr = [0,1,4,9,16,25]
    assert(sorted_squares(arr) == squarr)

pytest.main()
