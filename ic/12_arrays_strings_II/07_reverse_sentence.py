# 07
# Easy

# Reverse the words in a sentence.

# For example: "this is a string" -> "string a is this"


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1) - this is what distinguishes this from Chapter 1 version

def reverse_sentence(s: str) -> str:
    s_arr = [c for c in s]
    reverse_span(s_arr, 0, len(s_arr)-1)
    last_space_i = 0
    for i in range(len(s_arr)):
        if s_arr[i] == ' ':
            reverse_span(s_arr, last_space_i, i-1)
            last_space_i = i+1
    reverse_span(s_arr, last_space_i, len(s_arr)-1)
    return ''.join(s_arr)

def reverse_span(s: list, low: int, high: int) -> None:
    while low < high:
        swap(s, low, high)
        low += 1
        high -= 1

def swap(s: list, i: int, j: int) -> None:
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

# -----------------------------------------------------

import pytest

def test_reverse_sentence():
    s_start = "this is a string"
    s_end = "string a is this"
    assert(reverse_sentence(s_start) == s_end)

pytest.main()
