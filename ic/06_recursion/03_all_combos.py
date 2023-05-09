# 03

# Given an array of integers, print all combinations of size X.


# -----------------------------------------------------

# Time Complexity: Factorial Complexity
# Space Complexity: O(X). We use O(X) space both in the buffer allocation and on the recursion stack

def all_combos_of_size_main(arr: list, size: int) -> None:
    buf = [None] * size
    return all_combos_of_size(arr, 0, buf, 0)

def all_combos_of_size(arr: list, arr_i: int, buf: list, buf_i: int) -> None:
    if buf_i == len(buf):
        print(buf)
        return
    if arr_i == len(arr):
        return
    
    for i in range(arr_i, len(arr)):
        buf[buf_i] = arr[i]
        all_combos_of_size(arr, i+1, buf, buf_i+1)

# -----------------------------------------------------

all_combos_of_size_main([1,2,3], 2)
