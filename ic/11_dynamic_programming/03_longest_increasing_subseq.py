# 03
# Medium

# Longest Increasing Subsequence: Given an array of integers, find the length of the 
# longest increasing subsequence.

# For e.g, in [1, 3, 2, 5, 3, 5, 6], the longest increasing subsequence is [1, 2, 3, 5, 6] 
# of length 5.


# -----------------------------------------------------

# Time Complexity: O(n^2)
# Space Complexity: O(n)

def longest_increasing_subseq(arr: list) -> int:
    tabs = [1] * len(arr)
    max_len = 1
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                tabs[i] = max(tabs[j]+1, tabs[i])
        max_len = max(tabs[i], max_len)
    return max_len

# -----------------------------------------------------

import pytest

def test_longest_increasing_subseq():
    arr1 = [1, 3, 2, 5, 3, 5, 6]
    assert(longest_increasing_subseq(arr1) == 5)
    arr2 = [1, 3, 14, 2, 3, 5, 22, 6, 2, 4, 39, 7, 9, 52, 12, 15]
    assert(longest_increasing_subseq(arr2) == 9)

pytest.main()
