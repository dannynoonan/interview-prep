# 03
# Medium

# An image is a square matrix of pixels. Rotate a square image by 90 degrees, given an array of
# pixels as integers.

# For example,

# 1 2 3     7 4 1
# 4 5 6  →  8 5 2
# 7 8 9     9 6 3

mx = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15,16] 
]

# -----------------------------------------------------

# Expected Time Complexity: O(n), where n is the total number of elements in 2D array
# Expected Space Complexity: O(1)

# 1:12

def rotate_pixel_square(mx: list) -> list:
    low = 0
    high = len(mx)-1
    while low <= high:
        for i in range(low, high):
            tmp = mx[low][low+i]
            mx[low][low+i] = mx[high-i][low]
            mx[high-i][low] = mx[high][high-i]
            mx[high][high-i] = mx[low+i][high]
            mx[low+i][high] = tmp
        low += 1
        high -= 1
    return mx

# -----------------------------------------------------

import pytest

def test_rotate_pixel_square():
    start_mx = [
        [ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12],
        [13,14,15,16] 
    ]
    end_mx = [
        [13, 9, 5, 1],
        [14,10, 6, 2],
        [15,11, 7, 3],
        [16,12, 8, 4] 
    ]
    assert(rotate_pixel_square(start_mx) == end_mx)

pytest.main()
    