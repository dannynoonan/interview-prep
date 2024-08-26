# 08
# Medium

# You are given an array of integers and a pivot. Rearrange the array in the following order:
# [all elements less than pivot, elements equal to pivot, elements greater than pivot]

# For example, a = [5,2,4,4,6,4,4,3] and pivot = 4 --> result = [3,2,4,4,4,4,5,6]


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def dnf(arr: list, pivot: int) -> None:
    i = 0
    low = 0
    high = len(arr)-1
    while i <= high:
        if arr[i] < pivot:
            swap(arr, i, low)
            i += 1
            low += 1
        elif arr[i] == pivot:
            i += 1
        else:
            swap(arr, i, high)
            high -= 1

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# -----------------------------------------------------

import pytest

def test_dnf():
    arr1 = [5, 2, 4, 4, 6, 4, 4, 3]
    result1 = [3, 2, 4, 4, 4, 4, 6, 5]
    dnf(arr1, 4)
    assert(arr1 == result1)

    arr2 = [4, 2, 0, 1, 3, 4, 2, 9, 7, 6, 5, 8]
    result2 = [2, 0, 1, 3, 2, 4, 4, 7, 6, 5, 8, 9]
    dnf(arr2, 4)
    assert(arr2 == result2)

    arr3 = [5, 6, 5, 0, 3, 8, 3, 0, 0, 9, 3, 4]
    result3 = [4, 0, 3, 3, 3, 0, 0, 5, 5, 9, 8, 6]
    dnf(arr3, 5)
    assert(arr3 == result3)

pytest.main()
