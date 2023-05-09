# 07

# A peak element in an array A is an A[i] where its neighboring elements are less than A[i].
# So, A[i - 1] < A[i] and A[i + 1] < A[i].
# Assume there are no duplicates. Also, assume that A[-1] and A[length] are negative infinity (-∞).
# So A[0] can be a peak if A[1] < A[0].
# A = [1,3,4,5,2] => Peak = 5
# A = [5,3,1] => Peak = 5
# A = [1,3,5] => Peak = 5


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def find_peak_element(arr: list) -> tuple:
    print(f"arr={arr}")
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = round(low + (high-low)/2)
        if (mid == len(arr)-1 or arr[mid] > arr[mid+1]) and (mid == 0 or arr[mid] > arr[mid-1]):
            return mid, arr[mid]
        if mid == 0 or arr[mid] > arr[mid-1]:
            low = mid+1
        elif mid == len(arr)-1 or arr[mid] > arr[mid+1]:
            high = mid-1
        else:
            low = mid+1
    raise Exception("FAIL")
  

# -----------------------------------------------------

import pytest 

def test_find_peak_element():
    arr1 = [1,3,4,5,2]
    peak1 = (3,5)
    assert(find_peak_element(arr1) == peak1)

    arr2 = [5,3,1]
    peak2 = (0,5)
    assert(find_peak_element(arr2) == peak2)

    arr3 = [1,3,5]
    peak3 = (2,5)
    assert(find_peak_element(arr3) == peak3)

pytest.main()
