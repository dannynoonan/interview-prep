# 02
# Easy

# Power Function: Implement a function to calculate X^N. Both X and N can be positive or negative. 
# You can assume that overflow doesn't happen.

# Try doing it in ​O(log(n))​ time

# For example: 
# 2 ^ 2  = 4 
# 2 ^ -2 = 0.25
# -2 ^ 3  = -8


# -----------------------------------------------------

# Time Complexity: O(log(n))
# Space Complexity: O(log(n)) on call stack

def power(x: int, n: int) -> float: 
    if (n == 0):
        return 1
    if (x == 0):
        return 0
    return x * power(x, n - 1)


# -----------------------------------------------------

import pytest

def test_power():
    assert(power(2, 3) == 8)
    assert(power(-5, 3) == -125)

pytest.main()
