# 11
# Hard

# Multiply two numbers given as Big Integers. In such an array, each element in the array 
# is a single digit number.

# For example:
# [1,6,4,3] * [1,3,1] = [2,1,5,2,3,3] 


# -----------------------------------------------------

# Time Complexity: O(m*n), where m and n are the lengths of the two BigIntegers
# Space Complexity: O(m+n), because the result array takes m+n space

def bigint_multiply(arr1: list, arr2: list) -> list:
    if len(arr1) > len(arr2):
        longer = arr1
        shorter = arr2
    else:
        longer = arr2
        shorter = arr1
    final = [0]
    for short_col in range(len(shorter)-1, -1, -1):
        row = [0] * (len(longer)+len(shorter)-short_col)
        carry = 0
        for long_col in range(len(longer)-1, -1, -1):
            val = (longer[long_col] * shorter[short_col]) + carry
            row[long_col+1] = val % 10
            carry = int(val / 10)
        if carry == 0:
            row = row[1:]
        else:
            row[0] = carry
        final = bigint_add(row, final)
    return final

def bigint_add(arr1: list, arr2: list) -> list:
    if len(arr1) > len(arr2):
        longer = arr1
        shorter = arr2
    else:
        longer = arr2
        shorter = arr1
    final = [0] * (len(longer)+1)
    diff = len(longer) - len(shorter)
    carry = 0
    for long_col in range(len(longer)-1, -1, -1):
        val = longer[long_col] + carry
        short_col = long_col - diff
        if short_col >= 0:
            val += shorter[short_col]
        final[long_col+1] = val % 10
        carry = int(val / 10)
    if carry > 0:
        final[0] = carry
        return final
    else:
        return final[1:]
    
# -----------------------------------------------------

import pytest

def test_bigint_addition():
    assert(bigint_add([1,1,1,1], [2,2,3,3]) == [3,3,4,4])
    assert(bigint_add([9,9], [1]) == [1,0,0])
    assert(bigint_add([1,6,4,3], [1,3,1]) == [1,7,7,4])

def test_bigint_multiply():
    assert(bigint_multiply([1,6,4,3], [1,3,1]) == [2,1,5,2,3,3])
    assert(bigint_multiply([1,2,3,4,5], [6,7,8,9,0]) == [8,3,8,1,0,2,0,5,0])

pytest.main()
