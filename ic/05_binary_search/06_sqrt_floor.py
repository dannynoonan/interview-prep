# 06

# Find the square root of an integer X. For example, squareRoot(4) = 2. 
# It is ok to find the integer floor of the square root. 
# So squareRoot(5) or squareRoot(8) can also return 2. squareRoot(9) will return 3.

# Using Binary Search, you can search for square roots over the integer space. 
# This is pretty fast because it takes O(log(n)) time. 
# Assume that x*x is less than the integer limit.


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def sqrt_floor(v: int) -> int|None:
    low = 1
    high = v
    closest_sqrt_floor = None
    closest_sqrt_floor_diff = None
    while low <= high:
        mid = round((low + high)/2)
        mid_sq = mid ** 2
        if mid_sq == v:
            return mid
        if mid_sq < v:
            if not closest_sqrt_floor_diff or (v - mid_sq) < closest_sqrt_floor_diff:
                closest_sqrt_floor_diff = v - mid_sq
                closest_sqrt_floor = mid
            low = mid + 1
        else:
            high = mid - 1
    return closest_sqrt_floor


# -----------------------------------------------------

import pytest

def test_sqrt_floor():
    assert(sqrt_floor(4) == 2)
    assert(sqrt_floor(5) == 2)
    assert(sqrt_floor(8) == 2)
    assert(sqrt_floor(9) == 3)
    assert(sqrt_floor(234256) == 484)
    assert(sqrt_floor(234255) == 483)

pytest.main()
