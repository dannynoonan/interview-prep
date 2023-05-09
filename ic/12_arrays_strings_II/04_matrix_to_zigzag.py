# 04
# Medium

# Print a 2D array in Diagonal ZigZag order.


# -----------------------------------------------------

# Expected time complexity: O(n), where n is the number of elements in the matrix
# Expected Space Complexity: O(1)

mx = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15,16] 
]

out = [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]

"""
[0,0]
[0,1] [1,0]
[2,0] [1,1] [0,2]
[0,3] [1,2] [2,1] [3,0]
[3,1] [2,2] [1,3]
[2,3] [3,2]
[3,3]
"""

mx = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12]
]

out = [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]

"""
[0,0]
[0,1] [1,0]
[2,0] [1,1] [0,2]
[0,3] [1,2] [2,1]
[2,2] [1,3]
[2,3]
"""

def matrix_to_zigzag(mx: list) -> list:
    cols = len(mx[0])
    rows = len(mx)
    # out = [[]] * (rows+cols-1)
    out = [[] for v in range(rows+cols-1)]
    for r in range(rows):
        for c in range(cols):
            row_col_sum = r+c
            if row_col_sum % 2 == 0:
                out[row_col_sum].insert(0, mx[r][c])
            else:
                out[row_col_sum].append(mx[r][c])
    # print(out)
    solution = []
    for set in out:
        for v in set:
            solution.append(v)
    return solution

# -----------------------------------------------------

import pytest

def test_matrix_to_zigzag():
    mx1 = [
        [ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12],
        [13,14,15,16] 
    ]
    solution1 = [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
    assert(matrix_to_zigzag(mx1) == solution1)

    mx2 = [
        [ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12]
    ]
    solution2 = [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
    assert(matrix_to_zigzag(mx2) == solution2)

pytest.main()
        