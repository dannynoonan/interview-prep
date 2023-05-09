# 06
# Medium

# Given an array A, print all permutations of size X.

# For example,
# Input:
# A = [1,2,3]
# X = 2
# Output:
# [1, 2]
# [1, 3]
# [2, 1]
# [2, 3]
# [3, 1]
# [3, 2]


# -----------------------------------------------------

# Time Complexity: Factorial
# Space Complexity:​ O(N), where N is A.length. We use O(N) space both in the buffer allocation

def all_permutations_of_size_main(arr: list, size: int) -> None:
    buf = [None] * size
    in_buf = [False] * len(arr)
    return all_permutations_of_size(arr, buf, 0, in_buf)

def all_permutations_of_size(arr: list, buf: list, buf_i: int, in_buf: list) -> None:
    if buf_i == len(buf):
        print(buf)
        return
    for i in range(len(arr)):
        if not in_buf[i]:
            buf[buf_i] = arr[i]
            in_buf[i] = True
            all_permutations_of_size(arr, buf, buf_i+1, in_buf)
            in_buf[i] = False

# -----------------------------------------------------

all_permutations_of_size_main([1,2,3], 2)
        