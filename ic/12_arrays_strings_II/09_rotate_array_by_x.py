# 09
# Easy

# Rotate an array A by X items. For example,

# A = [1,2,3,4,5,6] and X = 2, Result = [5,6,1,2,3,4]


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
[1,2,3,4,5,6], 4
      v
[6,5,4,3,2,1]
      v
[3,4,5,6,1,2]
'''

def rotate_array(arr: list, x: int) -> None:
    reverse(arr, 0, len(arr)-1)
    reverse(arr, 0, x-1)
    reverse(arr, x, len(arr)-1)

def reverse(arr: list, low: int, high: int) -> None:
    while low < high:
        swap(arr, low, high)
        low += 1
        high -= 1

def swap(arr: list, i: int, j: int) -> None:
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

# -----------------------------------------------------

import pytest

def test_rotate_array():
    arr1 = [1,2,3,4,5,6]
    rotated1 = [3,4,5,6,1,2]
    rotate_array(arr1, 4)
    assert(arr1 == rotated1)

    arr2 = [8,6,7,5,3,0,9]
    rotated2 = [8,6,7,5,3,0,9]
    rotate_array(arr2, 0)
    assert(arr2 == rotated2)
    rotate_array(arr2, 7)
    assert(arr2 == rotated2)
    with pytest.raises(Exception):
        rotate_array(arr2, 8)

pytest.main()
