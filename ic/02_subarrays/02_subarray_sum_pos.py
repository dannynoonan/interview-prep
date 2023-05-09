# 02
# Medium

# Given an array of positive integers, find a subarray that sums to a given number X.

# For example, input = [1,2,3,5,2] and X=8, Result = [3,5] (indexes 2,3)


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def subarray_sum(pos_arr: list, x: int) -> list:
    low = 0
    high = 0
    curr_sum = pos_arr[0]
    while high < len(pos_arr):
        if curr_sum == x:
            return pos_arr[low:high+1]
        elif curr_sum < x:
            high += 1
            if high == len(pos_arr):
                raise Exception("FAIL 1")
            curr_sum += pos_arr[high]
        else:
            curr_sum -= pos_arr[low]
            low += 1
            if low > high:
                high += 1
                if high == len(pos_arr):
                    raise Exception("FAIL 2")
                curr_sum += pos_arr[high]
    raise Exception("FAIL 3")


# -----------------------------------------------------

import pytest

def test_subarray_sum():
    pos_arr = [1,2,3,5,2]
    x = 8
    result = [3,5]
    assert(subarray_sum(pos_arr, x) == result)

    impossible_x = 4
    with pytest.raises(Exception):
        subarray_sum(pos_arr, impossible_x)

pytest.main()
