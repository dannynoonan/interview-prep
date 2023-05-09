# 05

# Given an array that is cyclically sorted, find the minimum element. A cyclically sorted
# array is a sorted array rotated by some number of elements. Assume all elements are unique.

# For example:
# A = [4,5,1,2,3], which is just [1,2,3,4,5] rotated by 2. Result = index 2


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

'''
My notes have a couple alternative solutions, they all have their own quirks and all pass unit tests
'''
def find_lowest(cs_arr: list) -> int:
    low = 0
    high = len(cs_arr)-1
    if cs_arr[low] < cs_arr[high]:
        return low 
    while low <= high:
        mid = round((low + high)/2)
        if cs_arr[mid] < cs_arr[mid-1] or (mid == 0 and cs_arr[mid] < cs_arr[len(cs_arr)-1]):
            return mid
        elif cs_arr[mid] < cs_arr[0]:
            high = mid - 1
        else:
            low = mid + 1
    raise Exception(f"No lowest found for cs_arr={cs_arr}")


# -----------------------------------------------------

import pytest

def test_find_lowest():
    cs_arr = [4,5,1,2,3]
    low_i = 2
    assert(find_lowest(cs_arr) == low_i)

    cs_arr2 = [1,3,4,7,9,11]
    low_i2 = 0
    assert(find_lowest(cs_arr2) == low_i2)

    cs_arr3 = [13,16,22,25,1,7,9]
    low_i3 = 4
    assert(find_lowest(cs_arr3) == low_i3)

pytest.main()
