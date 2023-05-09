# 01
# Easy

# Find the K smallest numbers in an array.

# For example,
# [6,3,6,6,2,2,4] => [2,2,3,4]


# -----------------------------------------------------

# Time Complexity: O(Nlog(K))
# Space Complexity: O(K)

# TODO I had more complex element-y-element solutions previously, but reading the question explicitly now I think this solution does the trick.

import heapq

def find_k_smallest(arr: list, k: int) -> list:
    heapq.heapify(arr)
    k_smallest = [None] * k
    for i in range(k):
        k_smallest[i] = heapq.heappop(arr)
    return k_smallest

# -----------------------------------------------------

import pytest

def test_find_k_smallest():
    arr = [6,3,6,6,2,2,4]
    assert(find_k_smallest(arr, 4) == [2,2,3,4])

pytest.main()
