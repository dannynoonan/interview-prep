# 03

# Given a sorted array A and a target T, return the index where the target would be placed
# if inserted in order.
#
# For example,
# A = [1,2,4,4,5,6,8] and T = 3, return index 2
# A = [1,2,4,4,5,6,8] and T = 0, return index 0
# A = [1,2,4,4,5,6,8] and T = 4, return index 4 (insert after other 4’s).


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def find_insertion_index(s_arr: list, t: int) -> int:
    low = 0
    high = len(s_arr)-1
    while low <= high:
        mid = round(low + (high-low)/2)
        if mid == 0 and s_arr[mid] > t:
            return mid
        elif s_arr[mid] <= t and (mid == len(s_arr)-1 or s_arr[mid+1] > t):
            return mid + 1
        elif s_arr[mid] <= t:
            low = mid + 1
        else:
            high = mid - 1
    raise Exception(f"Fail for target {t}")

# alt version 10/17 (maybe the other one doesn't work in every case?)
def insertion_index(arr: list, v: int) -> int:
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = round((low+high)/2)
        if v < arr[mid] and (mid == 0 or v >= arr[mid-1]):
            return mid
        if v < arr[mid]:
            high = mid-1
        elif v > arr[mid] and mid == len(arr)-1:
            return len(arr)
        else:
            low = mid+1
    raise Exception('problems')

# -----------------------------------------------------

import pytest

def test_find_insertion_index():
    s_arr = [1,2,4,4,5,6,8]
    t1 = 2
    index_of_t1 = 2
    assert(find_insertion_index(s_arr, t1) == index_of_t1)

    t2 = 0
    index_of_t2 = 0
    assert(find_insertion_index(s_arr, t2) == index_of_t2)

    t3 = 4
    index_of_t3 = 4
    assert(find_insertion_index(s_arr, t3) == index_of_t3)

pytest.main()
