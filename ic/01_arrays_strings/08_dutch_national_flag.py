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
    arr = [5,2,4,4,6,4,4,3]
    pivot = 4
    result = [3,2,4,4,4,4,6,5]
    dnf(arr, pivot)
    assert(arr == result)

pytest.main()
