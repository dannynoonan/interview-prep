# 01 
# Level: Easy

# Given an array of numbers, replace each even number with two of the same number. 

# e.g, [1,2,5,6,8, , , ,] -> [1,2,2,5,6,6,8,8].

# Assume that the array has the exact amount of space to accommodate the result.


# -----------------------------------------------------

# Time Complexity: O(n) aka linear time
# Space Complexity: O(1) aka constant space


def duplicate_evens(arr: list) -> None:
    ix = len(arr)-1
    for i in range(len(arr)-1, 0, -1):
        if arr[i]:
            arr[ix] = arr[i]
            ix -= 1
            if arr[i] % 2 == 0:
                arr[ix] = arr[i]
                ix -= 1


# -----------------------------------------------------

import pytest

def test_duplicate_evens():
    start_arr = [1, 2, 5, 6, 8, None, None, None]
    end_arr = [1, 2, 2, 5, 6, 6, 8, 8]
    duplicate_evens(start_arr)
    assert(start_arr == end_arr)

pytest.main()
