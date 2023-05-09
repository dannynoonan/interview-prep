# 05
# Medium

# Print elements of a matrix in spiral order.


# -----------------------------------------------------

# Time Complexity: O(n), where n is the number of elements in the matrix
# Space Complexity: O(1)

def matrix_to_spiral(mx: list) -> list:
    x_len = len(mx[0])
    y_len = len(mx)
    if x_len < y_len:
        shorter = x_len
    else:
        shorter = y_len
    out = [None] * (x_len * y_len)
    layer = 0
    slot = 0
    while layer <= shorter/2:
        low_x = layer
        high_x = x_len - layer - 1
        low_y = layer
        high_y = y_len - layer - 1
        for x in range(low_x, high_x):
            out[slot] = mx[low_y][x]
            slot += 1
        for y in range(low_y, high_y):
            out[slot] = mx[y][high_x]
            slot += 1
        for x in range(high_x, low_x, -1):
            out[slot] = mx[high_y][x]
            slot += 1
        for y in range(high_y, low_y, -1):
            out[slot] = mx[y][low_x]
            slot += 1
        layer += 1
    return out

# -----------------------------------------------------

import pytest

def test_matrix_to_spiral():
    mx1 = [
        [ 1, 2, 3, 4],
        [12,13,14, 5],
        [11,16,15, 6],
        [10, 9, 8, 7]
    ]
    solution1 = [v+1 for v in range(16)]
    assert(matrix_to_spiral(mx1) == solution1)

    mx2 = [
        [ 1, 2, 3, 4, 5],
        [14,15,16,17, 6],
        [13,20,19,18, 7],
        [12,11,10, 9, 8]
    ]
    solution2 = [v+1 for v in range(20)]
    assert(matrix_to_spiral(mx2) == solution2)

pytest.main()
