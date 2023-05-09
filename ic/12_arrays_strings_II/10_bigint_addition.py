# 10
# Hard

# You are given a number in the form of an array. Each digit in the array represents a digit in 
# the number. For example, 100 -> [1,0,0]. Perform addition of 2 such number arrays. 

# For example:
# [1,1,1,1] + [2,2,3,3] = [3,3,4,4]
# [9,9] + [1] = [1,0,0]
# [1,6,4,3] + [1,3,1] = [1,7,7,4]


# -----------------------------------------------------

# Time Complexity: O(n), where n is the length of the larger input array
# Space Complexity: O(n), because we allocate an array to store the result

def bigint_addition(arr1: list, arr2: list) -> list:
    if len(arr1) > len(arr2):
        longer = arr1
        shorter = arr2
    else:
        longer = arr2
        shorter = arr1
    len_diff = len(longer) - len(shorter)
    final = [0] * (len(longer)+1)
    carry = 0
    for long_col in range(len(longer)-1, -1, -1):
        col_sum = carry + longer[long_col]
        short_col = long_col - len_diff
        if short_col >= 0:
            col_sum += shorter[short_col]
        final[long_col+1] = col_sum % 10
        carry = int(col_sum / 10)
    if carry:
        final[0] = carry
    else:
        final = final[1:]
    return final

# -----------------------------------------------------

import pytest

def test_bigint_addition():
    assert(bigint_addition([1,1,1,1], [2,2,3,3]) == [3,3,4,4])
    assert(bigint_addition([9,9], [1]) == [1,0,0])
    assert(bigint_addition([1,6,4,3], [1,3,1]) == [1,7,7,4])

pytest.main()
