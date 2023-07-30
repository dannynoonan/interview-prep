# 03
# Medium

# Given a String, find the longest substring with unique characters.

# For example: "whatwhywhere" --> "atwhy"


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(size of character set), which is typically a fixed number, so O(1)

def longest_unique_substring(string: str) -> str:
    longest_low = 0
    longest_high = 0
    low = 0
    char_to_i = {}
    for i in range(len(string)):
        c = string[i]
        if c in char_to_i:
            if low < char_to_i[c] + 1:
                low = char_to_i[c] + 1
        char_to_i[c] = i
        if (i - low) > (longest_high - longest_low):
            longest_high = i
            longest_low = low
    return string[longest_low:longest_high+1]


# -----------------------------------------------------

import pytest

def test_longest_unique_substring():
    string = "whatwhywhere"
    longest_unique = "atwhy"
    assert(longest_unique_substring(string) == longest_unique)
    assert(longest_unique_substring('flavaflavehassomeflavortosavor') == 'meflavort')

pytest.main()
