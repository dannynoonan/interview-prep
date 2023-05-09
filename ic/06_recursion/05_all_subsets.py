# 05
# Medium

# Given an array of integers A, print all its subsets.

# For example:
# Input: [1, 2, 3]
# Output:
# []
# [1]
# [2]
# [3]
# [1, 2]
# [1, 3]
# [2, 3]
# [1, 2, 3]


# -----------------------------------------------------

# Time Complexity: Factorial Complexity
# Space Complexity: ​O(N), where N is A's length; buffer allocation and on recursion stack

def all_subsets_main(arr: list) -> None:
    buf = []
    return all_subsets(arr, 0, buf)

def all_subsets(arr: list, arr_i: int, buf: list) -> None:
    print(buf)
    if arr_i == len(arr):
        buf = []
        return
    for i in range(arr_i, len(arr)):
        buf.append(arr[i])
        all_subsets(arr, i+1, buf)
        buf.pop()

# -----------------------------------------------------

all_subsets_main([1,2,3])
