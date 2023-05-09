# 04
# Medium

# Given an array of positive and negative integers, find a subarray whose sum equals X.

# For example: Input = [2,4,-2,1,-3,5,-3], X = 5 --> Result = [2,4,-2,1]


# -----------------------------------------------------

# Time complexity: O(n) time 
# Space complexity: O(n) space

def subarray_sum(ints: list, x: int) -> list:
    curr_sum = 0
    sums_to_indices = {}
    for i in range(len(ints)):
        curr_sum += ints[i]
        diff = curr_sum - x
        if curr_sum == x:
            return ints[:i+1]
        if diff in sums_to_indices:
            return ints[sums_to_indices[diff]+1:i+1]
        sums_to_indices[curr_sum] = i
    raise Exception("no match")


# -----------------------------------------------------

import pytest

def test_subarray_sum():
    ints = [2,4,-2,1,-3,5,-3]
    x = 5
    result = [2,4,-2,1]
    assert(subarray_sum(ints, x) == result)

pytest.main()
