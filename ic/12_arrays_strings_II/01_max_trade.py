# 01
# Medium

# Given a list of stock prices for a company, find the maximum amount of money you can make
# with one trade. A trade is a buy and sell.


# -----------------------------------------------------

# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

def max_trade(prices: list) -> int:
    max_so_far = 0
    lowest = prices[0]
    for p in prices:
        lowest = min(p, lowest)
        diff = p - lowest
        max_so_far = max(max_so_far, diff)
    return max_so_far

# -----------------------------------------------------

import pytest

def test_max_trade():
    prices = [8,10,13,12,15,11,8,6,4,5,9]
    assert(max_trade(prices) == 7)
    prices.append(12)
    assert(max_trade(prices) == 8)

pytest.main()
