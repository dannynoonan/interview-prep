# 04

# Given a sorted array of Integers, find the target. If the target is not found,
# return the element closest to the target.

# For example,
# A = [1,2,4,5,7,8,9], Target = 6 -> Output Index = 3 or 4 (since both 5 and 7 are equally close)


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def find_closest_val(s_arr: list, t: int) -> int:
    closest = None
    closest_diff = None
    low = 0
    high = len(s_arr)-1
    while low <= high:
        mid = round((high + low)/2)
        diff = abs(s_arr[mid] - t)
        if diff == 0:
            return s_arr[mid]
        if not closest_diff or diff < closest_diff:
            closest_diff = diff
            closest = s_arr[mid]
        if s_arr[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    return closest


# -----------------------------------------------------

import pytest

def test_find_closest_val():
    s_arr = [1,2,4,5,7,8,9]
    t1 = 6
    v1 = [5,7]
    assert(find_closest_val(s_arr, t1) in v1)

    t2 = 10
    v2 = 9
    assert(find_closest_val(s_arr, t2) == v2)

    t3 = 2
    v3 = 2
    assert(find_closest_val(s_arr, t3) == v3)

pytest.main()
