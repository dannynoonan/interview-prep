# 01
# Easy

# Find the nth number in the Fibonacci series. Fibonacci series is as follows:
# 1, 1, 2, 3, 5, 8, 13, 21, ..
# After the first two 1’s, each number is the sum of the previous two numbers.


# -----------------------------------------------------

# Time Complexity: O(2​^n​)
# Space Complexity: O(n)

def fibonacci(x: int) -> int:
    if x <= 2:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


# -----------------------------------------------------

# With memoization

# Time Complexity: O(n​)
# Space Complexity: O(n)

def fibonacci_memo(x, memo):
    if x <= 2:
        return 1
    if x in memo:
        return memo[x]
    fib = fibonacci_memo(x - 1, memo) + fibonacci_memo(x - 2, memo)
    memo[x] = fib
    return fib


# -----------------------------------------------------

import pytest

def test_fibonacci():
    assert(fibonacci(1) == 1)
    assert(fibonacci(4) == 3)
    assert(fibonacci(5) == 5)
    assert(fibonacci(7) == 13)
    assert(fibonacci_memo(1, {}) == 1)
    assert(fibonacci_memo(4, {}) == 3)
    assert(fibonacci_memo(5, {}) == 5)
    assert(fibonacci_memo(7, {}) == 13)
    assert(fibonacci_memo(20, {}) == 6765)

pytest.main()
