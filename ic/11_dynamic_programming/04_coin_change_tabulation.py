# 04
# Hard

# Coin Change - Print Count: Given a set of coin denominations, print out the number of ways
# you can make a target amount. You can use as many coins of each denomination as you like.

# For example: If coins are [1,2,5] and the target is 5, the different ways are:
# [1,1,1,1,1]
# [1,1,1,2]
# [1,2,2]
# [5]

# The Output will be 4.

# Note: In the Recursion Section, we looked at the Coin Change Problem where we printed each
# combination. If we just need to output the number of combinations, we can do it faster using DP.


# -----------------------------------------------------

# Time Complexity: O(Amount*Coins)
# Space Complexity: O(Amount)

def coin_change(coins: list, t: int) -> int:
    tabs = [0] * (t+1)
    tabs[0] = 1
    for c in coins:
        for i in range(c, len(tabs)):
            tabs[i] += tabs[i-c]
    return tabs[len(tabs)-1]

# -----------------------------------------------------

import pytest

def test_coin_change():
    coins1 = [1,2,5]
    t1 = 5
    assert(coin_change(coins1, t1) == 4)

    coins2 = [1,2,5,10]
    t2 = 10
    assert(coin_change(coins2, t2) == 11)

pytest.main()
