# 08
# Medium

# Find the longest palindrome in a string. 

# For example, "ab|babab|aab" -> "babab"


# -----------------------------------------------------

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def longest_palindromic_substr(s: str) -> str:
    longest = 0
    longest_low = 0
    longest_high = 0
    for i in range(len(s)):
        low_i = i-1
        high_i = i+1
        while low_i >= 0 and high_i < len(s):
            if s[low_i] != s[high_i]:
                break
            if high_i-low_i > longest:
                longest = high_i-low_i
                longest_low = low_i
                longest_high = high_i
            low_i -= 1
            high_i += 1

        low_i = i
        high_i = i+1
        while low_i >= 0 and high_i < len(s):
            if s[low_i] != s[high_i]:
                break
            if high_i-low_i > longest:
                longest = high_i-low_i
                longest_low = low_i
                longest_high = high_i
            low_i -= 1
            high_i += 1

    return s[longest_low:longest_high+1]

# -----------------------------------------------------

import pytest

def test_longest_palindromic_substr():
    s1 = "abbababaab"
    solution1 = "babab"
    assert(longest_palindromic_substr(s1) == solution1)

    s2 = "enicoabbafilousd"
    solution2 = "abba"
    assert(longest_palindromic_substr(s2) == solution2)

    s3 = "madaminedenimadam"
    solution3 = "madaminedenimadam"
    assert(longest_palindromic_substr(s3) == solution3)

    s4 = "ono"
    solution4 = "ono"
    assert(longest_palindromic_substr(s4) == solution4)

    s5 = "onno"
    solution5 = "onno"
    assert(longest_palindromic_substr(s5) == solution5)

    s6 = "uioiuoiuoiuoiuoiuoiuiuoiuouiuoiuoiuoiuoiuoi"
    solution6 = "uioiu"
    assert(longest_palindromic_substr(s6) == solution6)

pytest.main()
