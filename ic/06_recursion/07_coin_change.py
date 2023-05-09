# 07
# Medium

# Coin Change Problem: Given a set of coin denominations, print out the different ways you can 
# make a target amount. You can use as many coins of each denomination as you like.

# For example: If coins are [1,2,5] and the target is 5, output will be:
# [1,1,1,1,1]
# [1,1,1,2]
# [1,2,2]
# [5]


# -----------------------------------------------------

# Time Complexity: Factorial
# Space Complexity: ​O(Target), because in the worst case, both our buffer and the recursion
# stack will be the size of the target. (if we use all 1's to make target)

def coin_change_main(coin_types: list, t: int) -> None:
    return coin_change(coin_types, 0, [], t)

def coin_change(coin_types: list, coin_type_i: int, wallet: list, t: int) -> None:
    if sum(wallet) == t:
        print(wallet)
        return
    if sum(wallet) > t:
        return
    for i in range(coin_type_i, len(coin_types)):
        wallet.append(coin_types[i])
        coin_change(coin_types, i, wallet, t)
        wallet.pop()

# -----------------------------------------------------

coin_change_main([1,2,5], 5)
