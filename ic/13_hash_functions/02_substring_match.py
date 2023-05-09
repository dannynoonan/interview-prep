# 02
# Hard

# Rabin Karp String Search: Find the index where the larger string A contains a target string T


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def substring_match(needle: str, haystack: str) -> tuple:
    c = 31
    c_pow = 1
    needle_hash = 0
    haystack_hash = 0
    
    for i in range(len(needle)):
        needle_hash = needle_hash * c + ord(needle[i])
        haystack_hash = haystack_hash * c + ord(haystack[i])
        if i > 0:
            c_pow *= c

    if haystack_hash == needle_hash:
            return (0, len(needle)-1)

    for i in range(len(needle), len(haystack)):
        haystack_hash = haystack_hash - (ord(haystack[i-len(needle)]) * c_pow)
        haystack_hash = haystack_hash * c + ord(haystack[i])
        if haystack_hash == needle_hash:
            return (i-len(needle)+1, i)
        
    raise Exception(f"No match found for needle={needle} in haystack={haystack}")

# -----------------------------------------------------

import pytest

def test_substring_match():
    assert(substring_match('fee', 'time for coffee') == (12,14))
    assert(substring_match('time', 'time for coffee') == (0,3))
    assert(substring_match('time for coffee', 'time for coffee') == (0,14))
    assert(substring_match('for', 'time for coffee') != (0,14))
    with pytest.raises(Exception):
        substring_match('tea', 'time for coffee')
    with pytest.raises(Exception):
        substring_match('coffeee', 'time for coffee')

pytest.main()
